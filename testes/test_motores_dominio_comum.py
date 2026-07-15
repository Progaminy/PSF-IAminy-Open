from matematica import MotorMatematica
from motor import MotorComumPSF, MotorGeralIAMiny
from lingua_portuguesa import MotorPortugues
from motor.fluxo import relatorio_fluxo


def test_motor_matematica_inventaria_linha_unica():
    motor = MotorMatematica()
    auditoria = motor.auditar()
    assert auditoria.conceitos == 203
    assert auditoria.linha_unica
    assert auditoria.nomes_duplicados == ()
    assert auditoria.referencias_de_implementacao_ausentes == ()
    assert auditoria.referencias_de_teste_ausentes == ()


def test_motor_matematica_resolve_precedencia_sem_cortar_expressao():
    motor = MotorMatematica()
    assert motor.calcular("2+2*3").resultado == "8"
    assert motor.calcular("(2+2)*3").resultado == "12"
    assert motor.calcular("1+2+3").resultado == "6"
    assert motor.calcular("2^5").resultado == "32"


def test_motor_matematica_reconstroi_divisao_nao_exata():
    resposta = MotorMatematica().calcular("12/5")
    assert resposta.resultado == "2,4"
    assert resposta.resultado_exato == "12/5"
    assert resposta.estado == "RESOLVIDO_EXATAMENTE_POR_CONSTRUÇÃO_PSF"


def test_reconstrucao_e_monografia_nascem_do_conhecimento():
    motor = MotorMatematica()
    reconstrucao = motor.reconstruir("fatorial natural")
    assert reconstrucao.conceito is not None
    assert "produtório" in reconstrucao.conceito.construcao
    monografia = motor.produzir_monografia("fatorial natural")
    assert monografia.estado == "CONSOLIDAÇÃO_PSF"
    assert "Construção" in monografia.texto_markdown
    assert "cópia de monografia pronta" in monografia.texto_markdown


def test_legado_entra_como_candidato_nao_como_verdade():
    motor = MotorMatematica()
    candidatos = motor.candidatos_de_reconstrucao()
    assert len(candidatos) == 153
    assert "Fórmula de Bhaskara" in candidatos
    assert motor.reconstruir("Correspondência de Langlands").estado == "NÃO_MATERIALIZADO"


def test_motor_comum_registra_sem_misturar_dominios():
    comum = MotorComumPSF()
    pt = MotorPortugues()
    mat = MotorMatematica()
    comum.registrar_portugues(pt.conhecimento_puro())
    comum.registrar_matematica(mat.conhecimento_puro())
    auditoria = comum.auditar()
    assert auditoria["por_dominio"]["português"] == 1141
    assert auditoria["por_dominio"]["matemática"] == 203
    assert auditoria["unidades"] == 1344
    assert comum.rastrear("matemática", "fatorial natural") == "conhecimento/ETAPA_40_FATORIAL_NATURAL.md"


def test_motor_geral_orquestra_tres_motores():
    geral = MotorGeralIAMiny()
    assert geral.calcular_matematica("2+2*3").resultado == "8"
    assert geral.analisar_portugues("As meninas estudam.").tokens
    assert geral.auditar_motores()["comum"]["unidades"] == 1344
    assert geral.comum.memoria()[-1].dominio == "matemática"


def test_etapas_sao_marcadores_na_linha_unica():
    relatorio = relatorio_fluxo()
    assert relatorio["linha_unica"] is True
    assert relatorio["etapas_sao_marcadores"] is True
    assert "dependências" in relatorio["autoridade_estrutural"]

def test_motor_matematica_prova_finita_certificada():
    imp = lambda a, b: ("implica", a, b)
    prova = MotorMatematica().provar_finito(("p", imp("p", "q"), imp("q", "r")), "r")
    assert prova.valida is True
    assert prova.estado == "PROVA_FINITA_CERTIFICADA"
    assert prova.passos

def test_motor_portugues_expoe_leitura_revisao_sentido_e_producao_controlada():
    motor = MotorPortugues()
    assert motor.ler("As meninas estudam.").tokens
    sentido = motor.interpretar_sentido("As meninas estudam.")
    assert sentido["lemas_reconhecidos"]
    revisao = motor.revisar_escrita("As meninas estudam.")
    assert revisao["original"] == "As meninas estudam."
    assert motor.produzir_texto(["A matemática reconstrói", "O português interpreta"]) == (
        "A matemática reconstrói. O português interpreta."
    )


def test_divisao_racional_e_decimal_sao_reconstruidas_sem_magia():
    motor = MotorMatematica()
    resposta = motor.calcular("12:5")
    assert resposta.resultado == "2,4"
    assert resposta.resultado_exato == "12/5"
    assert resposta.estado == "RESOLVIDO_EXATAMENTE_POR_CONSTRUÇÃO_PSF"
    assert any("resto" in passo.justificacao.lower() for passo in resposta.passos)

    tres_casas = motor.calcular("12:5", casas_decimais=3)
    assert tres_casas.resultado == "2,400"
    assert tres_casas.casas_decimais == 3


