# PSF-IAminy — Marcador histórico 1066: emparelhamento e Teorema de Hall

## Construção pura

Um **emparelhamento** num grafo é um conjunto de arestas onde nenhum
vértice se repete — cada vértice participa de, no máximo, uma delas.
Num grafo **bipartido** (vértices divididos em dois grupos A e B, toda
aresta ligando um vértice de A a um de B), a pergunta natural é: existe
um emparelhamento que cobre TODO o grupo A, casando cada vértice de A
com um vértice diferente de B? O **Teorema de Hall** (1935) responde
isso sem precisar testar todas as combinações possíveis: existe esse
emparelhamento se e somente se todo subconjunto S de A tiver pelo menos
|S| vizinhos em B (a "condição de Hall") — se algum grupo de vértices de
A, juntos, só alcançam menos vizinhos do que o próprio tamanho do
grupo, não há vizinhos suficientes para casar todos eles, e o
emparelhamento completo é impossível.

Bloco 421-430 do segundo lote de currículo externo (Teoria dos Grafos
Avançada): coloração (ETAPA 118) e grafo Hamiltoniano (ETAPA 124) já
existiam; planaridade e fluxo em redes continuam **explicitamente
proibidos** no bloco de grafos (`nucleo/grafos_finitos.py`, linhas
14-17). Emparelhamento e Teorema de Hall não violam essa proibição e
têm ponte direta: reaproveitam grafo bipartido (ETAPA 117), não
recomeçam do zero.

```text
grafo bipartido (ETAPA 117)
→ bipartição explícita = mesma busca 2-coloração de BIPARTIDO_PURA,
  devolvendo os dois grupos em vez de só V/F
→ emparelhamento = subconjunto de arestas onde nenhum vértice se repete
→ emparelhamento perfeito cobrindo grupo A = bijeção de A para um
  subconjunto de B, ligada por arestas reais (busca exaustiva sobre
  bijeções candidatas, mesma disciplina de HAMILTONIANO_PURA)
→ vizinhança de um subconjunto S de A = vértices de B ligados a algum
  vértice de S
→ condição de Hall = todo S ⊆ A tem |N(S)| >= |S| (busca exaustiva
  sobre os 2^|A| subconjuntos, mesma disciplina de EXISTE_COLORACAO_PURA)
→ Teorema de Hall (1935): existe emparelhamento cobrindo A sse A
  satisfaz a condição de Hall
```

O Teorema de Hall não é fingido nem citado como fato — é confirmado
computacionalmente, instância por instância, comparando as duas
respostas (existência por busca exaustiva × condição de Hall por busca
exaustiva), a mesma disciplina já usada para confirmar o Teorema de
Euler contra as Pontes de Königsberg (ETAPA 123, `EULERIANO_PURA`).
Testado com um caso positivo (condição vale, emparelhamento existe) e
dois casos negativos — incluindo um onde `|grupo_a| = |grupo_b|` mas a
estrutura das arestas ainda bloqueia o emparelhamento perfeito (dois
vértices de A competindo pelo mesmo único vizinho em B), para não
aceitar `|A| <= |B|` como condição suficiente por engano.

Random graphs, expanders e redes complexas (mesmo bloco 421-430)
continuam fora de escopo: exigiriam noção de probabilidade sobre grafos
ainda não construída — próximo alvo, não este.

## Exemplo

- Grupo A = {v0, v1}, grupo B = {v2, v3}, arestas v0-v2, v0-v3, v1-v2: existe emparelhamento perfeito (v0-v3, v1-v2), e a condição de Hall vale para todo subconjunto de A.
- Grupo A = {v0, v1}, grupo B = {v2}, arestas v0-v2, v1-v2: v0 e v1 competem pelo único vizinho v2 -- condição de Hall falha (|N({v0,v1})|=1 < 2), e de facto não existe emparelhamento cobrindo A.

## Dependências permitidas

- grafo bipartido

## Implementação

```text
nucleo/grafos_emparelhamento.py
```

## Validação

```text
testes/test_grafos_emparelhamento.py
```

## Estado

Bipartição explícita, emparelhamento, emparelhamento perfeito, vizinhança
de subconjunto, condição de Hall e confirmação computacional do Teorema
de Hall construídos e testados (15 verificações, caso positivo e dois
casos negativos). Random graphs, expanders e redes complexas do mesmo
bloco de currículo continuam como próximo alvo, sem base de probabilidade
sobre grafos ainda construída.
