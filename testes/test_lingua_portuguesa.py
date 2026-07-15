import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lingua_portuguesa import (
    ClasseGramatical,
    Dicionario,
    EntradaLexical,
    Genero,
    MotorPortugues,
    Numero,
)


falhas = []


def ok(nome, obtido, esperado):
    print(("[OK]" if obtido == esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido != esperado:
        falhas.append(nome)


def main():
    motor = MotorPortugues()

    analise = motor.analisar("As meninas estudam rapidamente.")
    ok("tokens", tuple(token.texto for token in analise.tokens), ("As", "meninas", "estudam", "rapidamente", "."))
    ok("classe determinante", analise.morfologia[0].principal.classe, ClasseGramatical.DETERMINANTE)
    ok("classe substantivo", analise.morfologia[1].principal.classe, ClasseGramatical.SUBSTANTIVO)
    ok("classe verbo", analise.morfologia[2].principal.classe, ClasseGramatical.VERBO)
    ok("classe adverbio", analise.morfologia[3].principal.classe, ClasseGramatical.ADVERBIO)
    ok("sem diagnosticos", analise.diagnosticos, ())
    ok(
        "constituintes",
        tuple((item.funcao, item.texto) for item in analise.constituintes),
        (("sujeito", "As meninas"), ("predicado", "estudam rapidamente")),
    )

    discordante = motor.analisar("As menina bonito.")
    ok(
        "diagnosticos concordancia",
        tuple(item.codigo for item in discordante.diagnosticos),
        ("CONCORDANCIA_DET_NOME", "CONCORDANCIA_NOME_ADJ"),
    )

    ok("definicao casa", motor.definir("casa"), ("Edifício destinado a habitação.",))
    ok("sugestao portugues", motor.sugerir("porgugues")[0], "português")

    dicionario = Dicionario.padrao()
    dicionario.adicionar(
        EntradaLexical(
            lema="zeta",
            forma="zeta",
            classe=ClasseGramatical.SUBSTANTIVO,
            definicoes=("Nome da letra z no alfabeto grego.",),
            genero=Genero.FEMININO,
            numero=Numero.SINGULAR,
        )
    )
    motor_extendido = MotorPortugues(dicionario=dicionario)
    analise_extendida = motor_extendido.analisar("A zeta é bonita.")
    ok("dicionario extensivel lema", analise_extendida.morfologia[1].principal.lema, "zeta")
    ok("dicionario extensivel definicao", motor_extendido.definir("zeta"), ("Nome da letra z no alfabeto grego.",))

    fluxo = motor.fluxo_natural("A língua portuguesa é excelente.")
    ok(
        "estagios fluxo",
        tuple(estagio.nome for estagio in fluxo.estagios),
        (
            "sons_isolados",
            "grafia",
            "combinacao",
            "palavras",
            "significado",
            "frases_oracoes",
            "texto_livro",
            "gramatica_aplicada",
        ),
    )
    ok("sons sem significado", all(not som.tem_significado for som in fluxo.sons), True)
    ok("grafema com acento", any(grafema.acento == "agudo" for grafema in fluxo.grafemas), True)
    ok("digrafo gu", any(item.tipo == "digrafo" and item.texto.casefold() == "gu" for item in fluxo.combinacoes), True)
    ok("palavra com significado", fluxo.palavras[1].lema, "língua")
    ok("definicao no fluxo", fluxo.palavras[1].definicoes[0].startswith("Sistema de comunicação"), True)
    ok("oracao com verbo", (len(fluxo.oracoes), fluxo.oracoes[0].verbo), (1, "é"))
    ok("explicar fluxo", motor.explicar_fluxo("A língua é natural.")[0].startswith("1. sons_isolados"), True)

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
