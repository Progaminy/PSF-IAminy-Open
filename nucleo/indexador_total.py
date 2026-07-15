# -*- coding: utf-8 -*-
"""
Etapa 64 — Indexador Total Vivo.

Correção de integridade: o PSF não pode depender de uma base pequena como
"300 perguntas" quando o utilizador despejou milhares de entradas ao longo do
projeto. Este módulo varre TODO o projeto materializado em ficheiros e cria
uma busca local simples, auditável e sem dependências externas.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re
import unicodedata
from functools import lru_cache

EXTENSOES_TEXTO = {'.md', '.txt', '.py', '.json', '.jsonl', '.csv'}
IGNORAR_PARTES = {'__pycache__', '.pytest_cache', '.git', '.mypy_cache', '.ruff_cache', 'node_modules', 'venv', '.venv'}
IGNORAR_EXT = {'.zip', '.pyc', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.pdf', '.docx', '.sqlite', '.db'}
IGNORAR_PREFIXOS_REL = (
    'interface/dados/conversas/',  # histórico antigo de chat não deve virar conhecimento
    'testes/',                     # testes validam comportamento; não são fonte de resposta ao usuário
)
IGNORAR_NOMES = {
    'INDICE_TOTAL_VIVO_ETAPA64.json',  # índice gerado não deve indexar a si próprio
    'auditoria_chat_vivo.jsonl',       # logs do chat não devem virar conhecimento
    'falhas_chat_vivo.jsonl',          # falhas do chat não devem virar conhecimento
}
PALAVRAS_FRACAS = {
    'o','a','os','as','um','uma','uns','umas','de','do','da','dos','das','e','ou',
    'que','qual','quais','quanto','quantos','porque','por','como','onde','quando',
    'para','com','sem','em','no','na','nos','nas','se','ser','sao','são','é','e',
    'me','te','voce','você','tu','isto','isso','aquilo','dê','de','explique',
    'provar','prove','demonstre','calcule','construa','crie','sobre',
    'pode','podes','consegue','consegues','ensina','ensinar','ensinas',
    'aprender','ajuda','ajude','quero','gostaria',
}

@dataclass(frozen=True, slots=True)
class RegistroTotal:
    id: str
    caminho: str
    etapa: str
    tipo: str
    titulo: str
    trecho: str
    tokens: tuple[str, ...]

@dataclass(frozen=True, slots=True)
class ResultadoBuscaTotal:
    encontrado: bool
    consulta: str
    score: int
    registro: RegistroTotal | None
    motivo: str


def raiz_projeto() -> Path:
    return Path(__file__).resolve().parents[1]


def sem_acentos(texto: str) -> str:
    texto = unicodedata.normalize('NFD', str(texto))
    return ''.join(ch for ch in texto if unicodedata.category(ch) != 'Mn')


def normalizar(texto: str) -> str:
    t = sem_acentos(texto).casefold()
    trocas = {
        'voçe': 'voce', 'vc': 'voce', 'ti criou': 'te criou', 'dispejei': 'despejei',
        'engeutei': 'injetei', 'enjectei': 'injetei', 'motvydo': 'motivo',
        'peguntas': 'perguntas', 'brexas': 'brechas', 'lacunas': 'lacunas',
    }
    for a, b in trocas.items():
        t = t.replace(a, b)
    t = re.sub(r'[^a-z0-9]+', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def tokens_de(texto: str) -> tuple[str, ...]:
    toks: list[str] = []
    for tok in normalizar(texto).split():
        if len(tok) >= 3 and tok not in PALAVRAS_FRACAS:
            toks.append(tok)
    vistos = set(); saida: list[str] = []
    for t in toks:
        if t not in vistos:
            vistos.add(t); saida.append(t)
    return tuple(saida)


def _deve_ignorar(path: Path) -> bool:
    if any(parte in IGNORAR_PARTES for parte in path.parts):
        return True
    if path.suffix.casefold() in IGNORAR_EXT:
        return True
    if path.name in IGNORAR_NOMES:
        return True
    try:
        rel = str(path.relative_to(raiz_projeto())).replace('\\', '/')
    except ValueError:
        rel = str(path).replace('\\', '/')
    if any(rel.startswith(prefixo) for prefixo in IGNORAR_PREFIXOS_REL):
        return True
    if path.name.startswith('.'):
        return True
    # Documentação operacional, auditorias e históricos validam o projeto,
    # mas não são fonte de resposta semântica ao usuário: podem conter termos
    # adversariais de teste e causar falso positivo confiante.
    nome = path.name
    if nome in {'README.md', 'COMO_RODAR.md', 'VALIDACAO.md', 'ROADMAP.md', 'REGRA_VERSAO_UNICA.md'}:
        return True
    if nome.startswith(('AUDITORIA_', 'HISTORICO_', 'RESULTADO_TESTE_')):
        return True
    return False


def _ler_texto(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding='latin-1')
        except Exception:
            return ''
    except Exception:
        return ''


def _extrair_etapa(caminho_rel: str, texto: str) -> str:
    alvo = caminho_rel + '\n' + texto[:2000]
    achados = re.findall(r'(?:ETAPA|etapa)[_\-\s]*(\d{1,5})', alvo)
    if achados:
        return 'ETAPA_' + achados[0]
    achados = re.findall(r'PSF\-K\s*(\d{1,5})', alvo, flags=re.I)
    if achados:
        return 'PSF-K_' + achados[0]
    return 'DESCONHECIDA'


def _tipo(caminho_rel: str) -> str:
    c = caminho_rel.casefold()
    nome = Path(caminho_rel).name.casefold()
    if 'auditoria' in nome: return 'auditoria'
    if 'indice' in nome or 'índice' in nome: return 'indice'
    if 'dossie' in nome or 'dossiê' in nome: return 'dossie'
    if 'regra' in nome: return 'regra'
    if 'teste' in c or c.startswith('testes/'): return 'teste'
    if c.startswith('ensino/') or 'aula' in nome: return 'aula'
    if c.startswith('nucleo/'): return 'nucleo'
    if c.startswith('conhecimento/'): return 'conhecimento'
    if c.startswith('validacao_externa/'): return 'validacao_externa'
    return 'arquivo'


def _titulo(caminho_rel: str, texto: str) -> str:
    for linha in texto.splitlines()[:80]:
        l = linha.strip()
        if not l:
            continue
        if l.startswith('#'):
            return l.lstrip('#').strip()[:140]
        if l.startswith('"""') or l.startswith("''"):
            continue
        if len(l) > 8 and not l.startswith(('from ', 'import ', '@')):
            return l[:140]
    return Path(caminho_rel).name


