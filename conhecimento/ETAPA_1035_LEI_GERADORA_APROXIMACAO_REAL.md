# PSF-IAminy — Marcador histórico 1035: lei geradora de aproximação real

## Construção pura

A ETAPA 1034 certificou intervalos racionais encaixados, mas declarou que
ainda faltava "sequência infinita ou lei geradora". Uma lista infinita não
pode ser escrita por um PSF finito; uma regra computável pode. Uma lei
geradora é uma função finita passo → intervalo, executável para qualquer
índice n, sem precisar guardar os passos anteriores.

```text
intervalos encaixados (ETAPA 1034)
→ regra computável determinística (lei geradora)
→ para cada erro racional positivo, busca finita do primeiro passo suficiente
→ módulo de convergência explícito
→ ainda faltam: equivalência entre leis, operações preservadas, ordem, prova de completude
```

Como testemunha concreta, a lei geradora de raiz quadrada por Newton usa
racionais exatos (`RacionalAssinado`, agora com soma, multiplicação e
recíproco, além da subtração e comparação já existentes). Para `x > 0` com
`x*x >= alvo`, o par `(alvo/x, x)` sempre contém `√alvo` — desigualdade das
médias. Partindo de `x0 = max(alvo, 1) >= √alvo`, Newton preserva
`x_n >= √alvo` a cada passo e decresce; por isso `alvo/x_n` cresce até
`x_n` por baixo. O intervalo `[alvo/x_n, x_n]` fica encaixado no do passo
anterior sem depender de convergência assumida — cada passo é verificado
isoladamente, e `AproximacaoReal` confere o encaixe na própria construção.

`modulo_convergencia` faz busca finita e explícita: dado um erro racional
positivo e um limite de passos, devolve o primeiro passo cuja largura já é
suficiente, ou declara falha honesta se o limite for atingido — nunca finge
sucesso.

Durante esta construção, dois auxiliares internos de normalização de
racionais (`_mdc` e a divisão exata de redução) usavam subtração/contagem
repetida — custo O(valor), não O(dígitos). Isso é invisível para frações
pequenas, mas Newton dobra a quantidade de dígitos a cada passo
(convergência quadrática), e travava a partir do quinto ou sexto passo.
Foram trocados por Euclides por resto e `divmod`, sem mudar nenhum
resultado — apenas a mesma aritmética, exigida para a lei geradora ser
executável na prática.

Isto **não é** prova de completude dos reais. É a lei geradora com módulo
de convergência explícito — o primeiro item que a ETAPA 1034 deixou como
próximo alvo. Equivalência entre leis diferentes que aproximam o mesmo
valor, operações aritméticas preservadas entre leis, ordem entre leis e a
prova de completude (propriedade do supremo) continuam pendentes.

Como esta lei geradora já é conhecimento PSF puro, consolidado, testado e
com ponte, ela pode agora ser conferida (não decidida) pelo
`MotorAuxiliarValidacao` (`validacao_externa/motor_auxiliar.py`), método
`validar_aproximacao_irracional`: recebe o intervalo já construído pelo PSF
e usa `Decimal` de alta precisão só para checar se a referência Python cai
dentro dele e medir a largura obtida. O auxiliar nunca escolhe o intervalo;
ele audita um intervalo que o PSF já provou sozinho.

## Dependências permitidas

- ponte racionais reais
- sequências finitas
- ordem total

## Implementação

```text
nucleo/reais_intervalos_naturais.py
nucleo/lei_geradora_real.py
validacao_externa/motor_auxiliar.py
```

## Validação

```text
testes/test_reais_intervalos_naturais.py
testes/test_lei_geradora_real.py
testes/test_validacao_auxiliar_lei_geradora.py
```

## Estado

Lei geradora com módulo de convergência explícito construída e testada
para o caso raiz quadrada. Completude dos reais continua como próximo
alvo, agora com um degrau a menos.
