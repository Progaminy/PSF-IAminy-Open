# PSF-IAminy — Etapa 107: Determinante em dimensão pequena

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Determinante 2×2 (ad-bc) e 3×3 (expansão por cofatores), por fórmula fechada — não eliminação gaussiana geral, que fica para uma etapa futura. Descoberta ao testar: a fórmula exige subtração verdadeira (a SUB truncada do núcleo dá resultado errado sem aviso sempre que um cofator intermédio é negativo) — documentado no próprio módulo.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- matriz aplicação linear.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
