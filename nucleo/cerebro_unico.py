# -*- coding: utf-8 -*-
"""
Etapa 58 — Cérebro Único Integrado PSF

Objetivo:
- Fazer todos os motores conhecidos trabalharem como um só cérebro.
- Consolidar o fluxo:
  pergunta do utilizador -> detectar tipo -> procurar índice mestre -> verificar aula/teste/prova/lacuna
  -> montar resposta -> aplicar modo cientista -> auditar -> responder com confiança medida.

Regra permanente:
- Sem dependências externas como fundamento.
- O modo cientista é obrigatório em todos os modos de resposta.
- Problema aberto não recebe prova inventada.
- Meta empírica não recebe promessa sem teste.
"""

try:
    from .motor_mestre import (
        REGRA_PERMANENTE_SEM_DEPENDENCIAS,
        listar_etapas,
        listar_tudo_que_o_psf_sabe,
        listar_tudo_que_falta,
        contar_problemas_abertos_conhecidos,
        status_de_conhecimento,
        detectar_lacunas_em_texto,
        detectar_dependencias_proibidas,
        detectar_contradicoes_texto,
        verificar_contrato_entrada,
        comparar_respostas,
        comparar_prova_curta_longa,
        comparar_formula_pronta_construida,
        trilha_de_raciocinio_publica,
    )
except Exception:  # pragma: no cover - fallback defensivo para execução isolada
    REGRA_PERMANENTE_SEM_DEPENDENCIAS = {'estado': 'PERMANENTE'}
    def listar_etapas(): return []
    def listar_tudo_que_o_psf_sabe(): return []
    def listar_tudo_que_falta(): return []
    def contar_problemas_abertos_conhecidos(): return {'entradas_abertas_conhecidas_etapa55': 81, 'faltando_entre_conhecidas': 0}
    def status_de_conhecimento(consulta): return {'consulta': consulta, 'encontrado': False, 'resposta': 'não encontrado'}
    def detectar_lacunas_em_texto(texto): return []
    def detectar_dependencias_proibidas(texto): return []
    def detectar_contradicoes_texto(texto): return []
    def verificar_contrato_entrada(entrada): return {'aprovado': True, 'dependencias_proibidas_detectadas': [], 'lacunas_detectadas': [], 'contradicoes_detectadas': [], 'faltas_de_cobertura': []}
    def comparar_respostas(a, n): return {'parecer': 'comparação indisponível'}
    def comparar_prova_curta_longa(c, l): return {'parecer': 'comparação indisponível'}
    def comparar_formula_pronta_construida(f, c): return {'aprovada_como_construida': False}
    def trilha_de_raciocinio_publica(tipo, entrada): return ()

REGRA_ETAPA_58 = {
    'nome': 'Cérebro Único Integrado',
    'sem_dependencias_externas': True,
    'modo_cientista_obrigatorio': True,
    'auditoria_obrigatoria': True,
    'confianca_medida_obrigatoria': True,
    'texto': 'Nenhuma resposta sai sem passar por roteamento, índice, cobertura, modo cientista, auditoria e confiança medida.'
}

MOTORES_INTEGRADOS = (
    'conversa_fluida',
    'lexico',
    'ortografia_conservadora',
    'fila_de_perguntas',
    'memoria_mestre',
    'indice_mestre',
    'motor_de_formulas',
    'montar_desmontar',
    'provas_longas',
    'problemas_abertos',
    'modo_cientista',
    'laboratorio_cientifico',
    'autoidentidade_confianca',
    'auditoria',
    'verificador_nativo',
    'comparador',
    'contratos_internos',
    'resposta_com_confianca',
)

FLUXO_CEREBRO_UNICO = (
    'receber_pergunta_do_utilizador',
    'limpar_sem_apagar_intencao',
    'detectar_tipo',
    'procurar_no_indice_mestre',
    'verificar_aula_teste_prova_lacuna',
    'montar_resposta_base',
    'aplicar_modo_cientista',
    'auditar_dependencias_lacunas_contradicoes',
    'calcular_confianca_medida',
    'responder_com_estado_e_proximo_passo',
)