def test_divisao_periodica_preserva_fracao_e_controla_precisao():
    motor = MotorMatematica()
    truncada = motor.calcular("1:3", casas_decimais=3)
    assert truncada.resultado == "0,333"
    assert truncada.resultado_exato == "1/3"
    assert truncada.limites

    arredondada = motor.calcular("2:3", casas_decimais=3, modo="arredondar")
    assert arredondada.resultado == "0,667"
    assert arredondada.modo_aproximacao == "arredondar"


def test_divisao_pode_participar_de_expressao_racional():
    resposta = MotorMatematica().calcular("1+1:2")
    assert resposta.resultado == "1,5"
    assert resposta.resultado_exato == "3/2"


def test_divisao_por_zero_e_conhecimento_reconstruido_e_nao_investigacao_aberta():
    resposta = MotorMatematica().calcular("12:0")
    assert resposta.estado == "DIVISÃO_POR_ZERO_NÃO_DEFINIDA_POR_CONSTRUÇÃO_PSF"
    assert resposta.resultado is None
    assert not resposta.referencia_convencional
    assert not resposta.investigacao
    assert any("0 × q" in passo.entrada for passo in resposta.passos)


def test_hipotese_do_autor_fica_pendente_e_nao_vira_primalidade_pronta():
    motor = MotorMatematica()
    hipoteses = motor.hipoteses_pendentes()
    assert len(hipoteses) == 1
    h = hipoteses[0]
    assert h.autor == "Pensador Sem Fronteiras"
    assert h.estado == "IDEIA_GUARDADA_ATÉ_O_MOTOR_ESTAR_MADURO"
    assert h.ambiguidades
    assert h.criterio_de_falsificacao
    assert "12" in " ".join(h.exemplos_originais)
    exemplos = " ".join(h.exemplos_originais)
    assert "12 não é primo" in exemplos
    assert "9 não é primo" in exemplos
    assert "7 é primo" in exemplos


def test_motor_auxiliar_compara_sem_virar_fundamento():
    geral = MotorGeralIAMiny()
    resolucao = geral.calcular_matematica("12:5", casas_decimais=3)
    validacao = geral.validar_calculo_matematica("12:5", resolucao)
    assert validacao.aprovado is True
    assert "não cria conhecimento" in validacao.aviso


def test_motor_auxiliar_nao_confunde_arredondamento_correto_com_divergencia():
    # Achado real de auditoria externa: "2:3 com 3 casas arredondado" dava
    # PSF "0,667" (correto) mas o comparador comparava contra 0,6666...
    # cru com tolerância fixa 1e-9 e gritava DIVERGÊNCIA_ENCONTRADA. A
    # tolerância agora é derivada das próprias casas/modo pedidos.
    geral = MotorGeralIAMiny()
    resolucao = geral.calcular_matematica("2:3", casas_decimais=3, modo="arredondar")
    assert resolucao.resultado == "0,667"
    validacao = geral.validar_calculo_matematica("2:3", resolucao)
    assert validacao.aprovado is True
    assert validacao.estado == "APROVADO_POR_COMPARAÇÃO"


def test_motor_auxiliar_aceita_truncamento_correto_tambem():
    geral = MotorGeralIAMiny()
    resolucao = geral.calcular_matematica("2:3", casas_decimais=3, modo="truncar")
    assert resolucao.resultado == "0,666"
    validacao = geral.validar_calculo_matematica("2:3", resolucao)
    assert validacao.aprovado is True


def test_motor_auxiliar_ainda_pega_divergencia_real():
    # a correção não deve virar uma tolerância frouxa demais: um valor PSF
    # genuinamente errado continua sendo pego.
    from matematica.tipos import ResolucaoMatematica

    resolucao_errada = ResolucaoMatematica(
        problema="2:3",
        estado="RESOLVIDO",
        resultado="0,700",
        passos=(),
        conhecimento_usado=(),
        casas_decimais=3,
        modo_aproximacao="arredondar",
    )
    geral = MotorGeralIAMiny()
    validacao = geral.validar_calculo_matematica("2:3", resolucao_errada)
    assert validacao.aprovado is False
    assert validacao.estado == "DIVERGÊNCIA_ENCONTRADA"


def test_motor_auxiliar_sem_casas_pedidas_continua_com_tolerancia_estrita():
    geral = MotorGeralIAMiny()
    resolucao = geral.calcular_matematica("12:5")
    validacao = geral.validar_calculo_matematica("12:5", resolucao)
    assert validacao.aprovado is True
    comparacao_textual = geral.comparar_textos_portugues("A casa é alta.", "A casa é alta.")
    assert comparacao_textual.estado == "COMPARAÇÃO_TEXTUAL_CONCLUÍDA"
    assert comparacao_textual.aprovado is None
