# PSF-IAminy — Etapa 103: Raízes de polinómios

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Uma raiz de p é um elemento r do domínio onde p(r)=0. Avaliação por método de Horner (só soma e produto, sem potências repetidas). Busca de raízes é exaustiva sobre um domínio finito — não um método analítico, que não existe de forma geral mesmo sobre corpos infinitos.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- polinómios anel;
- grau operações polinomiais.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
