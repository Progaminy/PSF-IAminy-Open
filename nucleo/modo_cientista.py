# Etapa 52 — Modo Cientista PSF
# Núcleo nativo: sem dependências externas como fundamento.
# Python só organiza texto, listas e verificações estruturais.

REGRA_SEM_DEPENDENCIAS_EXTERNAS = (
    'O modo cientista não usa internet, API externa, LLM externo, math, numpy, sympy, '
    'scipy, sklearn, pytorch, tensorflow, solver externo ou biblioteca como fundamento.'
)

ESTADO = 'DEFINITIVO_COM_RESPOSTA_AULA_TESTE'

FASES_CIENTISTA = [
    'observar',
    'definir_objeto',
    'listar_dependencias',
    'desmontar_fluxo',
    'montar_fluxo_minimo',
    'comparar_caminhos',
    'procurar_padrao',
    'procurar_lacunas',
    'testar_casos_minimos',
    'tentar_contraexemplo',
    'formular_hipotese',
    'auditar_passo_a_passo',
    'formalizar',
    'registrar_aprendizado',
]

TIPOS_DE_ALERTA = {
    'SALTO_DE_FORMULA': 'A resposta usou fórmula pronta sem montar a origem.',
    'SALTO_DE_PASSO': 'Há passagem brusca entre duas afirmações sem ponte explicativa.',
    'LACUNA_DE_DEPENDENCIA': 'O passo depende de conceito ainda não declarado no caminho.',
    'BRECHA_DE_VALIDACAO': 'A conclusão foi afirmada sem teste, caso mínimo ou contraexemplo tentado.',
    'PROMESSA_SEM_TESTE': 'Métrica, desempenho ou verdade empírica foi prometida sem validação.',
    'AMBIGUIDADE_DE_OBJETO': 'O objeto estudado não está definido com precisão suficiente.',
    'MISTURA_DE_NIVEIS': 'A explicação saltou para nível avançado sem construir o nível anterior.',
}

PALAVRAS_SALTO = [
    'obviamente', 'é óbvio', 'e obvio', 'claramente', 'pela fórmula', 'pela formula', 'usando a fórmula', 'usando a formula',
    'sabemos que', 'logo diretamente', 'basta aplicar', 'como é conhecido',
]

PALAVRAS_FORMULA_PRONTA = [
    'bhaskara', 'pitágoras', 'l\'hôpital', 'lhopital', 'taylor', 'stokes',
    'green', 'gauss-bonnet', 'riemann-roch', 'fourier', 'laplace', 'bayes',
    'newton', 'euler', 'determinante', 'gradiente', 'integral', 'derivada',
]

PALAVRAS_VALIDACAO_EMPIRICA = [
    'erro máximo', 'auc', 'recall', 'precisão', 'acurácia', 'garantido',
    'garantia', 'sempre atinge', 'sempre terá', 'resultado prometido',
]

DEPENDENCIAS_MINIMAS = {
    'derivada': ['limite', 'variação', 'função'],
    'integral': ['área', 'soma', 'limite'],
    'probabilidade': ['casos', 'acontecimento', 'espaço amostral'],
    'equação': ['igualdade', 'incógnita', 'operação inversa'],
    'função': ['entrada', 'saída', 'regra'],
    'teorema': ['hipótese', 'conclusão', 'prova'],
    'matriz': ['linha', 'coluna', 'transformação'],
    'geometria': ['ponto', 'reta', 'medida'],
    'estatística': ['dados', 'medida', 'variação'],
}

PERFIL_MODO_CIENTISTA = {
    'nome': 'modo cientista',
    'estado': ESTADO,
    'função': 'estudar padrões, investigar, comparar caminhos e detectar lacunas de construção.',
    'resposta_padrao': 'observação -> desmontagem -> dependências -> lacunas -> testes -> hipótese -> formalização',
    'fases': FASES_CIENTISTA,
    'sem_dependencias_externas': True,
}


