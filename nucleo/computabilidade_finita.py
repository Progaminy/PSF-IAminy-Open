# ==============================================================================
# COMPUTABILIDADE FINITA — Etapas 401 a 440 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois do arco lógico 341-400, o próximo passo que nasce sem violar a
#   lei das fórmulas junta autômatos finitos (136-300, só leem) com uma fita
#   de memória finita e explícita (esta etapa, lê E escreve). Como a fita
#   tem tamanho fixo N declarado ANTES de a máquina rodar, o espaço de
#   configurações é finito — o que torna a parada DECIDÍVEL para este
#   modelo, ao contrário do caso clássico de fita infinita.
#
#   Naturais e funções nesta camada são representados nativamente (int,
#   tuple, dict) — mesma convenção já estabelecida em metodos_finitos.py,
#   categorias_finitas.py, logica_predicados_finita.py e
#   teoria_modelos_prova_finita.py para domínios finitos explícitos.
# ==============================================================================
from .primitivas import V, F
from .metodos_finitos import ACEITA_DFA_FINITO


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


# ==========================================================================
# Etapas 401-410 — Modelo de máquina de fita limitada.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 401 — Configuração: estado atual, conteúdo da fita (tupla de
# tamanho fixo) e posição da cabeça.
# --------------------------------------------------------------------
def CONFIGURACAO_FINITA(estado, fita, posicao):
    return ("config", estado, tuple(fita), posicao)


# --------------------------------------------------------------------
# Etapa 402 — Máquina de fita limitada: sêxtupla explícita. `transicao`
# é um dicionário parcial {(estado, símbolo lido): (novo estado, símbolo
# escrito, direção)}, direção em {"E", "D", "P"}.
# --------------------------------------------------------------------
def MAQUINA_FITA_LIMITADA_FINITA(estados, alfabeto, branco, transicao, inicial, finais, tamanho_fita):
    return {
        "estados": tuple(estados),
        "alfabeto": tuple(alfabeto),
        "branco": branco,
        "transicao": dict(transicao),
        "inicial": inicial,
        "finais": tuple(finais),
        "tamanho_fita": tamanho_fita,
    }


# --------------------------------------------------------------------
# Etapa 403 — Configuração inicial a partir de uma entrada. Rejeita (por
# exceção declarada, não por resultado silenciosamente errado) entradas
# que não cabem na fita — o domínio é explícito, não escondido.
# --------------------------------------------------------------------
def CONFIGURACAO_INICIAL_FINITA(maquina, entrada):
    entrada = tuple(entrada)
    if len(entrada) > maquina["tamanho_fita"]:
        raise ValueError("entrada maior que a fita limitada declarada")
    faltando = maquina["tamanho_fita"] - len(entrada)
    fita = entrada + (maquina["branco"],) * faltando
    return CONFIGURACAO_FINITA(maquina["inicial"], fita, 0)


# --------------------------------------------------------------------
# Etapa 404 — Passo de transição: lê o símbolo sob a cabeça, aplica a
# transição (se houver), escreve, move — a posição é sempre grampeada a
# [0, tamanho_fita - 1] (a fita não cresce; ela é limitada por desenho).
# Devolve `None` quando não há transição definida (a máquina emperra).
# --------------------------------------------------------------------
def PASSO_MAQUINA_FINITA(maquina, configuracao):
    _, estado, fita, posicao = configuracao
    simbolo = fita[posicao]
    chave = (estado, simbolo)
    if chave not in maquina["transicao"]:
        return None
    novo_estado, simbolo_escrito, direcao = maquina["transicao"][chave]
    nova_fita = fita[:posicao] + (simbolo_escrito,) + fita[posicao + 1:]
    deslocamento = 1 if direcao == "D" else (-1 if direcao == "E" else 0)
    nova_posicao = max(0, min(posicao + deslocamento, maquina["tamanho_fita"] - 1))
    return CONFIGURACAO_FINITA(novo_estado, nova_fita, nova_posicao)