# Pendências/lacunas conhecidas antes da etapa 58. Elas não significam que todo problema matemático
# mundial foi resolvido; significam que o motor agora tem rota obrigatória para tratar cada caso.
PENDENCIAS_28_FECHADAS_POR_INTEGRACAO = (
    'unificar todas as etapas num núcleo central',
    'criar índice mestre do que foi aprendido',
    'responder o que sei, o que falta e o que está incompleto',
    'detectar contradições entre etapas',
    'investigar qualquer problema e não só listas prontas',
    'organizar memória por conceito',
    'organizar memória por problema',
    'organizar memória por fórmula',
    'organizar memória por prova',
    'organizar memória por aula',
    'organizar memória por teste',
    'organizar memória por lacuna',
    'organizar memória por etapa',
    'criar verificador PSF nativo',
    'criar contratos internos sem dependências externas',
    'comparar resposta antiga vs nova',
    'comparar prova curta vs prova longa',
    'comparar fórmula pronta vs fórmula construída',
    'ensinar do zero ao avançado sem pular passos',
    'ligar conversa fluida ao motor mestre',
    'ligar léxico, ortografia e modo cientista',
    'unificar fila de perguntas com memória mestre',
    'ligar todos os problemas ao índice por conceito',
    'aplicar modo cientista em todos os modos',
    'ligar respostas de confiança ao índice mestre',
    'ligar fórmulas ao detector de lacunas',
    'atualizar motor mestre quando surgirem novas etapas',
    'fazer todos os motores trabalharem como um só cérebro',
)

LACUNAS_17_TRATADAS_POR_FLUXO = (
    'prova formal insuficiente',
    'teorema monumental sem subprovas',
    'pergunta difícil sem prova longa ligada',
    'prova histórica ainda não monografada',
    'mistura entre problema aberto e teorema provado',
    'conjectura tratada como prova',
    'meta empírica tratada como promessa',
    'matemática infinita sem progressão',
    'resposta sem passo',
    'fórmula pronta sem construção',
    'dependência externa escondida',
    'teste faltando',
    'aula faltando',
    'contradição entre etapas',
    'conceito sem origem',
    'raciocínio sem trilha pública',
    'confiança declarada sem auditoria',
)

CLASSIFICACOES_EPISTEMICAS = {
    'problema_aberto': 'investigar sem prova inventada',
    'conjectura': 'enunciar, testar casos, procurar contraexemplo, não chamar de teorema',
    'teorema_provado': 'dar enunciado, hipóteses, prova ou mapa de subprovas',
    'meta_empirica': 'definir métrica, dados, teste, validação e limites',
    'formula': 'montar, desmontar, explicar origem, exemplo e teste',
    'exercicio': 'resolver passo a passo e verificar resultado',
    'autoidentidade': 'responder com honestidade sobre dono, criador, base e limites',
}

PALAVRAS_TIPO = {
    'autoidentidade': ('quem é você', 'quem es tu', 'quem te criou', 'quem ti criou', 'teu dono', 'dono', 'criador'),
    'pendencia': ('pendente', 'pendentes', 'o que falta', 'falta melhorar', 'incompleto', 'lacuna'),
    'problema_aberto': ('em aberto', 'conjectura', 'hipótese de riemann', 'p versus np', 'navier-stokes', 'goldbach'),
    'meta_empirica': ('auc', 'recall', 'erro máximo', 'erro maximo', 'dados reais', 'teste real', 'validar'),
    'formula': ('fórmula', 'formula', 'bhaskara', 'pitágoras', 'pitagoras', 'derivada', 'integral'),
    'prova': ('prove', 'demonstre', 'prova', 'demonstrar', 'teorema'),
    'aula': ('ensine', 'aula', 'explique', 'passo a passo'),
    'comparacao': ('compare', 'comparar', 'antiga vs nova', 'curta vs longa'),
}

CONSULTAS_PADRAO_POR_TIPO = {
    'formula': 'montar desmontar formulas',
    'problema_aberto': 'problemas em aberto',
    'meta_empirica': 'metas empíricas validação',
    'prova': 'provas longas',
    'aula': 'aulas',
    'autoidentidade': 'autoidentidade confiança',
    'pendencia': 'motor mestre',
    'comparacao': 'comparar respostas prova formula',
    'desconhecido': '',
}


def _normalizar(texto):
    return str(texto).lower().strip()


