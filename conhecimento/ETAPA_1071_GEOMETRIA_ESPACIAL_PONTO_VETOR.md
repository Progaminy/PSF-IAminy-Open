# PSF-IAminy — Marcador histórico 1071: geometria no espaço, Ponto3D/Vetor3D

## Construção pura

Item 239 pede geometria plana e geometria no espaço, do mesmo porte do
bloco de grafos — não uma etapa única. Este ramo é o primeiro corte
honesto do lado espacial: o primitivo `Ponto3D`/`Vetor3D`, extensão
mecânica de `Ponto`/`Vetor` (ETAPA 1038) para uma terceira coordenada,
sem polígono, plano, ângulo diedro ou volume de sólido arbitrário —
esses continuam próximo alvo.

```text
Ponto/Vetor (ETAPA 1038, RacionalAssinado)
→ Ponto3D/Vetor3D: mesma aritmética exata, terceira coordenada z
→ produto escalar 3D: soma dos três produtos coordenada a coordenada
  (extensão direta, sem peça nova)
→ produto vetorial 3D: aqui a diferença é conceitual, não só mecânica
  -- em 2D o produto vetorial é um NÚMERO (componente z, os dois
  vetores originais já têm z=0 implícito); em 3D é de novo um VETOR,
  perpendicular aos dois originais -- confirmado por produto escalar
  nulo contra ambos, não só aceito por sair da fórmula do determinante
→ colinearidade de três pontos = produto vetorial nulo (as três
  coordenadas, não uma só) -- mesmo teste do caso 2D (ETAPA 1038,
  `TrianguloGeral`)
```

Nenhuma peça nova de aritmética foi inventada: tudo em cima de
`RacionalAssinado.somar/subtrair/multiplicar` já provados.

## Dependências permitidas

- trigonometria plana

## Implementação

```text
nucleo/geometria_espacial.py
```

## Validação

```text
testes/test_geometria_espacial.py
```

## Estado

Primitivo `Ponto3D`/`Vetor3D` construído e testado: produto escalar,
produto vetorial (vetor, não número, perpendicular aos dois originais)
e colinearidade de três pontos no espaço. Segmento, ângulo diedro,
plano, polígono, área e volume continuam como próximo alvo — este
corte é só o primitivo de coordenadas, mesmo espírito de "ponto médio"
como primeiro passo da geometria plana.
