# Governança

O PSF-IAminy-Open é atualmente mantido por um mantenedor principal. Esta
estrutura simples não dispensa critérios públicos de decisão.

## Responsabilidades

O mantenedor decide integração, releases, segurança e classificação do
conhecimento. Colaboradores podem propor código, testes, documentação,
experimentos e correções; enviar uma contribuição não garante integração.

## Critérios de aceitação

Uma mudança deve:

- resolver um problema identificável ou ampliar uma capacidade declarada;
- preservar `REGRA_INTEGRIDADE.md` e `REGRA_VERSAO_UNICA.md`;
- incluir teste proporcional ao risco quando alterar comportamento;
- declarar limitações, dados e dependências externas;
- manter separados conhecimento implementado, experimento e hipótese;
- atualizar documentação e changelog quando afetar utilizadores.

Uma capacidade só é chamada de implementada quando possui código, teste,
documentação, casos extremos relevantes, rastreabilidade e limites claros.

## Conhecimento e hipóteses

Contribuições científicas devem indicar dependências, método de construção,
casos testados e formas de falsificação. Citação ou resultado de biblioteca
externa pode validar e comparar, mas não substitui a construção PSF.

Hipóteses permanecem identificadas como hipóteses até prova adequada. Uma
divergência confirmada deve ser registada; não deve ser apagada para proteger
uma conclusão desejada.

## Decisões e conflitos

Decisões relevantes devem ficar no pull request, issue, changelog ou plano,
com justificativa verificável. Em conflito técnico, prevalecem nesta ordem:

1. segurança e proteção de dados;
2. integridade e evidência reproduzível;
3. coerência arquitetural e compatibilidade;
4. simplicidade de manutenção;
5. preferência pessoal.

O mantenedor declara a decisão final e pode reabri-la diante de nova evidência.
Conflitos de conduta seguem `CODE_OF_CONDUCT.md`; vulnerabilidades seguem
`SECURITY.md`.

## Releases

Uma release exige commit identificado, integridade aprovada, testes completos,
limitações atuais e changelog. Falha conhecida relevante não deve ser ocultada;
ela bloqueia a release ou aparece explicitamente nas notas, conforme o risco.

## Evolução da governança

Se o projeto ganhar mantenedores ou uso externo recorrente, esta política deve
passar a definir papéis, quórum, revisão mínima, transferência de manutenção e
processo de recurso. Hoje, alegar essa estrutura seria fingir uma comunidade
que ainda não existe.

