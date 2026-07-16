# Release candidata: v0.1.0 — Public Research Preview

Estado: **candidata a release; ainda não publicada no GitHub**.

Esta primeira versão pública apresenta o PSF-IAminy como projeto científico e
experimental para construção rastreável de conhecimento de Matemática e
Português. Não afirma completude geral nem substitui validação independente.

## O que está incluído

- motor de Matemática com operações racionais finitas, reconstrução da divisão
  e fragmento de prova lógica finita;
- motor de Português com léxico interno, análise morfológica e correção
  ortográfica dentro dos limites documentados;
- motor comum de memória, dependências, auditoria e rastreabilidade;
- demonstração pública e três exemplos separados;
- interface local, sem chamadas de rede de saída pelo pacote principal;
- instalação por `pip install -e .` e entradas `psf-iaminy` e
  `python -m psf_iaminy`.

## Validação desta candidata

Em 17 de julho de 2026, no ambiente local de preparação:

```text
python3 verificar_integridade.py → APROVADO
python3 exemplo_publico.py        → executado com resultado real
python3 -m pytest -q              → 1084 passed em 81,06 s
cobertura de linhas               → 63% na medição documentada
```

O workflow de CI testa Python 3.10, 3.11, 3.12 e 3.13, mas esse resultado só
deve ser chamado de público depois de uma execução verde no GitHub Actions.

## Demonstração mínima

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python exemplo_publico.py
python -m pytest -q
```

No Windows, a ativação equivalente é `.venv\Scripts\activate`.

## Limitações principais

- Matemática opera sobre domínios finitos e racionais já construídos; não há
  alegação de completude sobre os números reais.
- A automação de Português é parcial e limitada ao conhecimento e léxico
  internos.
- A hipótese autoral de primalidade permanece experimental e não integrada.
- Cobertura de 63% deixa módulos e caminhos sem exercício automatizado.
- Ainda não existe validação externa sistemática, reprodução independente ou
  garantia para uso crítico.
- A base canónica de conversação está vazia por decisão documentada; o chat é
  mais limitado enquanto ela não for reconstruída por materialização PSF.

## Ficheiros de entrada

- `README.md`: apresentação, capacidades e limitações;
- `COMO_RODAR.md`: execução detalhada;
- `exemplo_publico.py` e `exemplos/`: demonstrações;
- `docs/ARQUITETURA.md`: componentes e fluxo;
- `docs/NOTA_CIENTIFICA.md`: método, resultados e falsificação;
- `docs/AUDITORIA_SEGURANCA.md` e `docs/POLITICA_DADOS.md`: segurança e dados;
- `CHANGELOG.md`: mudanças incluídas.

## Antes de publicar a tag

1. obter uma execução verde do CI no commit candidato;
2. repetir integridade, demonstração e suíte completa nesse commit;
3. mover as mudanças aplicáveis de `Não lançado` para `0.1.0` no changelog;
4. criar a tag anotada `v0.1.0` e publicar estas notas sem alterar métricas;
5. conferir instalação a partir da tag num ambiente limpo (a árvore candidata
   já passou antes da tag; ver `docs/REPRODUCAO.md`).
