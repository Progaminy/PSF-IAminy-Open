# PSF-IAminy — Marcador histórico 1072: centralidade de grau e coeficiente de agrupamento

## Construção pura

Em análise de redes sociais, dois números resumem a posição de uma
pessoa (vértice) na rede. A **centralidade de grau** mede quão
conectado o vértice é, comparado ao máximo possível: grau do vértice
dividido pelo maior grau que qualquer vértice poderia ter (n-1, se
tivesse aresta com todo mundo). O **coeficiente de agrupamento** mede
se os "amigos" de um vértice também são amigos entre si: dos pares de
vizinhos de v, que fração está de facto ligada — um valor alto indica
um grupo fechado (todo mundo se conhece), um valor baixo indica que v
liga pessoas que, sem ele, não se conectariam.

Bloco 661-670 (Matemática das Redes Sociais) da auditoria de currículo
externo: grafos reais já existiam (grau, conectividade, caminho, ciclo —
ETAPA 111-127), mas nenhuma métrica de rede social. Não recomeça do
zero: reaproveita `GRAU_VERTICE_PURO`/`_vizinhos` (ETAPA 112/115) e
`RacionalAssinado` (já provado na linha dos reais) para devolver frações
exatas, nunca `float`.

```text
grau de vértice (ETAPA 112) + vizinhos (ETAPA 115)
→ centralidade de grau = grau(v) / (n-1), a fração do máximo possível
  de vizinhos que v de facto tem
→ coeficiente de agrupamento = dos pares de vizinhos de v, que fração
  está ligada entre si (triângulos através de v / pares possíveis)
```

Nenhuma das duas métricas exige estrutura nova — são razões exatas
sobre o que já existe. O coeficiente de agrupamento é honestamente
`None` quando o grau é menor que 2 (não há par de vizinhos para
formar triângulo nenhum): fingir `0` esconderia a diferença real entre
"nenhum triângulo possível" e "triângulo possível mas ausente".

Testado com quatro grafos pequenos e reais, não só um: K4 (completo) —
centralidade e agrupamento máximos, `1/1`, todo vizinho de todo vértice
está ligado a todos os outros; grafo estrela (centro ligado a 3 folhas,
folhas sem ligação entre si) — centralidade do centro `1/1` mas
agrupamento `0/1` (nenhum par de folhas ligado), centralidade de folha
`1/3` e agrupamento `None` (grau 1); um triângulo aberto (0-1, 1-2, sem
0-2) — agrupamento de v1 é `0/1`; o mesmo grafo fechado com a aresta
0-2 acrescentada — agrupamento de v1 sobe para `1/1`, confirmando que a
métrica de facto reage à mudança estrutural, não é uma constante
disfarçada.

Centralidade de intermediação (betweenness, exige caminho mínimo entre
TODO par de vértices) e de proximidade (closeness) continuam fora de
escopo — pedem infraestrutura de caminho ponderado ainda não composta
com este bloco especificamente para essas métricas.

## Exemplo

- Grafo estrela (centro ligado a 3 folhas, folhas sem ligação entre si): centralidade do centro é 1 (grau 3 = n-1), mas coeficiente de agrupamento do centro é 0 (nenhum par de folhas está ligado entre si).
- K4 (grafo completo de 4 vértices): centralidade e agrupamento de qualquer vértice são ambos 1 -- todo vizinho está ligado a todos os outros.

## Dependências permitidas

- grafo relação simétrica

## Implementação

```text
nucleo/grafos_redes_sociais.py
```

## Validação

```text
testes/test_grafos_redes_sociais.py
```

## Estado

Centralidade de grau e coeficiente de agrupamento construídos e
testados (8 verificações: grafo completo, estrela, triângulo aberto e
fechado). Centralidade de intermediação e de proximidade continuam como
próximo alvo, sem infraestrutura de caminho ponderado composta ainda.
