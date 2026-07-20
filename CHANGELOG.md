# Changelog

Todas as mudanças relevantes da edição pública deste projeto são registadas aqui. Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/). Este repositório público começou com histórico squashado a partir do desenvolvimento interno (ver `PLANO_PSF_IAMINY.md` e `RELATORIO_UNICO.md` para o histórico técnico completo, item a item); o changelog cobre a partir daqui.

Ainda não houve nenhuma release marcada (`v0.1.0` ou posterior) — ver item 25 do plano de melhorias públicas.

## [Não lançado]

### Corrigido
- Evidência corrente de testes reconciliada entre README, guia de execução, nota científica, release candidata, relatório único, página pública e `docs/TESTES.md`: 1.223/1.223 aprovados em Python 3.13.5.
- Empacotamento por wheel agora inclui documentos de conhecimento, léxico, interface estática, dados canónicos, testes e documentação compartilhada; a instalação isolada deixou de depender da árvore-fonte.
- Metadados de licença migrados para expressão SPDX PEP 639 (`Apache-2.0`), build mínimo Setuptools 77 e pacote estático explícito; o wheel final foi construído sem avisos.
- Conversas, auditorias, identidade, memória ortográfica, padrões não reconhecidos e histórico de desempenho usam uma raiz gravável do utilizador em instalações, com `PSF_IAMINY_DATA_DIR` como substituição explícita, em vez de tentar modificar `site-packages`.
- Workflows passaram a usar versões existentes e fixas das actions oficiais; upload de artefactos usa a linha v4 compatível.
- `COMO_RODAR.md` afirmava `660 passed`, desatualizado em relação aos 1066 testes reais já refletidos no `README.md`. `motor/coerencia.py` ganhou `divergencia_contagem_testes_entre_documentos()` para detectar esse tipo de divergência entre os dois documentos automaticamente.
- CI pública auditada a partir dos logs reais do run `29505936596`: timeout HTTP de 5 s nos quatro ambientes e acesso a `ast.TryStar` no Python 3.10. O timeout candidato passou a 15 s, o percurso AST agora é compatível com 3.10 e ganhou regressão; as actions foram atualizadas para runtime Node 24 e permissões mínimas.
- Job estático dividido entre regras críticas bloqueantes e dívida completa informativa; Bandit passa a executar mesmo quando o relatório completo do Ruff encontra dívida existente.

### Segurança
- `interface/conversas.py`: `id_conversa` (vindo da URL) não era validado antes de virar caminho de ficheiro — permitia ler/apagar qualquer `.json` alcançável por travessia relativa (`../`) a partir da pasta de conversas. Confirmado explorável de verdade antes da correção. Corrigido exigindo o formato exato de `secrets.token_hex(6)`. Ver `docs/AUDITORIA_SEGURANCA.md`.
- `interface/servidor.py`: corpo do pedido HTTP era lido conforme o `Content-Length` declarado pelo cliente, sem limite. Corrigido com um teto de 1 MB (`413` acima disso).
- `ensino/leitura_documentos.py`: ZIP/DOCX agora têm limites compactados/descomprimidos, razão contra ZIP bomb, validação de nomes internos e leitura limitada; 18 regressões cobrem também DOCX hostil aninhado.

