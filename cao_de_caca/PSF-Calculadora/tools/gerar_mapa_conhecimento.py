#!/usr/bin/env python3
"""Gera o plano e o grafo de conhecimento das aulas 361 a 1000."""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import unicodedata


RAIZ = Path(__file__).resolve().parents[1]
ARQUIVO_CODIGO = RAIZ / "assistente_psf.py"
ARQUIVO_PLANO = RAIZ / "docs" / "PLANO_MAPA_CONHECIMENTO_361_1000.md"
ARQUIVO_GRAFO = RAIZ / "docs" / "mapa_conhecimento_361_1000.json"

PALAVRAS_VAZIAS = {
    "a", "as", "ao", "aos", "aplicacao", "aplicacoes", "avancada",
    "avancado", "com", "como", "da", "das", "de", "definicao", "do",
    "dos", "e", "em", "fundamentos", "introducao", "matematica", "modelo",
    "modelagem", "modelos", "novo", "nova", "para", "psf", "sua", "suas",
    "teoria", "um", "uma", "visao",
}

# Conceitos são hubs semânticos. Uma aula pode ligar-se a todos os hubs
# sustentados por palavras do seu título; não há limite artificial de grau.
CONCEITOS = {
    "algebra": ("algebra", "polinom", "grupo", "anel", "corpo", "reticulo"),
    "algoritmos": ("algoritm", "computacional", "complexidade", "software"),
    "aprendizagem": ("aprendizado", "aprendizagem", "neural", "deep learning", "transformer"),
    "biologia": ("biolog", "populac", "genet", "evolu", "proteina", "doenca"),
    "calculo": ("calculo", "deriv", "integral", "variacional", "gradiente"),
    "categorias": ("categoria", "funtor", "morfismo"),
    "combinatoria": ("combinator", "contagem", "ramsey", "partic"),
    "computacao_quantica": ("computacao quantica", "qubit", "porta quantica", "algoritmo quantico"),
    "controle": ("controle", "controlabilidade", "observabilidade", "realimentacao"),
    "criptografia": ("criptograf", "rsa", "assinatura", "hash", "conhecimento zero"),
    "decisao": ("decisao", "votacao", "escolha social", "mecanismo", "alocacao"),
    "dinamica": ("dinam", "caos", "bifurca", "estabilidade", "atrator", "fluxo"),
    "edp": ("edp", "equacao de onda", "difusao", "navier", "schrodinger", "calor"),
    "estatistica": ("estat", "estimador", "regressao", "inferencia", "dados"),
    "etica": ("etica", "justica", "privacidade", "vies", "inclusao"),
    "financas": ("financ", "opcao", "black-scholes", "risco", "seguro", "atuarial"),
    "fisica": ("fisica", "mecanica", "relatividade", "quantica", "cosmolog", "energia"),
    "fourier_sinais": ("fourier", "sinal", "espectral", "frequencia", "wavelet", "audio"),
    "geometria": ("geometr", "curvatura", "variedade", "superficie", "metrica"),
    "grafos_redes": ("grafo", "rede", "arvore", "caminho", "matching", "fluxo maximo"),
    "informacao": ("informacao", "entropia", "codificacao", "compressao", "canal"),
    "logica_fundamentos": ("logica", "prova", "axioma", "godel", "conjunto", "tipo"),
    "medicina": ("medicina", "tumor", "clinico", "epidemi", "farmaco", "mortalidade"),
    "numerico": ("numerico", "aproximacao", "elementos finitos", "diferencas finitas", "erro"),
    "numeros": ("numero", "primo", "diofant", "zeta", "aritmetica", "fatoracao"),
    "otimizacao": ("otimiz", "programacao", "simplex", "heuristica", "portfolio"),
    "probabilidade": ("probabil", "estocast", "markov", "browniano", "poisson", "aleator"),
    "processos_biologicos": ("presa", "predador", "sir", "seir", "morfogen", "hodgkin"),
    "robotica_visao": ("robot", "visao", "slam", "cinematica", "trajetoria"),
    "series_temporais": ("serie temporal", "arima", "previsao", "sazonal", "kalman"),
    "sistemas_complexos": ("complexo", "emergencia", "auto-organizacao", "agente", "criticalidade"),
    "topologia": ("topolog", "homologia", "homotopia", "cohomologia", "nos", "3-variedade"),
}

