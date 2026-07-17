# Contributing to PSF-IAminy-Open

This is an English translation of the canonical Portuguese
[contribution guide](CONTRIBUTING.md).

Thank you for your interest in contributing to PSF-IAminy-Open. The project
investigates the traceable construction of mathematical and linguistic
knowledge through the PSF method. Every contribution must preserve the
system's coherence, transparency and verifiability.

## Before contributing

1. Read the canonical [README](README.md), the English
   [project overview](README.en.md), the
   [improvement plan](PLANO_PSF_IAMINY.md) and the
   [integrity rules](REGRA_INTEGRIDADE.md).
2. Check whether an issue already covers the problem or proposal.
3. For a large change, open an issue explaining the idea first.
4. Do not include private data, credentials, personal conversations, keys or
   temporary files.

## Mandatory principles

- Do not present nonexistent capabilities as complete.
- Clearly distinguish implemented knowledge, experiments, hypotheses and
  future work.
- Preserve the traceability of constructions and decisions.
- Do not introduce external dependencies as a hidden foundation of PSF
  knowledge.
- External dependencies may be used for comparison, validation or
  optimisation when that role is clearly identified.
- Do not remove tests or checks merely to hide a failure.
- Keep the responsibilities of the Mathematics engine, Portuguese engine and
  common core separate.
- Do not add private content, local conversations or files from the private
  edition to the public repository.

## Prepare the environment

Clone the repository:

```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
```

Run the tests:

```bash
python -m pytest
```

Run the integrity check:

```bash
python verificar_integridade.py
```

## Create a contribution

Create a new branch:

```bash
git checkout -b type/short-description
```

Examples:

```text
fix/euclidean-division
feature/morphological-analysis
documentation/how-to-run
test/primality-coverage
```

Keep changes small, coherent and verifiable.

## Tests

Whenever possible, every bug fix should include a test that:

- demonstrates the previous problem;
- confirms the corrected behaviour;
- does not depend on private data;
- can be run by other contributors.

Before submitting, run:

```bash
python -m pytest
python verificar_integridade.py
```

## Commits

Use clear, objective messages. Examples:

```text
Fix Euclidean division reconstruction
Add tests for verbal agreement
Document local interface execution
```

Avoid vague messages such as:

```text
changes
adjustments
new
test
```

## Pull requests

The pull-request description should identify:

- the problem addressed;
- the solution implemented;
- the main files changed;
- the tests run;
- known limitations;
- possible effects on other parts of the system.

Do not claim that a feature is complete while its implementation or tests are
still partial.

## Hypotheses and research

Mathematical, linguistic and computational hypotheses must be explicitly
labelled as hypotheses. A hypothesis must not be incorporated as validated
knowledge before analysis, attempts at falsification, comparison and
reproducible tests.

## Security

Do not publish:

- passwords;
- tokens;
- API keys;
- private addresses;
- personal data;
- confidential documents;
- files from the project's private edition.

If you discover a vulnerability or data exposure, do not disclose it publicly
before allowing responsible remediation. Follow the English
[security policy](docs/en/SECURITY.md).

## Licence

By submitting a contribution, you agree that it may be distributed under the
[Apache License 2.0](LICENSE) adopted by this repository.
