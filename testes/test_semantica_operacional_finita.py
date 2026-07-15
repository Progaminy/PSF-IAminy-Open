import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import para_bool
from nucleo.semantica_operacional_finita import (
    ADD, LIT, MUL, LET, VAR, TERMO_FINITO, REGRA_REESCRITA_FINITA,
    CONFIGURACAO_OPERACIONAL_FINITA, REGRA_OPERACIONAL_FINITA,
    EXECUTAR_PASSOS_FINITOS, TERMINA_EM_ATE_FINITO,
    AVALIAR_EXPRESSAO_FINITA, FORMA_NORMAL_FINITA,
    CONFLUENCIA_POR_CATALOGO_FINITA, FECHAMENTO_SEMANTICA_OPERACIONAL_FINITA,
)

falhas=[]

def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)

def b(x): return para_bool(x)

def main():
    expr = LET("x", ADD(LIT(2), LIT(3)), MUL(VAR("x"), LIT(4)))
    ok("avalia let/add/mul", AVALIAR_EXPRESSAO_FINITA(expr), 20)

    regras = (REGRA_REESCRITA_FINITA(TERMO_FINITO("zero+", TERMO_FINITO("a")), TERMO_FINITO("a")),)
    termo = TERMO_FINITO("f", TERMO_FINITO("zero+", TERMO_FINITO("a")))
    ok("reescreve subtermo até forma normal", FORMA_NORMAL_FINITA(regras, termo, 5), TERMO_FINITO("f", TERMO_FINITO("a")))
    ok("confluência por catálogo finito", b(CONFLUENCIA_POR_CATALOGO_FINITA(regras, regras, (termo,), 5)), True)

    def cond(cfg): return cfg["estado"] != "fim" and cfg["combustivel"] > 0
    def acao(cfg):
        novo = dict(cfg)
        novo["combustivel"] -= 1
        novo["saida"] = cfg["saida"] + (cfg["combustivel"],)
        if novo["combustivel"] == 0:
            novo["estado"] = "fim"
        return novo
    cfg = CONFIGURACAO_OPERACIONAL_FINITA("inicio", combustivel=3)
    regra = REGRA_OPERACIONAL_FINITA("contar", cond, acao)
    traco = EXECUTAR_PASSOS_FINITOS((regra,), cfg, 10)
    ok("traço termina em quatro configurações", len(traco), 4)
    ok("termina em até limite", b(TERMINA_EM_ATE_FINITO((regra,), cfg, 10)), True)
    ok("fechamento", b(FECHAMENTO_SEMANTICA_OPERACIONAL_FINITA()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
