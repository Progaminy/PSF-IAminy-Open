# PSF-IAminy — Marcador histórico 1046: função por ramos

## Construção pura

Uma **função por ramos** não é conhecimento novo: é uma função cuja
relação é a união de várias sub-relações, cada uma válida numa parte
diferente do domínio (ex.: `f(x) = x²` se x<0, `f(x) = x+1` se x≥0).
Este ramo liga direto a `função como relação especial` (ETAPA 70) e
`aplicação finita` (ETAPA 71).

"Função por ramos" existia neste projeto só como texto de resposta
legada (`nucleo/conceitos_avancados_puros.py`): explicação e exemplo
prontos, sem prova PSF, código ou teste.

```text
função como relação especial (ETAPA 70) + aplicação finita (ETAPA 71)
→ cada ramo declara: a que parte do domínio pertence + qual fórmula usa
→ avaliar(x): encontra os ramos cujo domínio contém x
→ nenhum ramo contém x → domínio não cobre esse ponto, erro
→ mais de um ramo contém x → domínio sobreposto, função ambígua, erro
→ exatamente um ramo → aplica a fórmula desse ramo
```

Uma função por ramos só está bem definida quando os ramos particionam o
domínio (cada ponto pertence a exatamente um ramo). Isso não é assumido:
`FuncaoPorRamos.avaliar` confere as duas condições — sem ramo e ramo
duplicado — a cada chamada, sobre o `x` pedido, não sobre o domínio
inteiro de uma vez (o que exigiria enumerar um domínio potencialmente
infinito).

Testado com o exemplo clássico `f(x) = x² se x<0, x+1 se x≥0` (incluindo
o ponto de transição `x=0`), com uma lacuna proposital (nenhum ramo cobre
`x=0`) e com uma sobreposição proposital (dois ramos cobrem `x=0`) — as
duas falhas são detectadas, não silenciadas.

## Exemplo

- `f(x) = x²` se `x<0`, `f(x) = x+1` se `x≥0`: `f(-2) = 4` (usa o primeiro ramo), `f(0) = 1` (usa o segundo, ponto de transição incluído).
- Domínio com lacuna em `x=0` (nenhum ramo cobre) ou sobreposição em `x=0` (dois ramos cobrem): as duas falhas são detectadas, não silenciadas.

## Dependências permitidas

- função como relação especial
- aplicação finita
- ponte racionais reais

## Implementação

```text
nucleo/funcao_por_ramos.py
```

## Validação

```text
testes/test_funcao_por_ramos.py
```

## Estado

Função por ramos construída e testada: avaliação, detecção de lacuna no
domínio e detecção de sobreposição entre ramos.
