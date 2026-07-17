# Security policy

This is an English translation of the canonical Portuguese
[security policy](../../SECURITY.md). Security, scientific integrity and data
protection are part of PSF-IAminy-Open's principles.

For the current technical evidence and local-data rules, also read the
Portuguese [security audit](../AUDITORIA_SEGURANCA.md) and
[data policy](../POLITICA_DADOS.md). Those documents remain the source of truth
until their translations are maintained alongside them.

## Supported versions

Only the latest version available on the `main` branch currently receives
security fixes.

## Reporting a vulnerability

Do not publish serious vulnerabilities in public issues before giving the
maintainer an opportunity to analyse and fix them.

To report a vulnerability responsibly:

1. Open this repository's **Security** tab.
2. Look for **Report a vulnerability**.
3. Describe the problem, affected files and a safe way to reproduce it.
4. Do not include passwords, tokens, keys, personal data or private documents.

If private reporting is not available, open an issue containing only a general
description. Do not reveal details that would make the vulnerability
exploitable.

## Useful report information

Include, when possible:

- a clear description of the problem;
- the affected component or file;
- minimal reproduction steps;
- expected behaviour;
- observed behaviour;
- possible impact;
- Python and operating-system versions;
- a proposed fix, if one is available.

## Sensitive content

Never publish any of the following in the repository:

- passwords;
- access tokens;
- API keys;
- GitHub credentials;
- personal data;
- private conversations;
- confidential documents;
- files from the private PSF edition;
- content from the original private directory;
- local paths that reveal personal information.

## External dependencies

External dependencies used for comparison, validation or optimisation must be
reviewed before integration. Unknown, abandoned or unnecessary dependencies
must not be added without a risk analysis.

## Scientific integrity

The following are also integrity problems:

- presenting nonexistent capabilities as complete;
- hiding failures by removing tests;
- turning hypotheses into validated knowledge without evidence;
- tampering with test or evaluation results;
- removing traceability to hide the origin of a conclusion;
- introducing external dependencies as a hidden foundation of PSF knowledge.

## Remediation process

After receiving a report, the maintainer may:

1. confirm the problem;
2. assess its impact;
3. prepare a fix;
4. add regression tests;
5. publish the fix;
6. credit the reporter if they consent.

No specific remediation time is guaranteed because the project is maintained
independently.

## Responsible use

PSF-IAminy-Open is a scientific and experimental project. Independently verify
important results before using them in critical contexts.