PONTES = {
    ("algebra", "geometria"), ("algebra", "numeros"),
    ("algoritmos", "aprendizagem"), ("algoritmos", "criptografia"),
    ("aprendizagem", "estatistica"), ("aprendizagem", "informacao"),
    ("biologia", "estatistica"), ("biologia", "processos_biologicos"),
    ("calculo", "dinamica"), ("calculo", "edp"),
    ("combinatoria", "grafos_redes"), ("computacao_quantica", "informacao"),
    ("controle", "dinamica"), ("controle", "otimizacao"),
    ("criptografia", "numeros"), ("decisao", "otimizacao"),
    ("dinamica", "sistemas_complexos"), ("edp", "fisica"),
    ("estatistica", "probabilidade"), ("financas", "probabilidade"),
    ("fisica", "geometria"), ("fourier_sinais", "informacao"),
    ("fourier_sinais", "edp"), ("geometria", "topologia"),
    ("grafos_redes", "sistemas_complexos"), ("informacao", "probabilidade"),
    ("logica_fundamentos", "categorias"), ("medicina", "biologia"),
    ("numerico", "edp"), ("numerico", "otimizacao"),
    ("robotica_visao", "controle"), ("robotica_visao", "geometria"),
    ("series_temporais", "estatistica"), ("series_temporais", "probabilidade"),
}

COBERTURA_EXPLICITA = {
    "modelos populacionais": ("modelos_populacionais_novo",),
    "presa-predador": ("presa_predador_novo",),
    "propagacao de doencas": ("propagacao_doencas",),
    "epidemiologia matematica": ("propagacao_doencas", "modelos_ecologia_epidemiologia"),
    "reacao-difusao": ("reacao_difusao",),
    "padroes de turing": ("reacao_difusao",),
    "filogenetica": ("filogenetica",),
    "arvores filogeneticas": ("filogenetica",),
    "alinhamento de sequencias": ("smith_waterman",),
    "smith-waterman": ("smith_waterman",),
    "dobramento de proteinas": ("dobramento_proteinas",),
    "redes reguladoras genicas": ("redes_genicas_booleanas",),
    "hodgkin-huxley": ("hodgkin_huxley",),
    "lindenmayer": ("l_systems",),
    "l-systems": ("l_systems",),
    "informacao mutua": ("informacao_mutua_kl",),
    "entropia shannon": ("entropia_shannon",),
    "regressao logistica": ("regressao_logistica",),
    "support vector": ("svm",),
    "maquina de vetores": ("svm",),
    "redes neurais": ("redes_neurais",),
    "algoritmos geneticos": ("algoritmos_geneticos",),
    "series de fourier": ("series_fourier", "series_fourier_psf"),
    "transformada de fourier": ("transformada_fourier_r", "transformada_fourier_rn"),
    "programacao inteira": ("otimizacao_inteira",),
    "programacao linear": ("otimizacao_linear", "programacao_linear"),
    "teoria das filas": ("teoria_filas",),
    "cadeias de markov": ("markov_decisao",),
    "curvas elipticas": ("curvas_elipticas_lei_grupo", "criptografia_curvas_elipticas"),
    "polinomio de jones": ("polinomio_jones",),
    "polinomio de alexander": ("polinomio_alexander",),
    "homologia khovanov": ("homologia_khovanov",),
    "cirurgia de dehn": ("cirurgia_dehn",),
}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9+#-]+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def slug(texto: str) -> str:
    return normalizar(texto).replace(" ", "_")


def tokens_relevantes(texto: str) -> set[str]:
    return {
        token for token in normalizar(texto).replace("-", " ").split()
        if token not in PALAVRAS_VAZIAS and len(token) >= 3
    }


def ler_aulas(caminho: Path) -> list[dict]:
    aulas = []
    area = None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        cabecalho = re.match(r"Aulas (\d+) a (\d+) — (.+)", linha)
        if cabecalho:
            area = cabecalho.group(3).strip()
            continue
        item = re.match(r"^(\d{3,4})\s+(.+)$", linha)
        if item and 361 <= int(item.group(1)) <= 1000:
            aulas.append({
                "aula": int(item.group(1)),
                "tema": item.group(2).strip(),
                "area": area,
            })
    numeros = {aula["aula"] for aula in aulas}
    faltantes = sorted(set(range(361, 1001)) - numeros)
    if len(aulas) != 640 or faltantes:
        raise ValueError(f"Fonte incompleta: {len(aulas)} aulas; faltantes={faltantes}")
    return aulas