def _limpar_trecho(t: str, max_len: int = 900) -> str:
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) <= max_len:
        return t
    return t[:max_len].rstrip() + '...'


def _blocos(texto: str, max_len: int = 1400) -> list[str]:
    partes = [p.strip() for p in re.split(r'\n\s*\n', texto) if p.strip()]
    blocos: list[str] = []
    atual = ''
    for p in partes:
        if len(p) > max_len:
            if atual:
                blocos.append(atual); atual = ''
            for i in range(0, len(p), max_len):
                ped = p[i:i+max_len].strip()
                if ped:
                    blocos.append(ped)
            continue
        if not atual:
            atual = p
        elif len(atual) + len(p) + 2 <= max_len:
            atual += '\n\n' + p
        else:
            blocos.append(atual); atual = p
    if atual:
        blocos.append(atual)
    return blocos


@lru_cache(maxsize=1)
def construir_indice_total() -> tuple[RegistroTotal, ...]:
    raiz = raiz_projeto()
    registros: list[RegistroTotal] = []
    for path in sorted(raiz.rglob('*')):
        if not path.is_file() or _deve_ignorar(path):
            continue
        if path.suffix.casefold() not in EXTENSOES_TEXTO:
            continue
        rel = str(path.relative_to(raiz)).replace('\\', '/')
        texto = _ler_texto(path)
        if not texto.strip():
            continue
        etapa = _extrair_etapa(rel, texto)
        tipo = _tipo(rel)
        titulo = _titulo(rel, texto)
        for n, bloco in enumerate(_blocos(texto), 1):
            toks = tokens_de(titulo + ' ' + bloco + ' ' + rel)
            if not toks:
                continue
            registros.append(RegistroTotal(
                id=f'{rel}#b{n}', caminho=rel, etapa=etapa, tipo=tipo,
                titulo=titulo, trecho=_limpar_trecho(bloco), tokens=toks,
            ))
    return tuple(registros)


