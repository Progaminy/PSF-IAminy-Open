import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino import FormatoAula, MotorAulas
from motor import MotorGeralIAMiny


falhas = []


def ok(nome, obtido, esperado):
    print(("[OK]" if obtido == esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido != esperado:
        falhas.append(nome)


def main():
    aulas = MotorAulas()

    ok("areas", aulas.areas(), ("matematica", "portugues"))
    ok("primeiro pacote matematica", aulas.curriculo("matemática")[0].codigo, "MAT-000")
    ok("primeiro pacote portugues", aulas.curriculo("português")[0].codigo, "POR-000")
    ok("proximo respeita concluidos", aulas.proximo("matematica", {"MAT-000"}).codigo, "MAT-001")

    # currículo de matemática cresceu além dos 10 pacotes iniciais (MAT-000..009):
    # dezena, reagrupamento, multiplicação, tabuada, divisão, metade/dobro.
    codigos_matematica = [p.codigo for p in aulas.curriculo("matematica")]
    ok("matematica tem mais de dez pacotes agora", len(codigos_matematica) > 10, True)
    ok("matematica chega a MAT-017", "MAT-017" in codigos_matematica, True)
    ok("MAT-010 segue MAT-009", aulas.pacote("matematica", "MAT-010").pre_requisitos, ("MAT-009",))
    ok("MAT-014 introduz multiplicacao", "multiplicar" in aulas.pacote("matematica", "MAT-014").palavras_chave, True)

    # currículo de português cresceu na mesma medida (POR-000..009 -> ..017):
    # sílaba tônica, classes de palavras, concordância, tempos verbais,
    # sinônimos/antônimos, parágrafo, diálogo, pontuação.
    codigos_portugues = [p.codigo for p in aulas.curriculo("portugues")]
    ok("portugues tem mais de dez pacotes agora", len(codigos_portugues) > 10, True)
    ok("portugues chega a POR-017", "POR-017" in codigos_portugues, True)
    ok("POR-011 introduz classes de palavras", "substantivo" in aulas.pacote("portugues", "POR-011").palavras_chave, True)

    curta = aulas.gerar("matematica", "MAT-000", 1)
    ok("formato curto", curta.formato, FormatoAula.CURTA)
    ok("curto sem secao explicacao", "Ideia" in curta.texto, False)
    ok("curto tem passos", "Olhe." in curta.texto, True)

    explicada = aulas.gerar("matematica", "MAT-000", 2)
    ok("explicada tem ideia", "Ideia" in explicada.texto, True)
    ok("explicada sem exemplo", "Exemplo" in explicada.texto, False)

    com_exemplo = aulas.gerar("portugues", "POR-000", "exemplo")
    ok("com exemplo", "Exemplo" in com_exemplo.texto, True)
    ok("exemplo portugues som", "/a/" in com_exemplo.texto, True)

    com_exercicios = aulas.gerar("portugues", "POR-008", 4)
    ok("com exercicios", "Exercícios" in com_exercicios.texto, True)
    ok("oracao tem sujeito", "sujeito" in com_exercicios.texto, True)

    desmontada = aulas.gerar("matematica", "MAT-004", "detalhada")
    ok("desmontada formato", desmontada.formato, FormatoAula.DESMONTADA)
    ok("desmontada tem pre requisitos", "Pré-requisitos" in desmontada.texto, True)
    ok("desmontada tem desmontagem", "Desmontagem" in desmontada.texto, True)
    ok("desmontada tem avaliacao", "Como saber que entendeu" in desmontada.texto, True)

    geral = MotorGeralIAMiny()
    ok("motor geral nome", geral.nome, "PSF-IAminy")
    ok("motor geral mapa", geral.mapa_aulas("matematica")[0], "MAT-000 — Nada e alguma coisa")
    ok("motor geral aula", geral.aula("portugues", "POR-005", 3).pacote.titulo, "Palavra")
    ok("motor geral plano visivel", "Plano único do PSF-IAminy" in geral.plano_visivel(), True)
    ok("motor geral regra versao unica", "sobreposição de verdades" in geral.regra_versao_unica(), True)
    ok("motor geral identidade pasta", geral.identidade()["pasta"], "PSF-IAminy")
    ok("motor geral portugues", geral.fluxo_portugues("A palavra é bonita.").oracoes[0].verbo, "é")
    ok("motor geral melhorias", "matematica" in geral.melhorias(), True)

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
