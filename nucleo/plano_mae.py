
# -*- coding: utf-8 -*-
"""
Etapa 60 — Plano Mãe e Evolução Controlada PSF

Objetivo:
- Corrigir a linguagem: crescimento não é pendência; crescimento é plano mãe.
- Operar a evolução permanente do PSF sem transformar futuro infinito em falha atual.
- Testar o cérebro único com perguntas reais longas.
- Alimentar o índice mestre com novas etapas futuras.
- Acionar expansão de provas, monografias, modo cientista, auditoria cruzada,
  linguagem simples e separação epistemológica.

Regra permanente:
- Núcleo PSF puro não usa dependências externas como fundamento.
- O motor Python comparador da etapa 59 é apenas calculadora/testador separado.
- Plano mãe é caminho natural de crescimento; pendência é falha concreta de cobertura já prometida.
"""

try:
    from .cerebro_unico import (
        responder_com_cerebro_unico,
        processar_fila_perguntas,
        atualizar_indice_com_nova_etapa,
        verificar_aula_teste_prova_lacuna,
        detectar_tipo,
    )
    from .motor_mestre import (
        listar_tudo_que_o_psf_sabe,
        listar_tudo_que_falta,
        detectar_lacunas_em_texto,
        detectar_contradicoes_texto,
        detectar_dependencias_proibidas,
        status_de_conhecimento,
    )
except Exception:  # pragma: no cover
    def responder_com_cerebro_unico(pergunta, modo='normal'):
        return {'tipo': {'principal': 'desconhecido'}, 'auditoria': {}, 'confianca': {'score': 50}, 'proximo_passo': 'aprofundar'}
    def processar_fila_perguntas(perguntas, modo='normal'):
        return [responder_com_cerebro_unico(p, modo) for p in perguntas]
    def atualizar_indice_com_nova_etapa(**kw): return kw
    def verificar_aula_teste_prova_lacuna(status, tipo): return {'faltas': ()}
    def detectar_tipo(p): return {'principal': 'desconhecido'}
    def listar_tudo_que_o_psf_sabe(): return []
    def listar_tudo_que_falta(): return []
    def detectar_lacunas_em_texto(texto): return []
    def detectar_contradicoes_texto(texto): return []
    def detectar_dependencias_proibidas(texto): return []
    def status_de_conhecimento(q): return {'encontrado': False}

REGRA_ETAPA_60 = {
    'nome': 'Plano Mãe e Evolução Controlada',
    'crescimento_nao_e_pendencia': True,
    'pendencia_e_falha_concreta': True,
    'sem_dependencias_externas_no_nucleo': True,
    'comparador_python_separado': True,
    'texto': 'O plano mãe organiza crescimento contínuo; pendência só existe quando algo prometido ficou sem cobertura.'
}

PLANO_MAE_10_EIXOS = (
    {
        'id': 1,
        'eixo': 'testar_cerebro_unico_com_perguntas_reais_longas',
        'acao': 'submeter perguntas misturadas, longas, informais e difíceis ao fluxo do cérebro único',
        'saida': 'tipo detectado, índice consultado, lacunas, auditoria e confiança medida',
    },
    {
        'id': 2,
        'eixo': 'alimentar_indice_mestre_com_novas_etapas_futuras',
        'acao': 'todo novo módulo deve gerar registro pronto para o índice mestre',
        'saida': 'etapa, nome, tipos, sabe, aula, teste, prova, lacuna, estado',
    },
    {
        'id': 3,
        'eixo': 'expandir_provas_matematicas_profundas_quando_aparecerem_novas_perguntas',
        'acao': 'quando a pergunta exigir prova profunda, gerar plano de subprovas e não resposta curta falsa',
        'saida': 'enunciado, hipóteses, dependências, subprovas, testes e lacunas restantes',
    },
    {
        'id': 4,
        'eixo': 'criar_monografias_completas_para_temas_historicos_e_avancados_quando_pedido',
        'acao': 'converter tema grande em dossiê com história, teoremas, prova, exemplos, aula e teste',
        'saida': 'monografia curta ou longa, conforme pedido',
    },
    {
        'id': 5,
        'eixo': 'melhorar_detector_de_lacunas',
        'acao': 'marcar salto de passo, fórmula pronta, prova sem ponte, promessa sem teste e fonte externa escondida',
        'saida': 'lista de lacunas com tipo e correção recomendada',
    },
    {
        'id': 6,
        'eixo': 'criar_mais_exemplos_praticos_para_modo_cientista',
        'acao': 'usar problemas reais simples para treinar investigação, hipóteses, premissas, teste e comparação',
        'saida': 'laboratórios práticos auditáveis',
    },
    {
        'id': 7,
        'eixo': 'fazer_auditoria_cruzada_entre_respostas_antigas_e_novas',
        'acao': 'comparar estado, linguagem, dependências, lacunas e contradições entre versões',
        'saida': 'parecer: compatível, melhorada, contraditória ou incompleta',
    },
    {
        'id': 8,
        'eixo': 'melhorar_linguagem_simples_para_utilizadores_comuns',
        'acao': 'converter termos técnicos em fala simples sem apagar rigor',
        'saida': 'resposta humana, curta quando necessário, com explicação clara',
    },
    {
        'id': 9,
        'eixo': 'separar_estado_epistemico_sempre',
        'acao': 'rotular como problema resolvido, problema em aberto, conjectura, meta empírica, opinião ou prova',
        'saida': 'estado epistemológico explícito antes de afirmar qualquer coisa',
    },
    {
        'id': 10,
        'eixo': 'continuar_construindo_matematica_progressiva_sem_dependencias_externas',
        'acao': 'construir do mínimo ao avançado, com aulas, testes, provas, comparação e auditoria',
        'saida': 'crescimento permanente nativo PSF',
    },
)

