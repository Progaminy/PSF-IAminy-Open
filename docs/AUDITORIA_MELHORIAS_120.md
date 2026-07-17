# Auditoria das 64 melhorias — preparação pública “120/100”

Esta auditoria transforma a lista de melhorias num estado verificável. “120/100”
não é uma probabilidade de aprovação: é o nome interno para uma preparação que
ultrapassa o mínimo documental e técnico. Nenhuma estrela, utilizador, reprodução,
contribuição ou aprovação externa é inventada.

Legenda:

- ✅ **concluído na árvore atual** — existe evidência local reproduzível;
- 🟡 **preparado/parcial** — a parte controlável pelo mantenedor existe, mas falta
  publicação, execução pública ou revisão adicional;
- ⛔ **externo** — depende de outra pessoa, plataforma ou decisão da OpenAI.

## Estado item a item

| # | Melhoria | Estado | Evidência atual / próximo corte honesto |
|---:|---|:---:|---|
| 1 | README rápido de compreender | ✅ | Abertura “Em poucos minutos”, problema, estado, demonstração e diferencial em `README.md`. |
| 2 | Eliminar contradições documentais | ✅ | Testes de coerência e correções entre README, execução e estrutura; auditoria deve continuar a cada mudança. |
| 3 | Testes automáticos públicos | 🟡 | `.github/workflows/ci.yml` corrigido e validado sintaticamente; falta novo push e execução verde pública. |
| 4 | Selo dos testes | ✅ | Badge preparado no README, ligado ao workflow; só ficará verde depois de execução pública bem-sucedida. |
| 5 | Demonstração pública pequena | ✅ | `exemplo_publico.py` executado com saída real. |
| 6 | Exemplos separados | ✅ | `exemplos/matematica.py`, `portugues.py` e `rastreabilidade.py`, com testes correspondentes. |
| 7 | Secção clara de limitações | ✅ | README, nota científica, release e avaliações declaram limites e resultados negativos. |
| 8 | Separar validado, experimental e hipótese | ✅ | Tabela e secções próprias no README; hipótese de primalidade continua marcada como hipótese. |
| 9 | Instalação reproduzível | ✅ | `pyproject.toml`, instalação editável e wheel testado fora da árvore-fonte. O wheel leva léxico, conhecimento, interface, testes e documentos. |
| 10 | Comando principal claro | ✅ | `psf-iaminy` e `python -m psf_iaminy`; entradas antigas classificadas como secundárias. |
| 11 | Organização como pacote Python | 🟡 | Fachada instalável `psf_iaminy/` concluída; migração total para `src/` foi adiada para não mutilar centenas de imports estáveis. |
| 12 | Explicar PSF-Calculadora | ✅ | Papel e isolamento de `cao_de_caca/PSF-Calculadora` documentados; renomear/mover continua decisão futura. |
| 13 | Documento de arquitetura | ✅ | `docs/ARQUITETURA.md`. |
| 14 | Diagrama visual | ✅ | Diagrama Mermaid e fluxo textual em `docs/ARQUITETURA.md`; capturas reais em `docs/assets/`. |
| 15 | Nota científica resumida | ✅ | `docs/NOTA_CIENTIFICA.md`. |
| 16 | Tabela de capacidades reais | ✅ | README liga capacidade, estado, teste e limitação. |
| 17 | Cobertura de testes | ✅ | Linha de base de 63% em `docs/COBERTURA.md`; precisa ser atualizada após mudanças relevantes. |
| 18 | Identificar testes superficiais/duplicados | ✅ | `ferramentas/auditar_testes.py` e `ferramentas/classificar_testes.py`; limites da auditoria declarados. |
| 19 | Regressões para erros reais | ✅ | Travessia de caminho, corpo HTTP, ZIP/DOCX hostil, compatibilidade AST e recursos de instalação possuem regressões. |
| 20 | Várias versões do Python | 🟡 | Matriz 3.10–3.13 configurada; falta execução pública verde após as correções. |
| 21 | Análise estática | ✅ | Ruff e Bandit configurados; erros críticos bloqueiam CI, dívida histórica é visível e triada. |
| 22 | Auditoria de segurança | ✅ | Auditoria manual + Bandit em `docs/AUDITORIA_SEGURANCA.md`; não equivale a auditoria independente. |
| 23 | Testes de segurança | ✅ | 35 casos já classificados como segurança, mais regressões de recursos instalados; 0 médio/alto no Bandit local. |
| 24 | Política de dados | ✅ | `docs/POLITICA_DADOS.md`; wheel grava dados mutáveis em diretório do utilizador, não em `site-packages`. |
| 25 | Primeira release | 🟡 | Conteúdo candidato em `docs/RELEASE.md`; falta tag e publicação após CI verde. |
| 26 | Changelog | ✅ | `CHANGELOG.md`. |
| 27 | Roadmap público | ✅ | `ROADMAP.md` e versão inglesa. |
| 28 | Issues reais | 🟡 | Seis issues preparadas em `docs/ISSUES_PLANEJADAS.md`; publicação remota depende de permissão/autenticação. |
| 29 | Commits ligados a issues | ⛔ | Só pode começar depois de existirem números de issues públicos. |
| 30 | Templates de issues | ✅ | `.github/ISSUE_TEMPLATE/`. |
| 31 | Template de pull request | ✅ | `.github/pull_request_template.md`. |
| 32 | Código de conduta | ✅ | `CODE_OF_CONDUCT.md`. |
| 33 | README em inglês | ✅ | `README.en.md`. |
| 34 | Traduzir documentos essenciais | ✅ | `docs/en/` + `CONTRIBUTING.en.md`; não se finge tradução integral dos documentos científicos longos. |
| 35 | Página de documentação | 🟡 | `site/` e workflow Pages prontos; falta publicação no GitHub Pages. |
| 36 | Screenshots/GIFs reais | ✅ | Cinco capturas reais documentadas em `docs/IMAGENS.md`; GIF não é necessário para considerar o item demonstrável. |
| 37 | Vídeo curto | 🟡 | Roteiro reproduzível em `docs/ROTEIRO_VIDEO.md`; gravação e publicação dependem do mantenedor. |
| 38 | Benchmarks | ✅ | `benchmarks/benchmark_basico.py` e `docs/DESEMPENHO.md`. |
| 39 | Avaliação matemática | ✅ | Avaliação executável e resultados em `docs/AVALIACAO_QUALIDADE.md`. |
| 40 | Avaliação linguística | ✅ | Avaliação executável inclui resultados positivos e falsos positivos, sem maquilhagem. |
| 41 | Comparação externa | 🟡 | Primeira comparação matemática com SymPy documentada; validação linguística externa continua pendente. |
| 42 | Relatório de validação externa | ✅ | `docs/VALIDACAO_EXTERNA.md`, com escopo e divergências. |
| 43 | Testar noutro ambiente | 🟡 | Cópia limpa e wheel isolado validados na mesma infraestrutura; faltam outro computador/SO. |
| 44 | Reprodução por outra pessoa | ⛔ | Não pode ser fabricada pelo autor ou por automação local. Protocolo pronto em `docs/REPRODUCAO.md`. |
| 45 | Primeiros utilizadores reais | ⛔ | Depende de adoção externa verdadeira. |
| 46 | Contribuições externas | ⛔ | Depende de terceiro real; templates e guia já reduzem a barreira. |
| 47 | Divulgação técnica honesta | 🟡 | Material pronto em `docs/DIVULGACAO.md`; falta publicar em comunidades apropriadas. |
| 48 | Apresentação para investigadores | ✅ | Nota científica, candidatura e página estática explicam relevância por área. |
| 49 | Governança | ✅ | `GOVERNANCE.md`. |
| 50 | Critérios de conclusão | ✅ | Governança, roadmap e regras exigem código, teste, documentação, limites e validação. |
| 51 | Limpar nomes/estruturas confusas | ✅ | Nomes históricos são explicados; renomeações perigosas foram conscientemente adiadas. |
| 52 | Reduzir duplicação | 🟡 | `ferramentas/auditar_codigo.py` encontrou linha de base objetiva; 17 grupos exatos precisam de revisão sem refatoração automática. |
| 53 | Tipagem e contratos | 🟡 | Auditoria mede 57,3% das funções/métodos totalmente tipados; priorização deve começar pelas APIs públicas críticas. |
| 54 | Mensagens de erro | 🟡 | Casos HTTP/documentos/CLI foram melhorados; auditoria global de mensagens e exceções amplas continua aberta. |
| 55 | Logs estruturados | ✅ | Auditoria usa JSONL; caminhos, conteúdo, retenção e eliminação estão documentados. |
| 56 | Desempenho e limites | ✅ | `avaliacoes/avaliar_limites.py`, benchmarks e limites explícitos. |
| 57 | Política de compatibilidade | ✅ | `docs/COMPATIBILIDADE.md`; não chama Windows/macOS de suportados sem prova. |
| 58 | Inventário de dependências | ✅ | `docs/DEPENDENCIAS.md`; pacote principal sem dependências de runtime de terceiros. |
| 59 | Citação científica | ✅ | `CITATION.cff` e `REFERENCIAS.md`. |
| 60 | Autoria/propriedade intelectual | ✅ | `AUTHORS.md`, Apache-2.0 e instrução de citação; não reivindica patente/DOI inexistente. |
| 61 | Pacote de candidatura | ✅ | `docs/CANDIDATURA.md`, métricas, arquitetura, evidência, segurança e limites. |
| 62 | Atividade pública contínua | 🟡 | Estrutura pronta; é um processo temporal, não um ficheiro que possa ser concluído de uma vez. |
| 63 | Atualizar candidatura quando permitido | ⛔ | Só deve ocorrer se existir canal oficial ou pedido da OpenAI; não criar submissões duplicadas. |
| 64 | Importância real para o ecossistema | ⛔ | Só utilização, reprodução, contribuição e impacto externos verdadeiros podem fechar este item. |

## Resultado interno atual

- **Concluídos tecnicamente:** 43/64.
- **Preparados ou parcialmente concluídos:** 13/64.
- **Dependentes de terceiros/plataformas:** 8/64.
- **Testes:** 1106 casos coletados e 1106/1106 aprovados na árvore atual em Python 3.13.5
  (182,28 s neste ambiente). A duração não é comparada diretamente com a medição
  anterior em Python 3.14.4 e outra carga de máquina.
- **Empacotamento:** wheel instalado e exercitado fora da fonte; comando, Português,
  documentos, rastreabilidade, interface estática e dados mutáveis verificados.

## O que mais aumenta a candidatura agora

1. enviar esta árvore e obter CI verde em Python 3.10–3.13;
2. publicar a release candidata `v0.1.0`;
3. publicar GitHub Pages;
4. abrir as issues preparadas e relacionar commits futuros;
5. conseguir uma reprodução independente real;
6. recolher utilizadores, feedback e uma contribuição externa sem fabricar métricas.

Os últimos quatro pontos mais valiosos não podem ser substituídos por mais linhas de
código. O repositório já possui substância técnica; a próxima prova necessária é
confiança pública e utilidade externa.
