import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.formulas import resumo_auditoria_formulas, achados_modulo
from pathlib import Path
import tempfile


def test_detector_enxerga_operadores_prontos():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'m.py'
        p.write_text('def f(a,b):\n    return a // b, a % b\n', encoding='utf-8')
        valores=[a['valor'] for a in achados_modulo(p)]
        assert '//' in valores and '%' in valores


def test_resumo_tem_categorias_honestas():
    r=resumo_auditoria_formulas()
    assert 'suspeitos' in r and 'validacao_ou_legado' in r