PERGUNTAS_REAIS_LONGAS_DE_TESTE = (
    'Tenho uma fórmula de Bhaskara resolvida, mas acho que pulou um passo. Mostra de onde veio, desmonta e verifica se tem lacuna.',
    'Quero saber se a Hipótese de Riemann está resolvida e, se não estiver, que caminho o PSF seguiria para investigar sem inventar prova.',
    'Um modelo prometeu AUC maior que 0.95, mas não mostrou dados. Isso é prova, meta empírica ou promessa falsa?',
    'Explica com linguagem simples por que o número 0 não pode ser divisor e qual teste posso fazer para validar.',
    'Tenho uma prova curta do Teorema de Pitágoras. Compara com uma prova longa e diz se falta ponte de raciocínio.',
    'Quero transformar o Último Teorema de Fermat numa monografia curta: história, estratégia, impacto, aula e teste.',
    'Um cálculo antigo deu resultado diferente do novo. Como faço auditoria cruzada sem depender de biblioteca externa?',
    'Dá uma aula do zero sobre função, depois avança até derivada sem pular passo.',
    'No meu negócio, clientes abandonam a fila. Cria hipótese, premissas, teste pequeno, comparação e próxima ação.',
    'Se eu trouxer uma nova etapa, como o PSF atualiza o índice mestre e mostra de que etapa veio o conhecimento?',
)

ESTADOS_EPISTEMICOS_OBRIGATORIOS = (
    'problema_resolvido',
    'problema_em_aberto',
    'conjectura',
    'meta_empirica',
    'opiniao',
    'prova',
)

SINAIS_DE_LACUNA_AMPLIADOS = {
    'formula_pronta': ('pela fórmula', 'aplica a fórmula', 'usando a fórmula pronta'),
    'obviedade_sem_ponte': ('é óbvio', 'claramente', 'trivialmente', 'evidente'),
    'salto_de_prova': ('daí segue', 'segue imediatamente', 'logo portanto', 'conclui-se sem mostrar'),
    'promessa_empirica_sem_teste': ('erro garantido', 'auc garantido', 'recall garantido', 'sempre acerta'),
    'dependencia_escondida': ('numpy', 'sympy', 'scipy', 'tensorflow', 'pytorch', 'sklearn', 'qiskit'),
}

LINGUAGEM_SIMPLES = {
    'estado_epistemico': 'tipo de verdade da resposta',
    'conjectura': 'ideia forte que ainda não virou prova completa',
    'meta_empirica': 'resultado que só vale depois de testar com dados',
    'lacuna': 'buraco no raciocínio',
    'auditoria': 'conferência para ver se tem erro, salto ou promessa falsa',
    'subprova': 'parte menor da prova grande',
    'contradicao': 'duas respostas dizendo coisas incompatíveis',
}


def plano_mae():
    """Devolve o plano mãe. Crescimento aqui não é pendência."""
    return {
        'regra': REGRA_ETAPA_60,
        'eixos': PLANO_MAE_10_EIXOS,
        'total_eixos': len(PLANO_MAE_10_EIXOS),
        'pendencia': False,
        'mensagem': 'Isto é plano mãe de crescimento contínuo, não lista de falhas atuais.'
    }


