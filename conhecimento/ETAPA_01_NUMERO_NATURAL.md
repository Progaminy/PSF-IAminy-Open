# PSF-IAminy — Etapa 1

## Número natural: zero e sucessor

Lei permanente:

> Nenhum conceito pode ser usado antes de nascer.

Esta etapa nasce primeiro porque tudo o resto do PSF-Matemática -- divisibilidade
(Etapa 3), MDC (Etapa 4), quociente (Etapa 7), inteiros relativos (Etapa 16) e
todo o resto -- já citava "número natural", "zero", "sucessor" como se
existissem, sem nenhum documento próprio ter sido escrito para eles. Achado
real, não hipotético: a própria Etapa 3 dizia "nenhum conceito pode ser usado
antes de nascer" e no parágrafo seguinte usava "adição" e "multiplicação" sem
nenhuma das duas ter nascido ainda. Esta etapa fecha essa dívida pelo começo.

## Construção pura

Um número natural não é um símbolo (`"0"`, `"1"`, `"2"`...) — é a capacidade
de repetir uma ação um número determinado de vezes. Contar é isso: dizer
"mais um" repetidamente a partir de um ponto de partida.

```text
zero = a ausência de repetição -- o ponto de partida, antes de qualquer "mais um"
sucessor(n) = "mais um" aplicado a n -- o único jeito de andar para frente

zero
sucessor(zero) = "um"
sucessor(sucessor(zero)) = "dois"
sucessor(sucessor(sucessor(zero))) = "três"
...
```

Formalmente (numeral de Church/Peano): um número `n` é a própria capacidade de
aplicar uma função `f` (o "passo") `n` vezes a um ponto de partida `x`.

```text
zero = f -> x -> x                    (aplica f zero vezes: devolve x)
sucessor(n) = f -> x -> f(n(f)(x))    (aplica f mais uma vez que n aplicava)
```

Nenhum número é definido citando outro número por nome ("três é depois do
dois") — cada um nasce só de quantas vezes o sucessor foi aplicado ao zero.
Não existe símbolo `"3"` aqui: existe `sucessor(sucessor(sucessor(zero)))`, e o
símbolo é só uma abreviação para humanos lerem, nunca o objeto em si.

## Exemplo

- Contar até três é `sucessor(sucessor(sucessor(zero)))` -- "3" é só uma abreviação para isso, nunca o objeto em si.
- Dois números são o mesmo número exatamente quando o sucessor foi aplicado a mesma quantidade de vezes ao zero para os dois.

## Dependências permitidas

(nenhuma — esta é a raiz da linha matemática, o ponto antes do qual não há
mais nada para PSF-Matemática construir)

## Implementação

```text
nucleo/primitivas.py
```

`ZERO` e `S` (sucessor), linhas da "PRIMITIVA 1: Aplicação Sucessiva". Zero
função nativa do Python usada — só lambda calculus puro.

## Validação

```text
testes/test_numero_natural.py
```

## Estado

Zero e sucessor construídos e testados: contagem por aplicação repetida,
tradução para inteiro Python só como leitura de saída (`nucleo/traducao.py`,
nunca como fundamento do cálculo), e a prova de que dois números só são "o
mesmo número" quando a mesma quantidade de sucessores foi aplicada. Adição
(Etapa 2) é o próximo passo direto: contar é aplicar sucessor repetidamente.
