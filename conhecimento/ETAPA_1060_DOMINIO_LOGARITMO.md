# PSF-IAminy — Marcador histórico 1060: domínio de logaritmo composto com expressão linear

## Construção pura

Liga `logaritmos` (ETAPA 1045, que já recusa `x ≤ 0` internamente) a
`inequações` (ETAPA 1041): a resposta legada de
`nucleo/conceitos_avancados_puros.py` ("Qual é o domínio de f(x) =
ln(x - 4)?" → "x > 4", justificado por "logaritmo natural exige
argumento positivo") tinha só o resultado citado, sem resolver nada. Aqui
o domínio nasce de resolver `a·x+b > 0` como inequação linear de
verdade, reaproveitando `resolver_inequacao_linear` sem duplicar nenhuma
lógica de isolar x ou inverter comparador.

```text
logaritmos (ETAPA 1045) + inequações (ETAPA 1041)
→ domínio de log(a·x+b) = resolver a·x+b > 0
→ conferência: dentro do domínio, logaritmo_exato não levanta;
  fora do domínio, logaritmo_exato levanta de verdade
```

A conferência não se limita a resolver a inequação e aceitar por
confiança: `confirmar_fronteira_de_dominio` chama `logaritmo_exato` de
verdade dos dois lados do limite — dentro do domínio, com um argumento
escolhido como potência exata da base (para não levantar por outro
motivo que não seja domínio), e fora do domínio, onde `logaritmo_exato`
tem que levantar (é o primeiro código que ele checa, antes de qualquer
busca). Não é logaritmo natural (base `e`) especificamente: a exigência
de argumento positivo vale para qualquer base válida — a base usada na
conferência é só uma testemunha racional concreta.

Esta etapa cobre só domínio de composição linear dentro do logaritmo.
Resolver `eˣ = valor` (equação exponencial de verdade, não só domínio) e
provar que `eˣ` nunca cruza zero continuam dependendo de reais completos
(ETAPA 234) — não têm ponte rápida ainda.

## Dependências permitidas

- logaritmos
- inequações

## Implementação

```text
nucleo/dominio_logaritmo.py
```

## Validação

```text
testes/test_dominio_logaritmo.py
```

## Estado

Domínio de logaritmo composto com expressão linear construído e
testado: o exemplo legado (`ln(x-4)` → `x > 4`), um caso com coeficiente
positivo diferente, um caso com coeficiente negativo (inverte o
comparador) e rejeição de coeficiente zero — cada domínio confirmado
chamando `logaritmo_exato` de verdade dos dois lados da fronteira.
Equação exponencial de verdade e a prova de que `eˣ` nunca cruza zero
continuam como próximo alvo, dependendo de reais completos.
