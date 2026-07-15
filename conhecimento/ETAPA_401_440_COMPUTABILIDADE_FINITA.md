# PSF-IAminy — Etapas 401 a 440: Computabilidade finita (máquina de fita limitada, funções computáveis, decidibilidade)

Uma **máquina de fita limitada** é um modelo simples de computação: lê e
escreve símbolos numa fita finita, seguindo um conjunto fixo de regras,
até parar ou não. Uma função é **computável** quando existe uma máquina
que sempre para e devolve o resultado certo; um problema é **decidível**
quando existe uma máquina que sempre para respondendo sim ou não. Este
bloco constrói esses três conceitos em versão finita (fita de tamanho
limitado), sem citar o resultado geral (que exige fita infinita) como se
já estivesse provado aqui.

## Exemplo

- Máquina sucessora unária: para cada `n` de 0 a 5, a máquina computa o sucessor sobre uma fita de `n` símbolos `1` e o resultado bate com `n+1` calculado nativamente -- confirmado, não assumido.
- Entrada maior que o tamanho declarado da fita (ex.: 20 símbolos numa fita de 8) é rejeitada por exceção, em vez de estourar silenciosamente.

## Posição no fluxo natural

O arco lógico 341-400 fechou verificação, solidez e busca de derivação. O
próximo passo que nasce sem violar a lei das fórmulas junta duas linhas já
construídas — autômatos finitos (`DFA_FINITO`, etapas 136-300) e lógica
(341-400) — perguntando: o que significa "computar" quando a memória
também é finita e explícita, não apenas o alfabeto de entrada? Isto exige
um modelo novo (a fita, que o DFA não tem) e devolve, de graça, uma
observação honesta que o caso geral (Turing/fita infinita) não permite: com
memória GENUINAMENTE finita, o problema da parada é DECIDÍVEL.

```text
autômato finito determinístico — só lê (136-300)
↓
máquina de fita limitada — lê E escreve, fita de tamanho fixo N
↓
espaço de configurações é finito (estados × conteúdos × posições)
↓
decidibilidade da parada para ESTE modelo (pelo princípio da casa dos pombos)
↓
função computável finita (parcial, calculada por uma máquina)
↓
esquemas de recursão primitiva finita (zero, sucessor, projeção, composição, recursão limitada)
↓
decidibilidade e redução de problemas de decisão finitos
↓
máquina universal finita (um interpretador, não uma UTM clássica — limite declarado)
```

## Dependências permitidas

- `nucleo/metodos_finitos.py` (etapas 136-300): `DFA_FINITO`,
  `TRANSICAO_ESTENDIDA_DFA_FINITA`, `ACEITA_DFA_FINITO`, `ALFABETO_FINITO`,
  `PALAVRA_FINITA` — para comparar o modelo novo com o já aceito.
- primitivas fundacionais `V`, `F` (booleano de Church, para os predicados
  devolvidos) — etapa implícita 1, sempre disponível.

## Dependências proibidas

- `DIV`, `MOD`, `MDC`, `MMC` nativos, módulos antigos `primos`/`divisores`;
- nenhuma biblioteca de simulação de autômatos ou de máquina de Turing
  importada;
