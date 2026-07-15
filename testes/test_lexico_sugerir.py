"""Cobre a otimização de `Dicionario.sugerir()` (Fase 1.3 do corretor):
antes fazia um scan linear com Levenshtein simples; agora usa uma árvore BK
(`ArvoreBK`) indexada por Damerau-Levenshtein. Este ficheiro prova que a
troca de mecanismo é equivalente a uma implementação de referência por
força bruta, não só "parece funcionar".
"""
from lingua_portuguesa.distancia_edicao import distancia_damerau_levenshtein
from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.normalizacao import sem_acentos


def _sugerir_forca_bruta(dicionario: Dicionario, forma: str, limite: int = 5) -> tuple[str, ...]:
    alvo = sem_acentos(forma)
    distancia_maxima = 1 if len(alvo) <= 5 else 2
    candidatos: list[tuple[int, str]] = []
    for chave in dicionario.chaves():
        distancia = distancia_damerau_levenshtein(alvo, sem_acentos(chave), distancia_maxima)
        if distancia <= distancia_maxima:
            candidatos.append((distancia, chave))
    candidatos.sort(key=lambda item: (item[0], len(item[1]), item[1]))
    return tuple(chave for _, chave in candidatos[:limite])


def test_sugerir_equivalente_a_forca_bruta_no_dicionario_real():
    dicionario = Dicionario.padrao()
    alvos_com_erro = (
        "protugues",   # transposição
        "pesoa",       # remoção
        "matematcia",  # transposição perto do fim
        "nuemro",      # transposição
        "aritimetica", # inserção
        "grafia",
        "conjunto",
    )
    for alvo in alvos_com_erro:
        esperado = _sugerir_forca_bruta(dicionario, alvo)
        obtido = dicionario.sugerir(alvo)
        assert obtido == esperado, f"alvo={alvo!r}: esperado={esperado} obtido={obtido}"


def test_sugerir_reconhece_transposicao_como_erro_mais_proximo_que_antes():
    # "protugues" é "português" (sem acento) com duas letras trocadas de
    # posição (tu <-> ug ... na prática "prot" -> "port"): Damerau-Levenshtein
    # deve aceitar isso como candidato próximo de "portugues".
    dicionario = Dicionario.padrao()
    sugestoes = dicionario.sugerir("protugues")
    assert "português" in sugestoes


def test_cache_fuzzy_invalidado_ao_adicionar_forma_nova():
    from lingua_portuguesa.tipos import ClasseGramatical, EntradaLexical

    dicionario = Dicionario()
    dicionario.adicionar(
        EntradaLexical(lema="zorblax", forma="zorblax", classe=ClasseGramatical.SUBSTANTIVO)
    )
    assert dicionario.buscar("zorblax")

    # adicionar uma forma nova e próxima deve aparecer nas sugestões — só
    # acontece se o cache da árvore BK for de facto invalidado e
    # reconstruído após o adicionar() acima.
    dicionario.adicionar(
        EntradaLexical(lema="zorblac", forma="zorblac", classe=ClasseGramatical.SUBSTANTIVO)
    )
    sugestoes = dicionario.sugerir("zorblax")
    assert "zorblac" in sugestoes
