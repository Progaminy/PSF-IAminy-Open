# PSF-IAminy — Etapa 13
## Teorema Fundamental da Aritmética: existência da decomposição prima

## Lei de pureza

Nesta etapa já existem:

```text
número natural
ordem
multiplicação
divisibilidade
quociente e resto puros
primo
composto
menor fator
fatoração pura
```

Ainda não usamos:

```text
congruência
aritmética modular
função phi
Fermat
Euler
teorema chinês dos restos
```

## Ideia

Todo número natural maior que `1` ou é primo ou é composto.

Se é primo, a sua decomposição prima é ele próprio.

Se é composto, existe um divisor interno. A busca pelo menor fator encontra um `d` tal que:

```text
d | n
```

Logo existe um quociente `q` tal que:

```text
n = d × q
```

Como `d` foi escolhido como menor fator maior que `1`, `d` é primo. Se `d` não fosse primo, teria um fator menor que ele e esse fator também dividiria `n`, contradizendo a escolha de `d`.

Depois repetimos o mesmo raciocínio em `q`.

Como cada passo reduz o número restante, o processo termina.

## Forma PSF

```text
n > 1
↓
menor_fator(n) = p
↓
p é primo
↓
n = p × q
↓
repetir em q
↓
lista de primos cujo produto é n
```

## Conclusão

Para todo `n > 1`, existe uma lista finita de primos cujo produto é `n`.

No projeto, isto fica implementado por:

```text
FATORACAO_RECONSTROI_NUMERO
FATORACAO_CONTEM_APENAS_PRIMOS
TFA_EXISTENCIA_OPERACIONAL
```

## Exemplo

- `n = 12`: menor fator `2`, sobra `6`; menor fator de `6` é `2`, sobra `3`; `3` é primo. Lista: `[2, 2, 3]`, e de fato `2×2×3=12`.

## Implementação

```text
nucleo/teorema_fundamental_aritmetica.py
```

## Validação

```text
testes/test_teorema_fundamental_aritmetica.py
```