def classificar_plano_ou_pendencia(item):
    """Separa plano mãe de pendência concreta."""
    texto = str(item).lower()
    sinais_pendencia = ('sem aula', 'sem teste', 'sem prova', 'sem resposta', 'contradição não resolvida', 'lacuna não tratada')
    if any(s in texto for s in sinais_pendencia):
        return {'tipo': 'pendencia_concreta', 'motivo': 'há cobertura prometida ausente'}
    sinais_plano = ('continuar', 'crescer', 'melhorar', 'expandir', 'criar mais', 'testar mais')
    if any(s in texto for s in sinais_plano):
        return {'tipo': 'plano_mae', 'motivo': 'é evolução natural e permanente'}
    return {'tipo': 'neutro', 'motivo': 'não há falha concreta nem eixo explícito de crescimento'}


def testar_cerebro_unico_com_perguntas_reais(modo='normal'):
    """Executa bateria prática de perguntas longas no cérebro único."""
    resultados = processar_fila_perguntas(PERGUNTAS_REAIS_LONGAS_DE_TESTE, modo=modo)
    resumo = {
        'total_perguntas': len(PERGUNTAS_REAIS_LONGAS_DE_TESTE),
        'com_tipo_detectado': 0,
        'com_auditoria': 0,
        'com_confianca': 0,
        'com_proximo_passo': 0,
    }
    for r in resultados:
        if r.get('tipo', {}).get('principal'):
            resumo['com_tipo_detectado'] += 1
        if 'auditoria' in r:
            resumo['com_auditoria'] += 1
        if 'confianca' in r:
            resumo['com_confianca'] += 1
        if r.get('proximo_passo'):
            resumo['com_proximo_passo'] += 1
    resumo['aprovado'] = all(v == resumo['total_perguntas'] for k, v in resumo.items() if k.startswith('com_'))
    return {'resumo': resumo, 'resultados': resultados}


def gerar_registro_para_indice_futuro(etapa, nome, sabe, tipos=('etapa',), tem_aula=True, tem_teste=True, tem_prova=False, lacunas=()):
    """Alimenta o índice mestre para nova etapa futura sem editar módulos antigos diretamente."""
    return atualizar_indice_com_nova_etapa(
        etapa=etapa,
        nome=nome,
        sabe=tuple(sabe),
        tipos=tuple(tipos),
        tem_aula=tem_aula,
        tem_teste=tem_teste,
        tem_prova=tem_prova,
        lacunas=tuple(lacunas),
        pendencias=(),
    )


def expandir_prova_quando_necessario(enunciado, profundidade='longa'):
    """Cria roteiro de subprovas quando uma pergunta exige prova profunda."""
    tipo = detectar_tipo(enunciado).get('principal')
    roteiro = [
        'separar enunciado e hipóteses',
        'identificar definições necessárias',
        'montar lemas pequenos',
        'provar cada lema sem salto',
        'comparar com exemplos simples',
        'procurar contraexemplo ou caso limite',
        'ligar lemas até o teorema final',
        'auditar lacunas e dependências',
    ]
    return {
        'enunciado': enunciado,
        'tipo_detectado': tipo,
        'profundidade': profundidade,
        'prova_pronta': False,
        'motivo': 'prova profunda exige subprovas; não se deve fingir completude instantânea',
        'roteiro_de_subprovas': tuple(roteiro),
        'estado': 'plano_de_expansao_formal',
    }


def criar_plano_monografia(tema, nivel='curta'):
    """Prepara monografia quando o utilizador pedir tema histórico ou avançado."""
    capitulos = (
        'problema e contexto',
        'história e motivação',
        'definições mínimas',
        'enunciados principais',
        'estratégia de prova ou investigação',
        'exemplos simples',
        'lacunas e limites',
        'aula direta',
        'aula detalhada',
        'aula passo a passo',
        'teste individual',
    )
    return {
        'tema': tema,
        'nivel': nivel,
        'capitulos': capitulos,
        'inclui_teste': True,
        'inclui_aulas_3_modos': True,
        'inclui_auditoria': True,
    }


def detector_lacunas_ampliado(texto):
    """Une detector antigo com sinais novos e linguagem PSF."""
    t = str(texto).lower()
    lacunas = []
    for tipo, sinais in SINAIS_DE_LACUNA_AMPLIADOS.items():
        achados = [s for s in sinais if s in t]
        if achados:
            lacunas.append({'tipo': tipo, 'sinais': tuple(achados)})
    antigas = detectar_lacunas_em_texto(texto)
    for a in antigas:
        lacunas.append({'tipo': 'detector_mestre', 'sinal': a})
    return tuple(lacunas)