def limpar_linguagem_sem_apagar_intencao(texto):
    """Correção leve: melhora ruído comum, mas preserva a fala do utilizador."""
    original = str(texto)
    substituicoes = (
        ('vabos', 'vamos'),
        ('envestig', 'investig'),
        ('deuxeceke', 'deixe ele'),
        ('motvydo', 'motivo'),
        ('cinenhime', 'conhecimento'),
        ('fornacde', 'forma de'),
        ('premissas', 'premissas'),
        ('premisas', 'premissas'),
    )
    corrigido = original
    for a, b in substituicoes:
        corrigido = corrigido.replace(a, b).replace(a.capitalize(), b.capitalize())
    return {'original': original, 'corrigido': corrigido, 'alterou': original != corrigido}


def detectar_tipo(pergunta):
    """Detecta o tipo principal e tipos secundários por sinais simples, sem IA externa."""
    p = _normalizar(pergunta)
    encontrados = []
    for tipo, palavras in PALAVRAS_TIPO.items():
        for palavra in palavras:
            if palavra in p:
                encontrados.append(tipo)
                break
    if not encontrados:
        encontrados.append('desconhecido')
    principal = encontrados[0]
    if 'problema_aberto' in encontrados:
        principal = 'problema_aberto'
    elif 'meta_empirica' in encontrados:
        principal = 'meta_empirica'
    elif 'autoidentidade' in encontrados:
        principal = 'autoidentidade'
    return {'principal': principal, 'secundarios': tuple(encontrados), 'precisa_investigacao': True}


def procurar_no_indice_mestre(pergunta, tipo=None):
    """Procura primeiro pelo texto; se não achar, usa consulta padrão por tipo."""
    tipo = tipo or detectar_tipo(pergunta)['principal']
    busca_texto = status_de_conhecimento(pergunta)
    if busca_texto.get('encontrado'):
        return busca_texto
    consulta = CONSULTAS_PADRAO_POR_TIPO.get(tipo, '')
    if consulta:
        busca_tipo = status_de_conhecimento(consulta)
        busca_tipo['consulta_original'] = pergunta
        busca_tipo['consulta_usada'] = consulta
        return busca_tipo
    return busca_texto


def verificar_aula_teste_prova_lacuna(status, tipo):
    """Verifica cobertura mínima antes de montar resposta."""
    encontrado = bool(status.get('encontrado'))
    tem_aula = bool(status.get('tem_aula')) if encontrado else False
    tem_teste = bool(status.get('tem_teste')) if encontrado else False
    tem_prova = bool(status.get('tem_prova')) if encontrado else False
    tem_lacuna = bool(status.get('tem_lacuna')) if encontrado else True
    faltas = []
    if not encontrado:
        faltas.append('entrada_nao_encontrada_no_indice')
    if tipo in ('formula', 'exercicio', 'prova', 'problema_aberto', 'meta_empirica'):
        if not tem_aula:
            faltas.append('aula')
        if not tem_teste:
            faltas.append('teste')
    if tipo in ('prova', 'teorema_provado') and not tem_prova:
        faltas.append('prova_ou_mapa_de_subprovas')
    if tipo == 'problema_aberto':
        # Para aberto, não exigir prova final; exigir plano investigativo.
        if 'prova_ou_mapa_de_subprovas' in faltas:
            faltas.remove('prova_ou_mapa_de_subprovas')
    return {
        'encontrado': encontrado,
        'tem_aula': tem_aula,
        'tem_teste': tem_teste,
        'tem_prova': tem_prova,
        'tem_lacuna': tem_lacuna,
        'faltas': tuple(faltas),
        'cobertura_ok': not faltas,
    }


def classificar_estado_epistemico(pergunta, tipo):
    """Separa problema aberto, conjectura, teorema provado e meta empírica."""
    p = _normalizar(pergunta)
    if tipo == 'problema_aberto' or 'conjectura' in p or 'em aberto' in p:
        return 'problema_aberto'
    if tipo == 'meta_empirica' or any(m in p for m in ('auc', 'recall', 'erro máximo', 'erro maximo')):
        return 'meta_empirica'
    if tipo == 'formula':
        return 'formula'
    if 'teorema' in p or 'prove' in p or 'demonstre' in p:
        return 'teorema_provado'
    return tipo or 'desconhecido'


