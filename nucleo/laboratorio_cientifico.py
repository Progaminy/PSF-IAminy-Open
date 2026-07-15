# Etapa 53 — Laboratório Científico PSF
# Núcleo nativo, sem dependências externas como fundamento.
# Objetivo: pegar um problema real simples, investigar junto com o utilizador,
# criar hipóteses, premissas, axiomas locais, testes, comparação e plano de aplicação.

ESTADO = 'DEFINITIVO_COM_RESPOSTA_AULA_TESTE'
REGRA = 'Todo problema real deve ser investigado antes de receber conclusão forte.'
SEM_DEPENDENCIAS_EXTERNAS = True

PALAVRAS_INFORMAIS = {
    'envestigar': 'investigar',
    'enventigar': 'investigar',
    'intigue': 'investigue',
    'fundo': 'fundo',
    'brexas': 'brechas',
    'fornacde': 'forma de',
    'premissas': 'premissas',
    'metodjs': 'métodos',
    'cinenhime': 'conhecimento',
    'to que tem': 'que tem',
}

METODOS_PSF_DISPONIVEIS = [
    'observar sem julgar rápido',
    'definir o objeto do problema',
    'separar facto, hipótese e opinião',
    'montar e desmontar o fluxo',
    'procurar padrão em casos pequenos',
    'comparar com resultado anterior ou esperado',
    'criar premissas explícitas',
    'enunciar axiomas locais',
    'testar caso mínimo',
    'tentar contraexemplo',
    'procurar lacuna e salto de passo',
    'validar antes de prometer',
]

PROBLEMA_REAL_PADRAO = {
    'titulo': 'Fila grande numa padaria de manhã',
    'linguagem_humana': (
        'A padaria vende bem de manhã, mas algumas pessoas entram, veem a fila, desistem e vão embora. '
        'O dono acha que o problema é o preço, mas ainda não testou. O PSF vai investigar antes de concluir.'
    ),
    'objeto': 'desistência de clientes durante o pico da manhã',
    'observacoes': [
        {'dia': 1, 'chegaram': 80, 'atendidos': 60, 'desistiram': 20, 'caixas': 1, 'tempo_fila_min': 15},
        {'dia': 2, 'chegaram': 82, 'atendidos': 61, 'desistiram': 21, 'caixas': 1, 'tempo_fila_min': 16},
        {'dia': 3, 'chegaram': 79, 'atendidos': 59, 'desistiram': 20, 'caixas': 1, 'tempo_fila_min': 15},
        {'dia': 4, 'chegaram': 81, 'atendidos': 74, 'desistiram': 7, 'caixas': 2, 'tempo_fila_min': 6},
        {'dia': 5, 'chegaram': 83, 'atendidos': 75, 'desistiram': 8, 'caixas': 2, 'tempo_fila_min': 6},
    ],
}


def texto(objeto):
    if objeto is None:
        return ''
    if isinstance(objeto, str):
        return objeto
    if isinstance(objeto, (list, tuple)):
        return ' '.join(texto(x) for x in objeto)
    if isinstance(objeto, dict):
        return ' '.join(texto(v) for v in objeto.values())
    return str(objeto)


def normalizar_informal(frase):
    t = texto(frase)
    for errado, certo in PALAVRAS_INFORMAIS.items():
        t = t.replace(errado, certo)
    return t


def soma_nativa(a, b):
    resultado = a
    contador = 0
    while contador < b:
        resultado = resultado + 1
        contador = contador + 1
    return resultado


def subtrai_nativa(a, b):
    resultado = a
    contador = 0
    while contador < b:
        resultado = resultado - 1
        contador = contador + 1
    return resultado


def multiplica_nativa(a, b):
    total = 0
    contador = 0
    while contador < b:
        total = soma_nativa(total, a)
        contador = contador + 1
    return total


def dividir_com_resto_nativo(total, partes):
    if partes == 0:
        return {'erro': 'divisão por zero não permitida'}
    q = 0
    resto = total
    while resto >= partes:
        resto = subtrai_nativa(resto, partes)
        q = q + 1
    return {'quociente': q, 'resto': resto}


def percentual_inteiro(parte, total):
    produto = multiplica_nativa(parte, 100)
    div = dividir_com_resto_nativo(produto, total)
    if 'erro' in div:
        return 'indefinido'
    if div['resto'] == 0:
        return str(div['quociente']) + '%'
    return str(div['quociente']) + '% e mais uma parte pequena'


def media_inteira_aproximada(valores):
    total = 0
    qtd = 0
    for v in valores:
        total = soma_nativa(total, v)
        qtd = soma_nativa(qtd, 1)
    return dividir_com_resto_nativo(total, qtd)


def separar_por_caixa(observacoes):
    um = []
    dois = []
    for o in observacoes:
        if o['caixas'] == 1:
            um.append(o)
        if o['caixas'] == 2:
            dois.append(o)
    return um, dois