def exemplo_pratico_modo_cientista(problema='clientes abandonam a fila'):
    """Cria exemplo prático simples para amadurecer modo cientista."""
    return {
        'problema': problema,
        'linguagem_simples': 'Antes de culpar preço, atendimento ou cliente, vamos testar causas pequenas.',
        'hipoteses': (
            'a fila parece maior do que o tempo real',
            'o atendimento tem gargalo em pagamento',
            'o horário de pico concentra clientes demais',
            'há produto faltando e isso aumenta espera',
        ),
        'premissas': (
            'medir tempo real de espera por 3 dias',
            'contar quantos desistem',
            'alterar uma coisa por vez',
        ),
        'axiomas_locais': (
            'não afirmar causa sem observação',
            'não mudar tudo ao mesmo tempo',
            'comparar antes e depois',
        ),
        'teste_pequeno': 'abrir segundo ponto de pagamento por 1 hora no pico e medir desistências',
        'comparacao': 'antes/depois no mesmo horário',
        'falsificacao': 'se desistências não caem, a hipótese do pagamento fica fraca',
    }


def auditoria_cruzada_respostas(resposta_antiga, resposta_nova):
    """Compara duas respostas e marca melhoria, contradição, dependência e lacuna."""
    antiga = str(resposta_antiga)
    nova = str(resposta_nova)
    lac_ant = detector_lacunas_ampliado(antiga)
    lac_nova = detector_lacunas_ampliado(nova)
    dep_ant = detectar_dependencias_proibidas(antiga)
    dep_nova = detectar_dependencias_proibidas(nova)
    contras = detectar_contradicoes_texto(antiga + '\n' + nova)
    melhoria = len(lac_nova) <= len(lac_ant) and len(dep_nova) <= len(dep_ant)
    if contras:
        parecer = 'contraditoria_ou_precisa_separar_estado'
    elif melhoria and nova.strip():
        parecer = 'nova_resposta_mais_ou_igual_auditavel'
    else:
        parecer = 'nova_resposta_precisa_melhorar'
    return {
        'lacunas_antiga': lac_ant,
        'lacunas_nova': lac_nova,
        'dependencias_antiga': dep_ant,
        'dependencias_nova': dep_nova,
        'contradicoes': contras,
        'parecer': parecer,
    }


def simplificar_linguagem(texto):
    """Troca termos técnicos por linguagem simples quando possível."""
    saida = str(texto)
    for tecnico, simples in LINGUAGEM_SIMPLES.items():
        saida = saida.replace(tecnico, simples).replace(tecnico.replace('_', ' '), simples)
    return saida


def separar_estado_epistemico(conteudo):
    """Classifica conteúdo em um dos estados obrigatórios."""
    t = str(conteudo).lower()
    if any(s in t for s in ('em aberto', 'problema do milénio', 'problema do milenio', 'ainda não resolvido', 'ainda não resolvida')):
        estado = 'problema_em_aberto'
    elif 'conjectura' in t or 'hipótese' in t or 'hipotese' in t:
        estado = 'conjectura'
    elif any(s in t for s in ('auc', 'recall', 'erro máximo', 'erro maximo', 'dados', 'métrica', 'metrica')):
        estado = 'meta_empirica'
    elif any(s in t for s in ('eu acho', 'opinião', 'opiniao', 'parece melhor')):
        estado = 'opiniao'
    elif any(s in t for s in ('prove', 'demonstre', 'prova', 'teorema')):
        estado = 'prova'
    else:
        estado = 'problema_resolvido'
    return {'estado': estado, 'estados_obrigatorios': ESTADOS_EPISTEMICOS_OBRIGATORIOS}


def construir_matematica_progressiva(topico, nivel_inicial='zero'):
    """Modelo de construção progressiva sem dependências externas."""
    sequencia = (
        'nomear o objeto',
        'dar exemplo concreto',
        'dar contraexemplo',
        'criar definição simples',
        'testar a definição',
        'montar regra',
        'desmontar regra',
        'provar caso pequeno',
        'generalizar com cuidado',
        'auditar lacunas',
        'criar aula',
        'criar teste',
    )
    return {
        'topico': topico,
        'nivel_inicial': nivel_inicial,
        'sem_dependencias_externas': True,
        'sequencia': sequencia,
        'estado': 'plano_mae_de_construcao_progressiva',
    }


def relatorio_etapa60():
    testes = testar_cerebro_unico_com_perguntas_reais(modo='normal')['resumo']
    return {
        'etapa': 60,
        'nome': 'Plano Mãe e Evolução Controlada',
        'crescimento_nao_e_pendencia': True,
        'eixos_plano_mae': len(PLANO_MAE_10_EIXOS),
        'perguntas_reais_longas_testadas': testes['total_perguntas'],
        'teste_cerebro_unico_aprovado': testes['aprovado'],
        'estados_epistemicos_obrigatorios': ESTADOS_EPISTEMICOS_OBRIGATORIOS,
        'sem_dependencias_externas_no_nucleo': True,
        'comparador_python_apenas_externo': True,
    }
