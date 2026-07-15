# PSF-IAminy — Marcador histórico 1050: desvio padrão exato

## Construção pura

O **desvio padrão** mede o quanto os valores de um conjunto de dados se
espalham, em média, ao redor da média deles — é a raiz quadrada da
variância. Usar a raiz (em vez da variância crua) devolve essa
dispersão na mesma unidade dos dados originais, não na unidade ao
quadrado.

"Desvio padrão" existia neste projeto só como extensão implícita da
variância (ETAPA 961-990, `variancia_par`): a variância já estava
construída e testada; faltava só a raiz. Este ramo liga `variancia_par`
a `raiz_quadrada_exata_ou_none` (ETAPA 1048).

```text
estatística finita dados (ETAPA 961-990, variancia_par)
→ variância como racional exato (numerador, denominador)
→ raiz_quadrada_exata_ou_none (ETAPA 1048)
→ se a variância é quadrado perfeito racional: desvio padrão exato
→ senão: None, honestamente — dependeria de reais completos (ETAPA 1035)
```

Testado com o exemplo clássico de estatística descritiva `[2,4,4,4,5,5,7,9]`
(média 5, variância populacional 4, desvio padrão 2 — um caso conhecido
onde a raiz sai exata), com dados constantes (variância e desvio zero) e
com um caso honestamente sem forma exata (`[1,2,3]`, variância `2/3`, não
quadrado perfeito).

## Exemplo

- Dados `[2,4,4,4,5,5,7,9]`: média 5, variância 4 (quadrado perfeito), desvio padrão exato = 2.
- Dados `[1,2,3]`: variância `2/3`, não é quadrado perfeito racional -- desvio padrão honestamente `None`, não aproximado.

## Dependências permitidas

- estatística finita dados
- equação quadrática exata
- ponte racionais reais

## Implementação

```text
nucleo/desvio_padrao_exato.py
```

## Validação

```text
testes/test_desvio_padrao_exato.py
```

## Estado

Desvio padrão populacional exato construído e testado, ligado à
variância já provada e à raiz quadrada exata. Desvio padrão amostral
(divisor n−1) e o caso irracional (via lei geradora) continuam como
próximo alvo.