def ler_motores() -> list[str]:
    arvore = ast.parse(ARQUIVO_CODIGO.read_text(encoding="utf-8"))
    classe = next(
        no for no in arvore.body
        if isinstance(no, ast.ClassDef) and no.name == "PSFCalculadora"
    )
    atribuicao = next(
        no for no in classe.body
        if isinstance(no, ast.Assign)
        and any(isinstance(alvo, ast.Name) and alvo.id == "ORDEM_MOTORES" for alvo in no.targets)
    )
    return [item.value for item in atribuicao.value.elts]


def conceitos_da_aula(aula: dict) -> list[str]:
    texto = normalizar(f"{aula['area']} {aula['tema']}")
    palavras = texto.replace("-", " ").split()

    def corresponde(marca: str) -> bool:
        marca_normalizada = normalizar(marca)
        if " " in marca_normalizada:
            return re.search(
                rf"(?:^|\s){re.escape(marca_normalizada)}(?:\s|$)",
                texto,
            ) is not None
        if len(marca_normalizada) < 3:
            return False
        return any(palavra.startswith(marca_normalizada) for palavra in palavras)

    encontrados = []
    for conceito, marcas in CONCEITOS.items():
        if any(corresponde(marca) for marca in marcas):
            encontrados.append(conceito)
    return sorted(set(encontrados))


def avaliar_cobertura(tema: str, motores: list[str]) -> tuple[str, list[str]]:
    texto = normalizar(tema)
    evidencias_explicitas = []
    for frase, candidatos in COBERTURA_EXPLICITA.items():
        if normalizar(frase) in texto:
            evidencias_explicitas.extend(m for m in candidatos if m in motores)
    if evidencias_explicitas:
        return "TEMOS", sorted(set(evidencias_explicitas))

    tema_tokens = tokens_relevantes(tema)
    pontuados = []
    for motor in motores:
        motor_tokens = tokens_relevantes(motor.replace("_", " "))
        comuns = tema_tokens & motor_tokens
        if not comuns:
            continue
        cobertura_motor = len(comuns) / max(1, len(motor_tokens))
        cobertura_tema = len(comuns) / max(1, len(tema_tokens))
        forte = (
            motor_tokens <= tema_tokens
            or (len(comuns) >= 2 and min(cobertura_motor, cobertura_tema) >= 0.45)
            or (len(motor_tokens) == 1 and next(iter(motor_tokens)) in tema_tokens)
        )
        pontuados.append((forte, cobertura_motor + cobertura_tema, motor))
    pontuados.sort(reverse=True)
    fortes = [motor for forte, _, motor in pontuados if forte][:3]
    if fortes:
        return "TEMOS", fortes
    parciais = [motor for _, _, motor in pontuados][:3]
    if parciais:
        return "PARCIAL", parciais
    return "NAO_TEMOS", []


def adicionar_aresta(arestas: list[dict], vistos: set[tuple], origem: str, destino: str, tipo: str) -> None:
    chave = (origem, destino, tipo)
    if chave not in vistos:
        vistos.add(chave)
        arestas.append({"origem": origem, "destino": destino, "tipo": tipo})


def montar_grafo(aulas: list[dict], motores: list[str]) -> dict:
    nos = []
    arestas = []
    vistos = set()
    areas = sorted({aula["area"] for aula in aulas})
    for area in areas:
        nos.append({"id": f"area:{slug(area)}", "tipo": "area", "rotulo": area})
    for conceito in sorted(CONCEITOS):
        nos.append({"id": f"conceito:{conceito}", "tipo": "conceito", "rotulo": conceito.replace("_", " ").title()})
    for motor in motores:
        nos.append({"id": f"motor:{motor}", "tipo": "motor", "rotulo": motor})

    anterior_por_area = {}
    for aula in aulas:
        status, evidencias = avaliar_cobertura(aula["tema"], motores)
        conceitos = conceitos_da_aula(aula)
        aula.update(status=status, evidencias=evidencias, conceitos=conceitos)
        identificador = f"aula:{aula['aula']}"
        nos.append({
            "id": identificador,
            "tipo": "aula",
            "rotulo": f"{aula['aula']} — {aula['tema']}",
            "area": aula["area"],
            "status": status,
        })
        adicionar_aresta(arestas, vistos, identificador, f"area:{slug(aula['area'])}", "pertence_a")
        for conceito in conceitos:
            adicionar_aresta(arestas, vistos, identificador, f"conceito:{conceito}", "expressa")
        for motor in evidencias:
            adicionar_aresta(arestas, vistos, identificador, f"motor:{motor}", "implementado_por" if status == "TEMOS" else "relacionado_a")
        anterior = anterior_por_area.get(aula["area"])
        if anterior is not None:
            adicionar_aresta(arestas, vistos, f"aula:{anterior}", identificador, "prepara")
        anterior_por_area[aula["area"]] = aula["aula"]

    for primeiro, segundo in sorted(PONTES):
        adicionar_aresta(arestas, vistos, f"conceito:{primeiro}", f"conceito:{segundo}", "ponte_semantica")

    motores_ligados = sorted({
        aresta["destino"].removeprefix("motor:")
        for aresta in arestas
        if aresta["destino"].startswith("motor:")
    })

    return {
        "metadata": {
            "intervalo": [361, 1000],
            "total_aulas": len(aulas),
            "total_areas": len(areas),
            "total_motores": len(motores),
            "motores_ligados": len(motores_ligados),
            "motores_sem_ligacao": sorted(set(motores) - set(motores_ligados)),
            "regra": "Somente relações estruturais, lexicais ou curadas são criadas; não há limite artificial de ligações.",
        },
        "nos": nos,
        "arestas": arestas,
        "aulas": aulas,
    }


