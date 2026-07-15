"""Testes do progresso de aluno por pacote (ensino/progresso.py).

Cobre a lacuna descrita no plano público: antes, não havia lugar nenhum
que guardasse se uma pessoa viu, entendeu ou praticou um pacote — só uma
lista solta de "concluídos" que o chamador tinha que montar sozinho.

Roda com: python3 testes/test_progresso_pacotes.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino import EstadoPacote, RegistroProgresso
from motor import MotorGeralIAMiny

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste de progresso de aluno por pacote")

    # em memória: nada é escrito em disco.
    registro = RegistroProgresso()
    ok("sem estado ainda", registro.estado("ana", "matematica", "MAT-000"), None)

    registro.marcar("ana", "matematica", "MAT-000", "visto")
    ok("marcado visto", registro.estado("ana", "matematica", "MAT-000"), EstadoPacote.VISTO)

    registro.marcar("ana", "matematica", "MAT-000", "entendido")
    ok("avança para entendido", registro.estado("ana", "matematica", "MAT-000"), EstadoPacote.ENTENDIDO)

    registro.marcar("ana", "matematica", "MAT-000", "visto")
    ok("não regride ao marcar visto de novo", registro.estado("ana", "matematica", "MAT-000"), EstadoPacote.ENTENDIDO)

    registro.marcar("ana", "matematica", "MAT-000", EstadoPacote.PRATICADO)
    ok("chega a praticado", registro.estado("ana", "matematica", "MAT-000"), EstadoPacote.PRATICADO)

    registro.marcar("ana", "matematica", "MAT-001", "visto")
    ok("concluidos so conta praticado por padrao", registro.concluidos("ana", "matematica"), ("MAT-000",))
    ok(
        "concluidos aceita minimo mais baixo",
        set(registro.concluidos("ana", "matematica", "visto")),
        {"MAT-000", "MAT-001"},
    )

    ok("pessoas nao se misturam", registro.estado("beto", "matematica", "MAT-000"), None)
    ok("areas nao se misturam", registro.estado("ana", "portugues", "MAT-000"), None)

    resumo = registro.resumo("ana", "matematica")
    ok("resumo tem os dois pacotes", set(resumo), {"MAT-000", "MAT-001"})
    ok("resumo reflete estado certo", resumo["MAT-001"], EstadoPacote.VISTO)

    # persistência: o mesmo caminho, reaberto, tem que lembrar o progresso.
    caminho = Path(tempfile.mktemp(suffix=".json"))
    try:
        primeiro = RegistroProgresso(caminho)
        primeiro.marcar("ana", "matematica", "MAT-000", "praticado")

        segundo = RegistroProgresso(caminho)
        ok("progresso persiste entre instancias", segundo.estado("ana", "matematica", "MAT-000"), EstadoPacote.PRATICADO)
    finally:
        if caminho.exists():
            caminho.unlink()

    # integração com o motor geral: próxima aula deve pular o que já foi
    # praticado e devolver o próximo pacote da fila.
    geral = MotorGeralIAMiny()
    geral.marcar_progresso("carla", "matematica", "MAT-000", "praticado")
    proxima = geral.proxima_aula_aluno("carla", "matematica")
    ok("proxima aula do aluno pula o praticado", proxima.pacote.codigo, "MAT-001")

    ok("resumo_progresso do motor geral", geral.resumo_progresso("carla", "matematica")["MAT-000"], EstadoPacote.PRATICADO)

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