def _texto(objeto):
    if objeto is None:
        return ''
    if isinstance(objeto, str):
        return objeto
    if isinstance(objeto, (list, tuple)):
        return ' '.join(_texto(x) for x in objeto)
    if isinstance(objeto, dict):
        return ' '.join(_texto(v) for v in objeto.values())
    return str(objeto)


def normalizar(texto):
    t = _texto(texto).lower()
    troca = {
        'á':'a','à':'a','â':'a','ã':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c',
        '≤':'<=','≥':'>=','²':'^2','³':'^3','π':'pi','√':'raiz ',
    }
    for a,b in troca.items():
        t = t.replace(a,b)
    return t


def estudar_padrao(observacoes):
    texto = normalizar(observacoes)
    sinais = []
    for palavra in ['repete', 'sempre', 'cresce', 'diminui', 'alternado', 'periodico', 'proporcional', 'simetria']:
        if palavra in texto:
            sinais.append(palavra)
    if not sinais:
        sinais.append('padrão ainda não evidente: pedir mais exemplos ou construir casos mínimos')
    return {
        'estado': 'PADRAO_ESTUDADO',
        'sinais_detectados': sinais,
        'proxima_acao': 'gerar casos mínimos e comparar variações',
    }


def listar_dependencias(conteudo):
    texto = normalizar(conteudo)
    deps = []
    for conceito, necessarias in DEPENDENCIAS_MINIMAS.items():
        if conceito in texto:
            deps.extend(necessarias)
    unicas = []
    for d in deps:
        if d not in unicas:
            unicas.append(d)
    return unicas


def detectar_lacunas(construcao):
    texto_original = _texto(construcao)
    texto = normalizar(texto_original)
    alertas = []

    if len(texto.strip()) < 20:
        alertas.append({'tipo':'AMBIGUIDADE_DE_OBJETO','motivo':TIPOS_DE_ALERTA['AMBIGUIDADE_DE_OBJETO']})

    for palavra in PALAVRAS_SALTO:
        if palavra in texto:
            alertas.append({'tipo':'SALTO_DE_PASSO','termo':palavra,'motivo':TIPOS_DE_ALERTA['SALTO_DE_PASSO']})

    for formula in PALAVRAS_FORMULA_PRONTA:
        if formula in texto and not any(p in texto for p in ['deriva', 'monta', 'origem', 'prova', 'construi', 'passo a passo', 'desmonta']):
            alertas.append({'tipo':'SALTO_DE_FORMULA','termo':formula,'motivo':TIPOS_DE_ALERTA['SALTO_DE_FORMULA']})

    deps = listar_dependencias(texto)
    for dep in deps:
        if dep not in texto:
            alertas.append({'tipo':'LACUNA_DE_DEPENDENCIA','dependencia':dep,'motivo':TIPOS_DE_ALERTA['LACUNA_DE_DEPENDENCIA']})

    if any(p in texto for p in PALAVRAS_VALIDACAO_EMPIRICA) and not any(v in texto for v in ['teste', 'validacao', 'medido', 'observado', 'amostra']):
        alertas.append({'tipo':'PROMESSA_SEM_TESTE','motivo':TIPOS_DE_ALERTA['PROMESSA_SEM_TESTE']})

    if 'resultado' in texto and not any(v in texto for v in ['teste', 'exemplo', 'caso minimo', 'contraexemplo']):
        alertas.append({'tipo':'BRECHA_DE_VALIDACAO','motivo':TIPOS_DE_ALERTA['BRECHA_DE_VALIDACAO']})

    return alertas


def desmontar_fluxo(passos):
    if isinstance(passos, str):
        partes = [p.strip() for p in passos.replace('\n', '.').split('.') if p.strip()]
    else:
        partes = [str(p).strip() for p in passos if str(p).strip()]
    fluxo = []
    for pos, passo in enumerate(partes, start=1):
        fluxo.append({
            'ordem': pos,
            'passo': passo,
            'dependencias_sugeridas': listar_dependencias(passo),
            'alertas': detectar_lacunas(passo),
        })
    return fluxo


