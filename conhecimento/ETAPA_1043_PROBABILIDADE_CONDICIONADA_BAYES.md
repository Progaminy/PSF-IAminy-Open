# PSF-IAminy — Marcador histórico 1043: teorema de Bayes

## Construção pura

O **Teorema de Bayes** responde: sabendo que um evento B aconteceu,
qual é a nova probabilidade de A? Em vez de partir da fórmula pronta
`P(A|B) = P(B|A)·P(A)/P(B)`, este ramo constrói probabilidade
condicional diretamente como razão entre conjuntos — quantos casos
de B também são casos de A, sobre o total de casos de B — e só depois
confirma que essa razão coincide com a fórmula clássica. Não recomeça
do zero: liga direto a `medida e probabilidade finita` (ETAPA 921-960),
que já constrói `probabilidade_como_par` e `condicional_como_par` a
partir de conjuntos e pesos.

"Probabilidade condicionada (Bayes)" existia neste projeto só como texto
de resposta legada (`nucleo/conceitos_avancados_puros.py`): explicação e
exemplo prontos, sem prova PSF, código ou teste.

```text
medida e probabilidade finita (ETAPA 921-960)
→ P(A) e P(B) como pares (medida do evento, medida do universo)
→ P(A|B) direto = medida(A∩B) / medida(B) (já existe, condicional_como_par)
→ fórmula de Bayes: P(A|B) = P(B|A)·P(A) / P(B)
→ conferência: a fórmula precisa bater com P(A|B) calculado direto
```

Bayes não entra como fórmula pronta: `bayes_como_par` calcula
`P(B|A)·P(A)/P(B)` a partir dos mesmos conjuntos e pesos, e confere por
produto cruzado exato que o resultado bate com `condicional_como_par(a,
b, ...)` — a probabilidade condicional calculada diretamente da
interseção dos conjuntos, sem passar pela fórmula. Se divergirem, é erro
de construção, não um teorema aceito por confiança. Testado com pesos
uniformes e não uniformes.

Distribuições contínuas e Bayes com densidade de probabilidade (em vez de
conjuntos finitos) dependem de reais completos e continuam em aberto.

## Exemplo

- Dado de 6 faces: A = "número par" `{2,4,6}`, B = "maior que 3" `{4,5,6}`. `P(A|B)` direto = `|{4,6}|/|{4,5,6}| = 2/3`; a fórmula de Bayes `P(B|A)·P(A)/P(B)` chega exatamente ao mesmo `2/3`.

## Dependências permitidas

- medida probabilidade finita
- ponte racionais reais

## Implementação

```text
nucleo/probabilidade_condicionada_bayes.py
```

## Validação

```text
testes/test_probabilidade_condicionada_bayes.py
```

## Estado

Teorema de Bayes construído e testado sobre conjuntos finitos, conferido
contra a probabilidade condicional direta, com pesos uniformes e não
uniformes. Distribuições contínuas continuam como próximo alvo.
