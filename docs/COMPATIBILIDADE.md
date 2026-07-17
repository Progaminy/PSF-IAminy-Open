# Política de compatibilidade

## Python

O pacote declara `Python >= 3.10` em `pyproject.toml`. O workflow de CI está
configurado para 3.10, 3.11, 3.12 e 3.13. A primeira execução pública
([run 29505936596](https://github.com/Progaminy/PSF-IAminy-Open/actions/runs/29505936596))
falhou: o teste HTTP tinha timeout de 5 segundos nos quatro ambientes, e
`motor/rastreabilidade.py` acessava `ast.TryStar`, inexistente em 3.10.

Na árvore local candidata, o timeout do cliente de teste é 15 segundos e o
percurso AST forma os tipos `Try`/`TryStar` conforme o interpretador, com uma
regressão que simula a ausência de `TryStar`. Isso corrige as causas conhecidas;
não é ainda confirmação pública. As quatro versões só serão chamadas de
publicamente confirmadas depois de uma nova execução verde no GitHub.

A suíte completa passou localmente em Python 3.14.4 em 17 de julho de 2026,
mas 3.14 ainda não integra a matriz pública declarada. Esse resultado isolado
não estabelece suporte permanente.

## Sistemas operativos

O pacote principal usa Python e biblioteca padrão, sem código nativo próprio.
O fluxo principal é desenvolvido e validado em Linux, incluindo instalação e
suíte completa numa cópia sem Git/caches (`docs/REPRODUCAO.md`). Windows e macOS são
alvos pretendidos, ainda sem validação independente documentada.

Comandos de ativação do ambiente virtual diferem por sistema; o código do
motor não deve depender do diretório de trabalho nem de caminhos absolutos da
máquina do autor.

## Interfaces

- `python -m psf_iaminy` e `psf-iaminy` são as entradas públicas preferidas.
- `README.md`, `COMO_RODAR.md` e os exemplos são documentação pública.
- módulos internos de `nucleo/`, `motor/`, `matematica/`,
  `lingua_portuguesa/` e `interface/` ainda podem mudar antes de `v1.0.0`;
- formatos locais de conversa e progresso não possuem garantia de migração
  automática entre mudanças incompatíveis nesta fase experimental.

Mudanças incompatíveis devem ser registadas no `CHANGELOG.md`, acompanhadas
de instrução de migração quando afetarem dados ou uma entrada pública.

## Dependências e rede

O pacote principal não possui dependências obrigatórias de execução fora da
biblioteca padrão. Ferramentas de build, teste e análise são separadas em
`pyproject.toml`; o subprojeto `cao_de_caca/PSF-Calculadora` possui política e
dependências próprias e não define a compatibilidade do motor principal.

O servidor é local e não constitui compromisso de compatibilidade como API
HTTP pública. O pacote principal não deve iniciar comunicação externa sem uma
mudança explícita, documentada e testada da política de dados.

## Critério para declarar suporte

Uma combinação de Python e sistema operativo só deve ser declarada suportada
quando instalação, integridade, demonstração e suíte completa passarem num
ambiente limpo reproduzível. “Deve funcionar” não equivale a “suportado”.
