# Changelog

Todas as mudanças relevantes da edição pública deste projeto são registadas aqui. Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/). Este repositório público começou com histórico squashado a partir do desenvolvimento interno (ver `PLANO_PSF_IAMINY.md` e `RELATORIO_UNICO.md` para o histórico técnico completo, item a item); o changelog cobre a partir daqui.

Ainda não houve nenhuma release marcada (`v0.1.0` ou posterior) — ver item 25 do plano de melhorias públicas.

## [Não lançado]

### Corrigido
- `COMO_RODAR.md` afirmava `660 passed`, desatualizado em relação aos 1066 testes reais já refletidos no `README.md`. `motor/coerencia.py` ganhou `divergencia_contagem_testes_entre_documentos()` para detectar esse tipo de divergência entre os dois documentos automaticamente.

### Adicionado
- Seção "Em poucos minutos" no início do `README.md`: o que é, problema, o que já funciona, o que é experimental, demonstração rápida e diferencial — antes da filosofia completa.
- Seção "Capacidades reais e limitações" no `README.md`: tabela de capacidades com teste correspondente, separação em conhecimento implementado / experimentos / hipóteses / problemas pendentes / validação externa, e limitações reconhecidas abertamente.
- Explicação do papel de `cao_de_caca/PSF-Calculadora/` no `README.md` (subprojeto externo, por que o nome, por que fica fora da coleta padrão de testes).
- `docs/ARQUITETURA.md`: diagrama e descrição de cada componente (motores, motor comum, auditoria/pureza/rastreabilidade, validação externa, interface, dados, fluxo de entrada e saída).
- `docs/NOTA_CIENTIFICA.md`: problema estudado, hipótese do método PSF, metodologia, resultados verificáveis, limitações e critérios de falsificação.
- Este `CHANGELOG.md`.

## Histórico da edição pública

- **2026-07-16** — `Corrige inconsistências públicas do README` (`b45d1dc`)
- **2026-07-16** — `Adiciona política de segurança` (`5190416`) — `SECURITY.md`
- **2026-07-16** — `Create CONTRIBUTING.md with contribution instructions` (`5b991b9`)
- **2026-07-16** — `Add Apache License 2.0 to the project` (`a1bfc7a`) — `LICENSE`
- **2026-07-16** — `Publicação inicial do PSF-IAminy-Open` (`4d94c1d`) — primeiro commit da edição pública