def resumo_observacoes(observacoes):
    um, dois = separar_por_caixa(observacoes)
    media_desiste_um = media_inteira_aproximada([o['desistiram'] for o in um])
    media_desiste_dois = media_inteira_aproximada([o['desistiram'] for o in dois])
    media_fila_um = media_inteira_aproximada([o['tempo_fila_min'] for o in um])
    media_fila_dois = media_inteira_aproximada([o['tempo_fila_min'] for o in dois])
    return {
        'dias_com_1_caixa': len(um),
        'dias_com_2_caixas': len(dois),
        'media_desistencias_1_caixa': media_desiste_um,
        'media_desistencias_2_caixas': media_desiste_dois,
        'media_fila_1_caixa': media_fila_um,
        'media_fila_2_caixas': media_fila_dois,
    }


def pergunta_para_descobrir_causas():
    return [
        'Em que hora a fila fica maior?',
        'As pessoas desistem antes ou depois de ver o preço?',
        'Quando há dois atendentes, a desistência cai?',
        'O produto acaba antes do fim do pico?',
        'A fila demora porque falta caixa, falta pão pronto ou falta troco?',
        'O mesmo problema acontece em dia de chuva, feriado ou fim de semana?',
        'Qual é o menor teste que podemos fazer sem gastar muito?',
    ]


def criar_premissas(problema=PROBLEMA_REAL_PADRAO):
    return [
        'Premissa 1: desistência é cliente que chegou, mas saiu sem comprar.',
        'Premissa 2: tempo de fila pode influenciar desistência.',
        'Premissa 3: preço só pode ser acusado se houver evidência ligada ao preço.',
        'Premissa 4: uma causa só é aceita depois de comparação entre situações parecidas.',
        'Premissa 5: conclusão prática precisa de teste pequeno antes de aplicação grande.',
    ]


def criar_axiomas_locais():
    return [
        'Axioma local 1: não concluir causa sem comparação.',
        'Axioma local 2: se muda uma coisa e o efeito muda junto, isso vira pista, não prova final.',
        'Axioma local 3: se há salto de explicação, voltar um passo.',
        'Axioma local 4: se o teste falha, a hipótese deve ser corrigida ou abandonada.',
        'Axioma local 5: meta não é promessa; meta só vira resultado depois de medida.',
    ]


def formular_hipoteses(problema=PROBLEMA_REAL_PADRAO):
    return [
        {'nome': 'H1', 'texto': 'A fila longa é a principal causa da desistência.', 'estado': 'testável'},
        {'nome': 'H2', 'texto': 'O preço alto é a principal causa da desistência.', 'estado': 'precisa de dado de preço'},
        {'nome': 'H3', 'texto': 'Falta de produto pronto aumenta o tempo de espera.', 'estado': 'precisa observar produção'},
        {'nome': 'H4', 'texto': 'Dois caixas no pico reduzem desistência.', 'estado': 'testável com comparação'},
    ]


def comparar_resultados(observacoes):
    r = resumo_observacoes(observacoes)
    antes = r['media_desistencias_1_caixa']['quociente']
    depois = r['media_desistencias_2_caixas']['quociente']
    queda = subtrai_nativa(antes, depois) if antes >= depois else 0
    return {
        'resultado_observado': 'com 2 caixas, a média de desistência ficou menor na amostra',
        'media_desistencias_1_caixa': antes,
        'media_desistencias_2_caixas': depois,
        'queda_aproximada': queda,
        'interpretação_simples': 'a fila parece ser uma causa forte, mas ainda precisa de mais dias de teste',
        'cuidado': 'não afirmar certeza total; a amostra é pequena',
    }


def detectar_lacunas_do_estudo(problema=PROBLEMA_REAL_PADRAO):
    lacunas = []
    observacoes = problema['observacoes']
    if len(observacoes) < 7:
        lacunas.append('poucos dias observados; ideal testar pelo menos uma semana completa')
    if not any('preco' in texto(problema).lower() or 'preço' in texto(problema).lower() for _ in [0]):
        lacunas.append('não há dado de preço suficiente para culpar preço')
    if not any('chuva' in texto(o).lower() for o in observacoes):
        lacunas.append('não há comparação com clima, feriado ou dia especial')
    lacunas.append('ainda falta perguntar aos clientes que desistiram o motivo real')
    return lacunas


def plano_de_teste_simples():
    return [
        'Dia 1 e 2: medir fila com 1 caixa no mesmo horário.',
        'Dia 3 e 4: medir fila com 2 caixas no mesmo horário.',
        'Em todos os dias: contar quantos chegam, quantos compram e quantos desistem.',
        'Perguntar a 5 pessoas que desistiram: foi preço, fila, falta de produto ou outro motivo?',
        'Comparar só situações parecidas: mesmo horário, mesmo tipo de dia, mesmo produto.',
        'Se a desistência cair com 2 caixas, aplicar 2 caixas só no pico e medir novamente.',
    ]


def ideia_para_aplicar():
    return [
        'Abrir segundo caixa apenas no pico, não o dia todo.',
        'Separar fila rápida para quem só compra pão simples.',
        'Preparar produtos mais pedidos antes das 7h.',
        'Colocar placa simples com preços visíveis para não travar a fila.',
        'Medir durante 10 dias antes de dizer que resolveu.',
    ]


