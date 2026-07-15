# PSF-IAminy — Etapas 301 a 340: Categorias finitas

## Posição no fluxo natural

Depois de métodos finitos, relações, funções, identidade e composição, nasce uma categoria finita: uma estrutura onde objetos e morfismos são dados explicitamente, e os axiomas são verificados por tabela finita.

Nenhum teorema externo é usado como atalho. Uma categoria só é aceita quando:

```text
objetos finitos
↓
morfismos finitos
↓
origem e alvo
↓
identidade por objeto
↓
composição parcial explícita
↓
leis de identidade e associatividade verificadas por enumeração
```

## Etapas registradas

| Etapa | Conceito |
|---|---|
| 301 | Objeto de categoria finita |
| 302 | Morfismo finito |
| 303 | Origem de morfismo |
| 304 | Alvo de morfismo |
| 305 | Morfismos componíveis |
| 306 | Composição parcial |
| 307 | Identidade categórica |
| 308 | Lei da identidade à esquerda |
| 309 | Lei da identidade à direita |
| 310 | Associatividade categórica |
| 311 | Categoria finita |
| 312 | Hom finito |
| 313 | Endomorfismo |
| 314 | Isomorfismo categórico |
| 315 | Objetos isomorfos |
| 316 | Automorfismo |
| 317 | Subcategoria finita |
| 318 | Categoria oposta |
| 319 | Diagrama finito |
| 320 | Cone finito inicial |
| 321 | Cocone finito inicial |
| 322 | Produto categórico finito por propriedade |
| 323 | Coproduto categórico finito por propriedade |
| 324 | Objeto terminal |
| 325 | Objeto inicial |
| 326 | Categoria discreta finita |
| 327 | Pré-ordem como categoria |
| 328 | Monoide como categoria de um objeto |
| 329 | Functor finito |
| 330 | Functor identidade |
| 331 | Composição de functores |
| 332 | Preservação de identidade por functor |
| 333 | Preservação de composição por functor |
| 334 | Isomorfismo de categorias finitas inicial |
| 335 | Transformação natural finita |
| 336 | Naturalidade por quadrado comutativo |
| 337 | Categoria de functores finita inicial |
| 338 | Equivalência finita inicial |
| 339 | Auditoria categórica finita |
| 340 | Fechamento de categorias finitas |

## Forma operacional no projeto

Implementado em `nucleo/categorias_finitas.py` e validado em `testes/test_categorias_finitas_301_340.py`.

## Limite honesto

Este bloco não afirma resultados gerais de teoria das categorias. Ele constrói categorias pequenas e verifica seus axiomas por enumeração finita. Produtos, coprodutos e equivalências aparecem como conceitos registrados do bloco, mas versões universais completas exigem etapas futuras se forem usadas como método interno.
