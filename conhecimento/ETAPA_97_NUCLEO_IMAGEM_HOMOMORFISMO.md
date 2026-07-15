# PSF-IAminy — Etapa 97: Núcleo e imagem de homomorfismo

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

O núcleo de um homomorfismo é o conjunto de elementos que vão para o neutro do contradomínio; a imagem é o conjunto de valores efetivamente atingidos. Ambos nascem diretamente da noção de função finita já construída — não são estruturas novas, são leituras específicas de uma função já existente.

## Exemplo

- Para `f:(ℤ/6ℤ,+)→(ℤ/3ℤ,+)`, `f(x)=x mod 3` (Etapa 95): núcleo `={0,3}` (únicos elementos de `ℤ/6ℤ` que vão para o zero de `ℤ/3ℤ`); imagem `={0,1,2}` (todo elemento de `ℤ/3ℤ` é atingido -- `f` é sobrejetora).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- homomorfismo grupos;
- aplicação finita.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