def maturar_modo_cientifico():
    return [
        'Nível 1: entender a fala informal do utilizador sem corrigir de forma arrogante.',
        'Nível 2: transformar a fala em problema claro.',
        'Nível 3: separar facto, suspeita e conclusão.',
        'Nível 4: criar hipóteses pequenas e testáveis.',
        'Nível 5: testar com dados mínimos.',
        'Nível 6: comparar com resultado esperado ou resultado anterior.',
        'Nível 7: procurar lacunas, brechas e saltos de fluxo.',
        'Nível 8: criar premissas e axiomas locais.',
        'Nível 9: aplicar uma solução pequena.',
        'Nível 10: repetir, amadurecer e só então aprovar como conhecimento.',
    ]


def executar_laboratorio(problema=PROBLEMA_REAL_PADRAO, linguagem='simples'):
    observacoes = problema['observacoes']
    comparacao = comparar_resultados(observacoes)
    return {
        'modo': 'cientista_pratico',
        'estado': ESTADO,
        'sem_dependencias_externas': SEM_DEPENDENCIAS_EXTERNAS,
        'problema_real': problema['titulo'],
        'linguagem': 'simples e informal' if linguagem == 'simples' else linguagem,
        'explicacao_humana': problema['linguagem_humana'],
        'objeto_estudado': problema['objeto'],
        'metodos_psf_usados': METODOS_PSF_DISPONIVEIS,
        'perguntas_para_descobrir_causas': pergunta_para_descobrir_causas(),
        'premissas': criar_premissas(problema),
        'axiomas_locais': criar_axiomas_locais(),
        'hipoteses': formular_hipoteses(problema),
        'teste_simples': plano_de_teste_simples(),
        'comparacao': comparacao,
        'lacunas_encontradas': detectar_lacunas_do_estudo(problema),
        'ideias_para_aplicar': ideia_para_aplicar(),
        'maturacao_do_modo': maturar_modo_cientifico(),
        'decisao': 'a causa mais forte parece ser fila/atendimento, mas o PSF pede mais teste antes de fechar conclusão',
    }


def relatorio_laboratorio(problema=PROBLEMA_REAL_PADRAO):
    r = executar_laboratorio(problema)
    linhas = []
    linhas.append('LABORATÓRIO CIENTÍFICO PSF — TESTE REAL SIMPLES')
    linhas.append('Problema: ' + r['problema_real'])
    linhas.append('Em linguagem simples: ' + r['explicacao_humana'])
    linhas.append('O que vamos estudar: ' + r['objeto_estudado'])
    linhas.append('')
    linhas.append('1) Perguntas para descobrir causas:')
    for p in r['perguntas_para_descobrir_causas']:
        linhas.append('- ' + p)
    linhas.append('')
    linhas.append('2) Hipóteses:')
    for h in r['hipoteses']:
        linhas.append('- ' + h['nome'] + ': ' + h['texto'])
    linhas.append('')
    linhas.append('3) Teste feito com a amostra:')
    c = r['comparacao']
    linhas.append('- Com 1 caixa: média aproximada de ' + str(c['media_desistencias_1_caixa']) + ' desistências.')
    linhas.append('- Com 2 caixas: média aproximada de ' + str(c['media_desistencias_2_caixas']) + ' desistências.')
    linhas.append('- Queda aproximada: ' + str(c['queda_aproximada']) + ' desistências.')
    linhas.append('')
    linhas.append('4) Lacunas que o PSF encontrou:')
    for l in r['lacunas_encontradas']:
        linhas.append('- ' + l)
    linhas.append('')
    linhas.append('5) Ideia para aplicar sem prometer falso:')
    for i in r['ideias_para_aplicar']:
        linhas.append('- ' + i)
    linhas.append('')
    linhas.append('Decisão PSF: ' + r['decisao'])
    return '\n'.join(linhas)


def validar_laboratorio_cientifico():
    problemas = []
    r = executar_laboratorio()
    obrigatorios = [
        'perguntas_para_descobrir_causas', 'premissas', 'axiomas_locais', 'hipoteses',
        'teste_simples', 'comparacao', 'lacunas_encontradas', 'ideias_para_aplicar',
        'maturacao_do_modo', 'metodos_psf_usados'
    ]
    for campo in obrigatorios:
        if campo not in r or not r[campo]:
            problemas.append('campo_obrigatorio_faltando_' + campo)
    if r['comparacao']['queda_aproximada'] <= 0:
        problemas.append('comparacao_nao_detectou_melhoria')
    if 'dependencias' in globals() or 'math' in globals() or 'numpy' in globals() or 'sympy' in globals():
        problemas.append('dependencia_externa_detectada')
    rel = relatorio_laboratorio()
    for termo in ['Perguntas', 'Hipóteses', 'Lacunas', 'Decisão PSF']:
        if termo not in rel:
            problemas.append('relatorio_sem_' + termo)
    return problemas
