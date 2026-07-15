# PSF-IAminy — Marcador histórico 1042: equações com radical (√linear = constante ou linear)

## Construção pura

Uma **equação com radical** (`√(a·x+b) = valor`) resolve-se elevando
os dois lados ao quadrado para eliminar a raiz, isolando x, e depois
CONFERINDO a solução na equação original — o passo de conferência é
obrigatório, porque elevar ao quadrado pode introduzir uma raiz falsa
que não satisfaz a equação de partida. Isto não é a mesma coisa que a
lei geradora de raiz quadrada (ETAPA 1035) — aquela aproxima `√2`
numericamente porque `√2` é irracional; aqui a equação é montada para
que a resposta seja um racional exato, e o trabalho é puramente
algébrico.

"Radicais com variáveis" existia neste projeto só como texto de resposta
legada (`nucleo/conceitos_avancados_puros.py`): explicação e exemplo
prontos, sem prova PSF, código ou teste.

```text
equação primeiro grau finita (ETAPA 133)
→ √(a·x+b) = valor: se valor < 0, sem solução (raiz nunca é negativa)
→ eleva ao quadrado: a·x+b = valor²
→ isola x (mesma álgebra de ETAPA 133/1041)
→ reconstrói o radicando a partir de x e confere que bate com valor²
```

Exemplo clássico: `√(x+3) = 5` eleva a `x+3 = 25`, dando `x = 22`. A
checagem de domínio (raiz nunca negativa, radicando reconstruído não
negativo) não é decorativa: é a mesma disciplina de conferência de
`nucleo/contas_armadas.py` e `nucleo/progressoes.py` — a solução só é
aceita se reconstruir exatamente o que a elevação ao quadrado assumiu.

O caso mais geral, `√(a·x+b) = c·x+d`, foi fechado depois (ligado a
`equação quadrática exata`, ETAPA 1048): elevar ao quadrado dá
`c²x² + (2cd−a)x + (d²−b) = 0`, resolvida pela fórmula resolvente exata.
Aqui o lado direito também depende de x e pode ficar negativo para algum
candidato — isso é raiz estranha de verdade (soluciona a equação elevada
ao quadrado, mas não a original, porque raiz quadrada nunca é negativa).
`resolver_raiz_igual_a_linear` filtra cada candidato pelo sinal do lado
direito, não só reconstrói o radicando. Exemplo clássico: `√(2x+3) = x`
eleva a `x²−2x−3=0`, raízes `3` e `−1`; `x=−1` dá lado direito `−1 < 0` e
é descartada como estranha, sobrando só `x=3`.

Quando o discriminante da quadrática resultante não é quadrado perfeito
racional, a equação fica honestamente sem solução exata (dependeria de
reais completos), em vez de aproximar.

## Exemplo

- `√(2x+3) = x`: eleva a `x²-2x-3=0`, raízes 3 e -1; `x=-1` dá lado direito negativo (raiz estranha, descartada), sobra só `x=3`.

## Dependências permitidas

- equação primeiro grau finita
- equação quadrática exata
- ponte racionais reais

## Implementação

```text
nucleo/radicais_variaveis.py
```

## Validação

```text
testes/test_radicais_variaveis.py
```

## Estado

Equação `√(a·x+b) = valor` e `√(a·x+b) = c·x+d` construídas e testadas:
domínio, elevação ao quadrado, conferência do radicando reconstruído e
filtragem de raiz estranha pelo sinal do lado direito. Discriminante não
quadrado perfeito continua honestamente sem solução exata, depois de
reais completos.
