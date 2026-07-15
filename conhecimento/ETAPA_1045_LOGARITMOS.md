# PSF-IAminy — Marcador histórico 1045: logaritmo exato

## Construção pura

O **logaritmo** de x na base `base` é a pergunta "a que expoente devo
elevar `base` para chegar em x?" — o inverso da potenciação. Esta etapa
fecha o caso exato: quando x É de facto uma potência exata de `base`
(ex.: log₂8=3, porque 2³=8), o expoente é encontrado por busca, sem
aproximação nenhuma. O logaritmo geral (base e resultado reais
arbitrários, ex.: log₂10) exige reais completos, ainda em aberto (ETAPA
1035, próximo alvo).

"Logaritmos" existia neste projeto só como texto de resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova PSF, código ou teste.

```text
potência (já usada em potência modular, ETAPA 27, e progressão geométrica, ETAPA 1040)
→ log_base(x): buscar n tal que base^n = x
→ n >= 0: multiplica base por si mesma repetidamente
→ n < 0: multiplica o recíproco da base repetidamente (cobre x < 1)
→ se nenhum n dentro do limite de busca bater, declara honestamente
  que x não é potência exata — nunca aproxima o que deveria ser exato
```

A busca em duas direções evita ter que decidir de antemão se `x` é maior
ou menor que 1 em relação à base: tenta multiplicar a base (cobre bases
maiores que 1 subindo, ou bases menores que 1 descendo) e, se não achar,
tenta o recíproco. Testado com `log_2(8)=3`, `log_2(1/8)=-3` e
`log_(1/2)(1/8)=3` — a mesma pergunta respondida de lados diferentes.

Logaritmo de número que não é potência exata da base (por exemplo,
`log_2(5)`) continua indefinido nesta etapa: exigiria reais completos
para aproximar um expoente irracional.

## Exemplo

- `log_2(8) = 3`, porque `2³ = 8` (busca subindo, expoente positivo).
- `log_2(1/8) = -3` e `log_(1/2)(1/8) = 3` -- a mesma pergunta respondida de lados diferentes (base ou recíproco).

## Dependências permitidas

- potência modular
- ponte racionais reais

## Implementação

```text
nucleo/logaritmos.py
```

## Validação

```text
testes/test_logaritmos.py
```

## Estado

Logaritmo exato construído e testado por busca de expoente inteiro, nos
dois sentidos (base > 1 e base < 1, x > 1 e x < 1). Logaritmo de valor
que não é potência exata continua como próximo alvo, depois de reais
completos.