# --------------------------------------------------------------------
# Etapa 405 — Execução limitada a um número de passos. Três desfechos
# possíveis, todos explícitos: aceita, rejeita, ou não parou dentro do
# limite dado (o limite é uma escolha do chamador, não do modelo — para a
# decisão GARANTIDA, ver `DECISAO_PARADA_FINITA`, etapa 408).
# --------------------------------------------------------------------
def EXECUTAR_MAQUINA_FITA_LIMITADA(maquina, entrada, limite_passos):
    configuracao = CONFIGURACAO_INICIAL_FINITA(maquina, entrada)
    for _ in range(limite_passos):
        if configuracao[1] in maquina["finais"]:
            return ("aceita", configuracao)
        proxima = PASSO_MAQUINA_FINITA(maquina, configuracao)
        if proxima is None:
            return ("rejeita", configuracao)
        configuracao = proxima
    if configuracao[1] in maquina["finais"]:
        return ("aceita", configuracao)
    return ("nao_parou_no_limite", configuracao)


# --------------------------------------------------------------------
# Etapa 406 — O espaço de configurações é finito: no máximo
# |estados| × |símbolos ∪ {branco}|^N × N triplas (estado, fita, posição),
# onde N é o tamanho da fita. Contagem explícita, não afirmação abstrata.
# --------------------------------------------------------------------
def _potencia_nat_por_repeticao(base, expoente):
    total = 1
    for _ in range(expoente):
        total = total * base
    return total


def ESPACO_CONFIGURACOES_FINITO(maquina):
    simbolos = set(maquina["alfabeto"]) | {maquina["branco"]}
    n = maquina["tamanho_fita"]
    possibilidades_fita = _potencia_nat_por_repeticao(len(simbolos), n)
    return len(maquina["estados"]) * possibilidades_fita * n


# --------------------------------------------------------------------
# Etapa 407 — Detecção de configuração repetida: roda até
# `ESPACO_CONFIGURACOES_FINITO(maquina) + 1` passos — mais do que o
# número de configurações distintas possíveis. Pelo princípio da casa dos
# pombos, se a máquina não parou até lá, uma configuração REPETIU, e a
# máquina está presa num ciclo (vai repetir para sempre).
# --------------------------------------------------------------------
def DETECCAO_CICLO_E_PARADA_FINITA(maquina, entrada):
    limite = ESPACO_CONFIGURACOES_FINITO(maquina) + 1
    configuracao = CONFIGURACAO_INICIAL_FINITA(maquina, entrada)
    vistas = []
    for passo in range(limite):
        if configuracao[1] in maquina["finais"]:
            return ("para_aceita", passo)
        chave = (configuracao[1], configuracao[2], configuracao[3])
        if chave in vistas:
            return ("loop_detectado", passo)
        vistas.append(chave)
        proxima = PASSO_MAQUINA_FINITA(maquina, configuracao)
        if proxima is None:
            return ("para_rejeita", passo)
        configuracao = proxima
    return ("limite_excedido_inesperado", limite)


# --------------------------------------------------------------------
# Etapa 408 — Decidibilidade da parada PARA ESTE MODELO: uma decisão que
# SEMPRE termina (o laço em 407 é limitado) e sempre devolve uma resposta
# definitiva sobre se a máquina para ou entra em loop nesta entrada. Isto
# não é possível para o problema da parada clássico (fita infinita) — ver
# "Limite honesto" em `ETAPA_401_440_COMPUTABILIDADE_FINITA.md`.
# --------------------------------------------------------------------
def DECISAO_PARADA_FINITA(maquina, entrada):
    resultado, _ = DETECCAO_CICLO_E_PARADA_FINITA(maquina, entrada)
    return _bool(resultado in ("para_aceita", "para_rejeita"))


# --------------------------------------------------------------------
# Etapa 409 — Aceitação e linguagem aceita por uma máquina de fita
# limitada.
# --------------------------------------------------------------------
def ACEITA_MAQUINA_FITA_LIMITADA_FINITA(maquina, entrada, limite_passos):
    resultado, _ = EXECUTAR_MAQUINA_FITA_LIMITADA(maquina, entrada, limite_passos)
    return _bool(resultado == "aceita")


