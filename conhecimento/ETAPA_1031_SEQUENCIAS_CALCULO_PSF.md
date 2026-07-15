# PSF-IAminy — Etapa 1031
## Sequência de conhecimento matemático por níveis de cálculo

Regra desta etapa: conservar o padrão pedido pelo Pensador Sem Fronteiras:

```text
Nível 1 — adição diagonal / dobro:
1 + 1, 2 + 2, 3 + 3, 4 + 4, ...

Nível 2 — multiplicação diagonal / quadrado:
1 × 1, 2 × 2, 3 × 3, 4 × 4, ...

Nível 3 — potência diagonal:
1 ^ 1, 2 ^ 2, 3 ^ 3, ...

Nível 4 — superpotência finita / tetração diagonal:
1 ↑↑ 1, 2 ↑↑ 2, 3 ↑↑ 3, ...
```

O módulo operacional é:

`nucleo/sequencias_calculo_psf.py`

O teste é:

`testes/test_sequencias_calculo_psf.py`

## Construção PSF

A escada nasce assim:

```text
sucessor
↓
adição = sucessor repetido
↓
multiplicação = adição repetida
↓
potência = multiplicação repetida
↓
superpotência/tetração = potência repetida
↓
hiperoperação finita = operação anterior repetida
```

A regra de pureza é: fórmula pronta pode validar nos testes, mas não funda o conceito.

## Índice propulsional

O índice propulsional é uma tabela navegável por nível. Cada nível mantém a mesma forma:

```text
n operado consigo mesmo no nível atual
```

Assim, para cada `n`, o motor consegue acessar:

```text
n + n
n × n
n ^ n
n ↑↑ n
...
```

sem confundir fórmula com origem. O valor pode ser bloqueado por limite explícito quando cresce demais. Bloquear é honesto; fingir calcular infinito não é PSF.


## Extensão escolar nativa — Etapa 31 operacional

Para validar problemas básicos de sala de aula sem recorrer a bibliotecas matemáticas externas, foi acrescentado o módulo `nucleo/aritmetica_escolar_nativa.py`. Ele é uma especialização didática da mesma regra desta etapa: construir por sucessor, retirada, agrupamento e repartição finita, sem usar `math`, divisão pronta, divisão inteira pronta, resto pronto ou potência pronta como fundamento.
