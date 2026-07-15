# PSF-IAminy — Etapa 64: Simetria

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Uma relação é simétrica quando todo caminho aRb exige o caminho de volta bRa. A direção não desaparece; ela é compensada.

## Exemplo

- Na relação `{(0,0),(1,1),(2,2),(0,2),(2,0)}`: o par `(0,2)` está presente e o par de volta `(2,0)` também -- simétrica.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- relação finita;
- lógica booleana já construída.

## Dependências proibidas nesta etapa

- cálculo diferencial ou integral;
- topologia;
- cardinalidade infinita;
- álgebra abstrata avançada;
- análise real;
- probabilidade;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/relacoes_funcoes_naturais.py` e validado em `testes/test_relacoes_funcoes_naturais.py`.
