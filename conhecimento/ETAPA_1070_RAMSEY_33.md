# PSF-IAminy — Marcador histórico 1070: Teorema de Ramsey R(3,3)=6

## Construção pura

O **Teorema de Ramsey R(3,3)=6** responde uma pergunta sobre festas:
qual é o menor número de pessoas necessário para garantir que, não
importa como se dividam as amizades (cada par se conhece ou não), sempre
existam 3 pessoas que se conhecem mutuamente OU 3 que são estranhas
entre si? A resposta é 6 — traduzido para grafos: em qualquer coloração
de 2 cores das arestas do grafo completo K6, existe sempre um triângulo
com as três arestas da mesma cor; com apenas 5 pessoas (K5), isso deixa
de ser garantido.

Fecha o alvo real do bloco 551-560 (Combinatória Avançada) que a ETAPA
1069 (coloração de arestas) foi construída para servir de pré-requisito.
Não recomeça do zero: reaproveita `ARESTAS_NAO_DIRIGIDAS_PURA` e a chave
canônica de aresta da ETAPA 1069 diretamente.

```text
coloração de arestas (ETAPA 1069)
→ grafo completo K_n = todo par de vértices distintos é aresta
→ triângulo monocromático = três vértices cujas três arestas têm a
  mesma cor
→ R(3,3)=6 = duas metades, ambas confirmadas por busca exaustiva:
  (a) K6 não admite NENHUMA 2-coloração sem triângulo monocromático
  (b) K5 admite pelo menos uma (contraexemplo real, não hipotético)
```

O resultado não é citado como fato conhecido — é confirmado
computacionalmente, instância por instância, mesma disciplina já usada
para Euler (ETAPA 123) e Hall (ETAPA 1066): busca exaustiva sobre as
2^15 = 32768 atribuições de cor das 15 arestas de K6 (cada uma conferida
contra os 20 triângulos possíveis), e sobre as 2^10 = 1024 atribuições
das 10 arestas de K5. Cronometrado antes de comprometer, por segurança:
K6 completo roda em frações de segundo (~0,1s), não há risco de deixar a
suíte lenta. K4 também testado (folga extra, confirma que o "salto" para
6 é o correto, não um acidente de tamanho pequeno).

Ramsey geral (R(m,n) para m,n arbitrários) continua fora de escopo — só
o caso R(3,3) foi construído, com o mesmo n fixo (6) que a literatura
matemática já estabelece como resposta exata.

## Exemplo

- K5 (5 pessoas): existe uma 2-coloração das 10 arestas sem nenhum triângulo monocromático (por exemplo, dois "pentágonos" de cores diferentes) -- 5 pessoas não bastam.
- K6 (6 pessoas): testadas as 32768 colorações possíveis de 2 cores das 15 arestas, todas têm pelo menos um triângulo monocromático -- 6 pessoas já bastam.

## Dependências permitidas

- grafo relação simétrica

## Implementação

```text
nucleo/ramsey_33.py
```

## Validação

```text
testes/test_ramsey_33.py
```

## Estado

R(3,3)=6 confirmado computacionalmente nas duas direções: K6 sempre tem
triângulo monocromático (32768 colorações testadas, nenhuma escapa), K5
tem contraexemplo real (existe coloração sem triângulo monocromático).
K4 testado como folga extra. 7 verificações, incluindo tempo de execução
sob 30s. Ramsey geral (R(m,n) arbitrário) continua fora de escopo.
