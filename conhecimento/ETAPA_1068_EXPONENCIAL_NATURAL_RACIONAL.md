# PSF-IAminy — Marcador histórico 1068: exponencial natural para x racional

## Construção pura

ETAPA 1064 (completude por sequências de Cauchy) já deixou dito que a
base construída "já basta para o resto do projeto (séries, limites,
eˣ)". Este ramo fecha esse alvo — resíduo do item 300 — no escopo
honesto que a própria base permite: eˣ para x racional, não eˣ para x
real qualquer, nem a prova de que eˣ>0 sempre (as duas continuam
residuais).

```text
soma parcial exata (ETAPA 1033/1037, RacionalAssinado)
Σ_{k=0}^{n} xᵏ/k!, cada termo um racional exato
→ certificado de Cauchy: razão |x|/(N+2) <= 1/2 majora a cauda por
  série geométrica -- cauda <= 2×|termo(N+1)|, que encolhe pra zero
  porque o fatorial cresce mais rápido que qualquer potência fixa de x
→ lei_geradora_limite_de_sequencia_cauchy (ETAPA 1064) recebe a dupla
  (soma parcial exata empacotada como lei constante + certificado) e
  devolve a lei geradora do limite -- mesmo construtor já testado
  contra Newton de raiz quadrada
```

Nenhuma peça nova de aritmética foi inventada: `_potencia_racional` e
`_fatorial` são laços simples sobre inteiro (mesmo estilo de
`_potencia_de_dois`, já usado em `completude_leis_geradoras.py`), e cada
soma parcial usa só soma/multiplicação de `RacionalAssinado` já
provadas. `lei_geradora_constante` (ETAPA 1062) é reaproveitada direto
para empacotar cada soma parcial exata como lei degenerada, em vez de
reinventar essa peça.

Verificação sem nenhuma referência decimal externa: `eˣ · e⁻ˣ = 1` e
`e¹ · e¹ = e²` são identidades puras, conferidas com o produto de leis
geradoras já construído (ETAPA 1062) — a mesma disciplina usada em
`√4×√9` consistente com `√36`.

## Dependências permitidas

- completude leis geradoras
- lei geradora aproximação real
- operacoes leis geradoras

## Implementação

```text
nucleo/exponencial_natural_racional.py
```

## Validação

```text
testes/test_exponencial_natural_racional.py
```

## Estado

Exponencial natural para x racional construída e testada via limite de
Cauchy das somas parciais exatas, com certificado de convergência
próprio (razão geométrica da cauda). eˣ para x real arbitrário e a
prova de que eˣ>0 sempre continuam residuais do item 300. Trigonometria
em intervalos (círculo unitário simbólico) continua sem ponte de um
passo só — nenhuma infraestrutura parcial existe ainda para ela.
