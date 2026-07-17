# Running the live demonstrations

The PSF-IAminy-Open demonstrations call the real project engines. Their output
is generated at runtime; it is not a recorded transcript, canned response or
mocked result. This guide was checked by running all four commands below from
the repository root.

The output may evolve with the internal knowledge and lexicon. Treat the
descriptions below as behavioural landmarks, not as a byte-for-byte output
snapshot.

## Prepare a local environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Public demonstration

Run [the public example](../../exemplo_publico.py):

```bash
python3 exemplo_publico.py
```

The script makes live calls that show:

- rational division of `12:5`, including an exact fraction and reconstruction
  steps;
- advisory Portuguese spelling suggestions for a sentence containing `nao`
  and `nda`;
- a real dependency path to the Portuguese concept `interpretação`;
- division by zero reported as undefined by construction instead of hidden
  behind a fabricated result;
- the authorial primality idea still labelled as a pending hypothesis rather
  than implemented knowledge.

The spelling suggestions are deliberately advisory. They can include false
positives: in the validated live run, the correctly spelled word `assunto`
also received a suggestion. The engine does not silently rewrite the sentence.

## Mathematics example

Run the deeper [Mathematics example](../../exemplos/matematica.py):

```bash
python3 exemplos/matematica.py
```

It exercises exact and repeating rational division, controlled decimal
precision, division by zero, operator precedence, a chained modus-ponens proof
and a separately labelled pending hypothesis. The proof is only a proof in the
implemented finite logical fragment; it is not a claim of general theorem-
proving completeness.

## Portuguese example

Run the deeper [Portuguese example](../../exemplos/portugues.py):

```bash
python3 exemplos/portugues.py
```

It shows advisory correction, lexicon-bound morphological segmentation and a
structural audit of the live Portuguese knowledge graph. A word may return no
segmentation when no proposed split has a confirmed internal root. That is an
explicit operational limit, not a forced analysis.

## Traceability example

Run the [traceability example](../../exemplos/rastreabilidade.py):

```bash
python3 exemplos/rastreabilidade.py
```

It asks the live system for Portuguese dependency paths and mathematical
knowledge dependencies, then runs checks for broken ETAPA file references,
broken Python imports in the core and disagreement between the documents that
state the local test-suite status.

A clean traceability result establishes that the checked references and
imports are internally resolvable. It does not, by itself, prove that every
scientific conclusion is correct or externally validated.

## What these demonstrations establish

Together, the scripts provide reproducible evidence that the documented entry
points reach real engines, preserve construction steps and expose selected
limits. They do not establish:

- mathematical completeness beyond the implemented finite and rational
  domains;
- complete Portuguese coverage beyond the internal knowledge and lexicon;
- population-level spelling quality from a few examples;
- independent third-party reproduction;
- fitness for critical use without independent verification.

For component boundaries see [Architecture](ARCHITECTURE.md). For measured
quality limitations see the Portuguese
[quality evaluation](../AVALIACAO_QUALIDADE.md) and
[operational-limits report](../LIMITES_OPERACIONAIS.md).
