# PSF-IAminy — Etapa 123: Grafo Euleriano

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Existe um passeio que usa cada aresta exatamente uma vez? Pelo Teorema de Euler (1736) — o problema original das Sete Pontes de Königsberg — isso acontece sse o grafo é conexo e todo vértice tem grau par. Confirmado com o grafo real de Königsberg (graus 5,3,3,3, todos ímpares): NÃO é Euleriano, exatamente como Euler provou há quase 300 anos.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);
- grau vértice;
- conectividade grafo.

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
