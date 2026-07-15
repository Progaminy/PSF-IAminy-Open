# -*- coding: utf-8 -*-
"""
Etapa 57 — Motor Mestre PSF

Objetivo:
- Unificar as etapas conhecidas num registo central auditável.
- Responder: o que sei, o que falta, onde está, de que etapa veio,
  se tem aula/teste/prova/lacuna, se contradiz algo e se está pronto.
- Melhorar auditoria, investigação, comparação e contratos internos.

Regra permanente:
- Sem dependências externas como fundamento.
- Apenas Python base como suporte físico de execução.
"""

REGRA_PERMANENTE_SEM_DEPENDENCIAS = {
    'estado': 'PERMANENTE',
    'texto': 'Nem agora nem depois o núcleo PSF usa dependências externas como fundamento.',
    'proibidos_como_fundamento': (
        'internet', 'api externa', 'llm externo', 'math', 'numpy', 'sympy', 'scipy',
        'sklearn', 'tensorflow', 'pytorch', 'qiskit', 'solver externo', 'biblioteca externa'
    ),
    'permitido': 'Python base apenas como suporte físico de organização e execução local.'
}

TIPOS_MEMORIA = (
    'conceito', 'problema', 'formula', 'prova', 'aula', 'teste', 'lacuna', 'etapa',
    'monografia', 'curiosidade', 'modo', 'auditoria', 'investigacao', 'contrato'
)

