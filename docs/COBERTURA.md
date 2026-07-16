# Cobertura de testes

Medição real, gerada localmente com `pytest-cov` (config em `.coveragerc`, que exclui `cao_de_caca/` — subprojeto externo com sua própria suíte — e a própria pasta `testes/`):

```bash
pip install pytest-cov
python3 -m pytest -q --cov --cov-report=term-missing
```

## Resultado desta medição

```text
TOTAL: 14771 statements, 5455 não cobertos, 63% de cobertura
```

Isto é uma fotografia, não um número travado: cresce e varia a cada mudança real de código/teste. O CI (`.github/workflows/ci.yml`) roda a mesma medição a cada push/PR (job `testes`, Python 3.12) e publica `coverage.xml` como artefacto — não há badge de percentual fixo no README de propósito, para não repetir o mesmo tipo de número desatualizado que motivou a correção de `COMO_RODAR.md`.

## Módulos com 0% de cobertura nesta medição

Dois grupos diferentes, por motivos diferentes:

**Entradas de linha de comando** (esperado — só rodam via `if __name__ == "__main__"`, não são importadas pelos testes):
```text
main.py
psf.py
psf_chat.py
motor_iaminy.py
```

**Módulos sem nenhum teste próprio** (lacuna real, não uma limitação estrutural):
```text
ensino/aula_humana.py
ensino/execucao_em_lote.py
ensino/resolver_anexo.py
motor/desempenho.py
motor/fronteira.py
motor/intencoes.py
nucleo/autoidentidade_confianca.py
nucleo/cobertura_total_abertos.py
nucleo/laboratorio_cientifico.py
nucleo/modo_cientista.py
nucleo/roteador.py
nucleo/roteador_base_curiosidades.py
```

Nenhum destes é conhecimento matemático ou linguístico puro (todos são camada de motor/ensino/roteamento, já listados como tal em `README.md`, seção "Rastreabilidade técnica do núcleo") — mas ficam registados aqui como lacuna real de teste, não escondidos.

## O que este número não diz

63% de linhas executadas não equivale a 63% de comportamento correto verificado — cobertura mede o que rodou, não o que foi verificado com asserção significativa. Ver item 18 do plano de melhorias públicas (`PLANO_PSF_IAMINY.md`) sobre classificar testes por profundidade, ainda não feito.
