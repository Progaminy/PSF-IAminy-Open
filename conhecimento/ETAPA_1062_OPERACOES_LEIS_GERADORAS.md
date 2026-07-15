# PSF-IAminy — Marcador histórico 1062: operações preservadas entre leis geradoras

## Construção pura

Liga `equivalência leis geradoras` (ETAPA 1061) e `lei geradora
aproximação real` (ETAPA 1035): o segundo dos quatro itens que a ETAPA
1035 deixou pendentes. Soma e produto de duas leis geradoras nascem
combinando os intervalos das duas no mesmo passo — nunca avaliando um
valor real diretamente, porque nenhum valor real solto existe fora do
encaixe de intervalos.

```text
soma: [a_inf,a_sup] + [b_inf,b_sup] = [a_inf+b_inf, a_sup+b_sup]
produto: [a_inf,a_sup] × [b_inf,b_sup] = [min(4 cantos), max(4 cantos)]
```

A soma é direta porque é monótona nos dois lados. O produto precisa dos
quatro produtos dos cantos (inferior×inferior, inferior×superior,
superior×inferior, superior×superior) — não só canto-a-canto —, porque
o produto não preserva a mesma monotonicidade simples da soma quando um
intervalo pode conter valores negativos; os quatro cantos cobrem
qualquer combinação de sinal sem assumir que os valores envolvidos são
sempre positivos.

A prova de que a soma/produto construídos são a soma/produto **certos**
não é aceita por confiança na fórmula: é conferida reaproveitando
`sao_consistentes_ate_epsilon` (ETAPA 1061) contra uma lei geradora
constante (`lei_geradora_constante`, testemunha de largura zero) quando
o valor esperado é conhecido — `√4+√9` tem que ficar consistente com
`5`, `√2×√2` com `2`, e `√4×√9` com `√36` (identidade `√a×√b=√(ab)`
verificada por duas leis distintas convergindo ao mesmo valor). Um caso
de soma com valor deliberadamente errado (`√4+√9` contra `6`) confirma
que a conferência realmente rejeita quando o resultado está errado, não
aceita qualquer coisa.

## Dependências permitidas

- equivalência leis geradoras
- lei geradora aproximação real

## Implementação

```text
nucleo/operacoes_leis_geradoras.py
```

## Validação

```text
testes/test_operacoes_leis_geradoras.py
```

## Estado

Soma e produto entre leis geradoras construídos e testados: lei
constante como testemunha exata, soma de `√4+√9` consistente com `5`
(e rejeitando `6`), produto de `√2×√2` consistente com `2`, e produto de
`√4×√9` consistente com `√36` — a identidade `√a×√b=√(ab)` confirmada
entre duas leis geradoras estruturalmente diferentes. Restam ordem entre
leis e a prova de completude (propriedade do supremo) dentro do mesmo
item do plano.
