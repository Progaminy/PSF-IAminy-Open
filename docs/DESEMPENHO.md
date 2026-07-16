# Desempenho e benchmarks

## Método

`python3 benchmarks/benchmark_basico.py` mede operações reais do pacote
principal com `perf_counter`, sete repetições (três para a auditoria de
referências) e `tracemalloc`. Não usa plugin de benchmark nem dependência
externa. O JSON impresso pode ser guardado por CI no futuro.

Ambiente desta fotografia:

```text
data: 17 de julho de 2026
Python: 3.14.4
sistema: ambiente Linux local de desenvolvimento
```

Hardware, carga do sistema e cache afetam os valores. Estes números são linha
de base, não promessa de desempenho em outra máquina.

## Resultado local

| Operação | Mediana | Mínimo | Máximo |
| --- | ---: | ---: | ---: |
| importar `matematica`, `lingua_portuguesa` e `motor` num processo novo | 140,441 ms | 137,190 ms | 148,815 ms |
| calcular `2+2*3` | 0,313 ms | 0,302 ms | 0,527 ms |
| reconstruir `2:3` com oito casas | 2,393 ms | 2,182 ms | 2,455 ms |
| caminho de dependências de “interpretação” | 3,949 ms | 3,547 ms | 4,737 ms |
| corrigir frase com estruturas já carregadas | 53,731 ms | 53,516 ms | 65,171 ms |
| auditar referências citadas nas ETAPAs | 41,590 ms | 41,558 ms | 42,171 ms |

A primeira correção da frase levou **2343,072 ms**, muito acima da mediana
aquecida, porque materializa estruturas lexicais sob demanda. Esse custo frio é
declarado separadamente para não desaparecer dentro de uma média favorável.

O pico observado por `tracemalloc` foi **22,228 MiB**. Isso mede alocações
rastreadas pelo Python durante o script; não é o RSS total do processo.

A suíte completa mais recente levou **81,06 s** para 1084 testes. Ela
mede muito mais do que as operações acima e não deve ser comparada diretamente
com uma chamada isolada.

## Interpretação

- operações matemáticas escolhidas ficam em milissegundos neste ambiente;
- a inicialização preguiçosa do corretor é o maior custo visível;
- a auditoria de referências é curta o suficiente para uso frequente local;
- ainda não há série histórica, intervalo estatístico entre máquinas, RSS,
  carga concorrente nem benchmark de entradas grandes.

## Próximos limites a medir

1. textos progressivamente longos e léxico completo;
2. números grandes e expressões profundas;
3. muitas requisições locais concorrentes;
4. tamanho e quantidade de conversas guardadas;
5. memória RSS e comparação entre Python 3.10–3.14;
6. comparação antes/depois de otimizações, sempre no mesmo ambiente.

Uma otimização só deve ser aceite se preservar resultados, rastreabilidade e
testes; tempo menor não autoriza atalhos no conhecimento.
