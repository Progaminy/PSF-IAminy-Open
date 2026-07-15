"""Semântica denotacional finita — etapas 701-720.

Reconstrução PSF: expressão e comando são árvores finitas; significado é a
função que transforma ambiente finito em valor/novo ambiente. Não usa
fórmulas prontas, solver, divisão, módulo, primalidade ou análise infinita.
"""
from __future__ import annotations


def valor_expr(expr, ambiente):
    tipo = expr[0]
    if tipo == "const":
        return expr[1]
    if tipo == "var":
        return ambiente[expr[1]]
    if tipo == "add":
        return valor_expr(expr[1], ambiente) + valor_expr(expr[2], ambiente)
    if tipo == "mul":
        return valor_expr(expr[1], ambiente) * valor_expr(expr[2], ambiente)
    if tipo == "lt":
        return valor_expr(expr[1], ambiente) < valor_expr(expr[2], ambiente)
    if tipo == "eq":
        return valor_expr(expr[1], ambiente) == valor_expr(expr[2], ambiente)
    raise ValueError(f"expressão desconhecida: {tipo}")


def denota_comando(comando, ambiente, limite=100):
    """Devolve novo ambiente. Laços só executam com limite explícito."""
    tipo = comando[0]
    env = dict(ambiente)
    if tipo == "skip":
        return env
    if tipo == "assign":
        env[comando[1]] = valor_expr(comando[2], env)
        return env
    if tipo == "seq":
        for c in comando[1:]:
            env = denota_comando(c, env, limite=limite)
        return env
    if tipo == "if":
        return denota_comando(comando[2] if valor_expr(comando[1], env) else comando[3], env, limite=limite)
    if tipo == "while":
        cond, corpo = comando[1], comando[2]
        passos = 0
        while valor_expr(cond, env):
            if passos >= limite:
                raise RuntimeError("limite explícito de laço atingido")
            env = denota_comando(corpo, env, limite=limite)
            passos += 1
        return env
    raise ValueError(f"comando desconhecido: {tipo}")


def traco_comando(comando, ambiente, limite=100):
    """Executa e devolve estados visitados. Útil para invariantes finitos."""
    traco = [dict(ambiente)]

    def exec_cmd(cmd, env):
        tipo = cmd[0]
        if tipo == "while":
            cond, corpo = cmd[1], cmd[2]
            passos = 0
            while valor_expr(cond, env):
                if passos >= limite:
                    raise RuntimeError("limite explícito de laço atingido")
                env = exec_cmd(corpo, env)
                traco.append(dict(env))
                passos += 1
            return env
        novo = denota_comando(cmd, env, limite=limite)
        traco.append(dict(novo))
        return novo

    exec_cmd(comando, dict(ambiente))
    return traco


def equivalente_por_catalogo(programa_a, programa_b, ambientes, limite=100):
    """Equivalência honesta: só para o catálogo finito fornecido."""
    for env in ambientes:
        if denota_comando(programa_a, env, limite) != denota_comando(programa_b, env, limite):
            return False
    return True


def tripla_hoare_finita(pre, comando, post, ambientes, limite=100):
    """Verifica {pre} comando {post} por enumeração finita de ambientes."""
    for env in ambientes:
        if pre(env):
            saida = denota_comando(comando, env, limite=limite)
            if not post(saida):
                return False
    return True


def invariante_finito(invariante, comando, ambiente, limite=100):
    return all(invariante(e) for e in traco_comando(comando, ambiente, limite=limite))
