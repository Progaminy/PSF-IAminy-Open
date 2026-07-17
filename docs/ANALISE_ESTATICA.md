# Análise estática

Medição local de 17 de julho de 2026, com as mesmas exclusões do CI:

```bash
ruff check . --exclude cao_de_caca --statistics
bandit -r . -x ./cao_de_caca,./testes
```

Ferramentas: Ruff 0.15.22 e Bandit 1.9.4, Python 3.14.4.

## Ruff

| Regra | Quantidade | Interpretação inicial |
| --- | ---: | --- |
| E731 | 390 | atribuições lambda, sobretudo estilo matemático legado |
| F401 | 76 | imports não usados |
| E701 | 22 | múltiplas instruções após dois-pontos |
| E702 | 17 | múltiplas instruções separadas por ponto e vírgula |
| E401 | 11 | múltiplos imports na mesma linha |
| E402 | 7 | imports fora do topo |
| E741 | 6 | nomes de uma letra ambíguos |
| F841 | 5 | variáveis locais não usadas |
| F811 | 3 | redefinições não usadas em testes |
| **Total** | **537** | dívida existente; CI informativo |

Antes da triagem eram 541. Foram corrigidos uma chave literal duplicada
`variacao diacronica`, duas variáveis sem uso e uma f-string sem interpolação.

Não foi aplicado `ruff --fix` em massa: centenas de lambdas representam a
notação funcional histórica do núcleo e uma reescrita mecânica ampla teria
risco desproporcional. Imports F401 precisam de revisão por módulo, pois alguns
funcionam como exportação histórica.

## Bandit

Resultado após substituir um `assert` de runtime por erro explícito:

```text
11 alertas de severidade baixa / confiança alta
0 médios
0 altos
```

Triagem:

- oito B404/B603 vêm de quatro usos de `subprocess` com lista fixa e
  `shell=False`: avaliação de limites, benchmark, classificação da suíte e
  executor de testes; nenhum recebe comando de texto do utilizador;
- dois B311 vêm de `random.Random(semente)` para exercícios pedagógicos
  reproduzíveis, sem finalidade criptográfica;
- um B110 vem da tentativa final de matar processo já encerrado, onde falhar
  novamente não muda a limpeza possível.

Os alertas permanecem visíveis; não receberam `# nosec` apenas para zerar o
relatório. Mudança de entrada, comando ou finalidade exige nova análise.

## Correção de runtime

`MotorPortugues.fluxo_natural()` usava `assert fluxo is not None`. Em Python
otimizado (`-O`), o assert desapareceria. Agora levanta `RuntimeError` explícito
se a invariável falhar. A seleção de 61 testes relacionados passou depois das
mudanças.

## Política gradual

O job continua não bloqueante enquanto houver dívida conhecida. Regras devem
virar bloqueantes em grupos pequenos, começando por chaves duplicadas, nomes
indefinidos, erros de sintaxe e alertas Bandit médios/altos. O objetivo não é
um relatório verde artificial; é impedir novas ocorrências perigosas sem
reescrever cegamente conhecimento estável.

