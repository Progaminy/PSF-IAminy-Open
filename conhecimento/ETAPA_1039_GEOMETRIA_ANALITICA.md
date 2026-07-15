# PSF-IAminy — Marcador histórico 1039: geometria analítica (reta)

## Construção pura

**Geometria analítica** estuda figuras geométricas (retas, círculos)
através das coordenadas dos seus pontos, em vez de desenho ou régua e
compasso: uma reta vira "o conjunto de pontos que satisfazem uma certa
equação", pertencimento vira "verificar essa equação", e paralelismo,
perpendicularidade e ponto médio viram operações algébricas exatas
sobre coordenadas.

"Geometria analítica" existia neste projeto só como texto de resposta
legada (`nucleo/conceitos_avancados_puros.py`): explicação e exemplo
prontos, sem prova PSF, código ou teste. Este ramo não recomeça do zero:
liga direto a ETAPA 1038 (trigonometria plana), reaproveitando `Ponto` e
`Vetor` já construídos e provados ali — o conhecimento não é uma fila
única, é um mapa, e este é um ramo que se conecta a outro já existente.

```text
ponto e vetor (ETAPA 1038)
→ reta = dois pontos distintos → direção = vetor entre eles
→ pertencimento = produto vetorial nulo entre (P − p1) e a direção
  (mesmo teste já usado para rejeitar pontos colineares em ETAPA 1038)
→ paralelismo = produto vetorial nulo entre duas direções
→ perpendicularidade = produto escalar nulo entre duas direções
  (mesmo teste já usado para reduzir a lei dos cossenos a Pitágoras)
→ coeficiente angular = dy/dx exato, indefinido para reta vertical
```

Nenhuma equação `Ax + By = C` precisa ser montada à parte para pertencer,
paralelismo ou perpendicularidade: os mesmos dois produtos (escalar e
vetorial) que já provam a lei dos cossenos e a lei dos senos em ETAPA 1038
respondem essas três perguntas diretamente, sem raiz quadrada e sem
aproximação. Isso não é coincidência: é o mesmo par de ferramentas
vetoriais reaproveitado num ramo vizinho, exatamente o formato de "mapa"
em vez de fila que o crescimento deste projeto vem seguindo.

Ponto médio nasce da média de cada coordenada, conferida contra a própria
definição: a distância² do ponto médio a cada extremo tem que ser igual.
Distância exata entre dois pontos e circunferência (`(x−a)²+(y−b)²=r²`)
ligam a `raiz_quadrada_exata_ou_none` (ETAPA 1048): quando o quadrado da
distância não é quadrado perfeito racional, a distância fica
honestamente sem forma exata — `None`, não aproximação. Pertencer à
circunferência não precisa da raiz nenhuma: só comparar o quadrado da
distância ao centro com o raio ao quadrado, exato.

Distância entre ponto e reta, interseção de retas e equação geral
`Ax + By = C` continuam como próximo alvo desta mesma linha.

## Exemplo

- Pontos (0,0) e (3,4): distância ao quadrado = 25, quadrado perfeito -- distância exata = 5.
- Círculo de centro (0,0) e raio² = 25: o ponto (3,4) pertence (3²+4²=25); o ponto (1,1) não pertence (1²+1²=2 ≠ 25).

## Dependências permitidas

- trigonometria plana
- equação quadrática exata
- ponte racionais reais
- razão

## Implementação

```text
nucleo/geometria_analitica.py
```

## Validação

```text
testes/test_geometria_analitica.py
```

## Estado

Reta, pertencimento, paralelismo, perpendicularidade, coeficiente
angular, ponto médio, distância exata (quando é quadrado perfeito) e
circunferência (construção e pertencimento) construídos e testados.
Distância ponto-reta, interseção de retas e equação geral continuam como
próximo alvo.
