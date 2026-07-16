# Limites operacionais

`python3 avaliacoes/avaliar_limites.py` executa cada cenário num subprocesso
com teto de dez segundos. Timeout é resultado registrado, não teste apagado.

Medição local de 17 de julho de 2026, Python 3.14.4:

| Cenário | Resultado | Tempo do processo |
| --- | --- | ---: |
| `20*20` | `400` | 0,215 s |
| `99*99` | timeout | 10 s |
| `999*999` | timeout | 10 s |
| `999999999*999999999` | timeout | 10 s |
| soma de 20 termos `1` | `20` | 0,192 s |
| soma de 100 termos `1` | `100` | 0,249 s |
| texto de 500 palavras conhecidas | 0 sugestões | 0,357 s |
| 100 pedidos HTTP sequenciais à página inicial | todos 200 | 0,344 s |
| anexo `.pdf` não suportado | rejeitado com `ValueError` explícito | 0,112 s |

Os tempos incluem início do subprocesso e variam com a máquina.

## Achado matemático

Expressão longa não foi o limite nesta amostra: cem parcelas terminaram em
menos de um segundo. A magnitude intermediária foi: `99*99` não terminou em
dez segundos. O caminho de racionalização usa construções nativas por retirada
e predecessores, cujo custo cresce fortemente com o valor intermediário.

Logo, “resolve multiplicação” descreve capacidade funcional no domínio em que
termina; não autoriza chamar números grandes de suportados. Otimizar exigirá
preservar a construção e a rastreabilidade, não substituir silenciosamente o
método por operação pronta.

## Entradas e servidor

- corpos HTTP acima de 1 MB recebem 413;
- JSON truncado, UTF-8 inválido e raiz JSON não-objeto recebem 400;
- cem GETs sequenciais passaram, mas isso não é teste de concorrência;
- texto conhecido com 500 palavras passou, mas vocabulário desconhecido pode
  custar muito mais por busca de candidatos.

## Não avaliado

- requisições realmente concorrentes e prolongadas;
- milhares de conversas e crescimento do armazenamento;
- limite de memória imposto pelo sistema operativo;
- ZIP bomb, arquivos DOCX enormes e profundidade de ZIP;
- expressões profundamente aninhadas por parênteses;
- carga de vários utilizadores.

Esses itens continuam pendentes. O script não deve aumentar tamanhos sem
timeouts por processo, pois uma operação pura válida pode ter crescimento
intencionalmente elevado.

