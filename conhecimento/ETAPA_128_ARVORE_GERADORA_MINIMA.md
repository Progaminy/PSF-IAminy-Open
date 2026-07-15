# PSF-IAminy — Etapa 128: Árvore geradora mínima

## Posição no fluxo natural

Esta etapa fecha o bloco de grafos finitos iniciado na etapa 111.

## Construção pura

Dado um grafo conexo com pesos, encontra a árvore geradora (etapa 116) de menor peso total, pelo algoritmo de Kruskal: ordena as arestas por peso, adiciona gulosamente cada uma que não forma ciclo (via união de componentes), até ter |V|-1 arestas. Testado à mão: grafo de 4 vértices, MST correta encontrada com peso total 6.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana;
- árvore grafo;
- grafo ponderado;
- caminho grafo.

## Dependências proibidas nesta etapa

- pesos negativos; ciclos negativos; fluxo em redes;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_ponderados_algoritmos.py` e validado em `testes/test_grafos_ponderados_algoritmos.py`.
