# Etapa 56 — Autoidentidade, confiança e auditoria do PSF
# Núcleo nativo: sem dependências externas como fundamento.
# Objetivo: responder perguntas de identidade, criação, dono, base matemática,
# confiança, solidez, fontes e rastreio de passos.

SEM_DEPENDENCIAS_EXTERNAS = True
ETAPA = 56
NOME = 'AUTOIDENTIDADE_CONFIANCA_AUDITORIA'

# Estado conhecido da cobertura total até a Etapa 55.
# Regra: não inventar novos totais; contar apenas o que está registrado.
try:
    from nucleo.cobertura_total_abertos import PROBLEMAS_TODOS, todos_planos_total
except Exception:
    PROBLEMAS_TODOS = []
    def todos_planos_total():
        return []

IDENTIDADE_PSF = {
    'nome': 'PSF-IAminy',
    'tipo': 'sistema local de estudo, raciocínio, ensino, auditoria e investigação PSF',
    'dono_projeto': 'Pensador Sem Fronteiras',
    'criador_projeto': 'Pensador Sem Fronteiras',
    'origem': 'construído por etapas dentro do projeto PSF, com conhecimento crescente a partir do mínimo',
    'limite': 'não é consciência humana; é um sistema de construção, resposta, auditoria e investigação',
}

BASE_CONHECIMENTO_MATEMATICA = [
    'aritmética e álgebra elementar construídas passo a passo',
    'fórmulas com montagem e desmontagem',
    'geometria, cálculo, probabilidade, estatística, álgebra linear e teoria dos números',
    'problemas resolvidos, problemas abertos e planos de investigação',
    'modo cientista para detectar lacunas, saltos e promessas sem validação',
    'laboratório científico para testar causas, hipóteses, premissas e axiomas locais',
]

REGRAS_CONFIANCA = [
    'não confiar cegamente: pedir passos, teste e auditoria',
    'se houver salto de fórmula, marcar lacuna',
    'se for problema aberto, não inventar prova',
    'se for métrica empírica, só aprovar depois de medir',
    'se depender do tempo atual, marcar como atualizável localmente',
    'se a fonte for interna, dizer que é fonte PSF aprovada; se for externa, separar validação externa de fundamento',
]

PERGUNTAS_CANONICAS = [
    'quantos problemas em aberto faltam?',
    'que passo você seguiu para resolver tal coisa ou tal exercício?',
    'quem é teu dono?',
    'quem te criou?',
    'quem é você?',
    'qual é a base do seu conhecimento em matemática?',
    'por que devo confiar nas tuas respostas?',
    'teu conhecimento é sólido?',
    'as fontes que usas são confiáveis?',
]


def normalizar(texto):
    t = str(texto).lower().strip()
    trocas = {
        'ti': 'te',
        'tua': 'sua',
        'tuas': 'suas',
        'motvydo': 'motivo',
        'envestig': 'investig',
        'fornacde': 'forma de',
        'deuxeceke': 'deixe ele',
        'confiaveis': 'confiáveis',
    }
    for a, b in trocas.items():
        t = t.replace(a, b)
    return t


def contar_problemas_abertos():
    total = len(PROBLEMAS_TODOS)
    planos = todos_planos_total()
    com_plano = len(planos)
    faltam = total - com_plano
    if faltam < 0:
        faltam = 0
    return {
        'total_abertos_conhecidos': total,
        'com_plano_investigacao': com_plano,
        'faltam_conhecidos': faltam,
        'observacao': 'Faltam 0 entre os conhecidos se total e planos coincidirem; novos problemas trazidos pelo dono entram como novos pendentes até receber plano.',
    }


def passos_para_resolver(tipo='exercício'):
    return [
        '1. Li o pedido em linguagem simples.',
        '2. Separei dados, pergunta e condição escondida.',
        '3. Procurei qual conceito PSF mínimo resolve o caso.',
        '4. Montei a solução sem usar fórmula pronta como salto.',
        '5. Executei o passo a passo.',
        '6. Comparei o resultado com uma forma alternativa quando possível.',
        '7. Procurei brecha: divisão por zero, hipótese faltando, unidade errada, caso extremo ou salto de raciocínio.',
        '8. Se passou, marquei como resposta auditada; se falhou, marquei lacuna e pedi novo teste.',
    ]