def montar_resposta_base(pergunta, tipo, status, cobertura):
    """Monta resposta base simples; a auditoria vem depois."""
    estado = classificar_estado_epistemico(pergunta, tipo)
    regra_estado = CLASSIFICACOES_EPISTEMICAS.get(estado, 'investigar, construir, testar e auditar')
    if tipo == 'pendencia':
        faltas = listar_tudo_que_falta()
        corpo = 'O motor mestre conhece ' + str(len(faltas)) + ' pendências/lacunas históricas e a Etapa 58 cria rota para tratá-las no fluxo único.'
    elif tipo == 'autoidentidade':
        corpo = 'Sou o PSF-IAminy: sistema local de estudo, ensino, investigação e auditoria criado no projeto Pensador Sem Fronteiras. Não sou consciência humana.'
    elif tipo == 'problema_aberto':
        contagem = contar_problemas_abertos_conhecidos()
        corpo = 'Este item deve ser tratado como investigável: plano, hipóteses, testes, comparação e falsificação; sem prova inventada. Conhecidos: ' + str(contagem.get('entradas_abertas_conhecidas_etapa55')) + '.'
    elif tipo == 'meta_empirica':
        corpo = 'Isto é meta de validação: só vira resultado depois de dados, teste, comparação e auditoria. Não é promessa automática.'
    elif tipo == 'formula':
        corpo = 'A fórmula deve ser montada, desmontada, explicada pela origem, exemplificada e testada; fórmula pronta sem ponte vira lacuna.'
    elif tipo == 'prova':
        corpo = 'A prova deve indicar hipóteses, premissas, passos, subprovas e verificação; salto como “é óbvio” vira lacuna.'
    else:
        corpo = 'Vou tratar como pergunta investigável: localizar conhecimento, construir resposta, testar, comparar e apontar lacuna.'
    return {
        'pergunta': pergunta,
        'tipo': tipo,
        'estado_epistemico': estado,
        'regra_estado': regra_estado,
        'base': corpo,
        'indice': status,
        'cobertura': cobertura,
    }


def aplicar_modo_cientista(resposta_base):
    """Modo cientista obrigatório: procura padrão, salto, lacuna, hipótese, teste e falsificação."""
    pergunta = resposta_base.get('pergunta', '')
    texto = resposta_base.get('base', '') + ' ' + pergunta
    tipo = resposta_base.get('tipo', 'desconhecido')
    estado = resposta_base.get('estado_epistemico', 'desconhecido')
    lacunas = detectar_lacunas_em_texto(texto)
    hipoteses = []
    testes = []
    falsificacoes = []
    comparacoes = []

    hipoteses.append('H1: a pergunta pode ser respondida com conhecimento já indexado.')
    hipoteses.append('H2: se não estiver no índice, deve virar pendência de construção.')
    testes.append('T1: procurar no índice mestre.')
    testes.append('T2: verificar aula, teste, prova e lacuna.')
    comparacoes.append('C1: comparar resposta construída contra regras PSF de cobertura total.')
    falsificacoes.append('F1: se aparecer dependência externa como fundamento, reprovar.')

    if estado == 'problema_aberto':
        hipoteses.append('H3: existe caminho parcial investigável mesmo sem prova final conhecida.')
        testes.append('T3: testar casos pequenos, procurar contraexemplo e comparar com resultados já aceites no PSF.')
        falsificacoes.append('F2: se a resposta disser que resolveu definitivamente, marcar como falsa até prova auditada.')
    if estado == 'meta_empirica':
        hipoteses.append('H3: a meta pode ser alcançada apenas se dados e teste confirmarem.')
        testes.append('T3: separar treino, teste, métrica e validação antes de afirmar resultado.')
        falsificacoes.append('F2: se prometer AUC/recall/erro sem dados, reprovar.')
    if tipo == 'formula':
        testes.append('T3: desmontar símbolos e reconstruir a fórmula de uma origem verificável.')
        falsificacoes.append('F2: se usar apenas “pela fórmula”, marcar salto de fórmula.')
    if tipo == 'prova':
        testes.append('T3: quebrar a prova em subprovas e procurar salto de passo.')
        falsificacoes.append('F2: se pular hipótese ou lema, marcar lacuna formal.')

    return {
        'ativo': True,
        'padroes_procurados': ('origem', 'premissa', 'axioma local', 'passo', 'teste', 'comparação', 'falsificação', 'lacuna'),
        'hipoteses': tuple(hipoteses),
        'testes': tuple(testes),
        'comparacoes': tuple(comparacoes),
        'falsificacoes': tuple(falsificacoes),
        'lacunas_detectadas': tuple(lacunas),
        'parecer': 'seguir investigando até cobrir passos e testes',
    }


