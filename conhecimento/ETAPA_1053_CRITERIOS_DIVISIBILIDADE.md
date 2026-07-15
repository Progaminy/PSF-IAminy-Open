# PSF-IAminy — Marcador histórico 1053: critérios de divisibilidade

## Construção pura

Os critérios de divisibilidade (olhar só o último dígito, ou a soma dos
dígitos) existiam neste projeto apenas implícitos na base de
`divisibilidade pura` (ETAPA 3). Este ramo liga `contas armadas` (ETAPA
1037, `digitos()`) a essa base.

```text
divisibilidade pura (ETAPA 3) + contas armadas (ETAPA 1037, digitos())
→ por 2: último dígito par
→ por 5: último dígito 0 ou 5
→ por 10: último dígito 0
→ por 3: soma dos dígitos divisível por 3
→ por 9: soma dos dígitos divisível por 9
→ cada critério conferido contra o resto real, dígito a dígito
```

Nenhum critério é aceito como regra escolar decorada: cada função calcula
o resto real de dividir o número inteiro pelo divisor e confere que bate
com o que o critério previu, levantando erro se divergirem.

A conferência não chama a divisão sobre o número inteiro de uma vez: para
um divisor pequeno, isso reproduziria o mesmo custo escondido já corrigido
em ETAPA 1037 (`dividir_com_resto` passa por `subtrair` e `predecessor`,
que busca por sucessão a partir de zero). O resto real é calculado dígito
a dígito, como em `divisao_armada` — trazendo um dígito por vez, sempre
sobre valores pequenos. Testado que um número de 9 dígitos continua
rápido.

## Dependências permitidas

- divisibilidade pura
- contas armadas

## Implementação

```text
nucleo/criterios_divisibilidade.py
```

## Validação

```text
testes/test_criterios_divisibilidade.py
```

## Estado

Critérios de divisibilidade por 2, 3, 5, 9 e 10 construídos e testados,
cada um conferido contra o resto real calculado dígito a dígito. Critério
por 6, 11 e outros continuam como próximo alvo.