- nenhuma alegação sobre o problema da parada CLÁSSICO (fita infinita,
  auto-referência via codificação no mesmo alfabeto) — ver "Limite
  honesto".

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 401 | Fita finita explícita e configuração (estado, fita, posição da cabeça) |
| 402 | Máquina de fita limitada como sêxtupla explícita (`MAQUINA_FITA_LIMITADA_FINITA`) |
| 403 | Configuração inicial a partir de uma entrada (rejeita se a entrada não cabe na fita) |
| 404 | Passo de transição (ler, escrever, mover, com posição sempre grampeada a [0, N-1]) |
| 405 | Execução limitada a um número de passos (aceita / rejeita / não parou no limite) |
| 406 | Espaço de configurações é finito — contagem explícita (estados × símbolos^N × N) |
| 407 | Detecção de configuração repetida dentro do espaço finito (princípio da casa dos pombos) |
| 408 | Decidibilidade da parada PARA ESTE MODELO — decisão que sempre termina |
| 409 | Aceitação por máquina de fita limitada e linguagem aceita |
| 410 | Fechamento: modelo de máquina de fita limitada (401-410) |
| 411 | Função computável finita: parcial, calculada por alguma máquina dentro de um limite |
| 412 | Esquema: função zero (constante) |
| 413 | Esquema: função sucessor finita |
| 414 | Esquema: projeção finita |
| 415 | Esquema: composição de funções computáveis finitas |
| 416 | Esquema: recursão primitiva limitada finita (bounded, sobre um intervalo explícito) |
| 417 | Toda função pelos esquemas 412-416 é total no domínio declarado, por construção |
| 418 | Exemplo computado por máquina concreta: sucessor unário, validado contra oráculo nativo |
| 419 | Contraexemplo honesto: uma máquina que não pára para uma entrada específica do domínio — função parcial de fato |
| 420 | Fechamento: funções computáveis finitas (411-420) |
| 421 | Problema de decisão finito como predicado sobre domínio explícito |
| 422 | Decidibilidade de linguagem finita por DFA (reaproveita 136-300, não reinventa) |
| 423 | Decidibilidade de linguagem finita por máquina de fita limitada |
| 424 | Redução finita de um problema de decisão a outro (mapeamento computável que preserva resposta) |
| 425 | Se B é decidível e A reduz a B, então A é decidível (demonstrado construtivamente) |
| 426 | Limite honesto: todo problema sobre domínio FINITO é decidível por enumeração — a indecidibilidade clássica exige domínio infinito, fora do escopo |
| 427 | Fechamento de linguagem decidível sob complemento |
| 428 | Fechamento de linguagens decidíveis sob união e interseção |
| 429 | Toda linguagem aceita por um `DFA_FINITO` é aceita por alguma máquina de fita limitada equivalente |
| 430 | Fechamento: decidibilidade e redução finita (421-430) |
| 431 | Código de uma máquina como estrutura de dados finita explícita (não uma palavra codificada) |
| 432 | Máquina universal finita: um interpretador único que roda qualquer máquina passada como dado |
| 433 | Simulação validada: o interpretador concorda com a execução direta sobre um catálogo de máquinas |
| 434 | Limite honesto: isto não é uma UTM clássica — sem auto-referência, o argumento diagonal de indecidibilidade não se aplica aqui |
| 435 | Contagem finita de máquinas distintas para (estados, alfabeto, tamanho de fita) pequenos |
| 436 | Classificação por enumeração exaustiva de um catálogo pequeno de máquinas (para / não para) |
| 437 | Toda linguagem regular finita (DFA) é decidida por alguma máquina de fita limitada — tradução explícita |
| 438 | Diferença conceitual demonstrada: a fita permite memória (ex.: palíndromo), o DFA só lê |
| 439 | Síntese do que persiste do arco de computabilidade finita 401-440 |
| 440 | Fechamento do arco de computabilidade finita 401-440 |

## Forma operacional no projeto

Implementado em `nucleo/computabilidade_finita.py` e validado em
`testes/test_computabilidade_finita.py`.

## Validação contra factos independentes

1. **Princípio da casa dos pombos aplicado ao espaço de configurações**:
   se uma máquina de fita limitada não parou depois de mais passos do que
   configurações possíveis existem, ela REPETIU uma configuração —
   portanto vai repetir para sempre (facto matemático elementar, não
   específico deste projeto). `DETECCAO_CICLO_E_PARADA_FINITA` usa
   exatamente esse limite e é testado contra uma máquina construída para
   entrar em loop (posição grampeada na borda, mesma configuração se
   repete imediatamente) e uma que claramente para.
2. **Sucessor unário computado por máquina concreta**, validado contra
   `len(entrada) + 1` nativo do Python — mesmo padrão de oráculo
   independente já usado para `SOMA`/`MULT` em `aritmetica.py`.
3. **Verificador de palíndromo por máquina com memória** (etapa 438),
   validado contra `tuple(reversed(entrada)) == entrada` nativo — mostra
   concretamente por que a fita (memória) é estritamente mais poderosa
   que o DFA para esta tarefa dentro do domínio testado.

## Limite honesto

- "Decidibilidade da parada" aqui vale só para o MODELO de fita limitada
  deste projeto — memória genuinamente finita e fixa antes de a máquina
  rodar. O problema da parada CLÁSSICO (fita infinita, máquina podendo
  processar sua própria descrição no MESMO alfabeto da entrada, permitindo
  o argumento diagonal de Turing/Cantor) continua indecidível e este
  projeto não afirma o contrário — só demonstra que o argumento clássico
  depende crucialmente de recursos (fita infinita, auto-referência) que
  este modelo, por desenho, não tem.
- A "máquina universal finita" (431-435) é um interpretador que recebe a
  máquina simulada como uma estrutura de dados SEPARADA da fita de
  entrada — não uma codificação no mesmo alfabeto que permitiria a máquina
  processar sua própria descrição. Isto é uma escolha de escopo deliberada,
  não uma lacuna escondida: constrói a ideia central (um único
  interpretador roda qualquer máquina dada como dado) sem abrir a
  auto-referência que exigiria tratar indecidibilidade genuína — adiado.
- `RECURSAO_PRIMITIVA_LIMITADA_FINITA` é limitada a um intervalo explícito
  `[0, limite]` — não é recursão primitiva geral sobre todos os naturais.

## Próximo passo natural

```text
gramática formal finita (regular, livre de contexto) e derivação
↓
autômato de pilha finito
↓
equivalência gramática-autômato no fragmento finito/regular
↓
hierarquia de Chomsky revisitada em versão finita
```
