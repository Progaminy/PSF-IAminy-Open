# PSF-IAminy — Etapa 6: Euclides por subtração

## Lei da etapa

O algoritmo de Euclides não nasce primeiro como módulo.
Ele nasce como preservação de divisores comuns por diferença.

Ainda é proibido usar:

```text
divisão
resto
módulo
fatoração
primalidade
```

## Ideia central

Se `a > b`, então os divisores comuns de `a` e `b` são os mesmos divisores comuns de `a-b` e `b`.

```text
comuns(a,b) = comuns(a-b,b)
```

Se `b > a`, então:

```text
comuns(a,b) = comuns(a,b-a)
```

Logo o maior divisor comum também é preservado.

## Regra recursiva

```text
MDC(a,0) = a
MDC(0,b) = b
MDC(a,a) = a
```

Se `a > b`:

```text
MDC(a,b) = MDC(a-b,b)
```

Se `b > a`:

```text
MDC(a,b) = MDC(a,b-a)
```

## Estado de (0,0)

```text
MDC(0,0)
```

continua indefinido, porque todo natural positivo divide zero e não existe maior divisor comum.

O código pode devolver `ZERO` como sentinela operacional, mas a validade é dada por:

```text
MDC_SUBTRACAO_DEFINIDO(0,0) = falso
```

## Conclusão

Agora existem duas formas legítimas de obter o MDC:

1. **MDC por definição**: procura o maior divisor comum.
2. **MDC por subtração**: preserva os divisores comuns até chegar ao caso final.

As duas devem coincidir.

O próximo passo natural, depois desta etapa, será construir:

```text
quociente
resto
divisão euclidiana
Euclides eficiente por resto
```

Mas isso ainda não foi usado aqui.

## Exemplo

- `MDC(18, 12)` por subtração: `18 > 12` -> `comuns(18,12) = comuns(6,12)`; `12 > 6` -> `comuns(6,12) = comuns(6,6)`; `MDC(6,6) = 6`. Confere com o MDC por definição (Etapa 4): `MDC(18,12)=6`.
- `MDC(0,0)` continua indefinido -- nenhuma regra da lista acima se aplica (não é `a>b` nem `b>a` nem o caso `MDC(a,a)` com `a` positivo).

## Forma operacional no projeto

`nucleo/euclides_subtracao_pura.py`
`testes/test_fluxo_natural_sem_dependencias.py`