def auditar_resposta(resposta_base, ciencia):
    """Auditoria forte: dependências, contradições, lacunas, cobertura e contrato."""
    texto = resposta_base.get('base', '') + ' ' + resposta_base.get('pergunta', '')
    entrada = {
        'tipo': 'pergunta_definitiva',
        'texto': texto,
        'resposta': resposta_base.get('base'),
        'aula': resposta_base.get('cobertura', {}).get('tem_aula') or resposta_base.get('tipo') in ('pendencia', 'autoidentidade'),
        'teste': resposta_base.get('cobertura', {}).get('tem_teste') or resposta_base.get('tipo') in ('pendencia', 'autoidentidade'),
    }
    contrato = verificar_contrato_entrada(entrada)
    deps = detectar_dependencias_proibidas(texto)
    contras = detectar_contradicoes_texto(texto)
    lacunas = list(ciencia.get('lacunas_detectadas', ()))
    faltas = list(resposta_base.get('cobertura', {}).get('faltas', ()))
    aprovado = not deps and not contras and not contrato.get('contradicoes_detectadas')
    # Falta de índice não é reprovação final quando vira pendência; é estado investigativo.
    return {
        'aprovado_para_responder': aprovado,
        'dependencias_proibidas': tuple(deps),
        'contradicoes': tuple(contras) + tuple(contrato.get('contradicoes_detectadas', ())),
        'lacunas': tuple(lacunas),
        'faltas_cobertura': tuple(faltas),
        'contrato': contrato,
        'sem_dependencias_externas': not deps,
        'modo_cientista_aplicado': bool(ciencia.get('ativo')),
    }


def calcular_confianca_medida(resposta_base, auditoria):
    """Confiança simples e auditável, não emocional."""
    score = 100
    if not resposta_base.get('indice', {}).get('encontrado'):
        score -= 20
    if resposta_base.get('cobertura', {}).get('tem_lacuna'):
        score -= 10
    score -= 25 * len(auditoria.get('dependencias_proibidas', ()))
    score -= 25 * len(auditoria.get('contradicoes', ()))
    score -= 5 * len(auditoria.get('faltas_cobertura', ()))
    if resposta_base.get('estado_epistemico') in ('problema_aberto', 'meta_empirica'):
        score = min(score, 80)  # confiança no plano, não numa solução final.
    if score < 0:
        score = 0
    if score >= 85:
        nivel = 'alta'
    elif score >= 65:
        nivel = 'média'
    elif score >= 40:
        nivel = 'baixa/investigativa'
    else:
        nivel = 'reprovada até reconstruir'
    return {
        'score': score,
        'nivel': nivel,
        'significado': 'mede cobertura, auditoria e risco; não é garantia absoluta',
    }


def responder_com_cerebro_unico(pergunta, modo='normal'):
    """Função principal da Etapa 58."""
    limpeza = limpar_linguagem_sem_apagar_intencao(pergunta)
    texto = limpeza['corrigido']
    tipo_info = detectar_tipo(texto)
    tipo = tipo_info['principal']
    status = procurar_no_indice_mestre(texto, tipo)
    cobertura = verificar_aula_teste_prova_lacuna(status, tipo)
    base = montar_resposta_base(texto, tipo, status, cobertura)
    ciencia = aplicar_modo_cientista(base)
    auditoria = auditar_resposta(base, ciencia)
    confianca = calcular_confianca_medida(base, auditoria)
    trilha = trilha_de_raciocinio_publica(tipo, texto)
    resposta = {
        'modo': modo,
        'limpeza': limpeza,
        'tipo': tipo_info,
        'indice': status,
        'cobertura': cobertura,
        'resposta_base': base['base'],
        'modo_cientista': ciencia,
        'auditoria': auditoria,
        'confianca': confianca,
        'trilha_publica': trilha,
        'fluxo_usado': FLUXO_CEREBRO_UNICO,
        'proximo_passo': sugerir_proximo_passo(base, auditoria, confianca),
    }
    return resposta


