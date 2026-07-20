"""Item real do README ("materializar paradigmas regulares e irregulares
de flexão e conjugação") -- estende `_verbo()` (lexico_expansao.py) do
presente/pretérito perfeito parcial para também cobrir pretérito
imperfeito, futuro do presente, presente do subjuntivo, futuro do
pretérito (condicional) e imperativo afirmativo, cada forma etiquetada
com seu próprio tempo (campo `atributos["tempo"]`, mesma convenção já
usada pelos 11 verbos irregulares em `lexico_base.json`). Corte
deliberadamente estreito: só verbos regulares, só estes 7 tempos --
imperativo negativo (usa subjuntivo em toda pessoa, regra diferente do
afirmativo) e verbos irregulares além dos 11 já existentes continuam
de fora.

Achado ao construir o imperativo afirmativo: ele não introduz nenhuma
string nova -- "tu" reaproveita a forma do presente indicativo 3ª
singular, "você"/"nós"/"vocês" reaproveitam o presente do subjuntivo.
Por isso um mapa ingênuo `{forma: entrada}` (como os testes abaixo já
usavam antes desta mudança) perde uma das duas leituras quando a mesma
string carrega tempo/pessoa diferentes -- os testes que precisam de
uma forma ambígua agora filtram por tempo explicitamente, em vez de
assumir forma↔entrada 1:1.
"""
from lingua_portuguesa.tipos import Numero, Pessoa
from lingua_portuguesa.lexico_expansao import entradas_expandidas, _verbo


def _mapa(lema):
    return {e.forma: e for e in entradas_expandidas() if e.lema == lema}


def _por_tempo(infinitivo, forma, tempo):
    """A mesma `forma` pode carregar mais de uma leitura (ex.: imperativo
    reaproveitando subjuntivo) -- escolhe a leitura do tempo pedido."""
    candidatas = [e for e in _verbo(infinitivo, "x") if e.forma == forma and e.atributos.get("tempo") == tempo]
    assert len(candidatas) == 1, f"esperava 1 leitura de {forma!r} em {tempo!r}, achei {len(candidatas)}"
    return candidatas[0]


def test_preterito_imperfeito_verbo_ar_novo_via_geracao():
    # "conversar" só existe via _verbo() (lexico_expansao.py), não no
    # JSON base -- prova que o imperfeito vem da geração, não de dado
    # já pronto.
    formas = _mapa("conversar")
    assert formas["conversava"].pessoa == Pessoa.PRIMEIRA
    assert formas["conversava"].numero == Numero.SINGULAR
    assert formas["conversava"].atributos["tempo"] == "pretérito imperfeito"
    assert formas["conversávamos"].pessoa == Pessoa.PRIMEIRA
    assert formas["conversávamos"].numero == Numero.PLURAL
    assert formas["conversavam"].pessoa == Pessoa.TERCEIRA
    assert formas["conversavam"].numero == Numero.PLURAL


def test_futuro_do_presente_mesmo_sufixo_nas_tres_conjugacoes():
    for infinitivo, raiz_futuro in (("estudar", "estudar"), ("comer", "comer"), ("partir", "partir")):
        formas = _verbo(infinitivo, "x")
        por_forma = {f.forma: f for f in formas}
        assert por_forma[raiz_futuro + "ei"].atributos["tempo"] == "futuro do presente"
        assert por_forma[raiz_futuro + "ei"].pessoa == Pessoa.PRIMEIRA
        assert por_forma[raiz_futuro + "ei"].numero == Numero.SINGULAR
        assert por_forma[raiz_futuro + "ão"].pessoa == Pessoa.TERCEIRA
        assert por_forma[raiz_futuro + "ão"].numero == Numero.PLURAL


def test_imperfeito_er_e_ir_usa_mesmo_sufixo_ia():
    comer = {f.forma: f for f in _verbo("comer", "x")}
    partir = {f.forma: f for f in _verbo("partir", "x")}
    assert comer["comia"].atributos["tempo"] == "pretérito imperfeito"
    assert partir["partia"].atributos["tempo"] == "pretérito imperfeito"
    assert comer["comíamos"].numero == Numero.PLURAL
    assert partir["partíamos"].numero == Numero.PLURAL


def test_presente_e_preterito_perfeito_continuam_etiquetados_com_tempo():
    # Achado ao estender: antes desta mudança, _verbo() não etiquetava
    # tempo nenhum para presente/pretérito perfeito (só pessoa/número) --
    # agora todos os tempos gerados carregam o mesmo atributo, evitando
    # que presente/perfeito fiquem "sem tempo" enquanto imperfeito/futuro
    # têm.
    formas = {f.forma: f for f in _verbo("estudar", "x")}
    assert formas["estudo"].atributos["tempo"] == "presente"
    assert formas["estudei"].atributos["tempo"] == "pretérito perfeito"
    assert formas["estudar"].atributos == {}


def _por_forma_e_tempo(infinitivo, forma, tempo):
    """Localiza a leitura de `forma` com o `tempo` pedido -- algumas
    formas (ex. "estude") têm duas leituras (subjuntivo e imperativo),
    então um mapa ingênuo `{forma: entrada}` perderia uma delas."""
    candidatas = [f for f in _verbo(infinitivo, "x") if f.forma == forma and f.atributos.get("tempo") == tempo]
    assert len(candidatas) == 1, f"esperava 1 leitura de {forma!r} com tempo={tempo!r}, achei {len(candidatas)}"
    return candidatas[0]


