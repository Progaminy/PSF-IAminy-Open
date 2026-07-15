# PSF-IAminy — Marcador histórico 1044: regressão linear e coeficiente de determinação

## Construção pura

A **regressão linear** busca a reta que melhor se ajusta a um conjunto
de pontos, minimizando o erro quadrático total entre a reta e os
pontos reais. O **coeficiente de determinação** (R²) mede quão bem essa
reta explica os dados: quanto mais perto de 1, mais a variação dos
pontos é explicada pela reta; perto de 0, a reta não explica quase
nada. Este ramo liga a `estatística finita` (ETAPA 961-990) —
reaproveita a mesma ideia de erro quadrático de `erro_modelo` para
achar a reta que o minimiza, não só medi-lo — e a `otimização de
modelos finitos` (prova por comparação com vizinhos).

"Correlação/regressão" existia neste projeto só como texto de resposta
legada (`nucleo/conceitos_avancados_puros.py`): explicação e exemplo
prontos, sem prova PSF, código ou teste.

```text
estatística finita dados (ETAPA 961-990)
→ inclinação = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)², intercepto = ȳ − inclinação·x̄
→ conferência: nenhuma inclinação vizinha (±0.01) produz erro total menor
  (mesma prova por comparação com vizinhos de otimização finita)
→ coeficiente de determinação r² = 1 − erro residual / variação total de y
```

O coeficiente de correlação `r` clássico normaliza por um desvio-padrão —
uma raiz quadrada, geralmente irracional. Em vez de aproximar isso, esta
etapa usa o coeficiente de determinação `r²` (mede a mesma ideia: quanto
da variação de y a reta explica), que fica exato em racionais. A reta em
si (inclinação e intercepto) nunca precisou de raiz quadrada — só a
normalização de `r` clássico precisaria, e por isso não é essa a forma
usada aqui.

A reta não é aceita "porque é a fórmula de mínimos quadrados conhecida":
depois de calculada, o erro total é comparado contra duas retas vizinhas
(inclinação ligeiramente maior e menor); se alguma delas produzir erro
menor, a construção levanta erro em vez de aceitar um mínimo que não é
mínimo. Testado com dados perfeitamente lineares (r²=1) e dados com
ruído (r²=27/28).

## Exemplo

- Pontos perfeitamente alinhados numa reta: R²=1, a reta explica 100% da variação.
- Pontos com ruído real: R²=27/28, quase todo explicado mas não perfeito -- fração exata, não decimal arredondado.

## Dependências permitidas

- estatística finita dados
- otimização modelos finitos fechamento
- ponte racionais reais

## Implementação

```text
nucleo/correlacao_regressao.py
```

## Validação

```text
testes/test_correlacao_regressao.py
```

## Estado

Regressão linear (mínimos quadrados) e coeficiente de determinação
construídos e testados, exatos, com reta conferida contra vizinhos.
Regressão não linear e correlação `r` clássica (que exige raiz quadrada)
continuam como próximo alvo.
