from lingua_portuguesa.distancia_edicao import distancia_damerau_levenshtein
from lingua_portuguesa.indice_fuzzy import ArvoreBK, Trie


PALAVRAS = (
    "casa", "caso", "carro", "carta", "canto", "canta", "campo",
    "livro", "livre", "libra", "lindo", "linda",
    "pessoa", "pessoal", "passo", "posso", "possa",
    "estudar", "estudo", "estuda", "estudam",
    "mesa", "mesmo", "meio", "melo",
)


def test_trie_contem_e_nao_contem():
    trie = Trie()
    for palavra in PALAVRAS:
        trie.inserir(palavra)
    for palavra in PALAVRAS:
        assert trie.contem(palavra)
    assert not trie.contem("inexistente")
    assert not trie.contem("cas")  # prefixo não é a chave completa


def test_trie_prefixos():
    trie = Trie()
    for palavra in PALAVRAS:
        trie.inserir(palavra)
    assert set(trie.prefixos("est")) == {"estudar", "estudo", "estuda", "estudam"}
    assert trie.prefixos("zzz") == ()


def _busca_forca_bruta(alvo: str, raio: int) -> set[str]:
    return {
        palavra
        for palavra in PALAVRAS
        if distancia_damerau_levenshtein(alvo, palavra) <= raio
    }


def test_arvore_bk_equivalente_a_forca_bruta_para_bateria_de_erros():
    arvore = ArvoreBK.construir(PALAVRAS)
    alvos_com_erro = (
        "caza",     # substituição
        "carto",    # transposição
        "livr",     # remoção no fim
        "pesoa",    # remoção no meio
        "possoa",   # inserção
        "mesmoo",   # inserção no fim
        "estudaa",  # inserção no fim
        "xyzxyz",   # sem correspondência próxima
    )
    for alvo in alvos_com_erro:
        for raio in (1, 2):
            esperado = _busca_forca_bruta(alvo, raio)
            obtido = set(arvore.buscar(alvo, raio))
            assert obtido == esperado, f"alvo={alvo!r} raio={raio}: esperado={esperado} obtido={obtido}"


def test_arvore_bk_encontra_a_propria_palavra_a_distancia_zero():
    arvore = ArvoreBK.construir(PALAVRAS)
    for palavra in PALAVRAS:
        assert palavra in arvore.buscar(palavra, 0)


def test_arvore_bk_vazia_nao_encontra_nada():
    arvore = ArvoreBK()
    assert arvore.buscar("qualquer", 5) == ()


def test_arvore_bk_nao_duplica_insercao_da_mesma_chave():
    arvore = ArvoreBK.construir(["casa", "casa", "casa"])
    assert arvore.buscar("casa", 0) == ("casa",)
