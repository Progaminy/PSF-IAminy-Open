# PSF-IAminy — Marcador histórico 1038: trigonometria plana (lei dos cossenos e dos senos)

## Construção pura

A **lei dos cossenos** generaliza o Teorema de Pitágoras para qualquer
triângulo, não só o retângulo: `|AB|² = |CA|² + |CB|² − 2·(CA·CB)`, onde
o último termo mede o quanto o ângulo em C se afasta de 90°. Quando o
ângulo é reto, o produto escalar `CA·CB` zera e a fórmula volta a ser
exatamente `|AB|² = |CA|² + |CB|²`. A **lei dos senos** faz o mesmo
papel para relacionar lados e ângulos opostos entre si, sem depender de
um ângulo reto existir no triângulo.

"Lei dos cossenos" já existia neste projeto, mas só como texto de resposta
legada (`matematica/candidatos.py`, `nucleo/conceitos_avancados_puros.py`):
explicação e exemplo prontos, sem prova PSF, sem código e sem teste. A
trigonometria natural (ETAPA 1033) também fechou só o caso do triângulo
retângulo. Esta etapa constrói a generalização para triângulo qualquer.

```text
racionais assinados (ETAPA 1034/1035)
→ ponto (x, y) e vetor entre dois pontos
→ produto escalar: comprimento × comprimento × cosseno do ângulo entre eles
→ norma ao quadrado = produto escalar consigo mesmo (sem raiz quadrada)
→ |AB|² = |(A−C) − (B−C)|² = |A−C|² + |B−C|² − 2·(A−C)·(B−C)
→ lei dos cossenos: quando o ângulo é reto, o termo do produto escalar
  desaparece e a fórmula volta a ser exatamente a relação pitagórica
```

O ponto central: nenhuma função trigonométrica pronta é chamada, e nenhum
ângulo precisa ser medido em graus ou radianos. O cosseno de um ângulo
nasce definido pela própria relação — produto escalar dividido pelo
produto dos comprimentos — a mesma ideia de "razão" já usada em ETAPA
1033, agora aplicada a vetores em vez de lados de triângulo retângulo.
`produto_dos_lados_vezes_cosseno` devolve exatamente esse produto escalar,
sem precisar isolar comprimento (raiz quadrada) nem ângulo isoladamente.

A prova em si é álgebra pura (expandir o quadrado de uma diferença de
vetores), testada nos três vértices de cada triângulo, não assumida. Um
triângulo retângulo (3-4-5, ângulo reto na origem) confirma que a lei dos
cossenos e a relação pitagórica são a mesma fórmula — a lei dos cossenos
não é conhecimento novo isolado, é a generalização natural de ETAPA 1033
para quando o ângulo entre os lados não é reto. Um triângulo obliquo (sem
nenhum ângulo reto) confirma que a fórmula continua valendo fora do caso
particular.

A lei dos senos nasce do mesmo tipo de ideia, trocando produto escalar por
produto vetorial: `u.produto_vetorial(v)` (componente z do produto
vetorial em 2D) vale comprimento × comprimento × seno do ângulo entre
eles, e sua magnitude é o dobro da área do triângulo — o mesmo
determinante que `TrianguloGeral.__post_init__` já usava para rejeitar
pontos colineares. `bc·senA = ac·senB = ab·senC` (todas iguais à área
dobrada) é algebricamente equivalente a `a/senA = b/senB = c/senC`:
dividir dos dois lados por `senA·senB` dá `b/senB = a/senA`. Como a área
de um triângulo não depende de qual vértice a calcula, essa igualdade é
verificada nos três vértices, em racionais exatos, sem calcular nenhum
seno. `area_triangulo` devolve a área como `Area` (ETAPA 1036) — a mesma
grandeza que nasce de `area_retangulo`, não uma unidade solta.

Um triângulo retângulo (3-4-5) confirma que a lei dos senos e a área por
Pitágoras concordam (área dobrada 12, área 6 em qualquer vértice); um
triângulo oblíquo confirma a mesma igualdade fora do caso reto, com o
valor de área conferido de forma independente pela fórmula do
"shoelace" (soma cruzada de coordenadas).

Círculo circunscrito e ângulos gerais (obtuso medido, orientação,
radianos) continuam como próximo alvo desta mesma linha.

## Exemplo

- Triângulo retângulo de lados 3, 4, 5: `|AB|²=25`, `|CA|²+|CB|²=9+16=25` -- lei dos cossenos coincide com Pitágoras porque o ângulo em C é reto.
- Triângulo oblíquo (sem ângulo reto): a lei dos cossenos ainda vale, e a área calculada pela fórmula do "shoelace" (soma cruzada de coordenadas) confirma o mesmo valor.

## Dependências permitidas

- ponte racionais reais
- triângulo retângulo
- relação pitagórica
- semelhança de triângulos
- razão
- medidas e grandezas

## Implementação

```text
nucleo/trigonometria_plana.py
```

## Validação

```text
testes/test_trigonometria_plana.py
```

## Estado

Lei dos cossenos e lei dos senos construídas e testadas por álgebra
vetorial exata (produto escalar e produto vetorial), para triângulo
retângulo (reduz a Pitágoras) e triângulo oblíquo. Área do triângulo
construída como grandeza (ETAPA 1036). Círculo circunscrito e ângulos
gerais continuam como próximo alvo.
