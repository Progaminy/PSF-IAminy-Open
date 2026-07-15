import sys as _sys

# ==============================================================================
# NOTA HONESTA SOBRE ESCALA: cada numeral de Church de valor n é, por
# construção, n aplicações de função ANINHADAS (não há otimização de
# recursão de cauda em Python). Isso significa que operações sobre
# numerais "grandes" (ex.: 7! = 5040, ou o 30º primo) atingem o limite
# de recursão padrão do Python (~1000) mesmo sem nenhum laço "impuro" —
# é uma propriedade do próprio encoding, não um bug de implementação.
# Elevado aqui uma vez, no ponto de entrada do pacote, para que o núcleo
# formal não precise saber que Python existe por baixo dele.
if _sys.getrecursionlimit() < 100_000:
    _sys.setrecursionlimit(100_000)
