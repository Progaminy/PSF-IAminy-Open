# Política técnica de dados

Item 24 do plano de melhorias públicas. Este documento descreve o comportamento
real do código; não é uma política jurídica de privacidade.

## Rede e funcionamento offline

O pacote principal não faz chamadas de rede de saída, não envia telemetria e não
possui analytics. A interface HTTP liga-se por padrão a `127.0.0.1`; isso não
significa que deva ser exposta à internet.

## Onde dados mutáveis são gravados

Num checkout do código, os caminhos históricos dentro da árvore são preservados
para compatibilidade. Numa instalação por wheel, dados gerados durante o uso não
são escritos em `site-packages`; usam o diretório de dados do utilizador:

- Linux: `${XDG_DATA_HOME:-~/.local/share}/psf-iaminy/`;
- macOS: `~/Library/Application Support/PSF-IAminy/`;
- Windows: `%LOCALAPPDATA%\PSF-IAminy\`;
- qualquer sistema: `PSF_IAMINY_DATA_DIR` substitui explicitamente a raiz.

A implementação canónica está em `psf_iaminy/recursos.py`.

| Dado | Caminho relativo | Finalidade | Conteúdo sensível possível |
| --- | --- | --- | --- |
| Conversas locais | `interface/dados/conversas/<id>.json` | histórico da interface | texto integral das mensagens |
| Auditoria do Chat Vivo | `dados/auditoria_chat_vivo.jsonl` | intenção, confiança, lacunas e tempo | texto integral da mensagem |
| Falhas/fallbacks | `dados/falhas_chat_vivo.jsonl` | casos que precisam de melhoria | mesmo conteúdo da auditoria |
| Identidade humana | `motor/identidade_humana.json` | factos fornecidos voluntariamente durante a entrevista local | dados pessoais declarados pelo utilizador |
| Memória ortográfica aprovada | `lingua_portuguesa/dados/memoria_ortografica.tsv` | pares de correção acrescentados localmente | texto que o utilizador decidiu guardar |
| Padrões não reconhecidos | `ensino/padroes_nao_reconhecidos.json` | perguntas ainda sem padrão seguro | pergunta original |
| Histórico de desempenho | `motor/historico_desempenho.json` | tempos de testes para detectar regressões | nomes de testes e tempos; sem conversa |
| Base canónica | `dados/base_canonica.jsonl` | conhecimento materializado, não histórico de chat | depende do conteúdo materializado |

Os ficheiros gerados por sessão e ambiente estão ignorados pelo Git. O ficheiro
`ensino/padroes_nao_reconhecidos.json` e a linha de base de desempenho podem ter
conteúdo inicial distribuído; numa instalação, alterações posteriores ficam na
área do utilizador.

## Retenção e eliminação

Não existe expiração automática. Os dados permanecem até serem apagados pelo
utilizador. Para descobrir a raiz efetiva:

```bash
python - <<'PY'
from psf_iaminy.recursos import raiz_dados_usuario
print(raiz_dados_usuario())
PY
```

Para apagar todos os dados mutáveis de uma instalação, remova essa pasta. Num
checkout, os principais resíduos de sessão podem ser removidos assim:

```bash
rm -rf interface/dados/conversas/
rm -f dados/auditoria_chat_vivo.jsonl dados/falhas_chat_vivo.jsonl
rm -f motor/identidade_humana.json
rm -f lingua_portuguesa/dados/memoria_ortografica.tsv
```

Apagar dados de sessão não apaga o conhecimento versionado em `conhecimento/`,
`nucleo/`, `matematica/` ou `lingua_portuguesa/`. Antes de apagar
`ensino/padroes_nao_reconhecidos.json` ou `motor/historico_desempenho.json` num
checkout, confirme se pretende remover também a linha de base versionada.

## Dependências externas

O pacote principal não possui dependências de runtime de terceiros. Ferramentas
de desenvolvimento e validação (`pytest`, Ruff, Bandit, SymPy opcional) operam
localmente e não são fundamento do conhecimento PSF. O subprojeto
`cao_de_caca/PSF-Calculadora` tem dependências científicas próprias e ciclo
separado.
