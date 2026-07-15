# PSF-IAminy — Etapa 129: Caminho mínimo em grafo ponderado

## Posição no fluxo natural

Esta etapa fecha o bloco de grafos finitos iniciado na etapa 111.

## Construção pura

Pelo algoritmo de Dijkstra — correto porque pesos PSF são sempre não-negativos (não existe numeral negativo neste núcleo). Testado: um caminho de 2 arestas mais barato (peso 2) preferido corretamente sobre uma aresta direta mais cara (peso 4).

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana;
- grafo ponderado;
- caminho grafo.

## Dependências proibidas nesta etapa

- pesos negativos; ciclos negativos; fluxo em redes;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_ponderados_algoritmos.py` e validado em `testes/test_grafos_ponderados_algoritmos.py`.
