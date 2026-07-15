import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lingua_portuguesa import MotorPortugues
from lingua_portuguesa.conhecimento_puro import ConstrutorConhecimentoPortugues


def test_conhecimento_portugues_tem_ordem_pura_do_minimo_ao_texto():
    construtor = ConstrutorConhecimentoPortugues()
    caminho = construtor.caminho_natural()
    assert caminho[:5] == ("diferença", "som", "pausa", "marca", "grafema")
    assert "palavra" in caminho
    assert "texto" in caminho
    assert caminho[-1] == "funcionamento"
    assert construtor.validar_ordem()


def test_motor_expoe_funcionamento_sem_aula_pergunta_ou_resposta_pronta():
    motor = MotorPortugues()
    funcionamento = motor.funcionamento_portugues()
    texto = "\n".join(funcionamento).casefold()
    assert "diferença mínima" in texto
    assert "grafema" in texto
    assert "gramática" in texto
    assert "aula" not in texto
    assert "pergunta" not in texto
    assert "resposta pronta" not in texto


def test_motor_define_conceito_puro_sem_fingir_desconhecido():
    motor = MotorPortugues()
    assert motor.definir_conceito_puro("palavra").startswith("Palavra é combinação")
    assert motor.definir_conceito_puro("fonética total") is None


def test_lexico_reconhece_conceitos_novos_do_portugues():
    motor = MotorPortugues()
    analise = motor.analisar("A palavra tem sentido no texto.")
    lemas = tuple(item.principal.lema for item in analise.morfologia if item.token.texto.isalpha())
    assert "palavra" in lemas
    assert "sentido" in lemas
    assert "texto" in lemas


def test_portugues_cresceu_morfologia_sintaxe_texto_sem_saltar_ordem():
    construtor = ConstrutorConhecimentoPortugues()
    caminho = construtor.caminho_natural()
    assert len(caminho) >= 49
    for nome in (
        "morfema",
        "radical",
        "prefixo",
        "sufixo",
        "flexão",
        "concordância",
        "parágrafo",
        "coerência",
        "coesão",
    ):
        assert nome in caminho
    assert caminho.index("morfema") > caminho.index("lema")
    assert caminho.index("concordância") > caminho.index("relação")
    assert caminho.index("texto") > caminho.index("parágrafo")
    assert construtor.validar_pureza()


def test_motor_devolve_dependencias_e_trilho_sem_fingir():
    motor = MotorPortugues()
    assert motor.dependencias_conceito_puro("concordância") == (
        "relação",
        "gênero",
        "número gramatical",
        "classe gramatical",
    )
    trilho = motor.trilho_ate_conceito_puro("morfema")
    assert trilho[-1] == "morfema"
    assert "palavra" in trilho
    assert motor.trilho_ate_conceito_puro("gramática total externa") == ()


def test_lexico_portugues_expandido_reconhece_novos_conceitos():
    motor = MotorPortugues()
    for palavra in ("morfema", "concordância", "parágrafo", "coerência", "coesão"):
        assert motor.definir(palavra)
    estatisticas = motor.estatisticas_lexico()
    assert estatisticas["lemas"] >= 300
    assert estatisticas["formas"] >= 800



def test_portugues_cresceu_para_enunciado_referencia_periodo_e_uso():
    construtor = ConstrutorConhecimentoPortugues()
    caminho = construtor.caminho_natural()
    assert len(caminho) >= 75
    for nome in (
        "enunciado",
        "intenção comunicativa",
        "referência",
        "referente",
        "campo semântico",
        "polissemia",
        "conectivo",
        "retomada",
        "inferência",
        "período",
        "coordenação",
        "subordinação",
        "termo",
        "complemento",
        "regência",
        "norma",
        "uso",
        "variação linguística",
        "registro",
    ):
        assert nome in caminho
    assert caminho.index("enunciado") > caminho.index("frase")
    assert caminho.index("período") > caminho.index("oração")
    assert caminho.index("uso") > caminho.index("norma")
    assert caminho[-1] == "funcionamento"
    assert construtor.validar_pureza()


def test_lexico_reconhece_crescimento_portugues_sem_dicionario_externo():
    motor = MotorPortugues()
    for palavra in ("enunciado", "referência", "conectivo", "período", "regência", "norma", "registro"):
        assert motor.definir(palavra)
    estatisticas = motor.estatisticas_lexico()
    assert estatisticas["lemas"] >= 325
    assert estatisticas["formas"] >= 850

