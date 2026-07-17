# Reprodução em ambiente limpo

## Protocolo executado

Em 17 de julho de 2026, o estado completo da árvore de trabalho foi copiado
para `/tmp/psf-clean-mxYbGm/source` com exclusão de `.git`, caches, bytecode e
ambiente virtual. Em seguida foi criado um venv novo e executado:

```text
python3 -m venv /tmp/psf-clean-mxYbGm/venv
python -m pip install <cópia-do-projeto> pytest
cd /tmp
python -m psf_iaminy --help
cd <cópia-do-projeto>
python verificar_integridade.py
python exemplo_publico.py
python -m pytest -q
```

Resultados finais:

```text
instalação do pacote: aprovada
CLI fora do diretório do projeto: aprovada
integridade: APROVADO
demonstração pública: executada com saída real
suíte: 1081 passed em 71,44 s
Python: 3.14.4
sistema: Linux, mesma máquina de desenvolvimento
```

O diretório temporário foi preservado para inspeção durante esta sessão; ele
não faz parte do repositório.

## Falha encontrada e correção

Na primeira execução, 1080 testes passaram e
`test_fluxo_completo_de_chat_via_http_real` excedeu o timeout HTTP fixo de
cinco segundos. Uma medição fria direta da primeira resposta levou 3,65 s; o
mesmo teste isolado levou 4,48 s. Sob a carga da suíte, cinco segundos não
distinguiam travamento de inicialização lenta.

O timeout do cliente de teste foi ampliado para 15 s. O motor e o resultado não
foram alterados. Desempenho continua medido separadamente em
`docs/DESEMPENHO.md`; o teste HTTP verifica conclusão e resposta, não estabelece
um SLA de cinco segundos. A suíte limpa completa passou depois da mudança.

## O que esta reprodução prova

- a instalação não depende dos metadados Git nem dos caches da árvore original;
- a entrada instalada funciona fora do diretório do projeto;
- demonstração, integridade e testes passam no venv criado;
- o timeout anterior era frágil em ambiente frio.

## O que ainda não prova

- reprodução por outra pessoa;
- funcionamento em outra máquina, Windows ou macOS;
- matriz Python 3.10–3.13 verde no GitHub;
- instalação a partir de uma tag/release publicada;
- ausência de dependências obtidas da cache ou rede do mesmo ambiente.

O próximo passo válido é repetir este protocolo por terceiro e guardar sistema,
Python, commit, comandos e resultado sem editar o relato para parecer melhor.

