from matematica.conhecimento import ConhecimentoMatematico, _construcao_por_corte, _referencias_ampla, _secao


def test_referencias_ampla_encontra_caminho_em_crase_dentro_de_prosa():
    secao = "Implementado em `nucleo/exemplo.py` e validado em `testes/test_exemplo.py`."
    assert _referencias_ampla(secao) == ("nucleo/exemplo.py", "testes/test_exemplo.py")


def test_referencias_ampla_encontra_linha_solta_em_crase():
    secao = "`nucleo/exemplo.py`\n`testes/test_exemplo.py`"
    assert _referencias_ampla(secao) == ("nucleo/exemplo.py", "testes/test_exemplo.py")


def test_referencias_ampla_continua_encontrando_bloco_fenced():
    secao = "```text\nnucleo/exemplo.py\n```"
    assert _referencias_ampla(secao) == ("nucleo/exemplo.py",)


def test_referencias_ampla_ignora_crase_sem_caminho():
    secao = "Isto usa `SOMA` e `MULT`, sem nenhum arquivo."
    assert _referencias_ampla(secao) == ()


def test_construcao_por_corte_para_no_primeiro_metadado():
    texto = (
        "# Etapa X\n"
        "## Lei da etapa\n"
        "Conteúdo real de derivação aqui.\n\n"
        "## Dependências permitidas\n"
        "- igualdade\n"
    )
    resultado = _construcao_por_corte(texto)
    assert "Conteúdo real de derivação" in resultado
    assert "Dependências permitidas" not in resultado


def test_construcao_por_corte_usa_documento_inteiro_sem_metadado():
    texto = "# Etapa Y\n## Ideia\nSó existe isto, sem seção de dependência nenhuma.\n"
    resultado = _construcao_por_corte(texto)
    assert "Só existe isto" in resultado


def test_secao_ainda_reconhece_cabecalho_canonico():
    texto = "# T\n## Construção pura\nTexto canônico.\n\n## Dependências permitidas\n- x\n"
    assert _secao(texto, "Construção pura") == "Texto canônico."


def test_secao_exemplo_singular_e_extraida_em_bullets():
    texto = (
        "# T\n## Construção pura\nTexto.\n\n"
        "## Exemplo\n- primeiro caso\n- segundo caso\n\n"
        "## Dependências permitidas\n- x\n"
    )
    from matematica.conhecimento import _itens
    assert _itens(_secao(texto, "Exemplo")) == ("primeiro caso", "segundo caso")


def test_conceito_matematico_aceita_exemplos_minimos_com_default_vazio():
    from matematica.tipos import ConceitoMatematico

    sem_exemplo = ConceitoMatematico("x", "construção", (), (), (), "arquivo.md")
    assert sem_exemplo.exemplos_minimos == ()
    com_exemplo = ConceitoMatematico("y", "construção", (), (), (), "arquivo.md", exemplos_minimos=("um caso",))
    assert com_exemplo.exemplos_minimos == ("um caso",)


def test_primeiros_conceitos_fundacionais_tem_exemplo_real():
    """Achado real (auditoria externa): as primeiras aulas de Matemática
    não tinham exemplo estruturado -- `ConceitoMatematico` nunca teve esse
    campo, diferente de `ConceitoPortugues`. Trava de regressão para os 13
    primeiros conceitos (número natural até TFA existência), já curados."""
    c = ConhecimentoMatematico()
    por_marcador = {x.marcador_historico: x for x in c.todos()}
    for marcador in range(1, 14):
        conceito = por_marcador[marcador]
        assert conceito.exemplos_minimos, f"ETAPA {marcador} ({conceito.nome}) sem exemplo"


def test_conhecimento_matematico_real_fecha_as_tres_lacunas():
    """Trava de regressão: o corpo real de conhecimento/ não deve ter
    nenhum conceito sem construção, implementação ou validação reconhecidas."""
    from matematica.pontes import auditar_pontes

    c = ConhecimentoMatematico()
    auditoria = auditar_pontes(c.todos())
    assert auditoria["isolados"] == ()
    assert auditoria["sem_construcao"] == ()
    assert auditoria["sem_implementacao"] == ()
    assert auditoria["sem_validacao"] == ()

    aud = c.auditar()
    assert aud.referencias_de_implementacao_ausentes == ()
    assert aud.referencias_de_teste_ausentes == ()
    assert aud.nomes_duplicados == ()