def test_portugues_cresceu_para_contexto_modalidade_interpretacao():
    construtor = ConstrutorConhecimentoPortugues()
    caminho = construtor.caminho_natural()
    assert len(caminho) >= 101
    for nome in (
        "contexto",
        "modalidade",
        "afirmação",
        "negação",
        "interrogação",
        "exclamação",
        "tempo verbal",
        "aspecto verbal",
        "modo verbal",
        "voz verbal",
        "preposição",
        "conjunção",
        "interjeição",
        "numeral",
        "artigo",
        "locução",
        "perífrase verbal",
        "discurso direto",
        "discurso indireto",
        "tema",
        "progressão temática",
        "ambiguidade",
        "pragmática",
        "estilo",
        "revisão",
        "interpretação",
    ):
        assert nome in caminho
    assert caminho.index("contexto") > caminho.index("registro")
    assert caminho.index("modalidade") > caminho.index("contexto")
    assert caminho.index("tempo verbal") > caminho.index("verbo")
    assert caminho.index("interpretação") > caminho.index("pragmática")
    assert caminho[-1] == "funcionamento"
    assert construtor.validar_pureza()


def test_lexico_reconhece_crescimento_ate_interpretacao():
    motor = MotorPortugues()
    for palavra in ("modalidade", "negação", "preposição", "conjunção", "locução", "ambiguidade", "pragmática", "interpretação"):
        assert motor.definir(palavra)
    estatisticas = motor.estatisticas_lexico()
    assert estatisticas["lemas"] >= 350
    assert estatisticas["formas"] >= 900



def test_portugues_cresceu_na_mesma_linha_com_temas_apenas_consultivos():
    motor = MotorPortugues()
    estatisticas = motor.estatisticas_conhecimento_portugues()
    assert estatisticas["conceitos"] == 1141
    assert estatisticas["temas_de_consulta"] == 20
    assert estatisticas["conceitos_com_exemplo"] >= 670
    assert estatisticas["relacoes_de_dependencia"] >= 2100
    assert motor.caminho_conhecimento_portugues()[-1] == "funcionamento"


def test_crescimento_cobre_fonetica_ortografia_morfologia_sintaxe_semantica_texto_e_uso():
    motor = MotorPortugues()
    esperados = {
        "fonetica_fonologia": ("fonema", "prosódia", "ditongo"),
        "ortografia": ("ortografia", "acentuação gráfica", "crase"),
        "morfologia_lexico": ("lexema", "derivação", "conjugação"),
        "sintaxe": ("sintagma", "objeto direto", "oração subordinada"),
        "semantica_pragmatica": ("denotação", "metáfora", "implicatura"),
        "texto_discurso": ("gênero textual", "argumentação", "coesão referencial"),
        "variacao_letramento": ("adequação linguística", "leitura", "escrita"),
        "metalinguagem": ("dicionário", "gramaticalidade", "reconstrução linguística PSF"),
    }
    for camada, nomes in esperados.items():
        encontrados = {conceito.nome for conceito in motor.conceitos_por_tema(camada)}
        assert set(nomes) <= encontrados


def test_dependencias_transitivas_reconstroem_conceito_sem_salto():
    motor = MotorPortugues()
    dependencias = motor.dependencias_transitivas_conceito_puro("crase")
    for nome in ("diferença", "grafema", "palavra", "preposição", "artigo", "acento grave"):
        assert nome in dependencias
    assert dependencias.index("diferença") < dependencias.index("grafema")
    assert dependencias.index("grafema") < dependencias.index("acento grave")


def test_todos_os_conceitos_puros_sao_consultaveis_no_lexico_interno():
    motor = MotorPortugues()
    sem_definicao = [
        conceito.nome
        for conceito in motor.conhecimento_puro()
        if not motor.definir(conceito.nome)
    ]
    assert sem_definicao == []
    estatisticas = motor.estatisticas_lexico()
    assert estatisticas["lemas"] >= 670
    assert estatisticas["formas"] >= 1400


def test_busca_interna_encontra_conceito_por_nome_construcao_e_funcao():
    motor = MotorPortugues()
    nomes = {c.nome for c in motor.buscar_conceitos_puros("corrente de ar")}
    assert "corrente de ar" in nomes
    assert "articulação" in nomes
    nomes = {c.nome for c in motor.buscar_conceitos_puros("hierarquias de sentido")}
    assert "hiperonímia" in nomes


