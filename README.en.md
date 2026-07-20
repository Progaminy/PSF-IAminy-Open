# PSF-IAminy

[Português](README.md) · English

[![CI](https://github.com/Progaminy/PSF-IAminy-Open/actions/workflows/ci.yml/badge.svg)](https://github.com/Progaminy/PSF-IAminy-Open/actions/workflows/ci.yml)

PSF-IAminy is an experimental, local-first research system that constructs
traceable knowledge in Mathematics and Portuguese from explicit prior
dependencies. PSF stands for *Pensador Sem Fronteiras* (“Thinker Without
Borders”).

The Portuguese [README](README.md) is the canonical and most detailed project
description. This English document covers the public entry points, evidence
and limitations needed to evaluate and reproduce the current preview.

## OpenAI Build Week 2026

**PSF-IAminy** was submitted to [OpenAI Build Week](https://openai.devpost.com/)
as an open-source project. The public repository edition was created and
expanded during the challenge period with **Codex using GPT-5.6**.

Codex and GPT-5.6 supported codebase auditing, implementation and review,
regression-test design, debugging, packaging, documentation, security work and
demo preparation. The maintainer decided which changes to accept, ran the
checks and preserved the project's core boundary: external models may assist
development, comparison and validation, but they are neither the source of
PSF-IAminy's internal knowledge nor a runtime dependency.

The pre-existing scope, Build Week work, commit timeline and verification
commands are documented in
[`docs/OPENAI_BUILD_WEEK.md`](docs/OPENAI_BUILD_WEEK.md).

## The problem

Systems may return polished answers without showing how they were constructed
or what they do not know. PSF-IAminy studies the opposite discipline: a result
must retain a path to earlier knowledge, and a missing path must remain a gap,
hypothesis or operational limit rather than being presented as knowledge.

External libraries may compare, validate or optimise results. They may not be
the hidden foundation of pure PSF knowledge. The governing rule is simple:
**never pretend**.

## What works today

- **Mathematics:** finite rational expression evaluation, precedence,
  reconstructed division (quotient, remainder, exact fraction and decimal),
  and formal proof in an implemented finite logical fragment.
- **Portuguese:** an internal lexicon, morphological analysis, spelling
  suggestions and a traceable concept graph. Several linguistic operations
  remain partial or vocabulary-bound.
- **Common engine:** memory, dependency search, auditing, purity checks and
  traceability shared without merging mathematical and linguistic authority.
- **Evidence:** 1,223 automated tests pass in the current local suite; the documented line
  coverage snapshot is 63%.

The CI workflow targets Python 3.10–3.13. Its first public
[run](https://github.com/Progaminy/PSF-IAminy-Open/actions/runs/29505936596)
failed because of an HTTP-test timeout on all four versions and a Python 3.10
`ast.TryStar` incompatibility. Local candidate fixes exist, but those versions
remain publicly unconfirmed until a new run is green.

## Quick start

```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python exemplo_publico.py
python -m pytest -q
```

On Windows, activate with `.venv\Scripts\activate`. The preferred installed
entry points are:

```bash
psf-iaminy
python -m psf_iaminy
```

The public demonstration prints real output from the engines, including a
recognized limitation. More focused examples are available in
`exemplos/matematica.py`, `exemplos/portugues.py` and
`exemplos/rastreabilidade.py`.

## Public-readiness evidence

The Portuguese canonical documents include a factual
[64-item readiness audit](docs/AUDITORIA_MELHORIAS_120.md) and a
[production-code structural audit](docs/QUALIDADE_CODIGO.md). The recording
script is kept locally by the maintainer, outside this public edition.
External users, stars, reproductions and contributions are never marked
complete without real third-party evidence.

## Architecture

```text
Input
  ↓
Intent and routing
  ↓
Common PSF services
  ├── Mathematics engine
  ├── Portuguese engine
  ├── Audit and purity checks
  ├── Traceability
  └── External validation (comparison only)
  ↓
Justified result or explicit limitation
```

See [Architecture](docs/en/ARCHITECTURE.md) for the current component-level
description.

## Verifiable capability sample

| Capability | Status | Evidence | Main limitation |
| --- | --- | --- | --- |
| Rational expression precedence | Implemented | `testes/test_motores_dominio_comum.py` | Non-negative rational domain |
| Reconstructed division | Implemented | `testes/test_motores_dominio_comum.py` | Division by zero is reconstructed as undefined |
| Finite formal proof fragment | Implemented | `testes/test_motores_dominio_comum.py` | Only the constructed finite fragment |
| Morphological segmentation | Partial | `testes/test_morfemas_afixais.py` | Internal lexicon and known roots |
| Spelling suggestions | Implemented within internal scope | `testes/test_corretor.py` | No external dictionary as foundation |
| Authorial primality idea | Experimental, not integrated | pending-state regression test | Not a proven primality method |

## Limitations

- The Mathematics engine does not claim completeness over real numbers.
- Functional support is not scale support: `20*20` completed in 0.215 s, while
  `99*99` exceeded a 10 s limit in the local boundary evaluation.
- Portuguese declares open frontiers and operational limits; concept presence
  does not imply complete automation.
- An initial eight-word linguistic sample produced four false-positive spelling
  suggestions (50% in that tiny sample, not a population estimate); suggestions
  remain advisory. See `docs/AVALIACAO_QUALIDADE.md`.
- 63% line coverage leaves modules and paths untested, and coverage is not a
  measure of scientific correctness.
- An initial seven-case mathematical comparison agreed with SymPy 1.14.0 in
  that sample; broad systematic and linguistic external validation remain pending.
- Reproduction by an unrelated third party and Windows/macOS validation are
  still pending.
- The canonical conversation base is intentionally empty, so chat behaviour
  is limited while it is rebuilt through PSF materialisation.
- The project is experimental and must not be relied upon without independent
  verification in critical contexts.

## Knowledge status

The repository keeps five statuses separate:

1. implemented knowledge — code, tests and a closed dependency bridge;
2. experiments — tested work that may still change;
3. hypotheses — authorial ideas awaiting proof or falsification;
4. open problems — declared questions without fabricated solutions;
5. external validation — comparison that never decides pure knowledge.

## Security and local data

The main package has no required third-party runtime dependency and makes no
outbound network request in the audited state. The local interface stores
conversation data on the user's machine. Read [Security](docs/en/SECURITY.md), the
[security audit](docs/AUDITORIA_SEGURANCA.md) and the
[data policy](docs/POLITICA_DADOS.md) before exposing the server beyond its
documented local use.

## Research and project documents

- [OpenAI Build Week scope and Codex/GPT-5.6 use](docs/OPENAI_BUILD_WEEK.md)
- [Scientific note](docs/NOTA_CIENTIFICA.md)
- [Architecture in English](docs/en/ARCHITECTURE.md)
- [Live demonstration guide in English](docs/en/DEMO.md)
- [Test coverage](docs/COBERTURA.md)
- [Test classification](docs/TESTES.md)
- [Performance baseline](docs/DESEMPENHO.md)
- [Mathematical and linguistic quality evaluation](docs/AVALIACAO_QUALIDADE.md)
- [External validation report](docs/VALIDACAO_EXTERNA.md)
- [Clean-environment reproduction](docs/REPRODUCAO.md)
- [Static analysis](docs/ANALISE_ESTATICA.md)
- [Operational limits](docs/LIMITES_OPERACIONAIS.md)
- [Compatibility](docs/COMPATIBILIDADE.md)
- [Dependencies](docs/DEPENDENCIAS.md)
- [Public roadmap in English](docs/en/ROADMAP.md)
- [Release candidate notes in English](docs/en/RELEASE.md)
- [Real screenshots and their provenance](docs/IMAGENS.md)
- [Governance](GOVERNANCE.md)
- [Contributing in English](CONTRIBUTING.en.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Citation metadata](CITATION.cff)

Most detailed documents currently remain in Portuguese. Translation must not
drift into a second source of truth; when documents disagree, the live code,
tests and canonical Portuguese documents must be reconciled explicitly.

## License and citation

The repository is licensed under Apache License 2.0. Citation metadata is in
`CITATION.cff`. Until a release with a persistent identifier exists, include
the repository URL and exact commit in research citations; do not infer a DOI
or peer-review status.