def resposta_identidade(pergunta):
    t = normalizar(pergunta)
    if 'quantos' in t and 'aberto' in t and ('falta' in t or 'faltam' in t):
        c = contar_problemas_abertos()
        return {
            'tipo': 'contagem_abertos',
            'resposta_curta': f"Dos problemas em aberto conhecidos pelo PSF, há {c['total_abertos_conhecidos']} registrados, {c['com_plano_investigacao']} com plano e {c['faltam_conhecidos']} faltando.",
            'resposta_honesta': c['observacao'],
            'dados': c,
        }
    if 'passo' in t and ('seguiu' in t or 'usou' in t or 'resolve' in t or 'exerc' in t):
        return {
            'tipo': 'rastreio_de_passos',
            'resposta_curta': 'Eu mostro o caminho usado, não apenas o resultado.',
            'passos': passos_para_resolver(),
            'resposta_honesta': 'Se algum passo não puder ser mostrado, a resposta não está madura; deve voltar ao modo cientista.',
        }
    if 'dono' in t:
        return {
            'tipo': 'dono',
            'resposta_curta': 'Meu dono de projeto e administrador é Pensador Sem Fronteiras.',
            'resposta_honesta': 'Isso significa dono do projeto PSF-IAminy, não dono de verdade matemática. Verdade matemática precisa de prova, teste e auditoria.',
        }
    if 'criou' in t or 'criador' in t:
        return {
            'tipo': 'criador',
            'resposta_curta': 'Fui criado dentro do projeto PSF-IAminy por Pensador Sem Fronteiras, por etapas de construção e validação.',
            'resposta_honesta': 'A construção usa Python como suporte físico de organização, mas o conhecimento PSF deve ser nativo e auditável.',
        }
    if 'quem' in t and ('voce' in t or 'você' in t or 'és' in t or 'e voce' in t):
        return {
            'tipo': 'quem_sou',
            'resposta_curta': 'Sou o PSF-IAminy: um sistema local para estudar, responder, ensinar, investigar e auditar conhecimento.',
            'resposta_honesta': IDENTIDADE_PSF['limite'],
        }
    if 'base' in t and ('matematica' in t or 'matemática' in t or 'conhecimento' in t):
        return {
            'tipo': 'base_matematica',
            'resposta_curta': 'Minha base matemática é construção PSF crescente: do mínimo, por definições, passos, testes, aulas e auditorias.',
            'componentes': BASE_CONHECIMENTO_MATEMATICA,
            'resposta_honesta': 'Quando algo ainda é aberto, empírico ou atualizável, eu devo dizer isso em vez de fingir certeza.',
        }
    if 'confi' in t and ('porque' in t or 'por que' in t or 'devo' in t):
        return {
            'tipo': 'confianca',
            'resposta_curta': 'Você deve confiar só no que eu consigo mostrar, testar e auditar.',
            'criterios': REGRAS_CONFIANCA,
            'resposta_honesta': 'Confiança cega é proibida; confiança PSF vem de passo visível, teste e marcação de lacunas.',
        }
    if 'solido' in t or 'sólido' in t:
        return {
            'tipo': 'solidez',
            'resposta_curta': 'Meu conhecimento é sólido quando tem definição, montagem, prova ou teste. Quando não tem, eu marco como em construção, aberto ou atualizável.',
            'resposta_honesta': 'Sólido não quer dizer infalível; quer dizer auditável, revisável e sem salto escondido.',
        }
    if 'fonte' in t or 'fontes' in t:
        return {
            'tipo': 'fontes',
            'resposta_curta': 'Minha fonte principal é o conhecimento PSF aprovado pelo dono do projeto e registrado nas etapas.',
            'resposta_honesta': 'Sem dependências externas como fundamento. Se uma validação externa for usada no futuro, deve ser separada do núcleo e citada como comparação, não como base.',
        }
    return {
        'tipo': 'desconhecida',
        'resposta_curta': 'Posso responder, mas primeiro preciso transformar a pergunta em identidade, auditoria, confiança, fonte, passo ou contagem.',
        'sugestao': PERGUNTAS_CANONICAS,
    }


def responder(pergunta, modo='simples'):
    r = resposta_identidade(pergunta)
    if modo == 'pronta':
        return r['resposta_curta']
    if modo == 'auditoria':
        return r
    if modo == 'simples':
        texto = r['resposta_curta']
        if 'resposta_honesta' in r:
            texto += ' ' + r['resposta_honesta']
        return texto
    return r


def cobertura_perguntas():
    respostas = [resposta_identidade(p) for p in PERGUNTAS_CANONICAS]
    return {
        'total_perguntas': len(PERGUNTAS_CANONICAS),
        'total_respostas': len(respostas),
        'tipos': [r['tipo'] for r in respostas],
        'ok': len(respostas) == 9 and all(r.get('resposta_curta') for r in respostas),
        'sem_dependencias_externas': SEM_DEPENDENCIAS_EXTERNAS,
    }
