# PSF-IAminy — Marcador histórico 1047: funções avançadas (domínio, imagem, inversa, composição)

## Construção pura

Uma **função avançada**, neste projeto, não é conhecimento novo — é a
mesma função já construída, mas com domínio explícito e finito, imagem
rastreada (não assumida) e, quando injetora, uma inversa conferida por
composição de ida e volta (aplicar a função e depois a inversa devolve
o valor original). Liga direto a `função como relação especial` (ETAPA
70), `aplicação finita` (ETAPA 71), `composição de funções` (ETAPA 74),
`injetividade` (ETAPA 75) e `inversa relacional` (ETAPA 78).

"Funções avançadas" existia neste projeto só como texto de resposta
legada (`nucleo/conceitos_avancados_puros.py`): explicação e exemplo
prontos, sem prova PSF, código ou teste.

```text
função como relação especial + aplicação finita + injetividade + inversa relacional
→ f(x) = coeficiente·x + constante, sobre domínio finito explícito
→ imagem: aplica a regra em cada x do domínio, não assume o resultado
→ injetora: confere que nenhum par de entradas produz a mesma saída
→ inversa: f⁻¹(y) = (y−constante)/coeficiente, testada desfazendo f em cada ponto
→ composição: (f∘g)(x) = f(g(x)), exige que a imagem de g caiba no domínio de f
```

Exemplo clássico: `f(x) = 2x-3` tem inversa `f⁻¹(y) = (y+3)/2` —
`coeficiente=1/2`, `constante=3/2`, exatamente o que a construção produz
e confere ao aplicar `f` seguido de `f⁻¹` de volta ao ponto original.
Função constante (`coeficiente=0`) é detectada como não-injetora e
rejeitada explicitamente ao pedir inversa, em vez de produzir um
resultado sem sentido. Composição indefinida (quando a imagem de `g` sai
do domínio de `f`) também é erro, não silenciada.

Funções não lineares (quadráticas, com radical, por ramos) já têm
construção própria em etapas separadas (equação quadrática finita,
ETAPA 1042, ETAPA 1046); esta etapa cobre o caso linear como base comum
de domínio/imagem/inversa/composição.

## Exemplo

- `f(x) = 2x-3` tem inversa `f⁻¹(y) = (y+3)/2` -- aplicar `f` e depois `f⁻¹` devolve o ponto original.
- Função constante (`coeficiente=0`) é rejeitada explicitamente ao pedir inversa, por não ser injetora.

## Dependências permitidas

- função como relação especial
- aplicação finita
- composição de funções
- injetividade
- inversa relacional
- ponte racionais reais

## Implementação

```text
nucleo/funcoes_avancadas.py
```

## Validação

```text
testes/test_funcoes_avancadas.py
```

## Estado

Domínio controlado, imagem rastreada, injetividade, inversa e composição
construídos e testados para função linear, incluindo os casos de rejeição
(função constante sem inversa, composição indefinida, domínio vazio).
