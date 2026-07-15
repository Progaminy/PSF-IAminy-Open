# PSF-IAminy — Etapa 130: Fechamento discreto geral

## Posição no fluxo natural

Esta etapa fecha o bloco de grafos finitos iniciado na etapa 111.

## Construção pura

Confirma o arco completo do projeto até este ponto: relação binária dá função e ordem; função e operação dão grupo, anel e corpo; corpo dá espaço vetorial e matriz; relação simétrica dá grafo; grafo, peso e comparação dão árvore geradora mínima e caminho mínimo — cada camada usando só o que nasceu antes dela.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana;
- grupo;
- corpo finito;
- espaço vetorial finito;
- matriz aplicação linear;
- grafo relação simétrica;
- árvore geradora mínima;
- caminho mínimo ponderado.

## Dependências proibidas nesta etapa

- pesos negativos; ciclos negativos; fluxo em redes;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_ponderados_algoritmos.py` e validado em `testes/test_grafos_ponderados_algoritmos.py`.
