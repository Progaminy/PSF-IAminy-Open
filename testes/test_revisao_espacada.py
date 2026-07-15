"""Testes da revisão espaçada por pacote (ensino/revisao.py).

Cobre a lacuna descrita no plano público: antes, nada decidia quando um
pacote já visto precisava reaparecer, nem marcava pacotes fracos para
voltar automaticamente. A agenda é contada em sessões de estudo (inteiros),
não em relógio real, então os testes são determinísticos.

Roda com: python3 testes/test_revisao_espacada.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino import RegistroRevisao
from motor import MotorGeralIAMiny

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste de revisão espaçada")

    registro = RegistroRevisao()
    ok("sem estado antes da primeira revisão", registro.estado("ana", "matematica", "MAT-000"), None)

    r1 = registro.registrar("ana", "matematica", "MAT-000", acertou=True, sessao_atual=1)
    ok("primeiro acerto vai ao degrau 0", r1.degrau, 0)
    ok("primeiro acerto agenda +1 sessão", r1.proxima_sessao, 2)
    ok("primeiro acerto não é fraco", r1.fraco, False)

    r2 = registro.registrar("ana", "matematica", "MAT-000", acertou=True, sessao_atual=2)
    ok("segundo acerto sobe degrau", r2.degrau, 1)
    ok("segundo acerto agenda +2 sessões", r2.proxima_sessao, 4)

    r3 = registro.registrar("ana", "matematica", "MAT-000", acertou=False, sessao_atual=4)
    ok("erro derruba ao degrau 0", r3.degrau, 0)
    ok("erro agenda revisão já na sessão seguinte", r3.proxima_sessao, 5)
    ok("erro marca como fraco", r3.fraco, True)

    ok("nada pendente antes da sessão vencer", registro.pendentes("ana", "matematica", 4), ())
    ok("pendente aparece na sessão vencida", registro.pendentes("ana", "matematica", 5), ("MAT-000",))
    ok("fracos lista o pacote que errou", registro.fracos("ana", "matematica"), ("MAT-000",))

    # um segundo pacote, sem erro, não deve aparecer como fraco.
    registro.registrar("ana", "matematica", "MAT-001", acertou=True, sessao_atual=5)
    ok("pacote sem erro nao entra em fracos", registro.fracos("ana", "matematica"), ("MAT-000",))
    ok(
        "pendentes ordena o mais vencido primeiro (MAT-000 vence na sessão 5, MAT-001 na 6)",
        registro.pendentes("ana", "matematica", 6),
        ("MAT-000", "MAT-001"),
    )

    ok("pessoas nao se misturam", registro.estado("beto", "matematica", "MAT-000"), None)

    # persistência: reabrir o mesmo caminho tem que lembrar a agenda.
    caminho = Path(tempfile.mktemp(suffix=".json"))
    try:
        primeiro = RegistroRevisao(caminho)
        primeiro.registrar("ana", "matematica", "MAT-000", acertou=False, sessao_atual=1)

        segundo = RegistroRevisao(caminho)
        estado = segundo.estado("ana", "matematica", "MAT-000")
        ok("revisao persiste entre instancias", estado.fraco, True)
    finally:
        if caminho.exists():
            caminho.unlink()

    # integração com o motor geral: pacote fraco tem prioridade sobre pacote novo.
    geral = MotorGeralIAMiny()
    geral.marcar_progresso("carla", "matematica", "MAT-000", "praticado")
    geral.registrar_revisao("carla", "matematica", "MAT-000", acertou=False, sessao_atual=1)

    tipo, aula = geral.proxima_atividade_aluno("carla", "matematica", sessao_atual=2)
    ok("prioriza revisao do pacote fraco", tipo, "revisao")
    ok("revisao aponta para o pacote fraco", aula.pacote.codigo, "MAT-000")

    # ao acertar a revisão, o intervalo cresce e o pacote some da lista de
    # pendentes por um tempo — só então o motor cai para um pacote novo.
    geral.registrar_revisao("carla", "matematica", "MAT-000", acertou=True, sessao_atual=2)
    tipo2, aula2 = geral.proxima_atividade_aluno("carla", "matematica", sessao_atual=3)
    ok("sem pendentes oferece pacote novo", tipo2, "novo")
    ok("pacote novo é o seguinte da fila", aula2.pacote.codigo, "MAT-001")

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