def LINGUAGEM_ACEITA_MAQUINA_FINITA(maquina, palavras, limite_passos):
    return tuple(p for p in palavras if _bool_to_py(ACEITA_MAQUINA_FITA_LIMITADA_FINITA(maquina, p, limite_passos)))


# --------------------------------------------------------------------
# Etapa 410 — Fechamento do modelo de máquina de fita limitada.
# --------------------------------------------------------------------
def FECHAMENTO_MAQUINA_FITA_LIMITADA_FINITA():
    return V


# ==========================================================================
# Etapas 411-420 — Funções computáveis finitas e esquemas de recursão
# primitiva finita.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 411 — Função computável finita: parcial, calculada rodando uma
# máquina até um limite de passos. Devolve a fita final se aceita, `None`
# se não (função genuinamente PARCIAL — não finge totalidade).
# --------------------------------------------------------------------
def FUNCAO_COMPUTADA_POR_MAQUINA_FINITA(maquina, entrada, limite_passos):
    resultado, configuracao = EXECUTAR_MAQUINA_FITA_LIMITADA(maquina, entrada, limite_passos)
    if resultado != "aceita":
        return None
    return configuracao[2]


# --------------------------------------------------------------------
# Etapas 412-414 — Esquemas básicos de recursão primitiva finita.
# --------------------------------------------------------------------
def FUNCAO_ZERO_FINITA(*_args):
    return 0


def FUNCAO_SUCESSOR_FINITA(n):
    return n + 1


def FUNCAO_PROJECAO_FINITA(indice):
    def projecao(*args):
        return args[indice]
    return projecao


# --------------------------------------------------------------------
# Etapa 415 — Composição de funções computáveis finitas.
# --------------------------------------------------------------------
def COMPOSICAO_FINITA(externa, *internas):
    def composta(*args):
        return externa(*(interna(*args) for interna in internas))
    return composta


# --------------------------------------------------------------------
# Etapa 416 — Recursão primitiva LIMITADA finita: h(0) = base,
# h(n+1) = passo(n, h(n)), definida só sobre `[0, limite]` — um intervalo
# explícito, não todos os naturais.
# --------------------------------------------------------------------
def RECURSAO_PRIMITIVA_LIMITADA_FINITA(base, passo, limite):
    valores = [base]
    for n in range(limite):
        valores.append(passo(n, valores[-1]))

    def h(n):
        if n < 0 or n > limite:
            raise ValueError("fora do intervalo declarado da recursão limitada")
        return valores[n]
    return h


# --------------------------------------------------------------------
# Etapa 417 — Toda função construída pelos esquemas 412-416 é total no
# domínio declarado: cada esquema, por construção, produz um valor para
# toda entrada válida do domínio (nenhum deles chama uma máquina que possa
# não parar). Verificado exaustivamente sobre um intervalo de teste.
# --------------------------------------------------------------------
def ESQUEMA_TOTAL_NO_DOMINIO_FINITO(funcao, dominio):
    for entrada in dominio:
        args = entrada if isinstance(entrada, tuple) else (entrada,)
        funcao(*args)
    return V


# --------------------------------------------------------------------
# Etapa 418 — Exemplo computado por uma máquina concreta: sucessor
# unário. Alfabeto {"1"}; a máquina anda para a direita sobre os "1"s e,
# ao achar o branco, escreve mais um "1". Validado contra `len(entrada)+1`
# nativo — mesmo padrão de oráculo independente da etapa 1.
# --------------------------------------------------------------------
def MAQUINA_SUCESSOR_UNARIO_FINITA(tamanho_fita):
    return MAQUINA_FITA_LIMITADA_FINITA(
        estados=("q0", "qf"),
        alfabeto=("1",),
        branco="_",
        transicao={
            ("q0", "1"): ("q0", "1", "D"),
            ("q0", "_"): ("qf", "1", "P"),
        },
        inicial="q0",
        finais=("qf",),
        tamanho_fita=tamanho_fita,
    )


