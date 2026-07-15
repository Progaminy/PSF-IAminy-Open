# PSF Calculadora

Calculadora de terminal em português com motores para aritmética, álgebra,
geometria, cálculo, estatística, otimização, sinais e outros domínios.

## Requisitos

- Python 3.10 ou superior;
- `pip` atualizado;
- ambiente virtual recomendado.

## Instalação completa

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[completo]'
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[completo]"
```

O extra `completo` instala todas as dependências científicas necessárias:
NumPy, SymPy, Pandas, Matplotlib, SciPy, NetworkX, mpmath e scikit-learn.
Como alternativa, use `python -m pip install -r requirements.txt`.

## Instalação mínima

```bash
python -m pip install -e .
```

A instalação mínima permite importar e usar os motores baseados apenas na
biblioteca padrão. Um recurso científico que dependa de pacote ausente informará
o erro sem impedir a inicialização dos motores básicos.

## Execução

```bash
psf-calculadora
# alternativas:
python -m psf_calculadora
python assistente_psf.py
```

Exemplos:

```text
calcule 2 + 3
múltiplos de 7
15% de 200
equacao 2x + 4 = 10
sair
```

## Desenvolvimento e testes

```bash
python -m pip install -e '.[completo,dev]'
python -m pytest
```

## Organização

- `assistente_psf.py`: implementação legada, mantida para compatibilidade;
- `psf_calculadora/`: API, terminal, dependências e registro;
- `psf_calculadora/dominios/`: catálogo modular por domínio;
- `tests/`: testes de fumaça e do despachante.

O registro avalia primeiro as intenções encontradas no pedido e usa a prioridade
original como desempate. Novos motores devem declarar nome, prioridade e termos
de intenção específicos.

Pontuação e os símbolos Unicode `÷`, `×` e `−` são normalizados antes da
seleção. Intenções explicitamente declaradas têm precedência sobre palavras
inferidas do nome da classe. O parser matemático geral participa do mesmo registro
e é consultado somente depois dos motores específicos e dos fallbacks básicos.

### Migração do legado

O despacho usa um índice invertido `intenção → motores`; somente os candidatos
encontrados são executados. Cada registro também informa suas dependências
opcionais antes da execução.

Os motores de adição/subtração, divisão e múltiplos já residem no módulo
independente `psf_calculadora.dominios.aritmetica`. Os demais continuam acessíveis
pela ponte de compatibilidade e podem ser migrados gradualmente, acompanhados de
testes, antes da remoção de `assistente_psf.py`.

## Mapa de conhecimento

O plano das aulas 361 a 1000 está em
[`docs/PLANO_MAPA_CONHECIMENTO_361_1000.md`](docs/PLANO_MAPA_CONHECIMENTO_361_1000.md).
O grafo completo e consumível por software está em
[`docs/mapa_conhecimento_361_1000.json`](docs/mapa_conhecimento_361_1000.json).

O mapa registra aulas, áreas, conceitos, motores, sequência didática e os estados
`TEMOS`, `PARCIAL` e `NÃO TEMOS`. Relações sem evidência não são criadas; itens
isolados permanecem documentados no plano.
