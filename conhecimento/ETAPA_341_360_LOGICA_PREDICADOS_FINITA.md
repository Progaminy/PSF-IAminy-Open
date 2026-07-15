# PSF-IAminy — Etapas 341 a 360: Lógica de predicados finita

## Posição no fluxo natural

Depois da lógica proposicional finita (etapas 261-300, dentro de
`nucleo/metodos_finitos.py`) e das categorias finitas (etapas 301-340,
`nucleo/categorias_finitas.py`), o próximo conceito que nasce sem violar a
lei das fórmulas é a lógica de predicados (primeira ordem) sobre um
domínio finito explícito.

A etapa 300 fechou o bloco "métodos finitos" com valorações e tabela
verdade para variáveis PROPOSICIONAIS (átomos sem estrutura interna). Este
bloco dá um passo que a lógica proposicional deliberadamente não dava:
fórmulas cujos átomos são predicados aplicados a termos, com
quantificadores que variam sobre um domínio.

```text
lógica proposicional finita (261-300)
↓
domínio finito de interpretação
↓
estrutura finita (domínio + interpretação de predicados/funções)
↓
termo de primeira ordem
↓
fórmula atômica sobre termos
↓
conectivos reaproveitados (¬ ∧ ∨ →)
↓
variável livre / variável ligada
↓
quantificador universal e existencial como SINTAXE
↓
substituição de termo por variável
↓
atribuição de variáveis
↓
satisfação (⊨) por recursão estrutural + varredura finita do domínio
↓
modelo finito de uma teoria
↓
validade sobre amostra finita de estruturas
```

Nenhum teorema externo é usado como atalho. Os conectivos ¬,∧,∨,→ não são
reinventados: são os mesmos construtores `PROP_NAO`, `PROP_E`, `PROP_OU`,
`PROP_IMPLICA` de `nucleo/metodos_finitos.py` (etapas 262-265),
reaproveitados aqui aplicados sobre fórmulas atômicas de predicados em vez
de variáveis proposicionais — o mesmo tipo de reaproveitamento legítimo já
registado em `ETAPA_10_PRIMALIDADE_PURA.md` sobre `RESTO_PURO`.

O quantificador limitado de `predicados.py` (`PARA_TODO`/`EXISTE`,
das etapas implícitas iniciais) já mostrava que ∀/∃ só são decidíveis por
busca quando limitados a um intervalo finito. Este bloco formaliza essa
mesma ideia como sintaxe explícita (fórmula é um dado, não uma chamada de
função Python) e acrescenta a camada que faltava: termos, estruturas
arbitrárias (não só `[0, limite]` de inteiros) e a relação de satisfação.

## Dependências permitidas

- `metodos_finitos.PROP_NAO/PROP_E/PROP_OU/PROP_IMPLICA` (etapas 262-265);
- o precedente operacional de `predicados.PARA_TODO/EXISTE` (quantificador
  limitado, das etapas implícitas iniciais);
- tuplas e dicionários finitos, no mesmo estilo operacional já usado desde
  a etapa 136 (`metodos_finitos.py`) e 301 (`categorias_finitas.py`).

## Dependências proibidas

- nenhuma biblioteca de lógica, SAT/SMT ou prova automática externa;
- nenhuma quantificação sobre domínio infinito (ℕ, ℤ, ℝ) — só domínio
  finito explícito, dado pelo chamador;
- `DIV`, `MOD`, `MDC`, `MMC` nativos de `aritmetica.py`;
- os módulos antigos `primos` e `divisores`;
- tratar "validade sobre uma amostra de estruturas" como validade lógica
  geral (ver "Limite honesto" abaixo).

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 341 | Domínio finito de interpretação |
| 342 | Estrutura finita (domínio + interpretação) |
| 343 | Símbolo de predicado n-ário e sua interpretação |
| 344 | Símbolo de função n-ária e sua interpretação |
| 345 | Termo de primeira ordem |
| 346 | Avaliação de termo numa estrutura sob atribuição |
| 347 | Fórmula atômica |
| 348 | Conectivos sobre fórmulas de predicados (reaproveitados) |
| 349 | Variável livre |
| 350 | Variável ligada |
| 351 | Quantificador universal como sintaxe |
| 352 | Quantificador existencial como sintaxe |
| 353 | Substituição de termo por variável |
| 354 | Atribuição de variáveis |
| 355 | Satisfação de fórmula atômica (base da ⊨) |
| 356 | Satisfação de conectivos por indução na fórmula |
| 357 | Satisfação do quantificador universal por varredura finita |
| 358 | Satisfação do quantificador existencial por varredura finita |
| 359 | Modelo finito de uma teoria |
| 360 | Validade sobre amostra finita de estruturas + fechamento do bloco |

## Forma operacional no projeto

Implementado em `nucleo/logica_predicados_finita.py` e validado em
`testes/test_logica_predicados_finita.py`.

## Validação contra factos independentes (regra de `VALIDACAO.md`)

Este bloco não é validado só contra valores auto-calculados. Dois factos
publicados, verificáveis em qualquer livro-texto de lógica ou álgebra,
foram usados como oráculo:

1. **∀x∃y R(x,y) não implica ∃y∀x R(x,y)** — facto padrão de lógica de
   primeira ordem (ex.: Enderton, *A Mathematical Introduction to Logic*).
   Testado sobre o sucessor cíclico em `{0,1,2}`: `∀x∃y suc(x,y)` é
   verdadeiro (todo elemento tem sucessor), `∃y∀x suc(x,y)` é falso
   (nenhum elemento é sucessor de todos) — a ordem dos quantificadores
   muda o valor de verdade, exatamente como a teoria prevê.
2. **Z₃ sob adição é um grupo cíclico de ordem 3** — facto padrão de
   álgebra (grupo cíclico gerado por um elemento de ordem 3). Os três
   axiomas de grupo (associatividade, elemento neutro, existência de
   inverso) foram escritos como sentenças de primeira ordem e verificados
   satisfeitos pela tabela de adição módulo 3, dada por extensão.

## Limite honesto

- `SUBSTITUIR_LIVRE_FINITA` não faz alpha-conversão: não renomeia
  variáveis ligadas para evitar captura. É seguro quando as variáveis
  ligadas da fórmula e as variáveis do termo substituído não colidem —
  caso contrário, o resultado não é a substituição lógica padrão de
  livro-texto. Ver docstring da função.
- `VALIDA_SOBRE_ESTRUTURAS_FINITA` verifica validade sobre uma AMOSTRA
  finita e explícita de estruturas fornecida pelo chamador — não é
  validade lógica geral (verdadeiro em toda estrutura possível, de
  qualquer domínio, para uma assinatura dada). Essa noção quantifica
  sobre uma coleção infinita de estruturas e não é decidível por
  enumeração. Mesma fronteira honesta que `predicados.PARA_TODO/EXISTE`
  (limitado a `[0, limite]`) e `VERIFICAR_INDUCAO`
  (`calculo_discreto.py`, verificador — não provador) já respeitam.
- `EH_MODELO_FINITO`/`VALIDA_SOBRE_ESTRUTURAS_FINITA` só aceitam
  sentenças (fórmulas sem variável livre) — a noção clássica de "modelo de
  uma teoria" em teoria de modelos é definida para sentenças, não para
  fórmulas abertas.

## Próximo passo natural

```text
teoria de modelos finita revisitada (isomorfismo elementar, subestrutura)
↓
prova de primeira ordem como objeto finito (sequente/derivação)
↓
correção e completude relativas a um sistema de prova finito
```