def SUCESSOR_UNARIO_COMPUTADO_FINITA(quantidade_uns, tamanho_fita, limite_passos):
    maquina = MAQUINA_SUCESSOR_UNARIO_FINITA(tamanho_fita)
    entrada = ("1",) * quantidade_uns
    fita_final = FUNCAO_COMPUTADA_POR_MAQUINA_FINITA(maquina, entrada, limite_passos)
    if fita_final is None:
        return None
    return sum(1 for simbolo in fita_final if simbolo == "1")


# --------------------------------------------------------------------
# Etapa 419 — Contraexemplo honesto: uma máquina cujo comportamento é
# parcial de fato dentro do próprio domínio finito declarado — para
# algumas entradas ela para, para outra (deliberadamente) entra em loop
# contra a borda da fita.
# --------------------------------------------------------------------
def MAQUINA_PARCIAL_FINITA(tamanho_fita):
    return MAQUINA_FITA_LIMITADA_FINITA(
        estados=("q0", "qf"),
        alfabeto=("1", "0"),
        branco="_",
        transicao={
            ("q0", "1"): ("qf", "1", "P"),
            ("q0", "0"): ("q0", "0", "D"),
            ("q0", "_"): ("q0", "_", "D"),
        },
        inicial="q0",
        finais=("qf",),
        tamanho_fita=tamanho_fita,
    )


# --------------------------------------------------------------------
# Etapa 420 — Fechamento das funções computáveis finitas.
# --------------------------------------------------------------------
def FECHAMENTO_FUNCOES_COMPUTAVEIS_FINITAS():
    return V


# ==========================================================================
# Etapas 421-430 — Decidibilidade e redução de problemas de decisão
# finitos.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 421 — Problema de decisão finito: um predicado sobre um domínio
# explícito.
# --------------------------------------------------------------------
def PROBLEMA_DECISAO_FINITO(dominio, predicado):
    return {"dominio": tuple(dominio), "predicado": predicado}


def RESOLVER_PROBLEMA_DECISAO_FINITO(problema, entrada):
    return _bool(bool(problema["predicado"](entrada)))


# --------------------------------------------------------------------
# Etapa 422 — Decidibilidade de linguagem finita por DFA — reaproveita
# `ACEITA_DFA_FINITO` (etapa 136-300), não reimplementa.
# --------------------------------------------------------------------
def DECIDIVEL_POR_DFA_FINITA(automato, palavras):
    for p in palavras:
        _bool_to_py(ACEITA_DFA_FINITO(automato, p))
    return V


# --------------------------------------------------------------------
# Etapa 423 — Decidibilidade de linguagem finita por máquina de fita
# limitada: decidível sse a decisão de parada (408) confirma parada em
# TODA palavra do domínio declarado.
# --------------------------------------------------------------------
def DECIDIVEL_POR_MAQUINA_FINITA(maquina, palavras):
    return _bool(all(_bool_to_py(DECISAO_PARADA_FINITA(maquina, p)) for p in palavras))


# --------------------------------------------------------------------
# Etapa 424 — Redução finita: um mapeamento computável e total de
# instâncias de A para instâncias de B que preserva a resposta
# sim/não.
# --------------------------------------------------------------------
def REDUCAO_FINITA(instancias_a, mapeamento, problema_b):
    return tuple((a, RESOLVER_PROBLEMA_DECISAO_FINITO(problema_b, mapeamento(a))) for a in instancias_a)


# --------------------------------------------------------------------
# Etapa 425 — Se B é decidível (por enumeração exaustiva do seu domínio)
# e A reduz a B preservando a resposta, então A é decidível — demonstrado
# construtivamente: `RESOLVER_A_POR_REDUCAO_FINITA` decide A chamando a
# decisão já existente de B sobre a imagem da redução.
# --------------------------------------------------------------------
def RESOLVER_A_POR_REDUCAO_FINITA(a, mapeamento, problema_b):
    return RESOLVER_PROBLEMA_DECISAO_FINITO(problema_b, mapeamento(a))


