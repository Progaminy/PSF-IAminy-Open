# Auditoria estrutural do código de produção

| Métrica | Valor |
| --- | ---: |
| Ficheiros Python analisados | 242 |
| Funções/métodos | 1754 |
| Funções públicas | 1355 |
| Totalmente tipadas | 1005 (57.3%) |
| Com retorno tipado | 1019 (58.1%) |
| Com docstring própria | 473 (27.0%) |
| `except:` sem tipo | 0 |
| `except Exception/BaseException` | 17 |
| `raise Exception/BaseException` genérico | 0 |
| Grupos de corpos exatamente duplicados | 17 |
| Funções nesses grupos | 52 |
| Erros de sintaxe/leitura | 0 |

## Duplicações exatas a rever

- `nucleo/analise_sintatica_finita.py:13` (_bool); `nucleo/automatos_finitos_naturais.py:11` (_bool); `nucleo/busca_prova_finita.py:40` (_bool); `nucleo/categorias_finitas.py:15` (_bool); `nucleo/computabilidade_finita.py:21` (_bool); `nucleo/gramaticas_finitas.py:15` (_bool); `nucleo/gramaticas_livres_contexto_naturais.py:12` (_bool); `nucleo/linguagens_regulares_naturais.py:11` (_bool); `nucleo/logica_predicados_finita.py:35` (_bool); `nucleo/metodos_finitos.py:20` (_bool); `nucleo/semantica_operacional_finita.py:13` (_bool); `nucleo/semantica_tipos_finitos.py:13` (_bool); `nucleo/teoria_modelos_prova_finita.py:32` (_bool)

- `nucleo/base_curiosidades_reais.py:19` (sem_acentos); `nucleo/chat_texto.py:73` (sem_acentos); `nucleo/indexador_total.py:64` (sem_acentos); `nucleo/roteador_base_curiosidades.py:28` (sem_acentos)

- `nucleo/busca_prova_finita.py:52` (_unicos); `nucleo/logica_predicados_finita.py:47` (_unicos); `nucleo/metodos_finitos.py:32` (_unicos); `nucleo/teoria_modelos_prova_finita.py:44` (_unicos)

- `nucleo/aritmetica_escolar_nativa.py:28` (validar_natural); `nucleo/sequencias_calculo_psf.py:24` (_validar_natural); `nucleo/zeta_psf_finita.py:38` (_validar_natural)

- `nucleo/automatos_finitos_naturais.py:19` (_unicos); `nucleo/gramaticas_finitas.py:23` (_unicos); `nucleo/linguagens_regulares_naturais.py:19` (_unicos)

- `nucleo/busca_prova_finita.py:48` (_contem); `nucleo/logica_predicados_finita.py:43` (_contem); `nucleo/teoria_modelos_prova_finita.py:40` (_contem)

- `ensino/progresso.py:54` (_carregar); `ensino/revisao.py:45` (_carregar)

- `ensino/progresso.py:59` (_guardar); `ensino/revisao.py:50` (_guardar)

- `lingua_portuguesa/conhecimento_puro.py:1251` (nomes); `lingua_portuguesa/conhecimento_puro.py:1280` (caminho_natural)

- `lingua_portuguesa/tipos.py:73` (__post_init__); `lingua_portuguesa/tipos.py:90` (__post_init__)

- `matematica/divisao.py:59` (exato); `nucleo/trigonometria_natural.py:28` (texto)

- `matematica/expressao.py:85` (atual); `nucleo/analise_sintatica_finita.py:50` (atual)

- `nucleo/categorias_finitas.py:318` (CONE_FINITO); `nucleo/categorias_finitas.py:342` (COCONE_FINITO)

- `nucleo/cerebro_unico.py:181` (_normalizar); `nucleo/motor_mestre.py:422` (_normalizar)

- `nucleo/geometria_espacial.py:66` (norma_ao_quadrado); `nucleo/trigonometria_plana.py:61` (norma_ao_quadrado)

- `nucleo/gramaticas_finitas.py:263` (ARVORE_DERIVACAO_FINITA); `nucleo/gramaticas_livres_contexto_naturais.py:93` (ARVORE_SINTATICA_FINITA)

- `nucleo/metodos_finitos.py:62` (SOLUCOES_PREDICADO_FINITO); `nucleo/metodos_finitos.py:158` (TESTEMUNHAS_FINITO)

Estas métricas são uma linha de base, não uma sentença automática. Funções internas
matemáticas e callbacks podem ter contratos claros por contexto mesmo sem anotações;
duplicação exata pode ser intencional. Cada caso deve ser revisto antes de alterar código estável.
