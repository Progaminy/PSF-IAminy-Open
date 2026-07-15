# PSF-IAminy — Marcador histórico 1037: contas armadas

## Construção pura

A aritmética escolar nativa (implementação da Etapa 31) já constrói soma e
subtração por sucessão e retirada repetida — mas devolve só o número final.
A conta armada é a forma escolar de mostrar o mesmo resultado coluna por
coluna, com "vai um" e "empresta um" visíveis. Esta etapa constrói essa
camada sem introduzir uma segunda fonte de verdade: cada resultado armado é
conferido contra a soma/subtração já provada, e diverge com erro se não
bater — a conta armada mostra o procedimento; não decide o valor sozinha.

```text
sucessor/predecessor, soma e subtração por retirada repetida (Etapa 31)
→ dividir_com_resto (repartição por dez sem // nem %)
→ dígitos de um número (esquerda para a direita)
→ coluna a coluna, da unidade para a esquerda: somar dígitos + vai-um anterior
→ vai-um = quociente por dez da coluna; dígito do resultado = resto
→ (na subtração) empresta dez da coluna seguinte quando o dígito de cima é menor
→ conferência final contra somar(a, b) / subtrair(a, b) já provados
```

Um exemplo concreto mostra o "vai um" em cadeia: `999 + 1`, cada coluna soma
9, o vai-um de uma alimenta a próxima, e o resultado sai `1000` com uma
coluna nova. O espelho na subtração é `1000 - 1`: o empréstimo atravessa
três colunas de zero antes de chegar ao dígito que pode pagar, resultando
em `999`.

Multiplicação armada gera uma linha parcial por dígito do multiplicador
(`a` × esse dígito, com vai-um), desloca a linha para a casa certa
preenchendo zeros à direita, e soma as linhas deslocadas reaproveitando
`soma_armada` — não uma segunda forma de somar. Divisão armada traz um
dígito do dividendo de cada vez (`resto_parcial × 10 + dígito`) e usa
`dividir_com_resto` para achar o dígito do quociente e o novo resto —
sempre um dígito entre 0 e 9, porque o resto parcial já é menor que o
divisor antes de trazer o próximo dígito (invariante mantida a cada
passo). As duas são conferidas contra `multiplicar`/`somar` já provados.

Ao decompor números maiores em dígitos, `dividir_com_resto` (que passa por
`subtrair` e `predecessor`, um buscador por sucessão a partir de zero,
Etapa 31) revelou o mesmo tipo de custo escondido já corrigido em ETAPA
1035: decompor um número como 8910 assim passava de um minuto. `digitos`
passou a ler os algarismos do numeral escrito diretamente — isso não é a
conta armada em si, é o mesmo passo que uma criança já faz olhando o
número antes de armar a conta. O vai-um, o empréstimo, o produto parcial e
o dígito trazido continuam por `dividir_com_resto` sobre valores de uma
coluna (nunca sobre o número inteiro), que é onde a construção realmente
acontece.

## Dependências permitidas

- sucessor
- subtração natural
- adição
- multiplicação
- resto e divisão euclidiana

## Implementação

```text
nucleo/aritmetica_escolar_nativa.py
nucleo/contas_armadas.py
```

## Validação

```text
testes/test_aritmetica_escolar_nativa.py
testes/test_contas_armadas.py
```

## Estado

Soma, subtração, multiplicação e divisão armadas construídas e testadas,
cada uma conferida contra a aritmética escolar já provada. As quatro
operações escolares básicas em forma de papel estão fechadas nesta etapa.
