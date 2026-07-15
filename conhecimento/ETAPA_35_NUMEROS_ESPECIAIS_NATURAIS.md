# PSF-IAminy — Etapa 35
## Números especiais naturais

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Revisitamos números perfeitos (Etapa 3), e apresentamos números amigáveis, de Mersenne e de Fermat como propriedades já expressáveis com as peças atuais -- soma alíquota (Etapa 34), potenciação (Etapa 1076) e primalidade (Etapa 10), nenhuma peça nova.

```text
amigaveis(a,b)     = aliquota(a) = b  e  aliquota(b) = a  (a ≠ b)
mersenne(p)        = 2^p - 1
mersenne_primo(p)  = primo(p) e primo(mersenne(p))
fermat(n)          = 2^(2^n) + 1
fermat_primo(n)    = primo(fermat(n))
```

## Exemplo

- Mersenne com `p=3`: `2^3 - 1 = 7`, e `7` é primo -- `mersenne_primo(3)` é verdadeiro.
- Fermat com `n=1`: `2^(2^1) + 1 = 2^2+1 = 5`, e `5` é primo -- `fermat_primo(1)` é verdadeiro.
- `6` continua perfeito (soma alíquota `1+2+3=6`), revisitado com o vocabulário desta etapa.

## Dependências permitidas

- funcoes aritmeticas
- primalidade pura
- potenciacao por repeticao
- divisibilidade pura

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