def estatisticas() -> dict:
    regs = construir_indice_total()
    por_tipo: dict[str, int] = {}
    por_etapa: dict[str, int] = {}
    arquivos = set()
    for r in regs:
        por_tipo[r.tipo] = por_tipo.get(r.tipo, 0) + 1
        por_etapa[r.etapa] = por_etapa.get(r.etapa, 0) + 1
        arquivos.add(r.caminho)
    return {
        'registros': len(regs),
        'arquivos_indexados': len(arquivos),
        'tipos': dict(sorted(por_tipo.items())),
        'etapas_detectadas': dict(sorted(por_etapa.items())),
    }


def _pontuar(consulta_norm: str, consulta_tokens: tuple[str, ...], r: RegistroTotal) -> int:
    texto_norm = normalizar(r.titulo + ' ' + r.trecho + ' ' + r.caminho)
    score = 0
    if consulta_norm and consulta_norm in texto_norm:
        score += 120
    for janela in (3, 2):
        if len(consulta_tokens) >= janela:
            for i in range(len(consulta_tokens) - janela + 1):
                frase = ' '.join(consulta_tokens[i:i+janela])
                if frase and frase in texto_norm:
                    score += 15 * janela
    rtoks = set(r.tokens)
    for tok in consulta_tokens:
        if tok in rtoks:
            score += 10
        elif any(tok in rt or rt in tok for rt in rtoks if len(rt) >= 5):
            score += 4
    if r.tipo in {'conhecimento', 'dossie', 'indice', 'regra', 'nucleo', 'aula'}:
        score += 6
    if r.tipo == 'teste':
        score -= 4
    return score


def buscar_total(consulta: str, limite: int = 5) -> list[ResultadoBuscaTotal]:
    consulta_norm = normalizar(consulta)
    consulta_tokens = tokens_de(consulta)
    if not consulta_tokens and len(consulta_norm) < 3:
        return []
    candidatos: list[tuple[int, RegistroTotal]] = []
    for r in construir_indice_total():
        score = _pontuar(consulta_norm, consulta_tokens, r)
        if score > 0:
            candidatos.append((score, r))
    candidatos.sort(key=lambda x: (x[0], x[1].tipo != 'teste'), reverse=True)
    saida: list[ResultadoBuscaTotal] = []
    vistos = set()
    for score, r in candidatos:
        if r.id in vistos:
            continue
        vistos.add(r.id)
        if score < max(18, len(consulta_tokens) * 4):
            continue
        saida.append(ResultadoBuscaTotal(True, consulta, score, r, 'encontrado_no_indice_total'))
        if len(saida) >= limite:
            break
    return saida


def responder_por_indice_total(consulta: str) -> str | None:
    resultados = buscar_total(consulta, limite=3)
    if not resultados:
        return None
    linhas = ['Encontrei isto no índice total do projeto materializado. Não vou fingir que é prova final; vou mostrar a fonte e o trecho encontrado.']
    for i, res in enumerate(resultados, 1):
        r = res.registro
        if r is None:
            continue
        linhas.append(
            f"{i}. Fonte: {r.caminho} | {r.etapa} | tipo: {r.tipo} | score: {res.score}\n"
            f"   Título: {r.titulo}\n"
            f"   Trecho: {r.trecho}"
        )
    linhas.append('Próximo passo PSF: se o trecho for curto, expandir para resposta, aula, teste e auditoria; se já houver aula/prova, encaminhar para ela.')
    return '\n\n'.join(linhas)


def exportar_indice_json(destino: str | None = None) -> str:
    raiz = raiz_projeto()
    destino_path = Path(destino) if destino else raiz / 'conhecimento' / 'INDICE_TOTAL_VIVO_ETAPA64.json'
    regs = construir_indice_total()
    dados = [
        {
            'id': r.id, 'caminho': r.caminho, 'etapa': r.etapa, 'tipo': r.tipo,
            'titulo': r.titulo, 'trecho': r.trecho[:500], 'tokens': list(r.tokens[:40]),
        }
        for r in regs
    ]
    destino_path.write_text(json.dumps({'estatisticas': estatisticas(), 'registros': dados}, ensure_ascii=False, indent=2), encoding='utf-8')
    return str(destino_path)


if __name__ == '__main__':
    print(json.dumps(estatisticas(), ensure_ascii=False, indent=2))
