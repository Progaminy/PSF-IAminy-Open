# PSF-IAminy — Marcador histórico 1033: Trigonometria natural

## Construção pura

A trigonometria não começa por uma tabela nem por seis fórmulas prontas. Ela
nasce quando medidas de lados são comparadas e se observa que triângulos
retângulos semelhantes conservam as mesmas razões relativamente ao mesmo
ângulo agudo.

```text
diferença → unidade → comprimento → segmento → razão → proporção
                                          ↓
direção → ângulo → perpendicularidade → ângulo reto → triângulo retângulo
                                          ↓
                         hipotenusa, cateto oposto e cateto adjacente
                                          ↓
                    semelhança → razões invariantes do mesmo ângulo
                                          ↓
                 seno, cosseno, tangente, cotangente, secante, cossecante
                                          ↓
                      identidades de quociente, recíprocas e fundamental
```

Para um ângulo agudo escolhido num triângulo retângulo:

- seno nasce da razão cateto oposto/hipotenusa;
- cosseno nasce da razão cateto adjacente/hipotenusa;
- tangente nasce da razão cateto oposto/cateto adjacente e de seno/cosseno;
- cotangente inverte a tangente;
- secante inverte o cosseno;
- cossecante inverte o seno.

A identidade `sen² + cos² = 1` não é antecipada: ela nasce ao dividir a relação
entre os quadrados dos lados do triângulo retângulo pelo quadrado da hipotenusa.

## Dependências permitidas

- diferença controlada
- unidade de medida
- números naturais
- medida finita
- segmento
- direção
- ângulo
- razão
- proporção
- multiplicação cruzada
- perpendicularidade
- triângulo retângulo
- relação pitagórica
- semelhança de triângulos

## Implementação

```text
nucleo/trigonometria_natural.py
```

## Validação

```text
testes/test_trigonometria_natural.py
```

## Fronteira declarada

Esta construção fecha a trigonometria exata dos ângulos agudos representados por
triângulos retângulos. A extensão ao círculo orientado, radianos, quadrantes,
ângulos gerais, periodicidade, aproximações numéricas e funções inversas deve
continuar desta base, sem importar tabelas prontas como fundamento.

## Regra contra isolamento

Cada fórmula trigonométrica só pode ser usada depois de percorridas as suas
dependências. Respostas antigas sobre quadrantes, leis trigonométricas, limites
ou derivadas não ganham validade por estarem escritas no projeto: permanecem
material legado ou candidato enquanto a ponte correspondente não estiver
construída, implementada e testada.
