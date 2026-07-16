# Validação externa

Ferramentas externas aparecem aqui somente como comparadores. Elas não são
importadas pelos motores de conhecimento nem materializam verdade PSF.

## Protocolo

O comparador deve guardar entrada equivalente, versão da ferramenta externa,
resultado dos dois lados, critério de concordância, divergências e limites da
amostra. O script atual usa expressões constantes versionadas; nenhuma entrada
do utilizador chega ao avaliador de expressões do SymPy.

## Comparação matemática com SymPy

```bash
python3 avaliacoes/comparar_sympy.py
```

Medição de 17 de julho de 2026:

```text
SymPy 1.14.0
7 casos
7 concordâncias
0 divergências
estado: CONCORDANCIA_TOTAL_NA_AMOSTRA
```

Casos exatos: precedência, parênteses, `12/5`, `1/3` e `2/3`. Para `12/0` e
`0/0`, o critério confirma que nenhum lado produz número finito comum. O PSF
declara a operação não definida por construção; SymPy representa os casos como
`zoo` e `nan`, respetivamente.

Essa diferença de representação continua visível. “Concordância” nesses dois
casos significa apenas concordância sobre ausência de resultado finito, não
equivalência semântica completa entre os estados.

## Divergências encontradas

Nenhuma nos sete casos desta primeira amostra. Isso não autoriza afirmar
equivalência geral com SymPy. A amostra é pequena, escolhida a partir das
capacidades já públicas e não cobre números grandes, expressões inválidas,
raízes, polinómios, trigonometria nem outros módulos.

## Validação linguística externa

Ainda não executada. A avaliação interna em `docs/AVALIACAO_QUALIDADE.md`
encontrou falsos positivos reais, mas não há nesta sessão uma ferramenta
linguística externa selecionada, versionada e metodologicamente comparável.
Esse estado permanece pendente em vez de receber comparação improvisada.

## Próximos passos

1. ampliar casos matemáticos por capacidade e caso extremo;
2. gerar entradas independentemente do código PSF;
3. selecionar referência linguística adequada às variedades avaliadas;
4. guardar resultados estruturados como artefacto de CI;
5. transformar toda divergência corrigida em teste de regressão.