def gerar_mermaid() -> str:
    linhas = ["flowchart LR"]
    for primeiro, segundo in sorted(PONTES):
        a = primeiro.replace("_", " ").title()
        b = segundo.replace("_", " ").title()
        linhas.append(f"    {primeiro}[{a}] --> {segundo}[{b}]")
    return "\n".join(linhas)


def gerar_plano(grafo: dict, fonte: Path) -> str:
    aulas = grafo["aulas"]
    contagem = Counter(aula["status"] for aula in aulas)
    por_area = defaultdict(Counter)
    for aula in aulas:
        por_area[aula["area"]][aula["status"]] += 1
    sem_semantica = [aula["aula"] for aula in aulas if not aula["conceitos"]]
    motores_sem_ligacao = grafo["metadata"]["motores_sem_ligacao"]
    resumo_motores_sem_ligacao = ", ".join(
        f"`{motor}`" for motor in motores_sem_ligacao
    )
    linhas = [
        "# Plano do Mapa de Conhecimento — Aulas 361 a 1000",
        "",
        "> Estado vivo do conhecimento da PSF Calculadora. O mapa não cria ligações por aparência: cada aresta tem um tipo e uma justificativa reproduzível.",
        "",
        "## Escopo e legenda",
        "",
        f"- Fonte analisada: `{fonte.name}`.",
        f"- Aulas preservadas: **{len(aulas)}**, sem lacunas, de 361 a 1000.",
        f"- Áreas: **{grafo['metadata']['total_areas']}**.",
        f"- Motores examinados: **{grafo['metadata']['total_motores']}**.",
        f"- Motores ligados ao material: **{grafo['metadata']['motores_ligados']}**.",
        f"- Nós: **{len(grafo['nos'])}**; ligações documentadas: **{len(grafo['arestas'])}**.",
        "- `✅ TEMOS`: existe motor específico ou correspondência forte no código.",
        "- `🟡 PARCIAL`: existe conhecimento vizinho, mas não implementação específica comprovada.",
        "- `⬜ NÃO TEMOS`: nenhum motor foi ligado sem evidência.",
        "- `pertence_a`, `prepara`, `expressa`, `implementado_por`, `relacionado_a` e `ponte_semantica` são os únicos tipos de ligação.",
        "",
        "## Estado atual",
        "",
        f"- ✅ Temos: **{contagem['TEMOS']}** aulas.",
        f"- 🟡 Parcial: **{contagem['PARCIAL']}** aulas.",
        f"- ⬜ Não temos: **{contagem['NAO_TEMOS']}** aulas.",
        "",
        "O status mede presença de capacidade no código, não profundidade pedagógica. Toda marcação `TEMOS` deve continuar acompanhada do nome do motor que serve como evidência.",
        "",
        "## Como o conhecimento flui",
        "",
        "```mermaid",
        gerar_mermaid(),
        "```",
        "",
        "A visualização completa está em `mapa_conhecimento_361_1000.json`. A navegação ocorre como numa teia: `aula → conceito → outra aula`, `aula → motor` e `aula → próxima aula`. Um hub pode receber centenas ou milhares de ligações; o gerador não impõe limite.",
        "",
        "## Cobertura por área",
        "",
        "| Área | ✅ Temos | 🟡 Parcial | ⬜ Não temos |",
        "|---|---:|---:|---:|",
    ]
    for area in sorted(por_area):
        valores = por_area[area]
        linhas.append(f"| {area.replace('|', '/')} | {valores['TEMOS']} | {valores['PARCIAL']} | {valores['NAO_TEMOS']} |")

    linhas.extend([
        "",
        "## Aulas sem hub semântico adicional",
        "",
        "Todas as aulas possuem ao menos as ligações estruturais `pertence_a` e `prepara`. As aulas abaixo ainda não receberam um hub conceitual além da própria área; elas foram documentadas, não ligadas artificialmente:",
        "",
        ", ".join(map(str, sem_semantica)) if sem_semantica else "Nenhuma.",
        "",
        "## Motores existentes sem ligação comprovada a estas aulas",
        "",
        "Estes motores existem no projeto, mas o processo não encontrou evidência suficiente para ligá-los ao recorte 361–1000. Permanecem documentados e isolados, como solicitado:",
        "",
        resumo_motores_sem_ligacao if resumo_motores_sem_ligacao else "Nenhum.",
        "",
        "## Plano de evolução",
        "",
        "- [x] Preservar as 640 aulas e as 64 áreas.",
        "- [x] Ligar aulas a áreas, conceitos, sequência didática e motores comprovados.",
        "- [x] Marcar `TEMOS`, `PARCIAL` e `NÃO TEMOS` com evidência.",
        "- [x] Manter arquivo JSON consumível por visualizadores de grafos.",
        "- [ ] Revisar manualmente os itens `PARCIAL`, começando pelas áreas com maior número de lacunas.",
        "- [ ] Auditar cada item `TEMOS` com um teste funcional antes de considerá-lo cobertura pedagógica completa.",
        "- [ ] Criar testes de competência para cada item promovido de `PARCIAL` para `TEMOS`.",
        "- [ ] Migrar motores comprovados para módulos de domínio antes de retirar o monólito.",
        "- [ ] Acrescentar novas aulas sem renumerar ou apagar relações históricas.",
        "",
        "## Inventário completo",
        "",
    ])
    simbolo = {"TEMOS": "✅", "PARCIAL": "🟡", "NAO_TEMOS": "⬜"}
    area_atual = None
    for aula in aulas:
        if aula["area"] != area_atual:
            area_atual = aula["area"]
            linhas.extend([
                f"### {aula['aula'] // 10 * 10 + 1 if aula['aula'] % 10 else aula['aula'] - 9}–{aula['aula'] // 10 * 10 + 10 if aula['aula'] % 10 else aula['aula']} — {area_atual}",
                "",
                "| Aula | Tema | Estado | Evidência no projeto | Hubs conceituais |",
                "|---:|---|---|---|---|",
            ])
        evidencias = ", ".join(f"`{motor}`" for motor in aula["evidencias"]) or "—"
        conceitos = ", ".join(aula["conceitos"]) or "somente área/sequência"
        tema = aula["tema"].replace("|", "/")
        linhas.append(f"| {aula['aula']} | {tema} | {simbolo[aula['status']]} {aula['status'].replace('_', ' ')} | {evidencias} | {conceitos} |")
    linhas.extend([
        "",
        "## Regra de manutenção",
        "",
        "Uma nova ligação só entra no mapa quando houver pelo menos uma destas evidências: pertencimento explícito a uma área, sequência curricular, termo conceitual reconhecido, ponte curada ou motor real no código. Ausência de evidência deve permanecer documentada como ausência, nunca preenchida por suposição.",
        "",
    ])
    return "\n".join(linhas)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("fonte", type=Path, help="Arquivo de texto com as aulas")
    args = parser.parse_args()
    aulas = ler_aulas(args.fonte)
    motores = ler_motores()
    grafo = montar_grafo(aulas, motores)
    grafo["metadata"]["fonte_sha256"] = hashlib.sha256(args.fonte.read_bytes()).hexdigest()
    ARQUIVO_PLANO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO_GRAFO.write_text(
        json.dumps(grafo, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    ARQUIVO_PLANO.write_text(gerar_plano(grafo, args.fonte), encoding="utf-8")
    print(f"Plano: {ARQUIVO_PLANO}")
    print(f"Grafo: {ARQUIVO_GRAFO}")


if __name__ == "__main__":
    main()