def test_conhecimento_puro_nao_importa_dependencia_linguistica_externa():
    import ast
    from pathlib import Path

    caminho = Path(__file__).resolve().parents[1] / "lingua_portuguesa" / "conhecimento_puro.py"
    arvore = ast.parse(caminho.read_text(encoding="utf-8"))
    importacoes = set()
    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            importacoes.update(alias.name.split(".")[0] for alias in no.names)
        elif isinstance(no, ast.ImportFrom) and no.module:
            importacoes.add(no.module.split(".")[0])
    assert importacoes <= {"__future__", "dataclasses"}


def test_integracao_aproveita_conhecimento_util_sem_substituir_base_401():
    motor = MotorPortugues()
    estatisticas = motor.estatisticas_conhecimento_portugues()
    assert estatisticas["conceitos"] == 1141
    assert estatisticas["temas_de_consulta"] == 20
    assert estatisticas["aliases"] >= 8
    for nome in (
        "ato de fala",
        "meronímia",
        "intertextualidade",
        "multimodalidade",
        "aquisição da linguagem",
        "bilinguismo",
        "tradução",
        "sociolinguística",
        "psicolinguística",
        "arcaísmo",
    ):
        assert motor.definir_conceito_puro(nome)


def test_equivalencias_nao_criam_conceitos_duplicados():
    motor = MotorPortugues()
    aliases = motor.aliases_conhecimento_portugues()
    assert aliases["tipologia textual"] == "tipo textual"
    assert aliases["variação diatópica"] == "variação regional"
    assert aliases["variação diastrática"] == "variação social"
    assert aliases["variação diacrônica"] == "variação histórica"
    assert motor.definir_conceito_puro("tipologia textual") == motor.definir_conceito_puro("tipo textual")
    assert motor.definir_conceito_puro("variação diatópica") == motor.definir_conceito_puro("variação regional")


def test_lacunas_antigas_ja_materializadas_foram_corrigidas():
    construtor = ConstrutorConhecimentoPortugues()
    for nome in (
        "encontro vocálico",
        "sílaba tônica",
        "gênero",
        "coordenação",
        "subordinação",
        "transitividade verbal",
        "numeral",
        "locução",
        "morfema",
        "prefixo",
        "sufixo",
    ):
        conceito = construtor.buscar(nome)
        assert conceito is not None
        assert conceito.lacuna == ""


def test_novas_familias_preenchem_fonetica_ortografia_morfologia_sintaxe_e_discurso():
    motor = MotorPortugues()
    esperados = (
        "vogal nasal",
        "consoante sonora",
        "bilabial",
        "assimilação fonológica",
        "regra de proparoxítona",
        "acento em hiato",
        "uso de ç",
        "plural em -ão",
        "substantivo sobrecomum",
        "pretérito imperfeito",
        "futuro do conjuntivo",
        "oração reduzida de infinitivo",
        "oração subordinada substantiva subjetiva",
        "ambiguidade estrutural",
        "ato diretivo",
        "contacto linguístico",
        "numeral fracionário",
        "locução conjuntiva",
        "oração coordenada assindética",
        "coesão lexical",
    )
    for nome in esperados:
        conceito = motor.conhecimento_portugues.buscar(nome)
        assert conceito is not None
        assert conceito.exemplos_minimos or conceito.lacuna


def test_todos_os_1100_conceitos_e_aliases_sao_consultaveis_no_lexico():
    motor = MotorPortugues()
    assert all(motor.definir(c.nome) for c in motor.conhecimento_puro())
    assert motor.definir("tipologia textual")
    assert motor.definir("variação diatópica")
    estatisticas = motor.estatisticas_lexico()
    assert estatisticas["lemas"] >= 1080
    assert estatisticas["formas"] >= 1820


def test_expansao_1100_cobre_estrutura_sonora_escrita_sintaxe_sentido_texto_e_metodo():
    motor = MotorPortugues()
    esperados = (
        "fonotática", "palavra fonológica", "fronteira prosódica",
        "segmentação gráfica", "uso de rr", "vírgula de vocativo",
        "alomorfia", "morfema zero", "verbo irregular",
        "estrutura argumental", "sujeito nulo", "oração finita",
        "significado composicional", "telicidade", "escopo da negação",
        "macroestrutura textual", "estrutura narrativa", "garantia argumentativa",
        "língua primeira", "unidade de tradução", "hipótese linguística",
        "descrição operacional", "análise pragmática", "indeterminação analítica",
        "notícia", "relatório", "poema", "peça teatral",
    )
    for nome in esperados:
        conceito = motor.conhecimento_portugues.buscar(nome)
        assert conceito is not None
        assert conceito.construcao and conceito.funcao
        assert conceito.exemplos_minimos or conceito.lacuna