# Registo mestre conhecido até esta etapa. Para etapas antigas, o registo é um índice
# central resumido; para etapas recentes, também há módulos físicos no pacote.
ETAPAS_MESTRE = [
    {
        'etapa': 29,
        'nome': 'Conversa fluida',
        'estado': 'conhecido_indexado',
        'tipos': ('modo', 'aula', 'conversa'),
        'sabe': ('conversa fluida', 'resposta natural', 'interação humana'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('precisa integrar no índice mestre',),
        'pendencias': ('ligar conversa fluida ao motor mestre',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 30,
        'nome': 'Motores aprimorados',
        'estado': 'conhecido_indexado',
        'tipos': ('modo', 'aula', 'motor'),
        'sabe': ('motores de ensino', 'léxico expandido', 'matemática infinita em direção'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('matemática infinita precisa sempre de construção progressiva',),
        'pendencias': ('ligar léxico ao corretor e ao modo cientista',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 31,
        'nome': 'Bateria matemática nativa 100',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'teste', 'aritmetica'),
        'sabe': ('100 problemas básicos', 'aritmética nativa', 'sem math como fundamento'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('revalidar cobertura no verificador mestre',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 32,
        'nome': 'Respostas explicadas',
        'estado': 'conhecido_indexado',
        'tipos': ('aula', 'problema', 'explicacao'),
        'sabe': ('imagem mental', 'explicação humana', '100 problemas visuais'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('padronizar explicação com motor de passos',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 33,
        'nome': 'Modos universais de resposta',
        'estado': 'conhecido_indexado',
        'tipos': ('modo', 'resposta'),
        'sabe': ('pronta', 'curta', 'media', 'normal', 'linha'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('alinhar modos com investigação obrigatória',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 34,
        'nome': 'Aulas fixas e execução em lote',
        'estado': 'conhecido_indexado',
        'tipos': ('aula', 'fila', 'execucao'),
        'sabe': ('aula direta', 'aula detalhada', 'aula passo a passo', 'perguntas em lote'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('unificar fila de perguntas com memória mestre',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 35,
        'nome': 'Bateria progressiva 200',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'matematica'),
        'sabe': ('200 problemas progressivos', 'resolução por lote'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('ligar problemas ao índice mestre por conceito',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 36,
        'nome': 'Ortografia e bateria 100',
        'estado': 'conhecido_indexado',
        'tipos': ('lingua', 'correcao', 'problema'),
        'sabe': ('correção ortográfica conservadora', 'preservar números', 'preservar frações'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('corretor ainda deve aprender por sessão sem apagar intenção do utilizador',),
        'pendencias': ('integrar ortografia no roteador mestre de perguntas',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 37,
        'nome': 'Matemática avançada progressiva',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'conceito', 'matematica_avancada'),
        'sabe': ('inequações', 'funções', 'trigonometria', 'geometria analítica', 'Bayes', 'limites'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('alguns conceitos foram inicialmente marcados como fronteira',),
        'pendencias': ('confirmar se todos os conceitos fronteira foram construídos depois',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 38,
        'nome': 'Conceitos avançados construídos',
        'estado': 'conhecido_indexado',
        'tipos': ('conceito', 'construcao'),
        'sabe': ('14 conceitos avançados construídos operacionalmente',),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('construção operacional inicial não significa completude infinita',),
        'pendencias': ('aprofundar provas formais de cada conceito avançado',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 39,
        'nome': 'Definitividade matemática',
        'estado': 'conhecido_indexado',
        'tipos': ('contrato', 'regra', 'matematica'),
        'sabe': ('tudo que o utilizador traz é definitivo por padrão', 'DEFINITIVO_REGISTADO'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('aplicar definitividade a todos os novos registros automaticamente',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 40,
        'nome': 'Matemática superior definitiva',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'conceito', 'ensino'),
        'sabe': ('250 perguntas superiores', 'cálculo', 'álgebra', 'topologia'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('algumas provas exigem expansão monográfica',),
        'pendencias': ('ligar cada pergunta a prova longa quando necessário',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 41,
        'nome': 'Cálculo integral I-II',
        'estado': 'conhecido_indexado_em_expansao',
        'tipos': ('problema', 'calculo', 'fourier', 'edo'),
        'sabe': ('200 questões cálculo integral', 'Fourier', 'complexa', 'EDO'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('estado corrigido para registrado em expansão por cobertura individual inicial insuficiente',),
        'pendencias': ('garantir resposta+aula+teste individual para todas as 200',),
        'pronto_para_uso': False,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 42,
        'nome': 'Cobertura total resposta aula teste',
        'estado': 'conhecido_indexado',
        'tipos': ('contrato', 'auditoria', 'cobertura'),
        'sabe': ('toda pergunta definitiva deve ter resposta, aula e teste'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('usar este contrato no motor mestre para reprovar incompletos',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 43,
        'nome': 'Matemática pesquisa definitiva',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'pesquisa', 'aula'),
        'sabe': ('200 problemas de pesquisa', 'funcional', 'medida', 'PDE', 'ergódica'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('teoremas monumentais precisam de subprovas e mapas longos',),
        'pendencias': ('expandir teoremas monumentais sem fingir prova curta',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 44,
        'nome': 'Provas longas e respostas completas',
        'estado': 'conhecido_indexado',
        'tipos': ('prova', 'aula', 'problema'),
        'sabe': ('provas longas', 'respostas completas', 'desenvolvimento rigoroso'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('problemas abertos não recebem prova inventada',),
        'pendencias': ('separar teorema provado de conjectura aberta em todo conteúdo',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 45,
        'nome': 'Pesquisa extrema definitiva',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'pesquisa_extrema', 'investigacao'),
        'sabe': ('100 problemas extremos', 'fronteira matemática', 'problemas abertos identificados'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('problemas abertos precisam investigação, não solução falsa',),
        'pendencias': ('manter lista herdada de abertos',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 46,
        'nome': '10 monografias matemática',
        'estado': 'conhecido_indexado',
        'tipos': ('monografia', 'aula', 'prova'),
        'sabe': ('Gauss-Bonnet', 'teorema espectral', 'Poincaré', 'Riemann-Roch', 'Langlands', 'Atiyah-Singer', 'Gibbs', 'LWE', 'De Giorgi-Nash-Moser', 'C*-álgebras'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('monografias podem crescer em capítulos e subprovas',),
        'pendencias': ('transformar monografias em trilho completo se exigido',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 47,
        'nome': 'Problemas PhD sem dependências',
        'estado': 'conhecido_indexado',
        'tipos': ('problema', 'phd', 'posdoc', 'industria', 'startup'),
        'sabe': ('50 problemas definitivos', 'metas empíricas como validação, não promessa'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('metas como AUC/recall/erro dependem de dados reais',),
        'pendencias': ('separar prova matemática de teste empírico',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 48,
        'nome': 'Problemas em aberto definitivos',
        'estado': 'conhecido_indexado',
        'tipos': ('problema_aberto', 'investigacao', 'aula'),
        'sabe': ('60 problemas em aberto', 'resposta honesta', 'plano de investigação'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('não há prova porque estão abertos',),
        'pendencias': ('investigar sem prometer resolução',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 49,
        'nome': 'Problemas históricos resolvidos',
        'estado': 'conhecido_indexado',
        'tipos': ('historia', 'problema_resolvido', 'prova'),
        'sabe': ('10 problemas históricos resolvidos', 'contexto', 'estratégia', 'impacto'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': ('provas completas podem ser convertidas em monografias próprias',),
        'pendencias': ('aprofundar cada prova histórica quando pedido',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 50,
        'nome': 'Montar e desmontar fórmulas',
        'estado': 'conhecido_indexado',
        'tipos': ('formula', 'desmontagem', 'aula', 'teste'),
        'sabe': ('39 fórmulas', 'montagem', 'desmontagem', 'exemplo', 'passo a passo'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': True,
        'lacunas': (),
        'pendencias': ('ligar todas as fórmulas ao motor de lacunas',),
        'pronto_para_uso': True,
        'fonte_interna': 'histórico do projeto PSF-IAminy'
    },
    {
        'etapa': 51,
        'nome': 'Curiosidades matemáticas 300',
        'estado': 'modulo_presente',
        'tipos': ('curiosidade', 'historia', 'tecnologia', 'aula', 'teste'),
        'sabe': ('300 perguntas de números, geometria, história, probabilidade, arte e tecnologia',),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('itens com atualmente são atualizáveis localmente',),
        'pendencias': ('se houver dado temporal, não congelar como verdade eterna',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 51'
    },
    {
        'etapa': 52,
        'nome': 'Modo cientista',
        'estado': 'modulo_presente',
        'tipos': ('modo', 'investigacao', 'auditoria'),
        'sabe': ('padrões', 'lacunas', 'saltos de passo', 'brechas', 'comparação'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('aplicar modo cientista em todos os modos de resposta',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 52'
    },
    {
        'etapa': 53,
        'nome': 'Laboratório científico PSF',
        'estado': 'modulo_presente',
        'tipos': ('investigacao', 'laboratorio', 'teste'),
        'sabe': ('problema real simples', 'causas', 'hipóteses', 'premissas', 'axiomas locais', 'teste pequeno'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('expandir para múltiplos problemas reais',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 53'
    },
    {
        'etapa': 54,
        'nome': 'Investigação problemas em aberto',
        'estado': 'modulo_presente_corrigido_por_etapa_55',
        'tipos': ('problema_aberto', 'investigacao'),
        'sabe': ('60 planos de investigação', 'hipóteses', 'falsificação'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('foi limitado aos 60 explícitos e corrigido na etapa 55',),
        'pendencias': (),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 54'
    },
    {
        'etapa': 55,
        'nome': 'Todos problemas abertos cobertura total',
        'estado': 'modulo_presente',
        'tipos': ('problema_aberto', 'cobertura_total', 'investigacao'),
        'sabe': ('81 entradas abertas/investigáveis conhecidas', 'cobertura total corrigida'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': ('novos problemas abertos futuros devem entrar automaticamente',),
        'pendencias': ('monitorar novos abertos acrescentados pelo utilizador',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 55'
    },
    {
        'etapa': 56,
        'nome': 'Autoidentidade confiança auditoria',
        'estado': 'modulo_presente',
        'tipos': ('autoidentidade', 'confianca', 'auditoria'),
        'sabe': ('quem é o PSF', 'quem criou', 'base matemática', 'por que confiar', 'fontes confiáveis'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('ligar respostas de confiança ao índice mestre',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 56'
    },
    {
        'etapa': 57,
        'nome': 'Motor mestre de memória, pendências e auditoria total',
        'estado': 'modulo_presente',
        'tipos': ('memoria', 'auditoria', 'contrato', 'comparacao', 'verificador', 'indice_mestre'),
        'sabe': ('índice mestre', 'lista do que sabe', 'lista do que falta', 'lacunas', 'contradições', 'contratos internos'),
        'tem_aula': True, 'tem_teste': True, 'tem_prova': False,
        'lacunas': (),
        'pendencias': ('continuar atualizando o mestre quando surgirem novas etapas',),
        'pronto_para_uso': True,
        'fonte_interna': 'módulo físico etapa 57'
    }
]

# Entradas explícitas de memória por tipo. Não substitui as etapas; organiza por uso.
MEMORIA_POR_TIPO = {
    'conceito': (
        'aritmética nativa', 'conceitos avançados construídos', 'matemática superior',
        'C*-álgebras', 'K-teoria', 'PDE', 'topologia', 'geometria', 'probabilidade',
        'modo cientista', 'contrato de cobertura total'
    ),
    'problema': (
        '100 problemas básicos', '100 problemas visuais', '200 progressivos',
        '250 superiores', '200 cálculo integral', '200 pesquisa', '100 pesquisa extrema',
        '50 PhD/pós-doc/indústria/startup', '300 curiosidades'
    ),
    'formula': ('39 fórmulas montar/desmontar',),
    'prova': ('provas longas etapa 44', 'provas históricas etapa 49', 'monografias etapa 46'),
    'aula': ('aula direta', 'aula detalhada', 'aula passo a passo'),
    'teste': ('teste individual por item definitivo', 'testes de cobertura total', 'testes de auditoria'),
    'lacuna': ('conceito em expansão', 'dado temporal atualizável', 'problema aberto sem prova', 'meta empírica sem dados'),
    'etapa': tuple('Etapa ' + str(e['etapa']) for e in ETAPAS_MESTRE),
}

CONTRATOS_INTERNOS = {
    'sem_dependencias_externas': 'Nenhum conhecimento pode depender de biblioteca, API, internet ou LLM externo como fundamento.',
    'cobertura_total': 'Toda pergunta definitiva precisa resposta, aula e teste.',
    'problema_aberto': 'Problema em aberto recebe investigação; não recebe prova inventada.',
    'metrica_empirica': 'Erro, AUC, recall e similares são metas de validação, não promessa antes de dados reais.',
    'passo_a_passo': 'Se houver salto de fórmula, salto de prova ou frase vazia, marcar lacuna.',
    'definitividade': 'Conteúdo trazido pelo utilizador entra como definitivo salvo correção posterior.'
}

EXPRESSOES_SUSPEITAS_DE_LACUNA = (
    'é óbvio', 'obviamente', 'pela fórmula', 'sabemos que', 'trivialmente',
    'claramente', 'basta ver', 'segue diretamente', 'sem mostrar', 'por magia',
    'resultado conhecido', 'aplica-se e pronto'
)

DEPENDENCIAS_PROIBIDAS_TEXTO = REGRA_PERMANENTE_SEM_DEPENDENCIAS['proibidos_como_fundamento']


def _normalizar(texto):
    return str(texto).lower().strip()


def listar_etapas():
    """Retorna cópia simples do índice de etapas conhecidas."""
    return [dict(e) for e in ETAPAS_MESTRE]


def indice_mestre_por_etapa():
    """Mapa etapa -> resumo central."""
    return {e['etapa']: dict(e) for e in ETAPAS_MESTRE}


def listar_tudo_que_o_psf_sabe():
    """Lista sintética de tudo que o PSF conhece por etapa e por tipo."""
    itens = []
    for etapa in ETAPAS_MESTRE:
        for conhecimento in etapa['sabe']:
            itens.append({
                'etapa': etapa['etapa'],
                'origem': etapa['nome'],
                'conhecimento': conhecimento,
                'tipos': etapa['tipos'],
                'estado': etapa['estado'],
                'tem_aula': etapa['tem_aula'],
                'tem_teste': etapa['tem_teste'],
                'tem_prova': etapa['tem_prova'],
                'pronto_para_uso': etapa['pronto_para_uso'],
            })
    return itens


def listar_tudo_que_falta():
    """Lista pendências conhecidas e lacunas abertas."""
    faltas = []
    for etapa in ETAPAS_MESTRE:
        for pendencia in etapa.get('pendencias', ()):
            faltas.append({'etapa': etapa['etapa'], 'tipo': 'pendencia', 'item': pendencia})
        for lacuna in etapa.get('lacunas', ()):
            faltas.append({'etapa': etapa['etapa'], 'tipo': 'lacuna', 'item': lacuna})
        if not etapa.get('tem_aula'):
            faltas.append({'etapa': etapa['etapa'], 'tipo': 'aula_faltando', 'item': etapa['nome']})
        if not etapa.get('tem_teste'):
            faltas.append({'etapa': etapa['etapa'], 'tipo': 'teste_faltando', 'item': etapa['nome']})
    return faltas


def listar_problemas_em_aberto():
    """Problemas/entradas abertas conhecidas no índice mestre."""
    abertos = []
    for etapa in ETAPAS_MESTRE:
        if 'problema_aberto' in etapa['tipos'] or 'investigacao' in etapa['tipos']:
            abertos.append({
                'etapa': etapa['etapa'],
                'nome': etapa['nome'],
                'estado': etapa['estado'],
                'sabe': etapa['sabe'],
                'tem_plano': True,
                'tem_prova': etapa['tem_prova'],
                'observacao': 'investigar sem prova inventada' if not etapa['tem_prova'] else 'contém provas quando o tema é resolvido'
            })
    return abertos


def contar_problemas_abertos_conhecidos():
    """Contagem operacional herdada da etapa 55."""
    return {
        'entradas_abertas_conhecidas_etapa55': 81,
        'faltando_entre_conhecidas': 0,
        'regra': 'novos problemas abertos futuros devem ser adicionados automaticamente ao índice mestre'
    }


def listar_conceitos_incompletos():
    """Conceitos que existem, mas ainda têm lacuna, expansão ou dependem de dados reais."""
    incompletos = []
    for etapa in ETAPAS_MESTRE:
        estado = etapa.get('estado', '')
        tem_lacuna = bool(etapa.get('lacunas'))
        em_expansao = 'expansao' in estado or 'corrigido' in estado
        if tem_lacuna or em_expansao or not etapa.get('pronto_para_uso'):
            incompletos.append({
                'etapa': etapa['etapa'],
                'nome': etapa['nome'],
                'estado': estado,
                'lacunas': etapa.get('lacunas', ()),
                'pendencias': etapa.get('pendencias', ()),
                'pronto_para_uso': etapa.get('pronto_para_uso')
            })
    return incompletos


def onde_esta_conhecimento(consulta):
    """Procura em etapa, nome, tipos, saberes, lacunas e pendências."""
    alvo = _normalizar(consulta)
    achados = []
    for etapa in ETAPAS_MESTRE:
        campos = [etapa['nome'], etapa['estado'], etapa['fonte_interna']]
        campos += list(etapa['tipos'])
        campos += list(etapa['sabe'])
        campos += list(etapa.get('lacunas', ()))
        campos += list(etapa.get('pendencias', ()))
        texto = ' '.join(_normalizar(c) for c in campos)
        if alvo in texto:
            achados.append({
                'etapa': etapa['etapa'],
                'nome': etapa['nome'],
                'estado': etapa['estado'],
                'tem_aula': etapa['tem_aula'],
                'tem_teste': etapa['tem_teste'],
                'tem_prova': etapa['tem_prova'],
                'lacunas': etapa.get('lacunas', ()),
                'pronto_para_uso': etapa['pronto_para_uso'],
                'fonte_interna': etapa['fonte_interna']
            })
    return achados


def status_de_conhecimento(consulta):
    """Resposta estruturada para: onde está, veio de que etapa, completo, teste, aula, prova, lacuna."""
    achados = onde_esta_conhecimento(consulta)
    if not achados:
        return {
            'consulta': consulta,
            'encontrado': False,
            'resposta': 'Não encontrei este conhecimento no índice mestre conhecido. Deve entrar como pendência de construção.'
        }
    principal = achados[0]
    return {
        'consulta': consulta,
        'encontrado': True,
        'onde_esta': principal['nome'],
        'etapa': principal['etapa'],
        'completo': principal['pronto_para_uso'] and not bool(principal['lacunas']),
        'tem_teste': principal['tem_teste'],
        'tem_aula': principal['tem_aula'],
        'tem_prova': principal['tem_prova'],
        'tem_lacuna': bool(principal['lacunas']),
        'lacunas': principal['lacunas'],
        'pronto_para_uso': principal['pronto_para_uso'],
        'contradiz_algo': False,
        'observacao': 'Use auditoria se a resposta concreta tiver passos ou fórmulas.'
    }


def detectar_lacunas_em_texto(texto):
    """Marca saltos de passo, fórmulas prontas e promessas sem teste."""
    t = _normalizar(texto)
    lacunas = []
    for exp in EXPRESSOES_SUSPEITAS_DE_LACUNA:
        if exp in t:
            lacunas.append({'tipo': 'salto_de_explicacao', 'marcador': exp})
    if 'auc > 0,95' in t or 'recall > 0,85' in t or 'erro máximo' in t or 'erro maximo' in t:
        if 'teste' not in t and 'valid' not in t and 'dados' not in t:
            lacunas.append({'tipo': 'promessa_empirica_sem_validacao', 'marcador': 'métrica sem teste/dados'})
    if 'prova' in t and 'conjectura' in t and 'resolvido' in t:
        lacunas.append({'tipo': 'possivel_confusao_aberto_resolvido', 'marcador': 'prova + conjectura + resolvido'})
    return lacunas


def detectar_dependencias_proibidas(texto):
    """Detecta nomes de dependências proibidas aparecendo como possível fundamento."""
    t = _normalizar(texto)
    achadas = []
    for dep in DEPENDENCIAS_PROIBIDAS_TEXTO:
        if dep in t:
            achadas.append(dep)
    return achadas


def detectar_contradicoes_texto(texto):
    """Detector conservador de contradições internas simples."""
    t = _normalizar(texto)
    contradicoes = []
    if 'sem depend' in t and any(dep in t for dep in ('numpy', 'sympy', 'qiskit', 'tensorflow', 'pytorch', 'sklearn')):
        contradicoes.append('Diz sem dependências, mas menciona biblioteca externa como possível fundamento.')
    if 'problema em aberto' in t and ('provado definitivamente' in t or 'resolvido definitivamente' in t):
        contradicoes.append('Diz que é aberto e também que foi resolvido/provado definitivamente.')
    if 'prometo' in t and any(m in t for m in ('auc', 'recall', 'erro máximo', 'erro maximo')):
        contradicoes.append('Promessa de métrica empírica antes de validação.')
    return contradicoes


def verificar_contrato_entrada(entrada):
    """Verificador PSF nativo para uma entrada de conhecimento."""
    texto = entrada.get('texto', '') if isinstance(entrada, dict) else str(entrada)
    tipo = entrada.get('tipo', '') if isinstance(entrada, dict) else ''
    tem_resposta = bool(entrada.get('resposta')) if isinstance(entrada, dict) else False
    tem_aula = bool(entrada.get('aula')) if isinstance(entrada, dict) else False
    tem_teste = bool(entrada.get('teste')) if isinstance(entrada, dict) else False
    deps = detectar_dependencias_proibidas(texto)
    lacunas = detectar_lacunas_em_texto(texto)
    contradicoes = detectar_contradicoes_texto(texto)
    faltas = []
    if tipo in ('pergunta_definitiva', 'problema', 'formula'):
        if not tem_resposta:
            faltas.append('resposta')
        if not tem_aula:
            faltas.append('aula')
        if not tem_teste:
            faltas.append('teste')
    aprovado = not deps and not contradicoes and not faltas
    return {
        'aprovado': aprovado,
        'dependencias_proibidas_detectadas': deps,
        'lacunas_detectadas': lacunas,
        'contradicoes_detectadas': contradicoes,
        'faltas_de_cobertura': faltas,
        'contratos_aplicados': tuple(CONTRATOS_INTERNOS.keys())
    }


def comparar_respostas(antiga, nova):
    """Compara resposta antiga vs nova de forma nativa e simples."""
    a = _normalizar(antiga)
    n = _normalizar(nova)
    resultado = {
        'mesma_resposta': a == n,
        'antiga_tamanho': len(a),
        'nova_tamanho': len(n),
        'nova_mais_detalhada': len(n) > len(a),
        'antiga_lacunas': detectar_lacunas_em_texto(a),
        'nova_lacunas': detectar_lacunas_em_texto(n),
        'antiga_dependencias': detectar_dependencias_proibidas(a),
        'nova_dependencias': detectar_dependencias_proibidas(n),
    }
    if resultado['nova_dependencias']:
        resultado['parecer'] = 'nova pior: contém dependência proibida como possível fundamento'
    elif len(resultado['nova_lacunas']) < len(resultado['antiga_lacunas']):
        resultado['parecer'] = 'nova melhor: removeu lacunas'
    elif resultado['nova_mais_detalhada'] and not resultado['nova_lacunas']:
        resultado['parecer'] = 'nova melhor: mais detalhada sem lacunas detectadas'
    elif resultado['mesma_resposta']:
        resultado['parecer'] = 'sem mudança real'
    else:
        resultado['parecer'] = 'precisa auditoria humana/PSF adicional'
    return resultado


def comparar_prova_curta_longa(prova_curta, prova_longa):
    """Compara prova curta vs prova longa pela presença de passos e lacunas."""
    curta_lacunas = detectar_lacunas_em_texto(prova_curta)
    longa_lacunas = detectar_lacunas_em_texto(prova_longa)
    return {
        'prova_longa_tem_mais_conteudo': len(str(prova_longa)) > len(str(prova_curta)),
        'lacunas_na_curta': curta_lacunas,
        'lacunas_na_longa': longa_lacunas,
        'parecer': 'prova longa preferível' if len(longa_lacunas) <= len(curta_lacunas) and len(str(prova_longa)) > len(str(prova_curta)) else 'comparar manualmente'
    }


def comparar_formula_pronta_construida(formula_pronta, construcao):
    """A fórmula construída é melhor se mostra origem, passos e teste."""
    c = _normalizar(construcao)
    criterios = {
        'tem_origem': 'origem' in c or 'de onde' in c or 'vem de' in c,
        'tem_passos': 'passo' in c or '1.' in c or 'primeiro' in c,
        'tem_teste': 'teste' in c or 'verificar' in c or 'substituir' in c,
        'evita_formula_pronta': 'pela fórmula' not in c,
    }
    return {
        'formula_pronta': formula_pronta,
        'criterios_construcao': criterios,
        'aprovada_como_construida': all(criterios.values())
    }


def resposta_automatica(pergunta):
    """Respostas do motor mestre para perguntas de estado, pendência, confiança e passo."""
    p = _normalizar(pergunta)
    if 'o que sei' in p or 'tudo que sabe' in p or 'lista de tudo' in p:
        total = len(listar_tudo_que_o_psf_sabe())
        return 'O PSF tem índice mestre com ' + str(total) + ' entradas resumidas de conhecimento por etapa. Use listar_tudo_que_o_psf_sabe().'
    if 'pendente' in p or 'falta melhorar' in p or 'o que falta' in p:
        faltas = listar_tudo_que_falta()
        return 'Há ' + str(len(faltas)) + ' pendências/lacunas conhecidas no índice mestre. Use listar_tudo_que_falta().'
    if 'problemas em aberto' in p or 'quantos em aberto' in p:
        c = contar_problemas_abertos_conhecidos()
        return 'Até a Etapa 55: 81 entradas abertas/investigáveis conhecidas, 0 faltando entre as conhecidas. Novas entradas futuras devem ser adicionadas.'
    if 'confi' in p or 'confiável' in p or 'confiavel' in p:
        return 'Confiança no PSF não é cega: a resposta deve mostrar etapa, base, passos, teste, lacuna e contrato aplicado.'
    if 'qual passo' in p or 'passo foi usado' in p or 'que passo seguiu' in p:
        return 'O PSF deve responder com trilha: entrada → conceito usado → construção → cálculo/prova → teste → lacuna se existir.'
    if 'contradiz' in p:
        return 'Use detectar_contradicoes_texto(texto) e auditar_etapas() para procurar conflito entre regras, estado aberto/resolvido e dependências.'
    return 'Pergunta não reconhecida pelo roteador mestre. Use status_de_conhecimento(consulta) ou verificar_contrato_entrada(entrada).'


def auditar_etapas():
    """Auditoria interna das etapas registradas."""
    problemas = []
    numeros = set()
    for etapa in ETAPAS_MESTRE:
        n = etapa['etapa']
        if n in numeros:
            problemas.append({'etapa': n, 'problema': 'etapa duplicada'})
        numeros.add(n)
        if not etapa.get('nome'):
            problemas.append({'etapa': n, 'problema': 'sem nome'})
        if not etapa.get('sabe'):
            problemas.append({'etapa': n, 'problema': 'sem conhecimento listado'})
        if etapa.get('tem_aula') is not True:
            problemas.append({'etapa': n, 'problema': 'sem aula marcada'})
        if etapa.get('tem_teste') is not True:
            problemas.append({'etapa': n, 'problema': 'sem teste marcado'})
        texto = ' '.join([etapa.get('nome',''), etapa.get('estado','')] + list(etapa.get('sabe',())))
        for c in detectar_contradicoes_texto(texto):
            problemas.append({'etapa': n, 'problema': c})
    return {
        'total_etapas': len(ETAPAS_MESTRE),
        'primeira_etapa': min(numeros),
        'ultima_etapa': max(numeros),
        'problemas_detectados': problemas,
        'aprovado': not problemas
    }


def trilha_de_raciocinio_publica(tipo, entrada):
    """Raciocínio público auditável, sem expor pensamento privado: mostra passos verificáveis."""
    return (
        {'ordem': 1, 'passo': 'receber entrada', 'acao': 'identificar tipo: ' + str(tipo)},
        {'ordem': 2, 'passo': 'localizar conhecimento', 'acao': 'consultar índice mestre por conceito/etapa'},
        {'ordem': 3, 'passo': 'construir', 'acao': 'usar definição, premissas e regras nativas PSF'},
        {'ordem': 4, 'passo': 'verificar', 'acao': 'aplicar contrato de cobertura, lacuna, dependência e contradição'},
        {'ordem': 5, 'passo': 'responder', 'acao': 'entregar resposta com estado, teste e lacuna se existir'},
    )


def relatorio_mestre():
    """Relatório compacto da etapa 57."""
    return {
        'etapa': 57,
        'nome': 'Motor Mestre PSF',
        'etapas_indexadas': len(ETAPAS_MESTRE),
        'intervalo': (min(e['etapa'] for e in ETAPAS_MESTRE), max(e['etapa'] for e in ETAPAS_MESTRE)),
        'entradas_sabe': len(listar_tudo_que_o_psf_sabe()),
        'pendencias_lacunas': len(listar_tudo_que_falta()),
        'problemas_abertos_conhecidos': contar_problemas_abertos_conhecidos()['entradas_abertas_conhecidas_etapa55'],
        'contratos': tuple(CONTRATOS_INTERNOS.keys()),
        'sem_dependencias_externas': True,
        'auditoria_aprovada': auditar_etapas()['aprovado']
    }
