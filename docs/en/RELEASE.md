# Release candidate: v0.1.0 — Public Research Preview

Status: **release candidate; not yet published on GitHub**.

This is an English version of the canonical Portuguese
[release-candidate notes](../RELEASE.md). This first public version presents
PSF-IAminy as a scientific and experimental project for traceable construction
of Mathematics and Portuguese knowledge. It does not claim general
completeness and does not replace independent validation.

## Included in the candidate

- a Mathematics engine for finite rational operations, division
  reconstruction and a finite logical proof fragment;
- a Portuguese engine with an internal lexicon, morphological analysis and
  spelling correction within documented limits;
- a common engine for memory, dependencies, audit and traceability;
- the public demonstration and three separate examples;
- a local interface, with no outbound network calls by the main package in the
  audited state;
- installation through `pip install -e .`, with `psf-iaminy` and
  `python -m psf_iaminy` entry points.

## Candidate validation state

The documented local preparation checks report:

```text
python3 verificar_integridade.py -> PASSED
python3 exemplo_publico.py        -> executed with real engine output
python3 -m pytest -q              -> current local suite passed
line coverage                     -> documented snapshot available
```

The coverage snapshot and its limits are recorded in the Portuguese
[coverage report](../COBERTURA.md). No changing local test count or duration is
fixed in this translation.

The CI workflow targets Python 3.10, 3.11, 3.12 and 3.13. Public GitHub Actions
[run 29505936596](https://github.com/Progaminy/PSF-IAminy-Open/actions/runs/29505936596)
failed, and there has not yet been a green public run. Therefore the public-CI
release gate remains unsatisfied; local success must not be described as green
public CI.

## Minimal demonstration

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python exemplo_publico.py
python -m pytest -q
```

On Windows, activate the environment with `.venv\Scripts\activate`. The English
[demonstration guide](DEMO.md) explains the live output and its limitations.

## Main limitations

- Mathematics operates over the finite and rational domains already
  constructed; there is no claim of completeness over the real numbers.
- Portuguese automation is partial and limited to internal knowledge and the
  internal lexicon.
- The authorial primality hypothesis remains experimental and is not
  integrated as knowledge.
- The documented coverage snapshot leaves modules and paths without automated
  exercise.
- Systematic external validation, unrelated third-party reproduction and a
  guarantee for critical use are not established.
- The canonical conversation base is empty by documented decision, so chat is
  more limited while that base is rebuilt through PSF materialisation.

## Entry documents

- [Portuguese README](../../README.md): presentation, capabilities and limits;
- [English README](../../README.en.md): English public overview;
- [execution guide](../../COMO_RODAR.md): detailed execution in Portuguese;
- [public example](../../exemplo_publico.py) and the
  [examples directory](../../exemplos/): live demonstrations;
- [English architecture](ARCHITECTURE.md): components and flow;
- [scientific note](../NOTA_CIENTIFICA.md): method, results and falsification;
- [security audit](../AUDITORIA_SEGURANCA.md) and
  [data policy](../POLITICA_DADOS.md): security and data;
- [changelog](../../CHANGELOG.md): included changes.

## Before publishing the tag

1. Fix the CI failure and obtain a green public run on the candidate commit.
2. Repeat integrity, demonstration and the complete suite on that commit.
3. Move applicable changes from `Unreleased` to `0.1.0` in the changelog.
4. Create the annotated `v0.1.0` tag and publish these notes without freezing
   stale metrics.
5. Verify installation from the tag in a clean environment. The candidate tree
   passed a pre-tag clean-environment check documented in the Portuguese
   [reproduction report](../REPRODUCAO.md), but the published tag must still be
   checked itself.