def test_temas_nao_controlam_ordem_nem_dependencias():
    motor = MotorPortugues()
    conceitos = motor.conhecimento_puro()
    posicao = {c.nome: c.ordem for c in conceitos}
    assert motor.temas_consulta_conhecimento_portugues() == motor.camadas_conhecimento_portugues()
    assert all(posicao[d] < c.ordem for c in conceitos for d in c.depende_de)
    # Dependências atravessam temas; por isso tema não pode ser etapa ou base paralela.
    cruzadas = sum(
        1 for c in conceitos for d in c.depende_de
        if motor.conhecimento_portugues.buscar(d).tema_consulta != c.tema_consulta
    )
    assert cruzadas > 1000


def test_conhecimento_1100_permanece_puro_sem_duplicacao_ou_salto():
    construtor = ConstrutorConhecimentoPortugues()
    nomes = construtor.nomes()
    assert len(nomes) == len(set(nomes)) == 1141
    assert construtor.validar_ordem()
    assert construtor.validar_pureza()
    assert nomes[-1] == "funcionamento"


def test_mestria_conceitual_sem_lacuna_interna_e_sem_fingir_mundo_aberto():
    motor = MotorPortugues()
    estatisticas = motor.estatisticas_conhecimento_portugues()
    assert estatisticas["conceitos"] == 1141
    assert estatisticas["lacunas_internas"] == 0
    assert estatisticas["fronteiras_abertas"] > 0
    assert estatisticas["limites_operacionais"] > 0
    assert motor.conhecimento_portugues.mestria_conceitual()
    assert motor.caminho_conhecimento_portugues()[-1] == "funcionamento"

def test_expansao_mestra_materializa_familias_antes_ausentes():
    motor = MotorPortugues()
    esperados = (
        "traço distintivo", "sândi externo", "ordem lexicográfica",
        "porquê substantivo", "raiz morfológica", "classe de conjugação",
        "oração interrogativa indireta total", "construção de controlo",
        "modalidade epistémica", "implicatura conversacional",
        "falácia de circularidade", "focalização interna",
        "consciência metalinguística", "mestria conceitual",
    )
    for nome in esperados:
        assert motor.conhecimento_portugues.buscar(nome) is not None
        assert motor.definir(nome)

def test_todos_os_conceitos_mestres_tem_exemplo_minimo():
    motor = MotorPortugues()
    novos = [c for c in motor.conhecimento_puro() if 785 <= c.ordem < 1100]
    assert len(novos) == 315
    assert all(c.exemplos_minimos for c in novos)


def test_conceitos_fundacionais_tem_exemplo_real_nao_generico():
    # achado real: os 20 primeiros conceitos (diferença -> lema, a base
    # fonética/gráfica exata que qualquer aula de português precisa
    # percorrer primeiro) tinham `exemplos_minimos=()` no código-fonte --
    # um fallback (`_conceito_sem_lacuna_interna`) preenchia isso com texto
    # genérico fabricado ("Aplicação mínima: reconhecer X..."), mascarando
    # a lacuna real em vez de expor. Corrigido com exemplo linguístico
    # concreto e verificável para cada um; este teste tranca o achado.
    motor = MotorPortugues()
    fundacionais = [c for c in motor.conhecimento_puro() if 1 <= c.ordem <= 20]
    assert len(fundacionais) == 20
    for conceito in fundacionais:
        assert conceito.exemplos_minimos, f"{conceito.nome} sem exemplo"
        assert not conceito.exemplos_minimos[0].startswith("Aplicação mínima: reconhecer"), (
            f"{conceito.nome} ainda usa o exemplo genérico de fallback"
        )


def test_nenhum_conceito_de_portugues_usa_exemplo_generico_de_fallback():
    # extensão do achado acima: em vez de corrigir só os fundacionais,
    # todos os 109/1141 conceitos que caíam no fallback genérico
    # (`_conceito_sem_lacuna_interna`) ganharam exemplo real e verificável.
    # Este teste tranca que nenhum concento no grafo inteiro ainda usa o
    # texto fabricado -- se um novo conceito futuro cair no mesmo buraco,
    # este teste falha e acusa, em vez de deixar passar em silêncio.
    motor = MotorPortugues()
    genericos = [
        c for c in motor.conhecimento_puro()
        if c.exemplos_minimos and c.exemplos_minimos[0].startswith("Aplicação mínima: reconhecer")
    ]
    assert genericos == [], f"conceitos ainda com exemplo genérico: {[c.nome for c in genericos]}"
