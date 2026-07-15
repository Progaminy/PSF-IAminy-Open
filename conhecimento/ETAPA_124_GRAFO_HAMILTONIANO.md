# PSF-IAminy — Etapa 124: Grafo Hamiltoniano

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Existe caminho que visita cada vértice exatamente uma vez? Busca exaustiva sobre permutações — NP-difícil em geral, correto aqui só porque o domínio é pequeno.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);
- caminho grafo.

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