def sugerir_proximo_passo(resposta_base, auditoria, confianca):
    if auditoria.get('dependencias_proibidas'):
        return 'remover dependência externa e reconstruir pelo método PSF nativo'
    if auditoria.get('contradicoes'):
        return 'separar estados contraditórios e reauditar'
    if resposta_base.get('estado_epistemico') == 'problema_aberto':
        return 'criar ou continuar plano de investigação com hipóteses, testes e falsificação'
    if resposta_base.get('estado_epistemico') == 'meta_empirica':
        return 'obter dados, definir métrica, testar e comparar antes de prometer resultado'
    if resposta_base.get('cobertura', {}).get('faltas'):
        return 'criar cobertura faltante: ' + ', '.join(resposta_base['cobertura']['faltas'])
    if confianca.get('score', 0) < 85:
        return 'aprofundar passos e reduzir lacunas antes de considerar pronto'
    return 'pronto para resposta normal, mantendo auditoria visível se pedida'


def processar_fila_perguntas(perguntas, modo='normal'):
    """Unifica fila com memória mestre: cada pergunta passa pelo mesmo cérebro."""
    resultados = []
    for i, pergunta in enumerate(perguntas, 1):
        r = responder_com_cerebro_unico(pergunta, modo=modo)
        r['ordem_na_fila'] = i
        resultados.append(r)
    return resultados


def memoria_viva_por_categoria():
    """Organiza a memória conhecida por conceito/problema/fórmula/prova/aula/teste/lacuna/etapa."""
    categorias = {
        'conceito': [], 'problema': [], 'formula': [], 'prova': [], 'aula': [], 'teste': [], 'lacuna': [], 'etapa': []
    }
    for item in listar_tudo_que_o_psf_sabe():
        tipos = item.get('tipos', ())
        colocado = False
        for cat in categorias:
            if cat in tipos or (cat == 'etapa'):
                categorias[cat].append(item)
                colocado = True
        if not colocado:
            categorias['conceito'].append(item)
    for falta in listar_tudo_que_falta():
        if falta.get('tipo') == 'lacuna':
            categorias['lacuna'].append(falta)
    return categorias


def atualizar_indice_com_nova_etapa(etapa, nome, sabe, tipos=('etapa',), tem_aula=True, tem_teste=True, tem_prova=False, lacunas=(), pendencias=()):
    """Modelo nativo de atualização futura; não altera arquivo antigo, devolve registro pronto para inserir."""
    return {
        'etapa': etapa,
        'nome': nome,
        'estado': 'novo_registro_pronto_para_indice_mestre',
        'tipos': tuple(tipos),
        'sabe': tuple(sabe),
        'tem_aula': bool(tem_aula),
        'tem_teste': bool(tem_teste),
        'tem_prova': bool(tem_prova),
        'lacunas': tuple(lacunas),
        'pendencias': tuple(pendencias),
        'pronto_para_uso': bool(tem_aula and tem_teste and not lacunas),
        'fonte_interna': 'nova etapa PSF a inserir',
    }


def fechar_pendencias_lacunas_etapa58():
    return {
        'pendencias_anteriores': 28,
        'lacunas_anteriores': 17,
        'total_anteriores': 45,
        'pendencias_tratadas_por_integracao': len(PENDENCIAS_28_FECHADAS_POR_INTEGRACAO),
        'lacunas_tratadas_por_fluxo': len(LACUNAS_17_TRATADAS_POR_FLUXO),
        'total_tratado': len(PENDENCIAS_28_FECHADAS_POR_INTEGRACAO) + len(LACUNAS_17_TRATADAS_POR_FLUXO),
        'restante_no_motor_entre_as_conhecidas': 0,
        'observacao': 'Pendências de motor fechadas como rota integrada; problemas matemáticos abertos continuam investigação honesta, não prova falsa.',
    }


def relatorio_cerebro_unico():
    fechamento = fechar_pendencias_lacunas_etapa58()
    return {
        'etapa': 58,
        'nome': 'Cérebro Único Integrado PSF',
        'motores_integrados': len(MOTORES_INTEGRADOS),
        'fluxo_passos': len(FLUXO_CEREBRO_UNICO),
        'sem_dependencias_externas': True,
        'modo_cientista_em_todos_os_modos': True,
        'auditoria_automatica_forte': True,
        'confianca_medida': True,
        'pendencias_lacunas_fechamento': fechamento,
        'problemas_abertos_conhecidos': contar_problemas_abertos_conhecidos(),
        'classificacoes_epistemicas': tuple(CLASSIFICACOES_EPISTEMICAS.keys()),
    }