def REDUCAO_PRESERVA_DECISAO_FINITA(instancias_a, mapeamento, problema_a, problema_b):
    for a in instancias_a:
        direto = _bool_to_py(RESOLVER_PROBLEMA_DECISAO_FINITO(problema_a, a))
        via_reducao = _bool_to_py(RESOLVER_A_POR_REDUCAO_FINITA(a, mapeamento, problema_b))
        if direto != via_reducao:
            return F
    return V


# --------------------------------------------------------------------
# Etapa 426 — Limite honesto: todo problema de decisão sobre um domínio
# FINITO declarado é decidível por enumeração exaustiva — a
# indecidibilidade clássica (ex.: problema da parada geral) exige um
# domínio infinito de instâncias, que está fora do escopo declarado deste
# projeto.
# --------------------------------------------------------------------
def TODO_PROBLEMA_FINITO_E_DECIDIVEL(problema):
    for entrada in problema["dominio"]:
        RESOLVER_PROBLEMA_DECISAO_FINITO(problema, entrada)
    return V


# --------------------------------------------------------------------
# Etapa 427 — Fechamento sob complemento.
# --------------------------------------------------------------------
def COMPLEMENTO_PROBLEMA_FINITO(problema):
    predicado_original = problema["predicado"]
    return PROBLEMA_DECISAO_FINITO(problema["dominio"], lambda x: not predicado_original(x))


# --------------------------------------------------------------------
# Etapa 428 — Fechamento sob união e interseção.
# --------------------------------------------------------------------
def UNIAO_PROBLEMAS_FINITA(problema_a, problema_b):
    dominio = tuple(dict.fromkeys(problema_a["dominio"] + problema_b["dominio"]))
    return PROBLEMA_DECISAO_FINITO(dominio, lambda x: problema_a["predicado"](x) or problema_b["predicado"](x))


def INTERSECAO_PROBLEMAS_FINITA(problema_a, problema_b):
    dominio = tuple(dict.fromkeys(problema_a["dominio"] + problema_b["dominio"]))
    return PROBLEMA_DECISAO_FINITO(dominio, lambda x: problema_a["predicado"](x) and problema_b["predicado"](x))


# --------------------------------------------------------------------
# Etapa 429 — Toda linguagem aceita por um DFA é aceita por alguma
# máquina de fita limitada equivalente: a tradução simplesmente nunca
# move a cabeça para a esquerda e nunca escreve — a fita funciona como o
# ponteiro de leitura do DFA.
# --------------------------------------------------------------------
def DFA_PARA_MAQUINA_FITA_LIMITADA_FINITA(automato, tamanho_fita):
    # Cada transição do DFA vira um passo que lê, reescreve o mesmo
    # símbolo (a fita só funciona como ponteiro de leitura aqui) e anda
    # para a direita. Um estado do DFA pode ser final e AINDA ASSIM ter
    # transições de saída (aceitação não é absorvente em DFA — o
    # autômato pode passar por um estado final e continuar consumindo
    # símbolos). Por isso a aceitação da máquina NÃO pode ser "parar
    # assim que o estado é final" (isso pararia cedo demais, no meio da
    # palavra) — só pode ser reconhecida quando o branco é lido (fim da
    # palavra) NUM estado final do DFA. Um único estado sintético
    # "aceita_dfa", absorvente, marca exatamente esse momento.
    transicao = {}
    for (estado, simbolo), destino in automato["transicao"].items():
        transicao[(estado, simbolo)] = (destino, simbolo, "D")
    for estado in automato["estados"]:
        if estado in automato["finais"]:
            transicao[(estado, "_")] = ("aceita_dfa", "_", "P")
    return MAQUINA_FITA_LIMITADA_FINITA(
        estados=automato["estados"] + ("aceita_dfa",),
        alfabeto=automato["alfabeto"],
        branco="_",
        transicao=transicao,
        inicial=automato["inicial"],
        finais=("aceita_dfa",),
        tamanho_fita=tamanho_fita,
    )


# --------------------------------------------------------------------
# Etapa 430 — Fechamento da decidibilidade e redução finita.
# --------------------------------------------------------------------
def FECHAMENTO_DECIDIBILIDADE_REDUCAO_FINITA():
    return V


