# PSF-IAminy — Marcador histórico 1064: completude por sequências de Cauchy de leis geradoras

## Construção pura

Liga `lei geradora aproximação real` (ETAPA 1035), `equivalência leis
geradoras` (ETAPA 1061) e `operações leis geradoras` (ETAPA 1062): o
quarto e último dos itens que a ETAPA 1035 deixou pendentes — mas com o
escopo que dá para construir honestamente.

A propriedade geral do supremo ("todo conjunto não vazio limitado
superiormente tem menor cota superior", para qualquer conjunto
arbitrário de reais) exigiria decidir ordem entre reais arbitrários — e
a ETAPA 1063 já mostrou, com honestidade, que isso às vezes fica
indeterminado em tempo finito (duas leis podem representar o mesmo
valor sem que nenhuma comparação finita prove igualdade). Fingir a
propriedade geral do supremo seria fingir uma decisão que este projeto
não tem. O que dá para construir sem fingir, e que já basta para o resto
do projeto (séries, limites, `eˣ`), é **completude por sequências de
Cauchy**: dada uma sequência explícita de leis geradoras com um
certificado de Cauchy fornecido por quem a constrói, o limite existe e
tem uma lei geradora própria.

```text
epsilon_k = 1/2^(k+1)  (decresce para zero)
N_k = modulo_cauchy(epsilon_k)  (certificado: termos a partir de N_k
                                  ficam a distância <= epsilon_k do limite)
bruto_k = termo(N_k) refinado até largura <= epsilon_k, alargado por
          epsilon_k dos dois lados
passo(indice) = interseção acumulada de bruto_0, ..., bruto_indice
```

A interseção acumulada garante o encaixamento por construção — interseção
com mais uma restrição só pode manter ou encolher o intervalo, nunca
alargar — sem depender de nenhuma monotonicidade delicada da sequência
original. A largura tende a zero porque cada `bruto_k` já tem largura
<= 3·epsilon_k, que também tende a zero.

A conferência não aceita a construção por confiança na fórmula: o teste
principal usa uma sequência de racionais genuinamente diferente da
lei original — o ponto médio do intervalo de Newton para `√2` em cada
passo, uma sequência de Cauchy que converge para `√2` sem citar "raiz
quadrada" no valor em si — e prova, reaproveitando
`sao_consistentes_ate_epsilon` (ETAPA 1061), que o limite construído é
consistente com a lei geradora original de `√2`.

## Dependências permitidas

- lei geradora aproximação real
- equivalência leis geradoras
- operações leis geradoras

## Implementação

```text
nucleo/completude_leis_geradoras.py
```

## Validação

```text
testes/test_completude_leis_geradoras.py
```

## Estado

Completude por sequências de Cauchy construída e testada: o limite da
sequência de pontos médios do intervalo de Newton para `√2` (sequência
independente, mesma raiz) consistente com a lei original, uma sequência
trivial (constante) consistente consigo mesma, prefixo encaixado com
largura decrescente e rejeição de índice negativo. Isto fecha os quatro
itens que a ETAPA 1035 deixara pendentes (equivalência, operações, ordem,
completude) dentro do escopo construtivo honesto — a propriedade geral
do supremo para conjuntos arbitrários de reais continua fora de alcance,
por exigir uma decisão de ordem que nem sempre existe em tempo finito.
