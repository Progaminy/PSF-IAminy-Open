# Pacote factual para eventual atualização da candidatura

Estado: **candidatura ao Codex for Open Source enviada em 20 de julho de 2026; este ficheiro é apenas registo local e material para eventual pedido de informação adicional**.

A candidatura original já foi enviada. Este resumo só deve ser usado se
existir um canal autorizado para atualização ou se a OpenAI pedir informação
adicional. Não autoriza um segundo envio, não promete aprovação e não converte
métricas locais em validação independente.


## Relação com o OpenAI Build Week

O mesmo repositório `Progaminy/PSF-IAminy-Open` foi usado na submissão do
OpenAI Build Week e na candidatura ao Codex for Open Source. Isso não duplica
nem substitui nenhuma inscrição: são programas independentes, com avaliações
diferentes. No momento da submissão ao Build Week, a candidatura ao programa
open source ainda não representava seleção, crédito ou apoio recebido.

## Resumo de uma página

O PSF-IAminy é um sistema experimental e local que investiga como construir
conhecimento de Matemática e Português com uma ponte explícita até dependências
anteriores. Quando a ponte não existe, o sistema deve declarar hipótese,
fronteira ou limite, em vez de produzir uma resposta com aparência de certeza.

O pacote principal usa apenas a biblioteca padrão em runtime. Bibliotecas e
modelos externos podem comparar, medir ou validar; não podem ser fundamento
oculto do conhecimento puro PSF.

## Evidência verificável atual

- 1.223 testes automatizados aprovados localmente e matriz de CI declarada para Python 3.10–3.13;
- cobertura de linhas com fotografia e lacunas por módulo documentadas;
- 203 documentos conceituais matemáticos auditados com pontes fechadas;
- 1.141 conceitos puros de Português e 2.545 relações de dependência;
- avaliação matemática inicial com 7/7 casos e uma prova no fragmento finito;
- comparação inicial com SymPy 1.14.0: 7/7 concordâncias na amostra;
- avaliação linguística que publicou 4 falsos positivos em 8 palavras válidas
  da amostra, sem apresentar 50% como estimativa da língua;
- auditoria de segurança com falhas reais corrigidas e limites de anexos
  compactados testados;
- instalação editável, CLI, demonstrações, página estática e capturas reais.

Os comandos, resultados e limites vivem em `docs/REPRODUCAO.md`,
`docs/TESTES.md`, `docs/AVALIACAO_QUALIDADE.md`,
`docs/VALIDACAO_EXTERNA.md` e `docs/IMAGENS.md`.

## Estado que não deve ser exagerado

- A primeira execução pública da CI, run `29505936596`, falhou. Há correções
  locais candidatas, mas ainda não existe execução pública verde delas.
- `v0.1.0` é apenas candidata; nenhuma release ou DOI foi publicado.
- A reprodução limpa ocorreu na mesma máquina; não há ainda reprodução por
  terceiro, validação Windows/macOS, utilizadores documentados ou contribuição
  externa.
- A cobertura e as amostras de avaliação não demonstram correção científica
  geral, completude matemática ou qualidade linguística representativa.

## Por que créditos seriam úteis

Se créditos fossem concedidos, o uso proposto seria isolado da camada de
conhecimento puro:

1. construir conjuntos de avaliação e críticas externas reproduzíveis;
2. comparar explicações, detecção de limites e rastreabilidade contra modelos
   externos, guardando versões, prompts, resultados e divergências;
3. investigar falsos positivos linguísticos e casos extremos matemáticos;
4. testar ferramentas de apoio ao mantenedor para revisão, documentação e
   triagem, sem importar respostas externas como verdade PSF.

Cada uso precisa respeitar `REGRA_INTEGRIDADE.md`, `docs/POLITICA_DADOS.md` e
o orçamento concedido. Dados pessoais ou conversas privadas não entram nas
avaliações.

## Materiais de apoio

- apresentação e execução: `README.md`, `README.en.md`, `COMO_RODAR.md`;
- arquitetura e método: `docs/ARQUITETURA.md`, `docs/NOTA_CIENTIFICA.md`;
- segurança e dados: `SECURITY.md`, `docs/AUDITORIA_SEGURANCA.md`,
  `docs/POLITICA_DADOS.md`;
- validação e limites: `docs/AVALIACAO_QUALIDADE.md`,
  `docs/VALIDACAO_EXTERNA.md`, `docs/LIMITES_OPERACIONAIS.md`;
- candidata, prioridades e governança: `docs/RELEASE.md`, `ROADMAP.md`,
  `GOVERNANCE.md`;
- autoria e citação: `AUTHORS.md`, `CITATION.cff`, `REFERENCIAS.md`.

Antes de qualquer atualização externa, substituir apenas métricas que tenham
sido repetidas no commit candidato e anexar o SHA exato. Ausência de resultado
deve permanecer ausência, nunca texto promocional.
