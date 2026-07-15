# PSF-IAminy — Etapas 361 a 380: Teoria de modelos finita revisitada + prova de primeira ordem como objeto finito

## Posição no fluxo natural

Depois da lógica de predicados finita (etapas 341-360, com estrutura, termo,
fórmula e satisfação ⊨ já construídos), o próximo passo que nasce sem violar
a lei das fórmulas tem duas partes: comparar estruturas entre si (a
"teoria de modelos" clássica, revisitada em versão finita) e formalizar
prova como objeto finito verificável (sequente, regra de inferência,
derivação).

```text
lógica de predicados finita (341-360)
↓
subestrutura finita
↓
subestrutura gerada por um conjunto
↓
homomorfismo / isomorfismo / mergulho de estruturas
↓
reduct / expansão de assinatura
↓
equivalência elementar sobre uma família finita de sentenças
↓
isomorfismo elementar finito
↓
assinatura finita
↓
sequente finito
↓
regra de inferência como transição finita (∧ ∨ → ∀ ∃)
↓
derivação como sequência finita de sequentes
```

Nenhuma regra de inferência aqui **gera** uma prova por busca ou por
mágica — cada `PASSO_VALIDO` só **verifica** se um passo já proposto é uma
instância legítima da regra correspondente, dados os sequentes anteriores
da mesma derivação. O projeto constrói verificadores de prova, não um
provador automático — o mesmo espírito de `VERIFICAR_INDUCAO`
(`calculo_discreto.py`) e de `PARA_TODO`/`EXISTE` limitados
(`predicados.py`).

## Dependências permitidas

- `logica_predicados_finita.py` inteiro (etapas 341-360): `ESTRUTURA_FINITA`,
  `SATISFAZ_FINITA`, `ATOMICA`, conectivos, quantificadores,
  `SUBSTITUIR_LIVRE_FINITA`, `VARIAVEIS_LIVRES_FINITA`;
- `metodos_finitos.CONSEQUENCIA_FINITA` (etapa 275) usado só como ORÁCULO
  de validação externa nos testes (não como método interno do módulo).

## Dependências proibidas

- nenhum provador automático de teoremas importado;
- nenhuma busca de derivação por enumeração (isso é o próximo bloco,
  384-386 — aqui só verificamos passos dados, não procuramos provas);
- `DIV`, `MOD`, `MDC`, `MMC` nativos, módulos antigos `primos`/`divisores`.

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 361 | Subestrutura finita |
| 362 | Subestrutura gerada por um conjunto |
| 363 | Homomorfismo de estruturas |
| 364 | Isomorfismo de estruturas |
| 365 | Mergulho (embedding) de estruturas |
| 366 | Redução de assinatura (reduct) |
| 367 | Expansão de assinatura |
| 368 | Equivalência elementar sobre uma teoria finita dada |
| 369 | Isomorfismo elementar finito |
| 370 | Fechamento da teoria de modelos finita revisitada |
| 371 | Assinatura finita |
| 372 | Sequente finito |
| 373 | Regra de inferência como transição finita |
| 374 | ∧-introdução / ∧-eliminação |
| 375 | ∨-introdução / ∨-eliminação (por casos) |
| 376 | →-introdução / modus ponens |
| 377 | ∀-introdução (generalização, com condição lateral) / ∀-eliminação |
| 378 | ∃-introdução (por testemunha) / ∃-eliminação (com condição lateral) |
| 379 | Derivação como sequência finita de sequentes |
| 380 | Fechamento: prova de primeira ordem como objeto finito |

## Forma operacional no projeto

Implementado em `nucleo/teoria_modelos_prova_finita.py` e validado em
`testes/test_teoria_modelos_prova_finita.py`.

## Validação contra factos independentes

1. **Z₃ e sua versão relabeled `{a,b,c}` são isomorfas** e satisfazem as
   mesmas sentenças de grupo (associatividade) — facto de que isomorfismo
   implica equivalência elementar, testado sobre a família de sentenças
   dada.
2. **1 gera Z₃ inteiro por adição sucessiva** (1, 1+1=2, 1+1+1=0) — facto
   padrão de grupos cíclicos (todo elemento não-nulo de Z_p, p primo,
   gera o grupo). Verificado por `SUBESTRUTURA_GERADA_FINITA`.
3. **Solidez cruzada da regra modus ponens**: a derivação sintática de `r`
   a partir de `{p, p→q, q→r}` (duas aplicações de modus ponens) é
   verificada válida por `DERIVACAO_VALIDA`, e o mesmo resultado — `r` é
   consequência semântica das três premissas — é confirmado
   independentemente pelo oráculo já validado da lógica proposicional,
   `metodos_finitos.CONSEQUENCIA_FINITA` (etapa 275). As duas rotas
   concordam, como a solidez da regra exige.
4. Uma derivação com um passo de modus ponens deliberadamente errado
   (premissas trocadas) é corretamente rejeitada por `DERIVACAO_VALIDA`.

## Limite honesto

- `EQUIVALENCIA_ELEMENTAR_FINITA` e `ISOMORFISMO_ELEMENTAR_FINITO`
  comparam satisfação sobre uma família **finita e explícita** de
  sentenças fornecida pelo chamador — não sobre toda sentença da
  linguagem (coleção infinita). Mesma fronteira honesta de
  `logica_predicados_finita.VALIDA_SOBRE_ESTRUTURAS_FINITA`.
- As regras de inferência aqui **verificam** passos dados; não há busca
  automática de derivação. Isso fica para a etapa 386
  (`BUSCA_DERIVACAO_FINITA`, com profundidade limitada).
- `∨-eliminação` e `∃-eliminação` modelam a hipótese temporária "Γ,φ ⊢ χ"
  como literalmente `premissas = Γ ∪ {φ}` — não há mecanismo de
  "descarte" (discharge) formal de caixas de dedução natural. É
  funcionalmente equivalente para os fins deste projeto, mas não é a
  contabilidade de caixas de um sistema de dedução natural de livro-texto
  completo.

## Próximo passo natural

```text
verificador de derivação (auditoria de cada passo já coberta por PASSO_VALIDO)
↓
correção (soundness): toda regra preserva satisfação numa amostra de estruturas
↓
busca de derivação por enumeração finita (profundidade limitada)
↓
completude relativa ao fragmento proposicional/Herbrand limitado
↓
fechamento do arco lógico 341-400
```
