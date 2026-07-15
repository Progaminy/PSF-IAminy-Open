# PSF-IAminy — Etapa 135: Equação quadrática finita

## Posição no fluxo natural

A etapa 133 parou antes da equação de segundo grau por um motivo correto: a fórmula real de segundo grau exige raiz quadrada geral, e `reais.py` ainda não entrega isso em tempo prático.

Esta etapa resolve uma versão diferente, mais estreita e já justificada pelo fluxo: equação quadrática sobre domínio finito explícito. Como o domínio é finito, não é preciso fórmula quadrática, discriminante nem raiz geral. Basta avaliar a expressão em todos os elementos do domínio.

## Construção pura

A expressão quadrática é montada com a gramática já nascida:

```text
ax² + bx + c
```

usando:

```text
CONST, VAR, SOMA_EXPR, MULT_EXPR, POT_EXPR
```

Depois:

```text
RESOLVER_QUADRATICA_FINITA_PURA(a,b,c,domínio,...)
```

devolve todas as raízes `x` do domínio tais que:

```text
ax² + bx + c = 0
```

Se `a=0`, a equação não é quadrática; a função devolve vazio e o caso linear continua pertencendo à etapa 133.

## Domínio declarado

- uma variável;
- domínio finito explícito;
- operações de anel/corpo fornecidas por fora;
- busca exaustiva;
- validação exaustiva de todas as quadráticas não degeneradas sobre `Z/5Z`.

## Dependências permitidas

- raízes polinômios;
- corpo finito (etapa 94);
- avaliação expressão;
- equação linear finita (etapa 133), para separar o caso degenerado;

## Dependências proibidas nesta etapa

- fórmula quadrática real;
- discriminante como número real;
- raiz quadrada geral;
- domínios infinitos;
- múltiplas variáveis.

## Forma operacional no projeto

Implementado em `nucleo/expressoes_simbolicas_finitas.py` e validado em `testes/test_equacao_quadratica_finita.py`.

## Limite honesto

Isto resolve o problema de equação de segundo grau **no caso finito**. O problema real, com fórmula e aproximação de raízes fora de domínio finito, continua dependendo de completar a aritmética binária/posicional iniciada na etapa 134.
