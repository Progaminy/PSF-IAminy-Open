# PSF-IAminy — Marcador histórico 1069: coloração de arestas

## Construção pura

Uma **coloração de arestas** atribui uma cor a cada aresta de um grafo
de forma que duas arestas que compartilham um vértice nunca tenham a
mesma cor (diferente da coloração de vértices, onde o conflito é entre
vértices ligados por uma aresta). A pergunta central é: qual é o menor
número de cores suficiente para colorir todas as arestas de um grafo
sem esse conflito?

Terceiro corte de P2, bloco 551-560 (Combinatória Avançada): o alvo real
seria Ramsey (R(3,3)=6, por busca exaustiva sobre colorações de arestas
de K6), mas o projeto só tinha coloração de VÉRTICES (ETAPA 118) — sem
coloração de arestas, nenhum resultado de Ramsey seria honesto. Este é o
pré-requisito, não recomeça do zero: reaproveita a mesma disciplina de
busca exaustiva de `EXISTE_COLORACAO_PURA` (ETAPA 118), só trocando o que
é colorido.

```text
grafo como relação binária (ETAPA 111)
→ arestas não-dirigidas = cada par {a,b} conta uma vez, não duas (a
  convenção do projeto representa {a,b} como DOIS pares na tupla)
→ coloração de arestas válida = nenhum par de arestas que compartilham
  um vértice tem a mesma cor
→ existe coloração com até k cores = busca exaustiva sobre as
  atribuições possíveis (mesma disciplina de EXISTE_COLORACAO_PURA)
```

Testado com três grafos pequenos e reais, não só um: K3 (triângulo) —
toda dupla de arestas compartilha vértice, então precisa de 3 cores, não
2; C4 (ciclo de 4, bipartido) — 2 cores bastam, confirmando o Teorema de
König de passagem (grafo bipartido é sempre Δ-colorível em arestas,
Δ=2 aqui); um caminho de 2 arestas — precisa de 2 cores, não 1, porque as
duas arestas compartilham o vértice do meio. Também testada a validação
direta de uma coloração explícita (não só a existência por busca), para
confirmar que `COLORACAO_ARESTAS_VALIDA_PURA` rejeita corretamente duas
arestas adjacentes com a mesma cor.

Índice cromático exato (Teorema de Vizing: Δ ou Δ+1, nunca mais) e
Ramsey propriamente dito continuam como próximo alvo — esta etapa só
prova existência para um k dado, não calcula o menor k nem aplica o
resultado a K6.

## Exemplo

- K3 (triângulo): as 3 arestas compartilham vértices duas a duas -- não é 2-colorível, mas é 3-colorível (cada aresta com sua própria cor).
- C4 (ciclo de 4 vértices): bipartido, 2 cores bastam (arestas opostas com a mesma cor).

## Dependências permitidas

- grafo relação simétrica

## Implementação

```text
nucleo/grafos_coloracao_arestas.py
```

## Validação

```text
testes/test_grafos_coloracao_arestas.py
```

## Estado

Arestas não-dirigidas, validação de coloração de arestas e existência de
coloração com k cores construídas e testadas (11 verificações: K3 precisa
de 3, C4 e caminho de 2 arestas precisam de 2, mais validação direta de
coloração explícita válida e inválida). Índice cromático exato e Teorema
de Ramsey (R(3,3)=6 em K6) continuam como próximo alvo, agora com a peça
que faltava para tentar honestamente.
