"""PSF-IAminy — Computabilidade finita, Etapas 401 a 440.
Roda com: python3 testes/test_computabilidade_finita.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.metodos_finitos import DFA_FINITO, ACEITA_DFA_FINITO
from nucleo.computabilidade_finita import (
    ACEITA_MAQUINA_FITA_LIMITADA_FINITA,
    CLASSIFICAR_CATALOGO_FINITA,
    CODIGO_DA_MAQUINA_FINITA,
    COMPLEMENTO_PROBLEMA_FINITO,
    COMPOSICAO_FINITA,
    CONFIGURACAO_INICIAL_FINITA,
    CONTAGEM_MAQUINAS_POSSIVEIS_FINITA,
    DECIDIVEL_POR_DFA_FINITA,
    DECIDIVEL_POR_MAQUINA_FINITA,
    DECISAO_PARADA_FINITA,
    DETECCAO_CICLO_E_PARADA_FINITA,
    DFA_E_MAQUINA_CONCORDAM_FINITA,
    DFA_PARA_MAQUINA_FITA_LIMITADA_FINITA,
    ESPACO_CONFIGURACOES_FINITO,
    ESQUEMA_TOTAL_NO_DOMINIO_FINITO,
    EXECUTAR_MAQUINA_FITA_LIMITADA,
    FECHAMENTO_COMPUTABILIDADE_FINITA_401_440,
    FECHAMENTO_DECIDIBILIDADE_REDUCAO_FINITA,
    FECHAMENTO_FUNCOES_COMPUTAVEIS_FINITAS,
    FECHAMENTO_MAQUINA_FITA_LIMITADA_FINITA,
    FUNCAO_COMPUTADA_POR_MAQUINA_FINITA,
    FUNCAO_PROJECAO_FINITA,
    FUNCAO_SUCESSOR_FINITA,
    FUNCAO_ZERO_FINITA,
    INTERSECAO_PROBLEMAS_FINITA,
    LINGUAGEM_ACEITA_MAQUINA_FINITA,
    MAQUINA_PALINDROMO_FINITA,
    MAQUINA_PARCIAL_FINITA,
    MAQUINA_SUCESSOR_UNARIO_FINITA,
    MAQUINA_UNIVERSAL_FINITA,
    NAO_E_UTM_CLASSICA_FINITA,
    PALINDROMO_POR_LEITURA_FINITA,
    PALINDROMO_POR_MAQUINA_FINITA,
    PASSO_MAQUINA_FINITA,
    PROBLEMA_DECISAO_FINITO,
    RECURSAO_PRIMITIVA_LIMITADA_FINITA,
    REDUCAO_FINITA,
    REDUCAO_PRESERVA_DECISAO_FINITA,
    RESOLVER_PROBLEMA_DECISAO_FINITO,
    SINTESE_COMPUTABILIDADE_FINITA_401_440,
    SUCESSOR_UNARIO_COMPUTADO_FINITA,
    TODO_PROBLEMA_FINITO_E_DECIDIVEL,
    UNIAO_PROBLEMAS_FINITA,
    UNIVERSAL_CONCORDA_COM_EXECUCAO_DIRETA_FINITA,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def b(valor):
    return para_bool(valor)


def verificar_pureza():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "computabilidade_finita.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em computabilidade_finita.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def main():
    print("PSF-IAminy — Computabilidade finita, Etapas 401 a 440")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 440", r["maior_etapa"] >= 440, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    # --- Etapas 401-405: modelo de máquina de fita limitada ---
    maquina_suc = MAQUINA_SUCESSOR_UNARIO_FINITA(8)
    config0 = CONFIGURACAO_INICIAL_FINITA(maquina_suc, ("1", "1", "1"))
    verificar("configuração inicial começa na posição 0", config0[3], 0)
    verificar("configuração inicial preenche o resto com branco", config0[2], ("1", "1", "1", "_", "_", "_", "_", "_"))
    config1 = PASSO_MAQUINA_FINITA(maquina_suc, config0)
    verificar("um passo de transição avança a posição (move D)", config1[3], 1)
    resultado, config_final = EXECUTAR_MAQUINA_FITA_LIMITADA(maquina_suc, ("1", "1", "1"), 20)
    verificar("máquina sucessora unária aceita e para dentro do limite", resultado, "aceita")

    entrada_grande = ("1",) * 20
    try:
        CONFIGURACAO_INICIAL_FINITA(maquina_suc, entrada_grande)
        verificar("entrada maior que a fita declarada é rejeitada por exceção", False, True)
    except ValueError:
        verificar("entrada maior que a fita declarada é rejeitada por exceção", True, True)

    # --- Etapa 406-408: espaço de configurações finito e decidibilidade da parada ---
    espaco = ESPACO_CONFIGURACOES_FINITO(maquina_suc)
    verificar("espaço de configurações é positivo e finito (int)", isinstance(espaco, int) and espaco > 0, True)
    resultado_ciclo, _ = DETECCAO_CICLO_E_PARADA_FINITA(maquina_suc, ("1", "1"))
    verificar("máquina sucessora para (não entra em loop)", resultado_ciclo, "para_aceita")
    verificar("decisão de parada confirma que a máquina sucessora para", b(DECISAO_PARADA_FINITA(maquina_suc, ("1", "1"))), True)

    maquina_parcial = MAQUINA_PARCIAL_FINITA(6)
    verificar("máquina parcial PARA na entrada ('1',) (aceita de imediato)", b(DECISAO_PARADA_FINITA(maquina_parcial, ("1",))), True)
    resultado_loop, _ = DETECCAO_CICLO_E_PARADA_FINITA(maquina_parcial, ("0", "0", "0", "0", "0", "0"))
    verificar("máquina parcial ENTRA EM LOOP em ('0'*6) — detectado, não escondido", resultado_loop, "loop_detectado")
    verificar("decisão de parada confirma corretamente que essa entrada NÃO para", b(DECISAO_PARADA_FINITA(maquina_parcial, ("0", "0", "0", "0", "0", "0"))), False)
    verificar("a decisão de parada nunca estoura o limite teórico (pombos correto)", resultado_loop != "limite_excedido_inesperado", True)

    # --- Etapa 409-410 ---
    verificar("máquina sucessora aceita ('1','1')", b(ACEITA_MAQUINA_FITA_LIMITADA_FINITA(maquina_suc, ("1", "1"), 20)), True)
    linguagem = LINGUAGEM_ACEITA_MAQUINA_FINITA(maquina_suc, (("1",), ("1", "1"), ()), 20)
    verificar("linguagem aceita pela máquina sucessora inclui todas as entradas testadas (sempre aceita, é total)", len(linguagem), 3)
    verificar("fechamento do modelo de máquina de fita limitada", b(FECHAMENTO_MAQUINA_FITA_LIMITADA_FINITA()), True)

    # --- Etapas 411-417: esquemas de recursão primitiva finita ---
    verificar("função zero ignora os argumentos", FUNCAO_ZERO_FINITA(5, 9, 1), 0)
    verificar("função sucessor finita", FUNCAO_SUCESSOR_FINITA(7), 8)
    projecao1 = FUNCAO_PROJECAO_FINITA(1)
    verificar("projeção finita devolve o argumento no índice pedido", projecao1(10, 20, 30), 20)
    composta = COMPOSICAO_FINITA(FUNCAO_SUCESSOR_FINITA, FUNCAO_PROJECAO_FINITA(0))
    verificar("composição de sucessor com projeção", composta(4, 99), 5)
    dobro = RECURSAO_PRIMITIVA_LIMITADA_FINITA(0, lambda n, anterior: anterior + 2, 5)
    verificar("recursão primitiva limitada calcula dobro(n)=2n para n em [0,5]", [dobro(n) for n in range(6)], [0, 2, 4, 6, 8, 10])
    try:
        dobro(6)
        verificar("recursão limitada rejeita fora do intervalo declarado", False, True)
    except ValueError:
        verificar("recursão limitada rejeita fora do intervalo declarado", True, True)
    verificar("esquemas 412-416 são totais no domínio de teste declarado", b(ESQUEMA_TOTAL_NO_DOMINIO_FINITO(FUNCAO_SUCESSOR_FINITA, range(10))), True)

    # --- Etapa 418: exemplo computado por máquina concreta, validado contra oráculo nativo ---
    for n in range(0, 6):
        obtido = SUCESSOR_UNARIO_COMPUTADO_FINITA(n, 10, 30)
        esperado = n + 1
        verificar(f"sucessor unário computado por máquina para n={n} bate com n+1 nativo", obtido, esperado)

    # --- Etapa 419: contraexemplo honesto — função parcial de fato ---
    saida_computavel = FUNCAO_COMPUTADA_POR_MAQUINA_FINITA(maquina_parcial, ("1",), 20)
    verificar("máquina parcial devolve saída definida numa entrada que para", saida_computavel is not None, True)
    saida_indefinida = FUNCAO_COMPUTADA_POR_MAQUINA_FINITA(maquina_parcial, ("0", "0", "0", "0", "0", "0"), 50)
    verificar("máquina parcial devolve None (indefinido) numa entrada que não para dentro do limite", saida_indefinida, None)

    # --- Etapa 420 ---
    verificar("fechamento das funções computáveis finitas", b(FECHAMENTO_FUNCOES_COMPUTAVEIS_FINITAS()), True)

    # --- Etapas 421-423: problemas de decisão finitos ---
    dominio_par = tuple(range(0, 10))
    problema_par = PROBLEMA_DECISAO_FINITO(dominio_par, lambda n: n % 2 == 0)
    verificar("problema de decisão finito resolve 4 como par", b(RESOLVER_PROBLEMA_DECISAO_FINITO(problema_par, 4)), True)
    verificar("problema de decisão finito resolve 7 como não-par", b(RESOLVER_PROBLEMA_DECISAO_FINITO(problema_par, 7)), False)

    dfa_ab = DFA_FINITO(
        estados=("s0", "s1", "lixo"),
        alfabeto=("a", "b"),
        transicao={
            ("s0", "a"): "s1", ("s0", "b"): "lixo",
            ("s1", "a"): "lixo", ("s1", "b"): "s0",
            ("lixo", "a"): "lixo", ("lixo", "b"): "lixo",
        },
        inicial="s0",
        finais=("s0",),
    )
    palavras_ab = (("a", "b"), ("a", "b", "a", "b"), ("a",), ("b",), ())
    verificar("DFA decide (reaproveitado) — sempre devolve resposta para toda palavra testada", b(DECIDIVEL_POR_DFA_FINITA(dfa_ab, palavras_ab)), True)

    maquina_dfa = DFA_PARA_MAQUINA_FITA_LIMITADA_FINITA(dfa_ab, 10)
    verificar("máquina de fita limitada traduzida do DFA decide a parada em todas as palavras testadas", b(DECIDIVEL_POR_MAQUINA_FINITA(maquina_dfa, palavras_ab)), True)

    # --- Etapas 424-425: redução finita ---
    problema_positivo = PROBLEMA_DECISAO_FINITO(range(-5, 6), lambda n: n > 0)
    instancias = tuple(range(-3, 4))
    reducao = REDUCAO_FINITA(instancias, lambda n: n + 10, problema_positivo)
    verificar("redução finita mapeia e resolve cada instância", len(reducao), len(instancias))
    problema_maior_que_5 = PROBLEMA_DECISAO_FINITO(range(0, 20), lambda n: n > 5)
    concorda = REDUCAO_PRESERVA_DECISAO_FINITA(instancias, lambda n: n + 5, problema_positivo, problema_maior_que_5)
    verificar("n>0 reduz para (n+5)>5 preservando a resposta (mesma condição, deslocada pelo mesmo tanto do limiar)", b(concorda), True)

    # --- Etapa 426: limite honesto ---
    verificar("todo problema sobre domínio finito é decidível por enumeração", b(TODO_PROBLEMA_FINITO_E_DECIDIVEL(problema_par)), True)

    # --- Etapas 427-428: fechamento sob complemento/união/interseção ---
    problema_impar = COMPLEMENTO_PROBLEMA_FINITO(problema_par)
    verificar("complemento de 'par' rejeita 4", b(RESOLVER_PROBLEMA_DECISAO_FINITO(problema_impar, 4)), False)
    verificar("complemento de 'par' aceita 7", b(RESOLVER_PROBLEMA_DECISAO_FINITO(problema_impar, 7)), True)
    problema_menor5 = PROBLEMA_DECISAO_FINITO(dominio_par, lambda n: n < 5)
    uniao = UNIAO_PROBLEMAS_FINITA(problema_par, problema_menor5)
    intersecao = INTERSECAO_PROBLEMAS_FINITA(problema_par, problema_menor5)
    verificar("união (par OU <5) aceita 3 (é <5, mesmo não sendo par)", b(RESOLVER_PROBLEMA_DECISAO_FINITO(uniao, 3)), True)
    verificar("interseção (par E <5) rejeita 7 (não é par)", b(RESOLVER_PROBLEMA_DECISAO_FINITO(intersecao, 7)), False)
    verificar("interseção (par E <5) aceita 2", b(RESOLVER_PROBLEMA_DECISAO_FINITO(intersecao, 2)), True)

    # --- Etapa 429 ---
    verificar("todo DFA tem máquina de fita limitada equivalente (traduzida) que concorda em todas as palavras testadas",
              b(DFA_E_MAQUINA_CONCORDAM_FINITA(dfa_ab, palavras_ab, 10, 30)), True)

    # --- Etapa 430 ---
    verificar("fechamento da decidibilidade e redução finita", b(FECHAMENTO_DECIDIBILIDADE_REDUCAO_FINITA()), True)

    # --- Etapas 431-434: máquina universal finita ---
    codigo = CODIGO_DA_MAQUINA_FINITA(maquina_suc)
    verificar("código de uma máquina é a própria estrutura de dados", codigo, maquina_suc)
    direto = EXECUTAR_MAQUINA_FITA_LIMITADA(maquina_suc, ("1", "1"), 20)
    universal = MAQUINA_UNIVERSAL_FINITA(codigo, ("1", "1"), 20)
    verificar("máquina universal finita concorda com a execução direta", universal, direto)
    catalogo_teste = (maquina_suc, maquina_parcial, maquina_dfa)
    entradas_teste = (("1", "1"), ("1",), ("a", "b"))
    verificar("universal concorda com execução direta sobre um catálogo de máquinas distintas",
              b(UNIVERSAL_CONCORDA_COM_EXECUCAO_DIRETA_FINITA(catalogo_teste, entradas_teste, 30)), True)
    verificar("marcador de limite honesto: não é uma UTM clássica", b(NAO_E_UTM_CLASSICA_FINITA()), True)

    # --- Etapa 435: contagem finita ---
    contagem = CONTAGEM_MAQUINAS_POSSIVEIS_FINITA(n_estados=2, n_simbolos=1)
    verificar("contagem de máquinas possíveis (2 estados, 1 símbolo) é finita e positiva", isinstance(contagem, int) and contagem > 0, True)

    # --- Etapa 436: classificação por enumeração ---
    classificacao = CLASSIFICAR_CATALOGO_FINITA((maquina_suc, maquina_parcial), ("1", "1"))
    verificar("classificação do catálogo por enumeração cobre as duas máquinas", len(classificacao), 2)
    verificar("máquina sucessora é classificada como parando", classificacao[0][1], True)

    # --- Etapa 437 ---
    verificar("linguagem regular finita (DFA) é decidida pela máquina de fita limitada equivalente (reafirma 429)",
              b(DFA_E_MAQUINA_CONCORDAM_FINITA(dfa_ab, palavras_ab, 10, 30)), True)

    # --- Etapa 438: palíndromo por máquina com memória, validado contra oráculo nativo ---
    casos_palindromo = ["", "0", "1", "00", "01", "10", "11", "010", "011", "0110", "10011001", "10011000"]
    todos_corretos = True
    for caso in casos_palindromo:
        obtido = b(PALINDROMO_POR_MAQUINA_FINITA(tuple(caso), 24, 200))
        esperado = PALINDROMO_POR_LEITURA_FINITA(tuple(caso))
        if obtido != esperado:
            todos_corretos = False
    verificar(f"máquina de palíndromo concorda com oráculo nativo em {len(casos_palindromo)}/{len(casos_palindromo)} casos", todos_corretos, True)

    # --- Etapa 439-440 ---
    sintese = SINTESE_COMPUTABILIDADE_FINITA_401_440()
    verificar("síntese do arco 401-440 registra as quatro partes", len(sintese), 4)
    verificar("fechamento do arco de computabilidade finita 401-440", b(FECHAMENTO_COMPUTABILIDADE_FINITA_401_440()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
