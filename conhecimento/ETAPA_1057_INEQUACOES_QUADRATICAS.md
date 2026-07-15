# PSF-IAminy — Marcador histórico 1057: inequações do 2º grau

## Construção pura

Liga `equação quadrática exata` (ETAPA 1048, raízes racionais exatas de
`a·x²+b·x+c=0`) a `inequações` (ETAPA 1041, que já terminava apontando
"inequações quadráticas" como próximo alvo): o sinal de `a·x²+b·x+c` só
pode trocar ao cruzar uma raiz real, então basta calcular as raízes
exatas (quando existem) e testar o sinal em pontos de amostra entre e
fora delas.

```text
equação quadrática exata (ETAPA 1048) + inequações (ETAPA 1041)
→ discriminante = b²-4ac; sem raiz quadrada exata real, sinal é constante
→ 0 raízes: testa em x=0 (satisfaz tudo ou nada, sinal nunca muda)
→ 1 raiz (dupla): testa no ponto e logo depois dele
→ 2 raízes: testa no ponto médio (entre) e logo depois da maior (fora)
→ classificação é sempre DERIVADA de satisfaz(x), nunca uma regra à parte
```

O ponto central da construção: `satisfaz(x)` avalia `a·x²+b·x+c` de
verdade (mesmo `avaliar` usado para achar as raízes) e compara contra o
comparador. A `classificacao` textual ("entre_raizes", "fora_das_raizes",
"todos_os_reais", "um_ponto", "todos_exceto_um_ponto", "vazio") nunca é
calculada por uma tabela de sinais decorada — é sempre obtida chamando
`satisfaz()` nos mesmos pontos de amostra usados para decidir o rótulo,
então a classificação não pode discordar do predicado que a gerou.

Quando o discriminante é negativo, não há raiz real e o sinal de
`a·x²+b·x+c` é constante em toda a reta (a parábola nunca cruza o eixo
x) — por isso basta um único teste em `x=0`. Quando o discriminante não é
quadrado perfeito racional (raízes existiriam mas seriam irracionais),
esta etapa levanta erro: fica fora do escopo exato, mesmo limite já
assumido por `equação quadrática exata` (ETAPA 1048).

## Dependências permitidas

- equação quadrática exata
- inequações

## Implementação

```text
nucleo/inequacoes_quadraticas.py
```

## Validação

```text
testes/test_inequacoes_quadraticas.py
```

## Estado

Inequação do 2º grau construída e testada para os cinco casos
qualitativos: fora das raízes (parábola para cima), entre raízes
(parábola para baixo), sem raiz real com sinal constante, raiz dupla com
`>` (todos exceto um ponto) e com `>=` (todos os reais) — cada
classificação derivada do mesmo predicado `satisfaz()` usado para
resolver, nunca de uma tabela de sinais separada. Rejeita `a=0` e
discriminante que não é quadrado perfeito racional.
