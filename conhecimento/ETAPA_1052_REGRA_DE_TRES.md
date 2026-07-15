# PSF-IAminy — Marcador histórico 1052: regra de três simples

## Construção pura

"Regra de três simples" já era, sem esse nome, `sao_grandezas_proporcionais`
(ETAPA 1036): `a1/b1 = a2/x` é exatamente a mesma multiplicação cruzada
`a1·x = a2·b1` já provada ali. Este ramo dá a forma de apresentação
pedagógica — resolver para o valor que falta — e acrescenta o caso
inverso.

```text
proporção (ETAPA 1036, sao_grandezas_proporcionais)
→ direta: a1/b1 = a2/x → x = a2·b1/a1, conferido por a1·x == a2·b1
→ inversa: a1·b1 = a2·x → x = a1·b1/a2, conferido reconstruindo o produto
```

Exemplo direto: 2 kg custam 10 reais, quanto custam 5 kg? `x=25`.
Exemplo inverso: 3 trabalhadores constroem um muro em 12 dias, quantos
dias com 4 trabalhadores? `x=9` — aumentar trabalhadores diminui dias na
mesma razão, por isso o produto (não a razão) se mantém constante.

## Dependências permitidas

- proporção
- ponte racionais reais

## Implementação

```text
nucleo/regra_de_tres.py
```

## Validação

```text
testes/test_regra_de_tres.py
```

## Estado

Regra de três direta e inversa construídas e testadas com os dois
exemplos clássicos, cada uma conferida pela sua prova de proporção.
