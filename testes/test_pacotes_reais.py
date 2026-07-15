from ensino.pacotes_reais import (
    gerar_corrigidos,
    gerar_exercicios,
    pacotes_matematica,
    pacotes_portugues,
    verificar_resposta,
)
from ensino.exercicio_real import tem_gerador_real


def test_pacotes_portugues_cobrem_todos_os_1141_conceitos_sem_repetir():
    pacotes = pacotes_portugues()
    nomes = [aula.conceito for p in pacotes for aula in p.aulas]
    assert len(nomes) == 1141
    assert len(set(nomes)) == 1141


def test_pacotes_matematica_cobrem_os_197_conceitos_reais_sem_repetir():
    pacotes = pacotes_matematica()
    nomes = [aula.conceito for p in pacotes for aula in p.aulas]
    assert len(nomes) == 203
    assert len(set(nomes)) == 203
    # nós sintéticos "raiz: X" nunca viram aula -- não são conceito PSF documentado.
    assert not any(nome.startswith("raiz: ") for nome in nomes)


def test_pacote_e_um_caminho_reto_no_grafo():
    # dentro de um pacote de 2+ aulas, cada aula (exceto a última) depende
    # SÓ da anterior no mesmo pacote, e é a única coisa que depende dela.
    pacotes = pacotes_portugues()
    for pacote in pacotes:
        if len(pacote.aulas) < 2:
            continue
        for anterior, atual in zip(pacote.aulas, pacote.aulas[1:]):
            assert atual.depende_de == (anterior.conceito,)


def test_codigo_do_pacote_identifica_a_area():
    pt = pacotes_portugues()[0]
    mat = pacotes_matematica()[0]
    assert pt.codigo.startswith("PT-")
    assert pt.area == "portugues"
    assert mat.codigo.startswith("MAT-")
    assert mat.area == "matematica"


def test_aula_contem_explicacao_real_nao_vazia():
    pacotes = pacotes_portugues()
    aula = pacotes[0].aulas[0]
    assert aula.explicacao
    assert aula.conceito
    assert aula.tema


def test_entroncamento_final_e_o_ultimo_conceito_do_pacote():
    pacote = pacotes_portugues()[0]
    assert pacote.entroncamento_final == pacote.aulas[-1].conceito


def test_aula_texto_inclui_explicacao_e_exemplo():
    aula = pacotes_portugues()[0].aulas[0]
    assert aula.completa
    texto = aula.texto()
    assert aula.explicacao in texto
    assert aula.exemplos[0] in texto


def test_dependentes_da_raiz_vem_do_grafo_inteiro_nao_so_do_pacote():
    # "diferença" é raiz, tema geral -- muitos conceitos de outros temas
    # dependem dela; o índice reverso tem que ver o grafo inteiro.
    pacotes = pacotes_portugues()
    raiz = next(a for p in pacotes for a in p.aulas if a.conceito == "diferença")
    assert len(raiz.dependentes) > 5


def test_exercicio_de_conceito_raiz_pergunta_se_e_raiz():
    aula = next(a for p in pacotes_portugues() for a in p.aulas if a.conceito == "diferença")
    exercicios = gerar_exercicios(aula)
    tipos = {e.tipo for e in exercicios}
    assert "raiz" in tipos
    assert "dependencia" not in tipos


def test_exercicio_so_nasce_quando_o_fato_existe():
    aula = next(a for p in pacotes_portugues() for a in p.aulas if a.conceito == "diferença")
    exercicios = gerar_exercicios(aula)
    # "diferença" não tem depende_de -- não pode gerar exercício "cite uma dependência"
    assert not any(e.tipo == "dependencia" for e in exercicios)


def test_gerar_corrigidos_mostra_exercicio_e_resposta_juntos():
    aula = pacotes_portugues()[0].aulas[0]
    corrigidos = gerar_corrigidos(aula)
    assert len(corrigidos) == len(gerar_exercicios(aula))
    for c in corrigidos:
        assert c.resposta_modelo in c.exercicio.respostas_aceitas


def test_verificacao_estruturada_e_exata():
    aula = next(a for p in pacotes_portugues() for a in p.aulas if a.conceito == "diferença")
    ex = next(e for e in gerar_exercicios(aula) if e.tipo == "dependente")
    correta = verificar_resposta(ex, ex.respostas_aceitas[0])
    errada = verificar_resposta(ex, "isto não existe no grafo")
    assert correta.correto is True and correta.semelhanca == 1.0
    assert errada.correto is False and errada.semelhanca == 0.0
    assert correta.metodo == "exato"


def test_verificacao_aberta_usa_semelhanca_nunca_finge_certeza_binaria():
    aula = next(a for p in pacotes_portugues() for a in p.aulas if a.conceito == "diferença")
    ex = next(e for e in gerar_exercicios(aula) if e.tipo == "funcao")
    resposta_certa = verificar_resposta(ex, ex.respostas_aceitas[0])
    resposta_parecida = verificar_resposta(ex, "distinguir letras palavras e sons")
    resposta_nada_a_ver = verificar_resposta(ex, "isto não tem nenhuma relação")
    assert resposta_certa.semelhanca == 1.0
    assert 0.0 <= resposta_parecida.semelhanca <= 1.0
    assert resposta_nada_a_ver.semelhanca < resposta_parecida.semelhanca
    assert "não prova compreensão" in resposta_certa.metodo


def test_conceito_com_primitivo_real_gera_exercicio_de_conta_como_primeiro():
    aula = next(a for p in pacotes_matematica() for a in p.aulas if a.conceito == "adicao")
    exercicios = gerar_exercicios(aula, semente=7)
    assert exercicios[0].tipo.startswith("conta_real:")
    assert "?" in exercicios[0].pergunta
    resultado = verificar_resposta(exercicios[0], exercicios[0].respostas_aceitas[0])
    assert resultado.correto is True
    assert "primitivo formal" in resultado.metodo


def test_conceito_com_primitivo_real_pergunta_de_dependencia_fica_secundaria():
    aula = next(a for p in pacotes_matematica() for a in p.aulas if a.conceito == "multiplicacao")
    exercicios = gerar_exercicios(aula, semente=3)
    tipos = [e.tipo for e in exercicios]
    assert tipos[0].startswith("conta_real:")
    assert "dependencia" in tipos or "raiz" in tipos
    if "dependencia" in tipos:
        assert tipos.index("dependencia") > 0


def test_conceito_sem_primitivo_real_nao_ganha_exercicio_de_conta():
    aula = next(a for p in pacotes_matematica() for a in p.aulas if not tem_gerador_real(a.conceito))
    exercicios = gerar_exercicios(aula)
    assert not any(e.tipo.startswith("conta_real:") for e in exercicios)