def test_nenhuma_forma_gerada_perde_leitura_por_colisao_de_string():
    # Formas que _parecem_ repetidas (ex. "estuda" é presente indicativo
    # 3ª singular E imperativo "tu") são leituras DIFERENTES, cada uma
    # com seu próprio tempo -- nenhuma pode desaparecer silenciosamente.
    # Total esperado por verbo regular: 25 formas sem repetição de string
    # (presente/perfeito/imperfeito/futuro/subjuntivo/condicional) + 4
    # leituras extra de imperativo que reaproveitam strings já existentes
    # ("tu"=presente 3ª sg, "você"/"nós"/"vocês"=subjuntivo) = 29.
    for infinitivo in ("estudar", "comer", "partir"):
        assert len(_verbo(infinitivo, "x")) == 29


def test_subjuntivo_presente_ambiguo_1a_3a_pessoa_singular():
    # "que eu fale" / "que ele fale" são a mesma forma na língua real --
    # pessoa=None em vez de fingir uma pessoa única, mesmo critério já
    # usado para "quis"/"soube"/"disse" no pretérito dos irregulares.
    for infinitivo, forma_ambigua in (("estudar", "estude"), ("comer", "coma"), ("partir", "parta")):
        entrada = _por_forma_e_tempo(infinitivo, forma_ambigua, "presente do subjuntivo")
        assert entrada.pessoa is None
        assert entrada.numero == Numero.SINGULAR


def test_subjuntivo_presente_er_ir_usa_mesma_vogal_a():
    comer_amos = _por_forma_e_tempo("comer", "comamos", "presente do subjuntivo")
    partir_amos = _por_forma_e_tempo("partir", "partamos", "presente do subjuntivo")
    assert comer_amos.pessoa == Pessoa.PRIMEIRA
    assert partir_amos.pessoa == Pessoa.PRIMEIRA
    comer_am = _por_forma_e_tempo("comer", "comam", "presente do subjuntivo")
    partir_am = _por_forma_e_tempo("partir", "partam", "presente do subjuntivo")
    assert comer_am.pessoa == Pessoa.TERCEIRA
    assert partir_am.pessoa == Pessoa.TERCEIRA


def test_imperativo_afirmativo_tu_reaproveita_presente_indicativo():
    # "tu" no imperativo é a MESMA string do presente indicativo 3ª
    # singular ("fala"/"come"/"parte") -- leitura adicional, não troca.
    for infinitivo, forma_tu in (("estudar", "estuda"), ("comer", "come"), ("partir", "parte")):
        indicativo = _por_forma_e_tempo(infinitivo, forma_tu, "presente")
        imperativo = _por_forma_e_tempo(infinitivo, forma_tu, "imperativo afirmativo")
        assert indicativo.pessoa == Pessoa.TERCEIRA
        assert imperativo.pessoa == Pessoa.SEGUNDA
        assert imperativo.numero == Numero.SINGULAR


def test_condicional_futuro_do_preterito_mesmo_sufixo_nas_tres_conjugacoes():
    for infinitivo in ("estudar", "comer", "partir"):
        formas = {f.forma: f for f in _verbo(infinitivo, "x")}
        forma_1a3a = formas[infinitivo + "ia"]
        assert forma_1a3a.pessoa is None
        assert forma_1a3a.atributos["tempo"] == "futuro do pretérito"
        assert formas[infinitivo + "íamos"].pessoa == Pessoa.PRIMEIRA
        assert formas[infinitivo + "íamos"].numero == Numero.PLURAL


def test_estrutura_do_portugues_continua_sem_lacuna_apos_a_extensao():
    from lingua_portuguesa import MotorPortugues

    motor = MotorPortugues()
    auditoria = motor.auditar_estrutura_portugues()
    assert len(auditoria.nomes_duplicados) == 0
    assert len(auditoria.dependencias_ausentes) == 0


def test_alternancias_ortograficas_preservam_som_diante_de_e():
    explicar = {entrada.forma for entrada in _verbo("explicar", "x")}
    chegar = {entrada.forma for entrada in _verbo("chegar", "x")}
    comecar = {entrada.forma for entrada in _verbo("começar", "x")}

    assert {"expliquei", "explique", "expliquem"} <= explicar
    assert not {"explicei", "explice", "explicem"} & explicar
    assert {"cheguei", "chegue", "cheguem"} <= chegar
    assert not {"chegei", "chege", "chegem"} & chegar
    assert {"comecei", "comece", "comecem"} <= comecar
    assert not {"começei", "começe", "começem"} & comecar


def test_g_muda_para_j_diante_de_a_e_o_em_ger_gir():
    reger = {entrada.forma for entrada in _verbo("reger", "x")}
    corrigir = {entrada.forma for entrada in _verbo("corrigir", "x")}

    assert {"rejo", "reja", "rejam"} <= reger
    assert not {"rego", "rega", "regam"} & reger
    assert {"corrijo", "corrija", "corrijam"} <= corrigir
    assert not {"corrigo", "corriga", "corrigam"} & corrigir


def test_gu_perde_u_diante_de_a_e_o_em_distinguir():
    distinguir = {entrada.forma for entrada in _verbo("distinguir", "x")}

    assert {"distingo", "distinga", "distingam"} <= distinguir
    assert not {"distinguo", "distingua", "distinguam"} & distinguir