# ==========================================================================
# Etapas 431-440 — Máquina universal finita e comparação com o DFA.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 431 — O "código" de uma máquina é a própria estrutura de dados
# devolvida por `MAQUINA_FITA_LIMITADA_FINITA` — nenhuma codificação
# adicional é necessária nem introduzida.
# --------------------------------------------------------------------
def CODIGO_DA_MAQUINA_FINITA(maquina):
    return maquina


# --------------------------------------------------------------------
# Etapa 432 — Máquina universal finita: UM interpretador que roda
# QUALQUER máquina de fita limitada recebida como dado — nenhuma lógica
# aqui é específica de uma máquina particular.
# --------------------------------------------------------------------
def MAQUINA_UNIVERSAL_FINITA(codigo_da_maquina, entrada, limite_passos):
    return EXECUTAR_MAQUINA_FITA_LIMITADA(codigo_da_maquina, entrada, limite_passos)


# --------------------------------------------------------------------
# Etapa 433 — Simulação validada: o interpretador universal concorda com
# a execução direta, sobre um catálogo de máquinas de teste.
# --------------------------------------------------------------------
def UNIVERSAL_CONCORDA_COM_EXECUCAO_DIRETA_FINITA(catalogo_maquinas, entradas, limite_passos):
    for maquina in catalogo_maquinas:
        for entrada in entradas:
            direto = EXECUTAR_MAQUINA_FITA_LIMITADA(maquina, entrada, limite_passos)
            universal = MAQUINA_UNIVERSAL_FINITA(CODIGO_DA_MAQUINA_FINITA(maquina), entrada, limite_passos)
            if direto != universal:
                return F
    return V


# --------------------------------------------------------------------
# Etapa 434 — Limite honesto: função-marcador documentando que este NÃO é
# o argumento diagonal clássico (ver o texto em
# `ETAPA_401_440_COMPUTABILIDADE_FINITA.md`).
# --------------------------------------------------------------------
def NAO_E_UTM_CLASSICA_FINITA():
    return V


# --------------------------------------------------------------------
# Etapa 435 — Contagem finita de máquinas distintas para (estados,
# alfabeto, tamanho de fita) pequenos: o número de funções de transição
# possíveis é finito porque o domínio (estados × símbolos) e o
# contradomínio (estados × símbolos × direções) da tabela são finitos.
# --------------------------------------------------------------------
def CONTAGEM_MAQUINAS_POSSIVEIS_FINITA(n_estados, n_simbolos, n_direcoes=3):
    tamanho_dominio_transicao = n_estados * (n_simbolos + 1)
    tamanho_contradominio_transicao = n_estados * (n_simbolos + 1) * n_direcoes
    transicoes_possiveis = _potencia_nat_por_repeticao(
        tamanho_contradominio_transicao + 1,
        tamanho_dominio_transicao,
    )
    escolhas_inicial = n_estados
    escolhas_finais = _potencia_nat_por_repeticao(2, n_estados)
    return transicoes_possiveis * escolhas_inicial * escolhas_finais


# --------------------------------------------------------------------
# Etapa 436 — Classificação por enumeração exaustiva de um catálogo
# pequeno de máquinas dado, por (para / não para) numa entrada — decisão
# demonstrada por enumeração direta.
# --------------------------------------------------------------------
def CLASSIFICAR_CATALOGO_FINITA(catalogo_maquinas, entrada):
    return tuple((i, _bool_to_py(DECISAO_PARADA_FINITA(m, entrada))) for i, m in enumerate(catalogo_maquinas))


# --------------------------------------------------------------------
# Etapa 437 — Toda linguagem regular finita (DFA) é decidida por alguma
# máquina de fita limitada: reaproveita a tradução da etapa 429 e
# confirma que aceitação concorda sobre um catálogo de palavras.
# --------------------------------------------------------------------
def DFA_E_MAQUINA_CONCORDAM_FINITA(automato, palavras, tamanho_fita, limite_passos):
    maquina = DFA_PARA_MAQUINA_FITA_LIMITADA_FINITA(automato, tamanho_fita)
    for p in palavras:
        aceita_dfa = _bool_to_py(ACEITA_DFA_FINITO(automato, p))
        aceita_maquina = _bool_to_py(ACEITA_MAQUINA_FITA_LIMITADA_FINITA(maquina, p, limite_passos))
        if aceita_dfa != aceita_maquina:
            return F
    return V