def comparar_caminhos(caminho_psf, caminho_alvo):
    a = [normalizar(x) for x in (caminho_psf if isinstance(caminho_psf, list) else [caminho_psf])]
    b = [normalizar(x) for x in (caminho_alvo if isinstance(caminho_alvo, list) else [caminho_alvo])]
    ausentes = []
    for passo in b:
        if not any(passo in item or item in passo for item in a):
            ausentes.append(passo)
    extras = []
    for passo in a:
        if not any(passo in item or item in passo for item in b):
            extras.append(passo)
    return {
        'estado': 'COMPARACAO_REALIZADA',
        'passos_ausentes_no_psf': ausentes,
        'passos_extras_no_psf': extras,
        'precisa_reconstrucao': bool(ausentes),
    }


def investigar(pergunta, construcao='', caminho_alvo=None):
    base = {
        'modo': 'cientista',
        'estado': ESTADO,
        'pergunta': pergunta,
        'observacao': 'o objeto será estudado antes de ser respondido como verdade final',
        'dependencias': listar_dependencias(pergunta + ' ' + _texto(construcao)),
        'padroes': estudar_padrao(pergunta + ' ' + _texto(construcao)),
        'fluxo': desmontar_fluxo(construcao or pergunta),
        'lacunas': detectar_lacunas(construcao or pergunta),
        'fora_da_caixa': [
            'testar caso mínimo',
            'trocar representação',
            'procurar contraexemplo pequeno',
            'comparar forma geométrica, algébrica e operacional',
            'perguntar se a conclusão depende de hipótese escondida',
        ],
        'decisao': 'não aprovar como completo se houver lacuna, salto ou promessa sem teste',
    }
    if caminho_alvo is not None:
        base['comparacao'] = comparar_caminhos(construcao or pergunta, caminho_alvo)
    return base


def relatorio_cientista(pergunta, construcao='', caminho_alvo=None):
    r = investigar(pergunta, construcao, caminho_alvo)
    linhas = []
    linhas.append('MODO CIENTISTA PSF')
    linhas.append('Objeto: ' + str(pergunta))
    linhas.append('Regra: estudar antes de concluir; detectar lacunas antes de aprovar.')
    if r['dependencias']:
        linhas.append('Dependências vistas: ' + ', '.join(r['dependencias']))
    else:
        linhas.append('Dependências vistas: ainda não declaradas; construir a partir do mínimo.')
    if r['lacunas']:
        linhas.append('Alertas:')
        for a in r['lacunas']:
            detalhe = a.get('termo') or a.get('dependencia') or ''
            linhas.append('- ' + a['tipo'] + (': ' + detalhe if detalhe else ''))
    else:
        linhas.append('Alertas: nenhum salto evidente no texto fornecido.')
    linhas.append('Ações científicas: observar, desmontar, comparar, testar, tentar contraexemplo, formalizar.')
    linhas.append('Decisão: ' + r['decisao'])
    return '\n'.join(linhas)


def validar_modo_cientista():
    problemas = []
    if len(FASES_CIENTISTA) < 10:
        problemas.append('fases_insuficientes')
    if 'math' in globals() or 'numpy' in globals() or 'sympy' in globals():
        problemas.append('dependencia_externa_detectada')
    amostra = relatorio_cientista('A fórmula é óbvia pela fórmula de Bhaskara e o resultado é garantido.')
    if 'SALTO_DE_PASSO' not in amostra:
        problemas.append('nao_detectou_salto_de_passo')
    if 'SALTO_DE_FORMULA' not in amostra:
        problemas.append('nao_detectou_formula_pronta')
    if 'BRECHA_DE_VALIDACAO' not in amostra:
        problemas.append('nao_detectou_brecha_validacao')
    return problemas
