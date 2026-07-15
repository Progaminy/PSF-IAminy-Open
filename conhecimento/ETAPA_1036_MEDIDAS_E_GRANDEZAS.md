# PSF-IAminy — Marcador histórico 1036: medidas e grandezas

## Construção pura

A trigonometria natural (ETAPA 1033) já cita "unidade", "medida de
comprimento", "razão" e "proporção" no seu fluxo — mas só como nome e
descrição dentro daquele documento, nunca como operação própria, testável
fora dali. Esta etapa constrói essa camada de verdade em código, para que
qualquer construção futura (geometria, física escolar, escalas) tenha uma
base real em vez de citar um passo narrativo emprestado.

```text
racionais assinados (ETAPA 1034/1035)
→ grandeza: algo que se compara e se combina com outra da mesma espécie
→ unidade: uma grandeza escolhida como referência
→ medir = contar por subtração repetida quantas unidades cabem na grandeza
→ resto menor que a unidade (a mesma forma de ETAPA 08, agora sobre grandezas)
→ proporção entre grandezas = produto cruzado exato, sem calcular razão decimal
```

`Comprimento` não inventa aritmética nova: é `RacionalAssinado` (já provado
em ETAPA 1034/1035) com duas obrigações de grandeza — comparar e somar
preservando a espécie. `medir` generaliza `ETAPA_06_EUCLIDES_POR_SUBTRACAO`
e `ETAPA_08_RESTO_E_DIVISAO_EUCLIDIANA` de números para grandezas: em vez de
"quantas vezes 3 cabe em 17", pergunta "quantas vezes esta unidade cabe
nesta grandeza" — mesma construção por subtração repetida, domínio maior.

`sao_grandezas_proporcionais` não calcula `a1/a2` e `b1/b2` como decimais
para comparar (isso escondería erro de arredondamento); confere
`a1 × b2 == b1 × a2` em racionais exatos — a mesma prova de proporção por
multiplicação cruzada já citada em ETAPA_1033, agora executável e testada.

A estrutura comum (comparar, somar, subtrair) foi extraída para
`_GrandezaEscalar`, da qual `Comprimento`, `Massa`, `Tempo`, `Area` e
`Volume` herdam — cinco espécies, um só código, sem repetir a prova cinco
vezes. `type(self)(...)` preserva a espécie do resultado: somar duas
massas devolve massa, nunca comprimento. `medir` agora rejeita medir uma
grandeza com unidade de outra espécie (`type(grandeza) is not
type(unidade)`), em vez de fingir que "5 kg cabem em 3 m" faz sentido.

Massa e tempo são espécies independentes — nenhuma se deriva de
comprimento, então entram como grandeza solta, do mesmo jeito que
comprimento. Área e volume **não** são independentes: nascem de
multiplicar comprimentos (`area_retangulo`, `volume_paralelepipedo`), não
de uma unidade inventada — a mesma disciplina de "nunca fingir" aplicada
à própria estrutura das grandezas, não só aos valores.

Isto ainda não fecha "medidas e grandezas" como assunto: conversão entre
unidades diferentes da mesma espécie (metro/centímetro, quilo/grama)
continua em aberto, e área/volume só nascem de retângulo/paralelepípedo —
área de círculo, volume de esfera etc. dependem de geometria plana e no
espaço, que ainda não foram construídas.

## Dependências permitidas

- ponte racionais reais
- euclides por subtração
- resto e divisão euclidiana
- razão
- proporção
- ordem total

## Implementação

```text
nucleo/medidas_grandezas.py
```

## Validação

```text
testes/test_medidas_grandezas.py
```

## Estado

Estrutura comum de grandeza, unidade, medição por subtração repetida e
proporção por produto cruzado construída e testada para cinco espécies:
comprimento, massa, tempo (independentes) e área, volume (derivadas por
multiplicação de comprimentos). Conversão entre unidades diferentes da
mesma espécie e área/volume de figuras além de retângulo/paralelepípedo
continuam como próximo alvo.
