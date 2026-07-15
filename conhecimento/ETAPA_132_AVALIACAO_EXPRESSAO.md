# PSF-IAminy — Etapa 132: Avaliação de expressão sobre um domínio finito

## Posição no fluxo natural

Esta etapa começa o bloco de expressões simbólicas, construído sobre corpo finito (etapa 94).

## Construção pura

Substitui a variável por um valor concreto e reduz recursivamente, usando só as operações do anel/corpo fornecidas — nunca operadores nativos do Python sobre os coeficientes. Descoberta ao testar: o expoente de POT_EXPR é guardado como int nativo do Python (por desenho, para a gramática ficar simples de escrever), e a conversão para numeral de Church acontece só neste avaliador — a única fronteira, não espalhada pelas funções de corpo.

## Dependências permitidas

- distinção; igualdade; domínio finito explícito; corpo (etapas 91-94);
- expressão simbólica finita.

## Dependências proibidas nesta etapa

- múltiplas variáveis; equações de grau >= 2; raízes gerais;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/expressoes_simbolicas_finitas.py` e validado em `testes/test_expressoes_simbolicas_finitas.py`.
