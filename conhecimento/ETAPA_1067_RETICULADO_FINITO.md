# PSF-IAminy — Marcador histórico 1067: reticulado finito

## Construção pura

Um **reticulado** é uma ordem parcial (um conjunto onde alguns pares de
elementos podem ser comparados por "≤", mas nem todos precisam ser) com
uma propriedade extra: TODO par de elementos tem um **supremo** (a
menor cota superior comum, o "mínimo teto" que fica acima dos dois) e
um **ínfimo** (a maior cota inferior comum, o "máximo chão" que fica
abaixo dos dois), ambos dentro do próprio conjunto. Nem toda ordem
parcial é reticulado: basta dois elementos terem duas cotas superiores
diferentes, nenhuma menor que a outra, para o supremo deixar de existir.

Bloco 461-470 do segundo lote de currículo externo (Álgebra Universal e
Teoria de Modelos): estrutura, homomorfismo e equivalência elementar
finita já existiam (`nucleo/teoria_modelos_prova_finita.py`, ETAPA
361-380); álgebra de Boole existia como raiz (`nucleo/logica.py`,
domínio fixo {V,F}); retículos gerais, não. A ponte mais direta não era
recomeçar do zero: já existe ordem parcial finita (ETAPA 68,
`ORDEM_PARCIAL_PURA`), e um reticulado é, por definição, um poset com
uma propriedade a mais.

```text
ordem parcial (ETAPA 68)
→ cota superior comum de x,y = elemento do domínio acima dos dois
→ supremo = a cota superior comum que fica abaixo de todas as outras
  (busca exaustiva sobre o domínio finito, mesma disciplina de
  EXISTE_COLORACAO_PURA)
→ ínfimo = dual, maior cota inferior comum
→ reticulado = poset onde TODO par do domínio tem supremo e ínfimo
```

A unicidade do supremo/ínfimo, quando existe, não precisa de verificação
à parte: se dois elementos fossem ambos "a menor cota superior", a
antissimetria da ordem parcial (já provada por `ORDEM_PARCIAL_PURA`)
força os dois a serem iguais. O que de fato falha, e é o ponto real deste
conceito, é a *existência*: testado com um reticulado real (domínio
{∅,{a},{b},{a,b}} ordenado por inclusão de subconjunto — o reticulado
booleano B2, o mesmo diamante que aparece em qualquer curso de álgebra) e
com um poset que não é reticulado, onde duas cotas superiores comuns são
incomparáveis entre si (nenhuma é a menor, logo o supremo não existe) — o
mesmo domínio, pela simetria da construção, também falha em ínfimo para
o par dual, deixando claro que "ter cota comum" não é o mesmo que "ter a
melhor cota comum".

Compacidade e Löwenheim-Skolem (mesmo bloco 461-470) continuam fora de
escopo: são teoremas sobre estruturas infinitas, sem sentido na versão
finita já construída em ETAPA 361-380.

## Exemplo

- Domínio {∅, {a}, {b}, {a,b}} ordenado por inclusão de subconjunto (o diamante booleano B2): supremo({a},{b}) = {a,b}, ínfimo({a},{b}) = ∅ -- é um reticulado.
- Domínio {0,1,2,3,4} com 0 abaixo de todos, 1 e 2 abaixo de 3 e de 4, mas 3 e 4 incomparáveis entre si: supremo(1,2) não existe (3 e 4 são duas cotas superiores, nenhuma menor que a outra) -- não é um reticulado.

## Dependências permitidas

- ordem parcial

## Implementação

```text
nucleo/reticulado_finito.py
```

## Validação

```text
testes/test_reticulado_finito.py
```

## Estado

Supremo, ínfimo e reticulado finito construídos e testados: um reticulado
real (B2, diamante de subconjuntos) com supremo/ínfimo confirmados par a
par, e um poset genuíno que não é reticulado (cotas comuns existem, mas
sem uma que seja a menor/maior) para não confundir "ter cota" com "ter
reticulado". Álgebra universal genérica (estrutura + operações +
axiomas verificados sobre domínio arbitrário) e álgebra de Boole sobre
domínio arbitrário (não só {V,F}) continuam como próximo alvo do mesmo
bloco.
