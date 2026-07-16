# Política de dados

Item 24 do plano de melhorias públicas. Descreve o que o PSF-IAminy guarda localmente, onde, por quanto tempo, como apagar, e se algo sai da máquina do utilizador. Não é uma política legal (privacidade/LGPD/GDPR); é uma descrição técnica honesta do que o código faz, verificada lendo o código, não apenas descrita de memória.

## Funciona totalmente offline

O pacote principal (tudo exceto `cao_de_caca/PSF-Calculadora`, subprojeto externo e opcional) **não faz nenhuma chamada de rede de saída** — confirmado por busca no código, não só por design pretendido. Nenhum dado é enviado a serviços externos, nenhuma telemetria, nenhuma analytics.

## O que é guardado, onde, e por quê

| Dado | Caminho | Guardado por quê | Conteúdo |
| --- | --- | --- | --- |
| Conversas do chat (interface web) | `interface/dados/conversas/<id>.json` | Persistência automática do histórico de chat local | Mensagens trocadas (utilizador e assistente), título, timestamps |
| Log de auditoria do Chat Vivo | `dados/auditoria_chat_vivo.jsonl` | Diagnóstico interno (intenção detectada, confiança, lacunas) | **Inclui o texto literal de cada mensagem enviada** (`nucleo/chat_auditoria.py`), timestamp, métricas de resposta |
| Log de falhas do Chat Vivo | `dados/falhas_chat_vivo.jsonl` | Subconjunto do log acima, só casos de fallback/melhoria necessária | Mesmo formato do log de auditoria |
| Base canónica | `dados/base_canonica.jsonl` | Conhecimento puro reconstruído (não conversas prontas) | Esvaziada deliberadamente numa limpeza anterior (ver `COMO_RODAR.md`); reconstruída por materialização PSF |

Todos os caminhos acima estão listados em `.gitignore` — nenhum dado de sessão real é commitado ou publicado neste repositório.

## Por quanto tempo

Indefinidamente. Nenhum destes ficheiros tem expiração ou rotação automática — crescem enquanto o chat é usado, até serem apagados manualmente.

## Como apagar

```bash
# Uma conversa específica, pela interface (API já protegida contra
# id malformado/travessia de caminho -- ver docs/AUDITORIA_SEGURANCA.md):
curl -X DELETE http://127.0.0.1:8765/api/conversas/<id>

# Todas as conversas locais:
rm -rf interface/dados/conversas/*

# Logs de auditoria/falha do Chat Vivo:
rm -f dados/auditoria_chat_vivo.jsonl dados/falhas_chat_vivo.jsonl
```

Nenhum destes comandos afeta o conhecimento puro do projeto (`conhecimento/`, `nucleo/`, `lingua_portuguesa/` etc.) — só dado de sessão/uso local.

## Componentes com dependências externas

- Pacote principal: nenhuma dependência de terceiros em runtime (só `pytest`/`pytest-cov`/`ruff`/`bandit` como dev, ver `pyproject.toml`) — nada disso lê ou envia dado do utilizador.
- `cao_de_caca/PSF-Calculadora`: subprojeto separado, usa NumPy/SciPy/SymPy/Pandas/Matplotlib/NetworkX/mpmath/scikit-learn de propósito (ver seção correspondente em `README.md`). Roda inteiramente local; nenhuma dessas bibliotecas científicas envia dado pela rede como parte do uso normal deste projeto.
