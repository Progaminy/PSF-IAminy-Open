# OpenAI Build Week 2026 — scope and verification

[Português](#resumo-em-português) · English

This document makes the challenge work auditable. It distinguishes the
pre-existing research project from the public engineering work performed during
OpenAI Build Week and explains how Codex and GPT-5.6 were used.

## Project submitted

- **Project:** PSF-IAminy
- **Public repository:** <https://github.com/Progaminy/PSF-IAminy-Open>
- **Public Devpost page:** <https://devpost.com/software/psf-iaminy>
- **Maintainer:** Pensador Sem Fronteiras (`Progaminy` on GitHub)
- **License:** Apache-2.0

The Devpost submission and the separate Codex for Open Source application use
the same public repository. They are independent programs: the first evaluates
a Build Week project, while the second evaluates an actively maintained
open-source repository.

## Scope before the challenge

PSF-IAminy existed as an ongoing private/internal research effort before the
public Build Week repository. Its prior foundation included the PSF integrity
principle ("Never pretend"), mathematical and Portuguese knowledge material,
and the separation between internal knowledge construction and external
validation.

The challenge claim is **not** that the entire research system was invented in
one week. The claim is that the public, testable and reviewable open-source
edition was created and substantially expanded during the challenge period.

## Work performed during Build Week

The Git history records the public engineering work. Key checkpoints include:

| Date (2026) | Commit | Verifiable work |
| --- | --- | --- |
| July 16 | `4d94c1d` | Initial publication of the open-source edition |
| July 16 | `a1bfc7a`–`5190416` | License, contribution guide and security policy |
| July 16 | `46fd0ce`–`e74740e` | Public architecture, CI, runnable demos, packaging and CLI |
| July 17–18 | `2692a86`–`06259f0` | Security corrections, validation, reproducibility, wheel resources and public-readiness audits |
| July 20 | `e3dc950` | Portuguese lexicon expansion and domain routing |
| July 20 | `3d98e89` | Reconstructed square-root engine and integration into hypotenuse and distance responses |
| July 20–21 | current candidate | Build Week evidence, bilingual documentation consistency and final verification |

Use `git show <commit>` or the repository history to inspect each checkpoint.

## How Codex and GPT-5.6 were used

Codex using GPT-5.6 acted as a development and review tool. It supported:

1. auditing a large codebase and locating inconsistencies across code, tests and documentation;
2. proposing and implementing focused patches under maintainer review;
3. designing regression tests for mathematical, linguistic, interface, packaging and security behaviour;
4. investigating CI, Python-version and runtime failures;
5. improving packaging, installation, CLI and clean-environment reproduction;
6. reviewing security boundaries and converting discovered defects into regression tests;
7. preparing bilingual documentation, runnable examples and submission material.

The maintainer retained final authority over architecture, mathematical and
linguistic claims, accepted changes and releases. Codex/GPT-5.6 is not required
to run the project and is not treated as an internal source of PSF knowledge.
External tools may compare, validate or optimise; they may not silently replace
the project's own knowledge construction.

## Reproduce the current evidence

```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m pytest --collect-only -q
python -m pytest -q
python exemplo_publico.py
python verificar_integridade.py
```

The current tree collects **1,223 tests**. Test count is evidence of exercised
behaviour, not proof of scientific completeness. The repository separately
documents coverage, finite evaluations, known false positives, operational
limits and unverified external adoption.

## Submission-specific evidence

- The public Devpost entry links this repository and a public demo video.
- The demo must remain under three minutes and include audio explaining both
  the working project and the use of Codex/GPT-5.6.
- The required `/feedback` Codex session ID belongs in the private Devpost
  submission field and is intentionally not copied into this public repository.
- No API key, temporary verification code or private conversation is required
  to run the public project.

## Resumo em Português

O PSF-IAminy já existia como investigação interna antes do concurso. Durante o
OpenAI Build Week foi criada e ampliada a edição pública, testável e auditável:
repositório aberto, licença, CI, demonstrações, empacotamento, segurança,
documentação, expansão de Português, roteamento por domínio e reconstrução de
raiz quadrada.

Codex com GPT-5.6 foi usado como ferramenta de engenharia para auditoria,
implementação, revisão, testes, depuração, empacotamento, segurança e
preparação da demonstração. As decisões finais permaneceram com o mantenedor.
O modelo externo não é fundamento do conhecimento PSF nem dependência de
execução.

A candidatura ao Codex for Open Source e a submissão ao OpenAI Build Week são
processos diferentes e podem referenciar o mesmo repositório público.
