# PSF-IAminy — Marcador histórico 1065: distância ponto-reta e interseção de retas

## Construção pura

ETAPA 1039 (geometria analítica) já deixou documentado o próprio "próximo
alvo": distância entre ponto e reta, interseção de retas e equação geral
`Ax + By = C`. Este ramo fecha essa continuação, sem recomeçar — reaproveita
`Reta`, `pertence_a_reta` e `retas_paralelas` (ETAPA 1039) e `Vetor`
(produto vetorial/escalar, ETAPA 1038) tal como já provados.

```text
ponto, vetor (ETAPA 1038) e reta (ETAPA 1039)
→ distância² de ponto a reta = (produto vetorial de (ponto−p1) pela
  direção)² / (norma² da direção) — mesma leitura de área usada pela lei
  dos senos em ETAPA 1038, sem raiz quadrada
→ distância exata = liga ao quadrado acima `raiz_quadrada_exata_ou_none`
  (ETAPA 1048); quadrado não-perfeito devolve None, nunca aproxima
→ equação geral a·x + b·y = c de uma reta = (a,b) = (dy, −dx) da direção,
  c = a·x1 + b·y1 de um ponto conhecido da reta
→ interseção de duas retas = sistema 2×2 das duas equações gerais,
  resolvido pela regra de Cramer sobre RacionalAssinado — o determinante
  a1·b2 − a2·b1 é a mesma expressão que `retas_paralelas` já usa (produto
  vetorial das direções): paralelas dá determinante zero, por isso a
  interseção honestamente devolve None nesse caso, nunca divide por zero
→ o ponto resultante é sempre conferido pertencendo às duas retas de
  verdade (`pertence_a_reta`), não só aceito por sair da fórmula de Cramer
```

Nenhuma peça nova de álgebra linear foi inventada nem importada: o sistema
2×2 é pequeno e fixo (sempre duas equações, duas incógnitas), então a
regra de Cramer direta sobre `RacionalAssinado` é mais honesta aqui do que
forçar `nucleo/eliminacao_gaussiana_finita.py` (ETAPA 110) — aquele
solver busca o inverso multiplicativo por busca num domínio finito
(`_reciproco_por_busca`), o que não se aplica a um corpo infinito como os
racionais, que já têm `.reciproco()` direto. Considerado antes de escrever
qualquer código, para não forçar uma peça que não serve.

## Dependências permitidas

- geometria analítica
- trigonometria plana
- equação quadrática exata

## Implementação

```text
nucleo/distancia_intersecao_retas.py
```

## Validação

```text
testes/test_distancia_intersecao_retas.py
```

## Estado

Distância ao quadrado de ponto a reta, distância exata (quando o quadrado
é quadrado perfeito racional) e interseção de duas retas não paralelas
construídas e testadas. Equação geral `Ax+By=C` isolada como objeto
próprio (em vez de só uma tupla `(a,b,c)` interna) e o resto do item 239
(segmento, ângulo, polígono, área, círculo além do já construído, e
geometria no espaço) continuam como próximo alvo.
