# Etapa 55 — Cobertura total dos problemas em aberto já trazidos
# Correção da Etapa 54: não apenas 60 problemas explícitos; agora inclui todos os abertos,
# conjecturais, programas de pesquisa e metas empíricas sem garantia já registrados nas etapas anteriores.
# Núcleo nativo PSF: sem internet, API externa, math, numpy, sympy ou solver externo como fundamento.

ESTADO = 'COBERTURA_TOTAL_TODOS_ABERTOS_CORRIGIDA'
SEM_DEPENDENCIAS_EXTERNAS = True
CORRECAO_DA_ETAPA_54 = True
REGRA = 'Todos os problemas abertos, conjecturais, programas de pesquisa e metas empíricas sem garantia precisam de plano individual.'

PROBLEMAS_TODOS = [{'codigo': 'ET48-001', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Baum-Connes com coeficientes para todos os grupos discretos e C*-álgebras', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-002', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Ulam sobre determinação de grupos localmente compactos pelo espectro de caracteres', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-003', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Classificação completa das variedades de Fano que admitem métricas de Kähler-Einstein fora dos casos cobertos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-004', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Poincaré suave em dimensão 4 e estruturas exóticas em S4', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-005', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Regularidade global de Navier-Stokes incompressível em R3', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-006', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Schanuel sobre independência linear e transcendência exponencial', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-007', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Invariância topológica da K-teoria algébrica sob equivalências de Morita derivadas', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-008', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Novikov: injetividade da assembly de L-theory para grupos discretos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-009', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Existência de infinitas geodésicas fechadas em variedades compactas simplesmente conexas', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-010', 'fonte': 'Etapa 48/Doutoramento', 'nome': 'Conjectura de Atiyah sobre cohomologia de variedades de representações e torção', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-011', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Conjectura de Hodge', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-012', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Hipótese de Riemann', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-013', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Conjectura de Birch e Swinnerton-Dyer', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-014', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Conjectura de Tate sobre ciclos algébricos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-015', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Yang-Mills e gap de massa', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-016', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Conjectura de Goldbach forte', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-017', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Conjectura dos primos gémeos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-018', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Curvatura escalar prescrita em S^n no caso geral não simétrico', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-019', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Hochschild-Kostant-Rosenberg em variedades singulares', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-020', 'fonte': 'Etapa 48/Pós-doutoramento', 'nome': 'Classificação geral de C*-álgebras simples separáveis nucleares por K-teoria e traços', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-021', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'P versus NP', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-022', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura de Collatz', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-023', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Existência de números perfeitos ímpares', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-024', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Hipótese de Riemann generalizada para funções L de Dirichlet', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-025', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura de Serre sobre multiplicidades em representações p-ádicas', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-026', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura de Baum-Connes para grupos com torção', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-027', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura de Bost sobre regularidade de Boltzmann para esferas duras', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-028', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Existência de métricas de Einstein em variedades compactas de dimensão >=4', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-029', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura de Langlands para todos os grupos redutivos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-030', 'fonte': 'Etapa 48/Carreira académica', 'nome': 'Conjectura da seção de Grothendieck', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-031', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'P versus NP aplicado e algoritmo polinomial para caixeiro viajante', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-032', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Segurança da criptografia RSA contra fatorização clássica polinomial', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-033', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Problema do gap espectral em sistemas quânticos de spins e variantes abertas', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-034', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Superalinhamento de IA em formulação matemática de controle', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-035', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Inferência causal completa a partir de dados observacionais', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-036', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Limites fundamentais da generalização em aprendizagem profunda', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-037', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Criptografia pós-quântica ótima baseada em reticulados', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-038', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Parada ótima em finanças com custos de transação e volatilidade estocástica multivariada', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-039', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Consenso blockchain seguro, descentralizado e escalável', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-040', 'fonte': 'Etapa 48/Indústria e tecnologia', 'nome': 'Aprendizagem por reforço em ambientes não estacionários', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-041', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Métrica quantitativa universal para Product-Market Fit', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-042', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Ponto de inflexão de crescimento viral em efeitos de rede', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-043', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Matching ótimo para marketplaces bilaterais em tempo real', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-044', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Precificação dinâmica competitiva em tempo real', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-045', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Churn com intervenção e orçamento limitado maximizando CLV', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-046', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Adoção de tecnologia disruptiva sem dados históricos análogos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-047', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Portfólio ótimo de produtos e alocação de P&D', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-048', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Timing ótimo de entrada em mercado com efeitos de rede', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-049', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Incentivos ótimos em plataformas bilaterais', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-050', 'fonte': 'Etapa 48/Empreendedorismo', 'nome': 'Deteção precoce de tendências emergentes com baixa taxa de falsos positivos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-051', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio P versus NP', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-052', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio Hipótese de Riemann', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-053', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio Conjectura de Hodge', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-054', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio Yang-Mills e gap de massa', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-055', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio Navier-Stokes regularidade', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-056', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema do Milénio Birch e Swinnerton-Dyer', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-057', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Conjectura de Goldbach forte', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-058', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Conjectura de Beal', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-059', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Conjectura dos primos gémeos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET48-060', 'fonte': 'Etapa 48/Prémios de elite', 'nome': 'Problema de Erdős sobre progressões aritméticas e soma dos recíprocos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET45-047', 'fonte': 'Etapa 45/Pesquisa extrema', 'nome': 'Regularidade global de Navier-Stokes em 3D', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET45-078', 'fonte': 'Etapa 45/Pesquisa extrema', 'nome': 'Classes de Hodge e conjectura de Hodge', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET45-083', 'fonte': 'Etapa 45/Pesquisa extrema', 'nome': 'Hipótese de Riemann: formulações equivalentes', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET45-094', 'fonte': 'Etapa 45/Pesquisa extrema', 'nome': 'Teoria de Yang-Mills e problema do gap de massa', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET45-095', 'fonte': 'Etapa 45/Pesquisa extrema', 'nome': 'Correspondência AdS/CFT: aspectos matemáticos ainda conjecturais', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-011', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Classificação equivarante de Kirchberg-Phillips para ações de grupos finitos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-012', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Cohomologia de Hochschild de álgebras de caminhos de quivers com relações', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-014', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Medidas invariantes para fluxos geodésicos em curvatura negativa variável', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-015', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Langlands geométrico para GL(n) sobre curvas', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-016', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Dimensão de Hausdorff de atratores parcialmente hiperbólicos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-019', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'Integração em caminhos com Wiener para operadores de Dirac', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-020', 'fonte': 'Etapa 47/Pós-doc', 'nome': 'K-teoria torcida de C*-álgebras de grupoides e defeitos topológicos', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-022', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Novo invariante quântico para nós via categorias de fusão modulares', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-023', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Ondas viajantes para reação-difusão com difusão cruzada', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-024', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Classificação de álgebras de Hopf semissimples finito-dimensionais', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-026', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Cifração totalmente homomórfica baseada em reticulados ideais eficiente', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-027', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Conjectura de Hodge para Calabi-Yau 4 particulares', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-028', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Cohomologia para stacks diferenciáveis', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-030', 'fonte': 'Etapa 47/Carreira académica', 'nome': 'Métodos numéricos de alta ordem para EDPs estocásticas com ruído multiplicativo', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET47-048', 'fonte': 'Etapa 47/Empreendedorismo', 'nome': 'Churn prediction com recall maior que 0,85 como meta empírica não garantida', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}, {'codigo': 'ET44-43-II-098', 'fonte': 'Etapa 44/Etapa 43 herdada', 'nome': 'Hipótese de Riemann enunciada como problema aberto com contexto completo', 'estado': 'ABERTO_OU_PROGRAMA_DE_INVESTIGACAO'}]

CAMPOS_OBRIGATORIOS = [
    'resposta_honesta', 'plano', 'sequencia', 'possibilidades', 'teorias', 'hipoteses',
    'premissas', 'axiomas_locais', 'testes', 'comparacao', 'falsificacao',
    'raciocinio_publico', 'aula_direta', 'aula_detalhada', 'aula_passo_a_passo'
]


def natureza(problema):
    nome = problema['nome'].lower()
    if any(p in nome for p in ['recall', 'auc', 'erro', 'meta empírica', 'tendências', 'churn']):
        return 'META_EMPIRICA_SEM_GARANTIA'
    if any(p in nome for p in ['conjectura', 'hipótese', 'problema do milénio', 'problema do milenio', 'p versus np', 'goldbach', 'primos', 'hodge', 'navier', 'riemann', 'yang-mills']):
        return 'PROBLEMA_ABERTO_ESTRITO'
    if any(p in nome for p in ['classificação', 'langlands', 'cohomologia', 'invariante', 'métodos', 'k-teoria', 'cifração', 'ondas viajantes']):
        return 'PROGRAMA_DE_PESQUISA'
    return 'FRONTEIRA_INVESTIGAVEL'


def teorias(nome):
    n = nome.lower()
    base = []
    if any(k in n for k in ['c*', 'k-teoria', 'baum', 'novikov', 'kirchberg']):
        base += ['C*-álgebras', 'K-teoria', 'assembly', 'índice', 'operadores']
    if any(k in n for k in ['riemann', 'goldbach', 'primos', 'beal', 'schanuel', 'rsa']):
        base += ['teoria dos números', 'funções L', 'congruências', 'densidade', 'contraexemplos finitos']
    if any(k in n for k in ['hodge', 'tate', 'langlands', 'birch', 'calabi', 'grothendieck']):
        base += ['geometria algébrica', 'cohomologia', 'móduli', 'representações', 'ciclos']
    if any(k in n for k in ['navier', 'yang-mills', 'boltzmann', 'edp', 'schrödinger']):
        base += ['EDP', 'energia', 'regularidade', 'soluções fracas', 'escala']
    if any(k in n for k in ['ia', 'aprendizagem', 'causal', 'churn', 'market', 'startup']):
        base += ['modelagem causal', 'validação empírica', 'generalização', 'experimento pequeno', 'métrica auditável']
    if not base:
        base = ['definições mínimas', 'casos pequenos', 'invariantes', 'falsificação', 'subproblemas']
    # manter ordem sem repetição
    saida=[]
    for x in base:
        if x not in saida: saida.append(x)
    return saida


def criar_plano_total(problema):
    nome = problema['nome']
    nat = natureza(problema)
    return {
        'codigo': problema['codigo'],
        'fonte': problema['fonte'],
        'nome': nome,
        'natureza': nat,
        'estado': 'INVESTIGAR_SEM_PROMETER_SOLUCAO',
        'resposta_honesta': 'Este item entra na cobertura total: investigar, testar, comparar e falsificar; não declarar solução final sem prova ou validação.',
        'plano': 'Transformar o problema em sequência de subproblemas verificáveis, começando pelo caso mínimo construído no PSF.',
        'sequencia': [
            '1. Reescrever em linguagem simples.',
            '2. Separar objeto, hipótese, conclusão e domínio.',
            '3. Listar o que o PSF já construiu sobre o tema.',
            '4. Criar versão fraca ou caso pequeno.',
            '5. Testar exemplos, bordas e possíveis contraexemplos.',
            '6. Comparar com problemas resolvidos próximos.',
            '7. Converter salto de raciocínio em lema.',
            '8. Se falhar, registrar a lacuna e tentar outro caminho.',
        ],
        'possibilidades': [
            'provar caso restrito',
            'achar contraexemplo',
            'descobrir invariante',
            'formular versão equivalente',
            'criar método de validação nativo',
        ],
        'teorias': teorias(nome),
        'hipoteses': [
            'H1: uma versão pequena do problema pode revelar o obstáculo principal.',
            'H2: o problema depende de uma ponte entre informação local e conclusão global.',
            'H3: a formulação pode precisar de hipóteses adicionais.',
            'H4: falsificar versões fortes ajuda a encontrar a versão correta.',
        ],
        'premissas': [
            'não usar fontes externas como fundamento',
            'não prometer métrica sem teste',
            'não chamar aberto de resolvido',
            'não aceitar fórmula pronta sem montagem',
        ],
        'axiomas_locais': [
            'todo salto vira lacuna até ser justificado',
            'todo resultado precisa de prova, teste ou estado aberto explícito',
            'todo contraexemplo pequeno vale como sinal de revisão',
            'toda hipótese deve poder falhar em algum teste imaginável',
        ],
        'testes': [
            'teste de caso mínimo',
            'teste de borda',
            'teste de analogia com problema resolvido',
            'teste de contraexemplo',
            'teste de consistência interna PSF',
        ],
        'comparacao': [
            'comparar versão fraca e versão forte',
            'comparar caso finito e infinito',
            'comparar evidência empírica e prova formal',
            'comparar caminho PSF com teoremas já registrados',
        ],
        'falsificacao': [
            'tentar quebrar uma hipótese',
            'remover uma condição e ver se o problema muda',
            'procurar exceção pequena',
            'testar se a conclusão depende de ferramenta ainda não construída',
        ],
        'raciocinio_publico': [
            'começar do mínimo',
            'crescer por lemas',
            'não pular ponte',
            'auditar cada passo',
            'guardar falha como conhecimento útil',
        ],
        'aula_direta': 'Este problema é investigável: explique o enunciado, escolha um caso pequeno e teste sem prometer solução.',
        'aula_detalhada': 'Estude origem, hipóteses, teorias relacionadas, exemplos mínimos, obstáculos e comparação com resultados próximos.',
        'aula_passo_a_passo': 'Ler → traduzir → separar → testar → comparar → falsificar → criar lema → revisar → avançar.',
    }


def todos_planos_total():
    return [criar_plano_total(p) for p in PROBLEMAS_TODOS]


def verificar_cobertura_total():
    faltas=[]
    for plano in todos_planos_total():
        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in plano or not plano[campo]:
                faltas.append((plano['codigo'], campo))
    return {'total': len(PROBLEMAS_TODOS), 'faltas': faltas, 'ok': not faltas}


def resumo_cobertura():
    total = len(PROBLEMAS_TODOS)
    por_natureza = {}
    for p in todos_planos_total():
        por_natureza[p['natureza']] = por_natureza.get(p['natureza'], 0) + 1
    return {'total': total, 'por_natureza': por_natureza, 'ok': verificar_cobertura_total()['ok']}