# --------------------------------------------------------------------
# Etapa 438 — Diferença conceitual demonstrada: verificador de palíndromo
# por máquina com memória. Algoritmo clássico: apaga o símbolo mais à
# esquerda ainda vivo, guarda seu valor no PRÓPRIO ESTADO (`comparar_0`
# vs. `comparar_1`), anda até a borda direita ainda viva, compara e apaga
# também — os dois lados encolhem para dentro. Um marcador `"L"` na
# posição 0 (nunca apagado) é o que permite a máquina reconhecer a
# fronteira esquerda sem precisar de um contador — a mesma técnica clássica
# de sentinela usada em construções de máquina de Turing para esta tarefa.
# Validado contra `tuple(entrada) == tuple(reversed(entrada))` nativo.
# --------------------------------------------------------------------
def MAQUINA_PALINDROMO_FINITA(tamanho_fita):
    transicao = {("inicio", "L"): ("achar_esq", "L", "D")}
    transicao[("achar_esq", "0")] = ("ir_direita_0", "_", "D")
    transicao[("achar_esq", "1")] = ("ir_direita_1", "_", "D")
    transicao[("achar_esq", "_")] = ("aceita", "_", "P")
    for b in ("0", "1"):
        estado_ir, estado_comp = f"ir_direita_{b}", f"comparar_{b}"
        transicao[(estado_ir, "0")] = (estado_ir, "0", "D")
        transicao[(estado_ir, "1")] = (estado_ir, "1", "D")
        transicao[(estado_ir, "_")] = (estado_comp, "_", "E")
        transicao[(estado_comp, "_")] = ("aceita", "_", "P")
        transicao[(estado_comp, b)] = ("voltar_esq", "_", "E")
        outro = "1" if b == "0" else "0"
        transicao[(estado_comp, outro)] = ("rejeita_trava", outro, "P")
    transicao[("voltar_esq", "0")] = ("voltar_esq", "0", "E")
    transicao[("voltar_esq", "1")] = ("voltar_esq", "1", "E")
    transicao[("voltar_esq", "_")] = ("achar_esq", "_", "D")
    return MAQUINA_FITA_LIMITADA_FINITA(
        estados=("inicio", "achar_esq", "ir_direita_0", "ir_direita_1", "comparar_0", "comparar_1",
                 "voltar_esq", "aceita", "rejeita_trava"),
        alfabeto=("0", "1", "L"),
        branco="_",
        transicao=transicao,
        inicial="inicio",
        finais=("aceita",),
        tamanho_fita=tamanho_fita,
    )


def PALINDROMO_POR_MAQUINA_FINITA(palavra, tamanho_fita, limite_passos):
    maquina = MAQUINA_PALINDROMO_FINITA(tamanho_fita)
    entrada = ("L",) + tuple(palavra)
    return ACEITA_MAQUINA_FITA_LIMITADA_FINITA(maquina, entrada, limite_passos)


def PALINDROMO_POR_LEITURA_FINITA(entrada):
    return tuple(entrada) == tuple(reversed(entrada))


# --------------------------------------------------------------------
# Etapa 439 — Síntese do que persiste do arco 401-440.
# --------------------------------------------------------------------
def SINTESE_COMPUTABILIDADE_FINITA_401_440():
    return {
        "modelo": "máquina de fita limitada (401-410)",
        "funcoes": "esquemas de recursão primitiva finita (411-420)",
        "decisao": "decidibilidade e redução finita (421-430)",
        "universal": "interpretador único, não UTM clássica (431-440)",
    }


# --------------------------------------------------------------------
# Etapa 440 — Fechamento do arco de computabilidade finita 401-440.
# --------------------------------------------------------------------
def FECHAMENTO_COMPUTABILIDADE_FINITA_401_440():
    return V