### Adicionado
- `docs/OPENAI_BUILD_WEEK.md` e secções bilingues nos READMEs documentam o escopo anterior, a linha temporal pública, o uso de Codex/GPT-5.6 e os comandos de verificação exigidos pelo concurso.
- A página estática pública passou a apresentar o trabalho do Build Week e a contagem atual de 1.223 testes recolhidos.
- `docs/AUDITORIA_MELHORIAS_120.md`: estado factual dos 64 pontos, separando concluído, parcial e dependente de terceiros.
- `ferramentas/auditar_codigo.py` e `docs/QUALIDADE_CODIGO.md`: linha de base de tipagem, docstrings, exceções amplas e duplicação exata no código de produção.
- `docs/ROTEIRO_VIDEO.md`: demonstração de 2–5 minutos que exige comandos e limitações reais.
- `psf_iaminy/recursos.py` e regressões de instalação/dados mutáveis.
- Seção "Em poucos minutos" no início do `README.md`: o que é, problema, o que já funciona, o que é experimental, demonstração rápida e diferencial — antes da filosofia completa.
- Seção "Capacidades reais e limitações" no `README.md`: tabela de capacidades com teste correspondente, separação em conhecimento implementado / experimentos / hipóteses / problemas pendentes / validação externa, e limitações reconhecidas abertamente.
- Explicação do papel de `cao_de_caca/PSF-Calculadora/` no `README.md` (subprojeto externo, por que o nome, por que fica fora da coleta padrão de testes).
- `docs/ARQUITETURA.md`: diagrama e descrição de cada componente (motores, motor comum, auditoria/pureza/rastreabilidade, validação externa, interface, dados, fluxo de entrada e saída).
- `docs/NOTA_CIENTIFICA.md`: problema estudado, hipótese do método PSF, metodologia, resultados verificáveis, limitações e critérios de falsificação.
- `docs/COBERTURA.md`: cobertura de testes medida localmente (63%), por módulo.
- `docs/AUDITORIA_SEGURANCA.md` e `docs/POLITICA_DADOS.md`: o que foi auditado/corrigido/continua como risco, e o que é guardado localmente, onde e por quanto tempo.
- `.github/workflows/ci.yml`: primeiro CI público (matriz Python 3.10-3.13, testes+cobertura+integridade, mais job informativo de Ruff/Bandit), templates de issue e PR.
- `exemplo_publico.py` e `exemplos/matematica.py`/`portugues.py`/`rastreabilidade.py`: demonstrações rodáveis com saída real conferida.
- `pyproject.toml` e pacote `psf_iaminy/`: instalação via `pip install -e .`, comando `psf-iaminy`/`python -m psf_iaminy`.
- `ROADMAP.md`: prioridades públicas reduzidas em Agora, Próximo, Depois e Em investigação.
- `docs/RELEASE.md`: conteúdo, limitações, validação local e checklist da primeira release candidata, sem afirmar publicação antes da tag existir.
- `CODE_OF_CONDUCT.md`: regras de convivência, escopo de aplicação e proteção do escrutínio científico respeitoso.
- `GOVERNANCE.md`: critérios de decisão, aceitação de contribuições, classificação científica e releases.
- `docs/COMPATIBILIDADE.md` e `docs/DEPENDENCIAS.md`: suporte declarado sem extrapolar a validação real e inventário do pacote principal.
- `CITATION.cff`, `AUTHORS.md` e `REFERENCIAS.md`: citação sem DOI/release inventados, autoria pública e protocolo para incorporar referências externas.
- `docs/TESTES.md` e `ferramentas/classificar_testes.py`: classificação reproduzível dos 1084 casos coletados e limites do número bruto.
- `docs/DESEMPENHO.md` e `benchmarks/benchmark_basico.py`: linha de base reproduzível, incluindo custo frio do corretor e limites da medição.
- `README.en.md`: apresentação pública essencial em inglês, com instalação, arquitetura, evidência e limitações sem criar uma segunda fonte de verdade.
- `avaliacoes/` e `docs/AVALIACAO_QUALIDADE.md`: avaliações executáveis; Matemática passou 7/7 casos + prova finita no escopo, Português expôs 4/8 falsos positivos numa amostra pequena.
- `avaliacoes/comparar_sympy.py` e `docs/VALIDACAO_EXTERNA.md`: primeira comparação externa isolada, com 7/7 concordâncias na amostra contra SymPy 1.14.0.
- `docs/REPRODUCAO.md`: instalação, CLI, integridade, demonstração e 1081 testes reproduzidos numa cópia limpa; timeout HTTP de teste ajustado após falha fria real.
- `docs/ANALISE_ESTATICA.md`: Ruff/Bandit executados e triados; chave duplicada e garantia de runtime por `assert` corrigidas sem autofix massivo.
- `ferramentas/auditar_testes.py`: 763 funções auditadas; nenhuma sem asserção explícita, duplicação AST exata ou erro de sintaxe.
- Servidor HTTP agora devolve 400 para JSON truncado, UTF-8 inválido e JSON que não seja objeto; três regressões elevam a suíte a 1084 casos.
- `avaliacoes/avaliar_limites.py` e `docs/LIMITES_OPERACIONAIS.md`: limites com timeout; `99*99` excedeu 10 s, enquanto 100 termos, 500 palavras e 100 GETs concluíram.
- `docs/ISSUES_PLANEJADAS.md`: seis issues reais preparadas após criação remota falhar com 403; nenhuma é apresentada como publicada.
- `docs/en/` e `CONTRIBUTING.en.md`: traduções essenciais de arquitetura, segurança, roadmap, demonstração, release e contribuição, ligadas aos documentos canónicos.
- `site/` e workflow de GitHub Pages com permissões separadas entre build/deploy; página para apresentação, arquitetura, evidência, limites e interesse científico. Ainda não é apresentada como publicada.
- `docs/IMAGENS.md` e cinco capturas reais: interface inicial, pergunta/resposta com origem e limite, mapa, ensino e página estática, todas sem dados persistentes do utilizador.
- `docs/CANDIDATURA.md` e `docs/DIVULGACAO.md`: pacote factual para atualização somente quando autorizada e texto técnico reutilizável sem alegar publicação externa.
- Suíte ampliada para 1103 casos em 109 ficheiros; 35 casos classificados como segurança. A execução completa atual passou em 80,10 s.
- Após regressões de recursos/instalação, a suíte passou a 1106 casos em 110 ficheiros; 1106/1106 passaram em Python 3.13.5 (182,28 s neste ambiente).
- Este `CHANGELOG.md`.

### Removido
- Pasta `privado/` (só continha um marcador estrutural nesta edição pública, sem conteúdo pessoal real) — removida por pedido explícito do autor, com as referências que a citavam como preservada ajustadas em `REGRA_INTEGRIDADE.md`, `COMO_RODAR.md`, `README.md` e `RELATORIO_UNICO.md`.

## Histórico da edição pública

- **2026-07-16** — `Corrige inconsistências públicas do README` (`b45d1dc`)
- **2026-07-16** — `Adiciona política de segurança` (`5190416`) — `SECURITY.md`
- **2026-07-16** — `Create CONTRIBUTING.md with contribution instructions` (`5b991b9`)
- **2026-07-16** — `Add Apache License 2.0 to the project` (`a1bfc7a`) — `LICENSE`
- **2026-07-16** — `Publicação inicial do PSF-IAminy-Open` (`4d94c1d`) — primeiro commit da edição pública
