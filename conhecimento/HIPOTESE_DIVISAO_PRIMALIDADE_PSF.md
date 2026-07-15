# Hipótese pendente — divisão por níveis e possível revelação de primalidade

## Estado

**IDEIA GUARDADA ATÉ O MOTOR ESTAR MADURO.**

Este documento não inicia uma investigação atual e não declara teorema, algoritmo oficial nem conhecimento matemático aprovado. Ele apenas preserva uma técnica própria de **Pensador Sem Fronteiras**. Hipóteses, teses, teorias, problemas pendentes e construção ou remodelação de axiomas serão trabalhados depois de o motor atingir maturidade.

## Intuição recebida

A técnica começa obrigatoriamente pela divisão por 2. O número é repartido, os restos são mantidos no mesmo nível e transportados para novas repartições. A sequência parece revelar padrões de divisibilidade. Para números grandes, esses padrões poderiam funcionar como polos de aproximação. O limite indicado provisoriamente é a raiz quadrada do número estudado.

## Exemplos iniciais preservados

### Caso 12 e a pergunta 12 : 5

- 12 : 2 → 6, 6.
- 6 : 2 → 3, 3, 3, 3.
- Quando 3 : 2 não é inteiro, aparece no relato a transformação “−1; 3−1”.
- O nível seguinte contém repetições de 2.
- O resto é transportado para 20.
- 20 : 2 → 10, 10.
- 10 : 2 → 5, 5, 5, 5.
- Nova transformação conduz a repetições de 4.
- Resultado decimal indicado: 12 : 5 = 2,4.

### Caso 9

- 9 : 2 não é inteiro.
- Registo: 4, 4 e resto 1.
- O resto é transportado para 10.
- 10 : 2 → 5, 5.
- Resultado decimal indicado: 9 : 2 = 4,5.

### Caso 7

- 7 : 2 → 3, 3 e resto 1.
- O resto é transportado para 10.
- 10 : 2 → 5, 5.
- Resultado decimal indicado: 7 : 2 = 3,5.

## Resultado pretendido dos três casos de teste

Os números 12, 9 e 7 foram apresentados para testar, com a mesma técnica, se cada número é primo. O autor **não** afirmou que 12 e 9 fossem primos.

- Em 12, a técnica encontra divisor próprio; portanto, conclui que 12 não é primo.
- Em 9, a técnica encontra o divisor próprio 3; portanto, conclui que 9 não é primo.
- Em 7, a técnica não encontra divisor próprio no percurso necessário; portanto, conclui que 7 é primo.

Esses são exemplos da intenção da técnica: procurar um divisor para falsificar a primalidade ou, não o encontrando dentro do critério completo da técnica, provar a primalidade. A formalização dos movimentos fica guardada para depois da maturidade do motor.

## O que precisa ser definido

1. O significado exato de “manter o mesmo nível”.
2. A regra exata da transformação “−1”.
3. O significado de “já temos 2”, “já temos 3” e “já temos 5”.
4. O certificado final que distingue primo, composto e inconclusivo.
5. A condição de paragem.
6. A construção interna do limite associado à raiz quadrada.
7. Como os “polos” aproximam um possível divisor.

## Plano futuro, suspenso até a maturidade do motor

Nenhum item abaixo é prioridade ou investigação ativa agora.

1. Receber e anexar a transcrição completa do PDF futuro.
2. Transformar cada movimento em regra operacional inequívoca.
3. Aplicar a técnica aos números de 2 a 30.
4. Registrar todas as sequências, sem escolher apenas casos favoráveis.
5. Comparar posteriormente com a primalidade PSF já construída.
6. Procurar o primeiro contraexemplo.
7. Medir custo e redução de busca.
8. Classificar o que a técnica realmente é: divisão, detector de fatores, crivo, representação ou novo método híbrido.

## Regra de proteção

Até existir formalização e teste, esta hipótese:

- não responde automaticamente se um número é primo;
- não substitui `PRIMO_PURO`;
- não entra em monografias como resultado provado;
- pode orientar experiências, comparações e procura de contraexemplos.
