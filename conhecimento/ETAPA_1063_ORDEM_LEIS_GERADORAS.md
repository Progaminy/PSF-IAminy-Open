# PSF-IAminy — Marcador histórico 1063: ordem entre leis geradoras

## Construção pura

Liga `ordem total` (ETAPA 69, já construída sobre racionais) e
`equivalência leis geradoras` (ETAPA 1061): o terceiro dos quatro itens
que a ETAPA 1035 deixou pendentes. A mesma ideia de refinar duas leis e
comparar intervalos, usada para checar consistência, agora decide `<`
ou `>` entre elas.

```text
i1 = lei1 refinada até largura <= epsilon/2; i2 = lei2 da mesma forma
→ i1.superior < i2.inferior: prova definitiva de lei1 < lei2
→ i2.superior < i1.inferior: prova definitiva de lei1 > lei2
→ nem um nem outro: indeterminado nesse epsilon
```

A assimetria é a mesma já estabelecida em `sao_consistentes_ate_epsilon`:
um resultado `MENOR`/`MAIOR` é prova definitiva e finita — os intervalos
não se tocam, então nenhum valor real cabe nos dois ao mesmo tempo do
lado errado. `INDETERMINADA` não significa "são iguais": significa
"não decidido nesse epsilon", porque tanto pode ser diferença pequena
ainda não separada quanto pode ser o mesmo valor. `decidir_ordem` refina
o epsilon pela metade repetidamente até decidir ou desistir: se as leis
representam valores diferentes, a diferença é um racional fixo positivo
e refinar o suficiente sempre a encontra (testado com `√2 < √3`); se
representam o mesmo valor (Newton e bisseção da mesma raiz, ETAPA 1061),
o processo nunca decide, e o módulo declara isso honestamente em vez de
fingir uma prova de igualdade que não tem.

## Dependências permitidas

- ordem total
- equivalência leis geradoras

## Implementação

```text
nucleo/ordem_leis_geradoras.py
```

## Validação

```text
testes/test_ordem_leis_geradoras.py
```

## Estado

Ordem entre leis geradoras construída e testada: `√2 < √3` e `√3 > √2`
decididos definitivamente, uma lei comparada consigo mesma
corretamente indeterminada, `decidir_ordem` encontrando a diferença
entre `√2` e `√3`, e o mesmo processo honestamente não decidindo entre
Newton e bisseção da mesma raiz (mesmo valor, ETAPA 1061). Resta a
prova de completude (propriedade do supremo) como último dos quatro
itens de reais completos.
