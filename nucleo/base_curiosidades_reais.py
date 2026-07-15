# -*- coding: utf-8 -*-
"""
Etapa 63 — Base real de perguntas despejadas pelo utilizador.

Correção: a Etapa 51 tinha 300 IDs, mas não guardava o texto real das perguntas
nem respostas específicas suficientes. Este módulo guarda uma base consultável
por texto normalizado e responde sem cair no fallback MAT-000.

Sem dependências externas. Usa só Python padrão.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher


def sem_acentos(texto: str) -> str:
    texto = unicodedata.normalize("NFD", str(texto))
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")


def normalizar(texto: str) -> str:
    t = sem_acentos(texto).casefold()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


@dataclass(frozen=True, slots=True)
class PerguntaCuriosidade:
    numero: int
    categoria: str
    pergunta: str
    resposta: str
    aula: str
    teste: str
    # Fase 6: separa 'encontrado' de 'útil'. True quando há resposta
    # materializada de verdade em RESPOSTAS_ESPECIFICAS; False quando o
    # texto é só o registro genérico (a entrada existe mas ainda está curta).
    resposta_real: bool = False


# Perguntas reais trazidas pelo utilizador na Etapa 51. As respostas abaixo são
# curtas e diretas: servem para a conversa viva. A expansão longa/aula/teste pode
# usar estes campos como semente, mas a conversa nunca deve dizer "não sei a rota"
# quando a pergunta está nesta lista.
PERGUNTAS_RAW = """
1|Números e Curiosidades Numéricas|Qual é o único número que é igual ao dobro da soma dos seus algarismos?
2|Números e Curiosidades Numéricas|Porque é que o número 1729 é conhecido como o número de Hardy-Ramanujan?
3|Números e Curiosidades Numéricas|Qual é o menor número que pode ser escrito como soma de dois cubos de duas maneiras diferentes?
4|Números e Curiosidades Numéricas|O que é um número capicua? Dê um exemplo.
5|Números e Curiosidades Numéricas|Qual é o maior número primo conhecido atualmente aproximadamente?
6|Números e Curiosidades Numéricas|O que é um número amigo? Dê o exemplo mais famoso 220 e 284.
7|Números e Curiosidades Numéricas|Porque é que o número 0 não pode ser divisor de nenhum número?
8|Números e Curiosidades Numéricas|O que são números figurados? Dê um exemplo de números triangulares.
9|Números e Curiosidades Numéricas|O que é um número perfeito? Cite os dois primeiros.
10|Números e Curiosidades Numéricas|Qual é o número de ouro phi e qual o seu valor aproximado?
11|Números e Curiosidades Numéricas|O que é a sequência de Fibonacci? Escreva os primeiros 10 termos.
12|Números e Curiosidades Numéricas|Como é que a sequência de Fibonacci aparece na natureza?
13|Números e Curiosidades Numéricas|O que é um número narcisista ou de Armstrong? Dê um exemplo.
14|Números e Curiosidades Numéricas|O que é um número vampiro?
15|Números e Curiosidades Numéricas|Qual é a particularidade do número 2520?
16|Números e Curiosidades Numéricas|O que é um número feliz? O 7 é um número feliz?
17|Números e Curiosidades Numéricas|O que são números gémeos? Dê um exemplo.
18|Números e Curiosidades Numéricas|Porque é que não existe um último número primo?
19|Números e Curiosidades Numéricas|O que significa a expressão googol? E googolplex?
20|Números e Curiosidades Numéricas|Qual é a origem do nome do motor de busca Google?
21|Números e Curiosidades Numéricas|O que são números transcendentes? O pi é transcendente?
22|Números e Curiosidades Numéricas|Qual é a diferença entre números racionais e irracionais?
23|Números e Curiosidades Numéricas|Porque é que raiz de 2 é irracional? Ideia da prova.
24|Números e Curiosidades Numéricas|Quanto vale 0,999... 9 periódico? É igual a 1?
25|Números e Curiosidades Numéricas|O que é o número de Graham? Para que serve?
26|Números e Curiosidades Numéricas|O que são números imaginários? Porque se chamam assim?
27|Números e Curiosidades Numéricas|Qual é o valor de i elevado a i?
28|Números e Curiosidades Numéricas|O que é a identidade de Euler e porque é considerada bela?
29|Números e Curiosidades Numéricas|O que são números primos de Mersenne?
30|Números e Curiosidades Numéricas|Porque é que o número 1 não é considerado primo?
31|Números e Curiosidades Numéricas|O que é o número e número de Euler e qual o seu valor aproximado?
32|Números e Curiosidades Numéricas|Onde é que o número e aparece na natureza?
33|Números e Curiosidades Numéricas|O que é um número oblongo ou pronico?
34|Números e Curiosidades Numéricas|O que significa dizer que um número é normal?
35|Números e Curiosidades Numéricas|O pi é um número normal? Sabe-se a resposta?
36|Números e Curiosidades Numéricas|Quantos algarismos de pi são conhecidos atualmente?
37|Números e Curiosidades Numéricas|Existe algum dia dedicado ao pi? Quando se celebra?
38|Números e Curiosidades Numéricas|O que é o número de Avogadro e quanto vale?
39|Números e Curiosidades Numéricas|O que são números deficientes, abundantes e perfeitos?
40|Números e Curiosidades Numéricas|O número 666 tem propriedades matemáticas especiais. Quais?
41|Números e Curiosidades Numéricas|Qual é a conjectura de Goldbach?
42|Números e Curiosidades Numéricas|O que é a hipótese de Riemann e porque é tão importante?
43|Números e Curiosidades Numéricas|Quanto é a soma de todos os números naturais resultado surpreendente -1/12?
44|Números e Curiosidades Numéricas|O que é um palíndromo numérico?
45|Números e Curiosidades Numéricas|O que é o teorema do macaco infinito?
46|Números e Curiosidades Numéricas|Qual é o número de Erdős e o que significa?
47|Números e Curiosidades Numéricas|O que é a constante de Kaprekar 6174?
48|Números e Curiosidades Numéricas|Como funciona a rotina de Kaprekar para chegar a 6174?
49|Números e Curiosidades Numéricas|Qual é o maior número que pode ser escrito com três algarismos sem operadores?
50|Números e Curiosidades Numéricas|O que é a prova dos nove?
51|Geometria e Formas|Quantos lados tem um heptágono? E um eneágono?
52|Geometria e Formas|O que é um polígono regular?
53|Geometria e Formas|Qual é a soma dos ângulos internos de um triângulo?
54|Geometria e Formas|Qual é a soma dos ângulos internos de um pentágono?
55|Geometria e Formas|Porque é que só existem 5 sólidos platónicos?
56|Geometria e Formas|Quais são os nomes dos 5 sólidos platónicos?
57|Geometria e Formas|Quantas faces, arestas e vértices tem um cubo?
58|Geometria e Formas|Quantas faces, arestas e vértices tem um icosaedro?
59|Geometria e Formas|O que diz a Fórmula de Euler para poliedros?
60|Geometria e Formas|O que é um fractal? Dê três exemplos famosos.
61|Geometria e Formas|Quem é considerado o pai dos fractais?
62|Geometria e Formas|O que é o conjunto de Mandelbrot?
63|Geometria e Formas|Qual é o perímetro do floco de neve de Koch após infinitas iterações?
64|Geometria e Formas|O que é a esponja de Menger?
65|Geometria e Formas|Qual é a dimensão fractal da esponja de Menger?
66|Geometria e Formas|O que é uma curva de Peano e porque é surpreendente?
67|Geometria e Formas|É possível uma curva preencher completamente um quadrado?
68|Geometria e Formas|O que são as geometrias não euclidianas?
69|Geometria e Formas|Quem foram os criadores das geometrias não euclidianas?
70|Geometria e Formas|O que é a fita de Möbius e quantos lados tem?
71|Geometria e Formas|O que acontece se cortar uma fita de Möbius ao meio no sentido longitudinal?
72|Geometria e Formas|O que é a garrafa de Klein?
73|Geometria e Formas|Quantas cores são necessárias para colorir qualquer mapa plano?
74|Geometria e Formas|Quem provou o Teorema das Quatro Cores e quando?
75|Geometria e Formas|Porque foi a prova do Teorema das Quatro Cores polémica?
76|Geometria e Formas|O que é o problema da ponte de Königsberg?
77|Geometria e Formas|Quem resolveu o problema da ponte de Königsberg e o que fundou?
78|Geometria e Formas|O que é a razão áurea e onde aparece na geometria?
79|Geometria e Formas|O que é o retângulo de ouro?
80|Geometria e Formas|Como se constrói uma espiral áurea?
81|Geometria e Formas|O que é um nó em Matemática?
82|Geometria e Formas|Quantos nós existem com 7 cruzamentos?
83|Geometria e Formas|O que é o quipu dos Incas e qual a sua relação com a Matemática?
84|Geometria e Formas|Qual é o maior polígono regular que pode ser construído com régua e compasso?
85|Geometria e Formas|O que diz o teorema de Gauss-Wantzel sobre polígonos construtíveis?
86|Geometria e Formas|O que é o pentagrama e qual a sua ligação com a razão áurea?
87|Geometria e Formas|Porque é que as abelhas constroem favos hexagonais?
88|Geometria e Formas|O que são os sólidos de Arquimedes?
89|Geometria e Formas|Quantos sólidos de Arquimedes existem?
90|Geometria e Formas|O que é um toro ou toroide?
91|Geometria e Formas|Quantos buracos tem um toro?
92|Geometria e Formas|O que é a conjetura de Poincaré?
93|Geometria e Formas|Quem resolveu a conjetura de Poincaré e em que ano?
94|Geometria e Formas|O que é uma esfera exótica?
95|Geometria e Formas|O que é o teorema de Pitágoras e quem foi Pitágoras?
96|Geometria e Formas|Os babilónios conheciam o teorema de Pitágoras antes de Pitágoras?
97|Geometria e Formas|O que é uma prova do teorema de Pitágoras sem palavras?
98|Geometria e Formas|O que são as lúnulas de Hipócrates?
99|Geometria e Formas|O que é a quadratura do círculo e porque é impossível?
100|Geometria e Formas|Quais são os três problemas clássicos da Geometria Grega?
101|História da Matemática|Quem é considerado o Pai da Matemática?
102|História da Matemática|O que são os Elementos de Euclides?
103|História da Matemática|Quantos livros compõem os Elementos de Euclides?
104|História da Matemática|Quem foi Pitágoras e o que defendia a sua escola?
105|História da Matemática|É verdade que Pitágoras descobriu o teorema que leva o seu nome?
106|História da Matemática|Quem foi Arquimedes e quais as suas principais contribuições?
107|História da Matemática|O que gritou Arquimedes ao descobrir o princípio da hidrostática?
108|História da Matemática|Como é que Arquimedes estimou o valor de pi?
109|História da Matemática|É verdade que Arquimedes incendiou navios romanos com espelhos?
110|História da Matemática|Quem foi Hipátia de Alexandria?
111|História da Matemática|Qual foi o destino trágico de Hipátia?
112|História da Matemática|Quem foi Al-Khwarizmi?
113|História da Matemática|De onde vem a palavra álgebra?
114|História da Matemática|De onde vem a palavra algoritmo?
115|História da Matemática|O que é o Liber Abaci de Fibonacci?
116|História da Matemática|Fibonacci inventou a sequência de Fibonacci? De onde veio?
117|História da Matemática|Qual é o problema dos coelhos de Fibonacci?
118|História da Matemática|Quem foi Leonhard Euler e quantas obras publicou?
119|História da Matemática|É verdade que Euler continuou a trabalhar mesmo depois de cego?
120|História da Matemática|Quem foi Carl Friedrich Gauss e porque é chamado Príncipe dos Matemáticos?
121|História da Matemática|Qual foi o feito de Gauss aos 8 anos?
122|História da Matemática|Quem foi Évariste Galois e porque morreu tão jovem?
123|História da Matemática|O que fez Galois na noite anterior ao seu duelo fatal?
124|História da Matemática|Quem foi Srinivasa Ramanujan?
125|História da Matemática|Como é que Ramanujan aprendeu Matemática?
126|História da Matemática|Qual foi a relação entre Hardy e Ramanujan?
127|História da Matemática|O que é o número de Hardy-Ramanujan 1729?
128|História da Matemática|Quem foi Emmy Noether e qual o seu teorema mais famoso?
129|História da Matemática|Porque é que o Teorema de Noether é importante para a Física?
130|História da Matemática|Quem foi Alan Turing e qual o seu papel na Segunda Guerra Mundial?
131|História da Matemática|O que é a Máquina de Turing?
132|História da Matemática|O que é o Teste de Turing?
133|História da Matemática|Quem foi Katherine Johnson e qual o seu contributo para a NASA?
134|História da Matemática|O que retrata o filme Hidden Figures Figuras Escondidas?
135|História da Matemática|Quem foi Maryam Mirzakhani?
136|História da Matemática|Porque é que a Medalha Fields de Maryam Mirzakhani foi histórica?
137|História da Matemática|Quem foi John Nash e que teoria desenvolveu?
138|História da Matemática|O que retrata o filme Uma Mente Brilhante?
139|História da Matemática|Quem foi Paul Erdős e qual o seu estilo de vida peculiar?
140|História da Matemática|O que é o número de Erdős?
141|História da Matemática|Quem foi Sofia Kovalevskaya?
142|História da Matemática|O que são os Problemas de Hilbert?
143|História da Matemática|Quantos problemas foram apresentados por Hilbert em 1900?
144|História da Matemática|O que são os Prémios do Milénio do Clay Institute?
145|História da Matemática|Quanto dinheiro ganha quem resolve um Problema do Milénio?
146|História da Matemática|Quem foi Grigori Perelman e porque recusou prémios milionários?
147|História da Matemática|Quem foi René Descartes e qual a sua frase mais famosa?
148|História da Matemática|O que é o plano cartesiano?
149|História da Matemática|Quem foi Blaise Pascal e quais os seus contributos matemáticos?
150|História da Matemática|Com que idade Pascal escreveu o seu primeiro tratado de Geometria?
151|Probabilidade Jogos e Paradoxos|O que é o Paradoxo de Monty Hall?
152|Probabilidade Jogos e Paradoxos|No Paradoxo de Monty Hall deve-se trocar de porta? Porquê?
153|Probabilidade Jogos e Paradoxos|O que é o Paradoxo do Aniversário?
154|Probabilidade Jogos e Paradoxos|Quantas pessoas são necessárias para ter 50% de probabilidade de aniversário repetido?
155|Probabilidade Jogos e Paradoxos|O que é o problema dos dois envelopes?
156|Probabilidade Jogos e Paradoxos|O que é o paradoxo de São Petersburgo?
157|Probabilidade Jogos e Paradoxos|O que é o paradoxo de Simpson?
158|Probabilidade Jogos e Paradoxos|O que é a Gambler's Fallacy Falácia do Jogador?
159|Probabilidade Jogos e Paradoxos|Se sair cara 10 vezes seguidas qual a probabilidade de sair cara na 11ª?
160|Probabilidade Jogos e Paradoxos|O que é a Lei dos Grandes Números?
161|Probabilidade Jogos e Paradoxos|O que é o Teorema do Limite Central?
162|Probabilidade Jogos e Paradoxos|Como é que a distribuição normal aparece na natureza?
163|Probabilidade Jogos e Paradoxos|O que é o problema do bode ou problema do carro e das cabras?
164|Probabilidade Jogos e Paradoxos|O que é a maldição do vencedor em leilões?
165|Probabilidade Jogos e Paradoxos|O que é o paradoxo de Parrondo?
166|Probabilidade Jogos e Paradoxos|É possível ganhar combinando dois jogos perdentes Paradoxo de Parrondo?
167|Probabilidade Jogos e Paradoxos|O que é o problema do colecionador de cromos cupons?
168|Probabilidade Jogos e Paradoxos|Quantos cromos em média são necessários para completar uma coleção de n?
169|Probabilidade Jogos e Paradoxos|O que é o problema da secretária?
170|Probabilidade Jogos e Paradoxos|Qual é a estratégia ótima no problema da secretária?
171|Probabilidade Jogos e Paradoxos|O que é o paradoxo de Bertrand probabilidade?
172|Probabilidade Jogos e Paradoxos|O que é o problema da agulha de Buffon?
173|Probabilidade Jogos e Paradoxos|Como estimar pi usando agulhas e linhas paralelas?
174|Probabilidade Jogos e Paradoxos|O que é o dilema do prisioneiro?
175|Probabilidade Jogos e Paradoxos|Qual é a estratégia dominante no dilema do prisioneiro?
176|Probabilidade Jogos e Paradoxos|O que é o equilíbrio de Nash?
177|Probabilidade Jogos e Paradoxos|O que é o jogo da vida de Conway?
178|Probabilidade Jogos e Paradoxos|O Jogo da Vida é um jogo propriamente dito?
179|Probabilidade Jogos e Paradoxos|O que são autómatos celulares?
180|Probabilidade Jogos e Paradoxos|O que é o teorema do ponto fixo de Brouwer?
181|Probabilidade Jogos e Paradoxos|Se agitar um copo de água há sempre um ponto que volta à posição inicial?
182|Probabilidade Jogos e Paradoxos|O que é o teorema de Bayes?
183|Probabilidade Jogos e Paradoxos|Qual é a aplicação mais famosa do teorema de Bayes?
184|Probabilidade Jogos e Paradoxos|O que é o problema do sono da Bela Adormecida?
185|Probabilidade Jogos e Paradoxos|Quantos baralhos de cartas diferentes existem?
186|Probabilidade Jogos e Paradoxos|Quanto tempo demoraria a criar todas as ordens possíveis de um baralho?
187|Probabilidade Jogos e Paradoxos|O que é um qubit em computação quântica?
188|Probabilidade Jogos e Paradoxos|O que é o algoritmo de Shor?
189|Probabilidade Jogos e Paradoxos|Porque é que o algoritmo de Shor é uma ameaça à criptografia?
190|Probabilidade Jogos e Paradoxos|O que é o emaranhamento quântico?
191|Probabilidade Jogos e Paradoxos|Qual é a diferença entre probabilidade clássica e quântica?
192|Probabilidade Jogos e Paradoxos|O que é o gato de Schrödinger?
193|Probabilidade Jogos e Paradoxos|O que é a interpretação de Copenhaga da Mecânica Quântica?
194|Probabilidade Jogos e Paradoxos|O que é o teorema de Bell?
195|Probabilidade Jogos e Paradoxos|O que é um número aleatório? Existem números verdadeiramente aleatórios?
196|Probabilidade Jogos e Paradoxos|Como são gerados números pseudoaleatórios em computadores?
197|Probabilidade Jogos e Paradoxos|O que é o paradoxo do exame surpresa?
198|Probabilidade Jogos e Paradoxos|O que é o paradoxo de Newcomb?
199|Probabilidade Jogos e Paradoxos|O que é o problema da troca de selos?
200|Probabilidade Jogos e Paradoxos|O que é o problema do mentiroso e do verdadeiro?
201|Matemática na Natureza e Arte|O que são os padrões de Turing na natureza?
202|Matemática na Natureza e Arte|Como é que as riscas das zebras se formam modelo matemático?
203|Matemática na Natureza e Arte|O que é a filotaxia e como se relaciona com Fibonacci?
204|Matemática na Natureza e Arte|Porque é que os girassóis têm espirais de Fibonacci?
205|Matemática na Natureza e Arte|O que é a proporção áurea no corpo humano?
206|Matemática na Natureza e Arte|Quem foi Luca Pacioli e qual a sua obra sobre a proporção divina?
207|Matemática na Natureza e Arte|Leonardo da Vinci usava Matemática na sua arte? Como?
208|Matemática na Natureza e Arte|O que é a perspetiva na pintura e qual a sua base matemática?
209|Matemática na Natureza e Arte|Quem foi Piero della Francesca e qual o seu contributo matemático?
210|Matemática na Natureza e Arte|O que são as figuras impossíveis de M.C. Escher?
211|Matemática na Natureza e Arte|Como é que Escher usou a Matemática?
212|Matemática na Natureza e Arte|O que é o grupo de simetria de um objeto?
213|Matemática na Natureza e Arte|Quantos grupos de simetria de rosáceas existem?
214|Matemática na Natureza e Arte|O que são os grupos de frisos? Quantos existem?
215|Matemática na Natureza e Arte|O que são os grupos de padrões de parede? Quantos existem?
216|Matemática na Natureza e Arte|O que é a simetria pentagonal e porque é proibida em cristais?
217|Matemática na Natureza e Arte|O que são quasicristais e quem os descobriu?
218|Matemática na Natureza e Arte|O que é a teoria do caos?
219|Matemática na Natureza e Arte|O que é o efeito borboleta?
220|Matemática na Natureza e Arte|Quem foi Edward Lorenz e como descobriu o efeito borboleta?
221|Matemática na Natureza e Arte|O que é um atrator estranho?
222|Matemática na Natureza e Arte|O que é o atrator de Lorenz?
223|Matemática na Natureza e Arte|O que são os conjuntos de Julia?
224|Matemática na Natureza e Arte|Qual é a relação entre o conjunto de Mandelbrot e os conjuntos de Julia?
225|Matemática na Natureza e Arte|O que é a geometria sagrada?
226|Matemática na Natureza e Arte|O que significa a Flor da Vida?
227|Matemática na Natureza e Arte|O que é o Homem Vitruviano de Leonardo da Vinci?
228|Matemática na Natureza e Arte|O que é o retângulo de raiz 2 e onde é usado tamanho de papel?
229|Matemática na Natureza e Arte|Porque é que o papel A4 tem a proporção raiz 2 para 1?
230|Matemática na Natureza e Arte|O que é a sequência de Padovan e onde aparece?
231|Curiosidades Truques e Factos|Porque é que multiplicar por zero dá sempre zero?
232|Curiosidades Truques e Factos|Qual é o truque para multiplicar por 11 rapidamente?
233|Curiosidades Truques e Factos|Qual é o truque para multiplicar por 9 com os dedos?
234|Curiosidades Truques e Factos|Porque é que a tabuada do 9 tem os algarismos a somar 9?
235|Curiosidades Truques e Factos|Como se faz a prova real da multiplicação?
236|Curiosidades Truques e Factos|O que é o método da borboleta para somar frações?
237|Curiosidades Truques e Factos|Qual é a forma mais rápida de somar números de 1 a 100?
238|Curiosidades Truques e Factos|Quanto vale 7 vezes 8? Truque mnemónico 5-6-7-8.
239|Curiosidades Truques e Factos|O que é o quadrado mágico? Dê um exemplo.
240|Curiosidades Truques e Factos|Qual é a constante mágica do quadrado de Dürer Melancolia I?
241|Curiosidades Truques e Factos|Em que ano foi criado o quadro Melancolia I de Dürer?
242|Curiosidades Truques e Factos|Onde aparece esse ano no quadrado mágico da obra?
243|Curiosidades Truques e Factos|O que é o Sudoku e qual a sua origem?
244|Curiosidades Truques e Factos|Quantos Sudokus diferentes existem?
245|Curiosidades Truques e Factos|O que é o problema do caixeiro viajante?
246|Curiosidades Truques e Factos|Quantas rotas possíveis existem para 10 cidades? E para 20?
247|Curiosidades Truques e Factos|O que é um grafo e para que serve?
248|Curiosidades Truques e Factos|O que são as pontes de Königsberg em teoria dos grafos?
249|Curiosidades Truques e Factos|O que é o número cromático de um grafo?
250|Curiosidades Truques e Factos|O que é a fórmula de Deus?
251|Curiosidades Truques e Factos|Qual é a fórmula mais bonita da Matemática?
252|Curiosidades Truques e Factos|Qual é a equação mais difícil do mundo?
253|Curiosidades Truques e Factos|O que é o Milagre da Matemática?
254|Curiosidades Truques e Factos|O que significa a frase A Matemática é a linguagem do Universo?
255|Curiosidades Truques e Factos|Quem disse Deus é um matemático?
256|Curiosidades Truques e Factos|Quem disse A Matemática é a rainha das ciências?
257|Curiosidades Truques e Factos|Qual é a origem da palavra Matemática?
258|Curiosidades Truques e Factos|O que significa Matemática em grego?
259|Curiosidades Truques e Factos|Qual é o livro mais traduzido do mundo depois da Bíblia?
260|Curiosidades Truques e Factos|Quantas páginas tem a maior demonstração matemática?
261|Curiosidades Truques e Factos|Qual foi a primeira mulher a ganhar a Medalha Fields?
262|Curiosidades Truques e Factos|Qual é o país com mais medalhas Fields per capita?
263|Curiosidades Truques e Factos|O que é o Nobel da Matemática?
264|Curiosidades Truques e Factos|Porque é que não existe Prémio Nobel de Matemática?
265|Curiosidades Truques e Factos|O que são os Prémios Abel?
266|Curiosidades Truques e Factos|O que são os Prémios Breakthrough?
267|Curiosidades Truques e Factos|Quanto dinheiro ganhou Perelman e recusou?
268|Curiosidades Truques e Factos|Qual é a instituição matemática mais antiga do mundo?
269|Curiosidades Truques e Factos|O que é o Instituto de Matemática Pura e Aplicada IMPA?
270|Curiosidades Truques e Factos|Em que país fica o IMPA e qual a sua importância?
271|Matemática Aplicada e Tecnologia|Como é que a Matemática é usada na compressão de imagens JPEG?
272|Matemática Aplicada e Tecnologia|O que é a transformada de Fourier e para que serve?
273|Matemática Aplicada e Tecnologia|Como funciona a Transformada Rápida de Fourier FFT?
274|Matemática Aplicada e Tecnologia|O que é a criptografia RSA e como funciona?
275|Matemática Aplicada e Tecnologia|Porque é que a fatorização de números grandes é difícil?
276|Matemática Aplicada e Tecnologia|O que é a criptografia de curva elíptica?
277|Matemática Aplicada e Tecnologia|Como é que o GPS usa a Matemática?
278|Matemática Aplicada e Tecnologia|O que é a teoria da relatividade de Einstein papel da Matemática?
279|Matemática Aplicada e Tecnologia|Qual é a equação mais famosa de Einstein?
280|Matemática Aplicada e Tecnologia|O que significa E=mc²?
281|Matemática Aplicada e Tecnologia|Como é que a Matemática é usada em inteligência artificial?
282|Matemática Aplicada e Tecnologia|O que é o algoritmo de retropropagação backpropagation?
283|Matemática Aplicada e Tecnologia|O que é o gradiente descendente?
284|Matemática Aplicada e Tecnologia|Como é que o Google PageRank funciona matematicamente?
285|Matemática Aplicada e Tecnologia|O que são cadeias de Markov e onde são usadas?
286|Matemática Aplicada e Tecnologia|Como é que a Matemática prevê a propagação de epidemias?
287|Matemática Aplicada e Tecnologia|O que é o modelo SIR em epidemiologia?
288|Matemática Aplicada e Tecnologia|Como é que os bancos usam a Matemática para calcular juros compostos?
289|Matemática Aplicada e Tecnologia|Qual é a fórmula dos juros compostos?
290|Matemática Aplicada e Tecnologia|O que é o interesse contínuo e como se relaciona com o número e?
291|Matemática Aplicada e Tecnologia|Como é que a Matemática é usada na animação 3D Pixar?
292|Matemática Aplicada e Tecnologia|O que são as curvas de Bézier?
293|Matemática Aplicada e Tecnologia|Como é que a Matemática prevê o tempo meteorologia?
294|Matemática Aplicada e Tecnologia|O que são as equações de Navier-Stokes?
295|Matemática Aplicada e Tecnologia|Porque é que a previsão do tempo é um problema caótico?
296|Matemática Aplicada e Tecnologia|Como é que a Matemática é usada na música?
297|Matemática Aplicada e Tecnologia|O que são os harmónicos e as séries de Fourier na música?
298|Matemática Aplicada e Tecnologia|Que instrumento musical é baseado em logaritmos construção?
299|Matemática Aplicada e Tecnologia|O que é a Matemática do cérebro neurociência computacional?
300|Matemática Aplicada e Tecnologia|Como é que os computadores quânticos usam a Matemática?
"""


RESPOSTAS_ESPECIFICAS: dict[int, str] = {
    1: "O número 18: a soma dos algarismos é 1+8=9 e o dobro é 18.",
    2: "1729 é o número de Hardy-Ramanujan porque é o menor número que se escreve como soma de dois cubos positivos de duas formas: 1³+12³ e 9³+10³.",
    3: "É 1729: 1³+12³=1729 e 9³+10³=1729.",
    4: "Número capicua é o que se lê igual da esquerda para a direita e da direita para a esquerda. Exemplo: 121 ou 1331.",
    7: "Zero não pode ser divisor porque dividir por zero perguntaria: quantas vezes 0 cabe para formar um número? Para número diferente de 0 é impossível; para 0 seria indefinido, pois qualquer quantidade de zeros dá 0.",
    9: "Número perfeito é igual à soma dos seus divisores próprios. Os dois primeiros são 6 = 1+2+3 e 28 = 1+2+4+7+14.",
    10: "O número de ouro φ é a razão em que todo/parte maior = parte maior/parte menor. Vale aproximadamente 1,618.",
    11: "Fibonacci é uma sequência em que cada termo nasce da soma dos dois anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.",
    18: "Não existe último primo: se alguém listar todos os primos e multiplicar todos, depois somar 1, o novo número deixa resto 1 ao dividir por cada primo da lista. Então a lista era incompleta.",
    21: "Transcendente é número que não é raiz de nenhum polinómio não nulo com coeficientes inteiros. π é transcendente.",
    23: "Ideia: se √2 fosse a/b em fração irredutível, então a²=2b², logo a seria par; escrevendo a=2k, resulta b também par. Contradição: a/b não era irredutível.",
    24: "0,999... é igual a 1. Se x=0,999..., então 10x=9,999...; subtraindo: 9x=9; logo x=1.",
    30: "O 1 não é primo porque primo deve ter exatamente dois divisores positivos: 1 e ele próprio. O 1 tem só um divisor positivo.",
    31: "O número e é a base do crescimento contínuo. Vale aproximadamente 2,71828.",
    41: "Goldbach forte diz que todo número par maior que 2 pode ser escrito como soma de dois primos. Continua em aberto.",
    42: "A hipótese de Riemann diz que os zeros não triviais da função zeta têm parte real 1/2. É importante porque controla finamente a distribuição dos primos.",
    43: "A soma comum 1+2+3+... diverge. O valor -1/12 aparece em regularização analítica, não como soma usual de números naturais.",
    47: "6174 é a constante de Kaprekar para números de 4 algarismos com pelo menos dois algarismos diferentes.",
    48: "Rotina de Kaprekar: escolhe um número de 4 algarismos, ordena algarismos em ordem decrescente e crescente, subtrai menor de maior e repete. Em muitos casos chega a 6174.",
    49: "Sem operadores, o maior número com três algarismos é 999.",
    50: "Prova dos nove é um teste rápido usando restos módulo 9 para verificar se uma conta provavelmente está certa. Não prova totalmente, mas ajuda a apanhar erros.",
    53: "Num triângulo plano euclidiano, a soma dos ângulos internos é 180 graus.",
    54: "Um pentágono tem soma dos ângulos internos igual a (5−2)×180 = 540 graus.",
    55: "Só existem 5 sólidos platónicos porque as faces regulares iguais precisam encontrar-se em vértices com soma angular menor que 360 graus. Essa restrição só permite tetraedro, cubo, octaedro, dodecaedro e icosaedro.",
    56: "Os 5 sólidos platónicos são: tetraedro, cubo, octaedro, dodecaedro e icosaedro.",
    57: "Um cubo tem 6 faces, 12 arestas e 8 vértices.",
    59: "Para poliedros convexos, a fórmula de Euler diz V − A + F = 2: vértices menos arestas mais faces é 2.",
    60: "Fractal é forma com detalhe repetido em escalas diferentes. Exemplos: conjunto de Mandelbrot, floco de Koch e triângulo de Sierpinski.",
    63: "O perímetro do floco de Koch tende ao infinito, embora a área fique finita.",
    70: "A fita de Möbius é uma superfície com uma só face e uma só borda, feita com meia torção antes de colar as pontas.",
    73: "Quatro cores bastam para colorir qualquer mapa plano, com regiões adjacentes de cores diferentes.",
    76: "O problema das pontes de Königsberg perguntava se era possível atravessar todas as pontes uma só vez e voltar. Euler mostrou que não, fundando a teoria dos grafos.",
    92: "A conjetura de Poincaré diz que toda 3-variedade fechada e simplesmente conexa é topologicamente uma 3-esfera.",
    93: "Foi resolvida por Grigori Perelman em trabalhos divulgados em 2002–2003.",
    99: "Quadratura do círculo é construir, só com régua e compasso, um quadrado com a mesma área de um círculo. É impossível porque π é transcendente.",
    112: "Al-Khwarizmi foi matemático persa associado ao desenvolvimento da álgebra e dos métodos algorítmicos.",
    113: "Álgebra vem de al-jabr, termo do livro de Al-Khwarizmi ligado à restauração/transposição em equações.",
    114: "Algoritmo vem do nome latinizado de Al-Khwarizmi.",
    121: "O feito famoso de Gauss criança foi somar rapidamente os números de 1 a 100 usando pares que somam 101.",
    127: "1729 é o número de Hardy-Ramanujan: 1³+12³ = 9³+10³ = 1729.",
    131: "Máquina de Turing é um modelo abstrato de computação com fita, estados e regras; serve para estudar o que pode ser computado.",
    151: "Monty Hall é um paradoxo de escolha com três portas: depois de escolher uma, o apresentador abre uma porta perdedora e oferece troca.",
    152: "Sim, deve-se trocar: a chance passa de 1/3 para 2/3, porque a informação do apresentador concentra a probabilidade na outra porta fechada.",
    153: "O paradoxo do aniversário mostra que num grupo relativamente pequeno já há boa chance de duas pessoas fazerem anos no mesmo dia.",
    154: "Com 23 pessoas, a probabilidade de aniversário repetido passa de 50% aproximadamente.",
    159: "Se a moeda é justa e os lançamentos são independentes, depois de 10 caras a probabilidade da 11ª ser cara continua 1/2.",
    160: "A Lei dos Grandes Números diz que, repetindo muitas vezes uma experiência, a média observada tende para o valor esperado.",
    161: "O Teorema do Limite Central diz que somas/médias de muitas variáveis independentes tendem a parecer normais sob condições adequadas.",
    174: "Dilema do prisioneiro é um jogo em que a escolha egoísta individual pode levar a resultado pior para todos do que a cooperação.",
    176: "Equilíbrio de Nash é situação em que ninguém melhora mudando sozinho a sua estratégia, dadas as estratégias dos outros.",
    182: "Bayes permite atualizar uma probabilidade quando surge evidência: crença anterior + evidência = crença posterior.",
    187: "Qubit é unidade de informação quântica que pode estar em combinação de 0 e 1, ao contrário do bit clássico que é 0 ou 1.",
    188: "Shor é um algoritmo quântico para fatorizar inteiros grandes de forma muito mais eficiente que métodos clássicos conhecidos.",
    201: "Padrões de Turing são padrões naturais que podem surgir quando duas substâncias se difundem e reagem em ritmos diferentes. Uma ativa a formação local e outra inibe ao redor. Dessa disputa podem nascer manchas, riscas e padrões repetidos.",
    202: "No modelo matemático, as riscas das zebras podem ser vistas como resultado de reação-difusão: células produzem sinais químicos; um sinal aumenta pigmento local e outro espalha inibição. A geometria do corpo e o tempo de crescimento esticam o padrão em riscas.",
    203: "Filotaxia é o arranjo de folhas, sementes ou pétalas numa planta. Ela se liga a Fibonacci porque ângulos de crescimento próximos do ângulo áureo distribuem novos elementos sem sobrepor muito, criando contagens em espirais como 34/55 ou 55/89.",
    204: "Girassóis mostram espirais de Fibonacci porque cada nova semente ocupa espaço onde há menos conflito com as anteriores. O ângulo próximo ao ângulo áureo espalha sementes de modo eficiente, e as espirais visíveis aparecem em contagens vizinhas da sequência de Fibonacci.",
    205: "A proporção áurea no corpo humano é a ideia de comparar comprimentos do corpo com a razão φ≈1,618. Aparece em algumas aproximações artísticas e anatómicas, mas não é uma lei universal perfeita do corpo humano.",
    218: "Teoria do caos estuda sistemas determinísticos muito sensíveis às condições iniciais: pequenas diferenças no início podem gerar grandes diferenças depois.",
    219: "Efeito borboleta é a ideia de que pequena mudança inicial pode alterar muito a evolução de um sistema caótico, como o clima.",
    228: "Retângulo de raiz 2 tem proporção √2:1. Ao cortar ao meio, conserva a mesma forma. É usado na família de papéis A, como A4.",
    229: "O papel A4 tem proporção √2:1 para que, ao dobrar ou cortar ao meio, o formato continue semelhante. Isso facilita escalas e cópias.",
    231: "Multiplicar por zero dá zero porque multiplicar é juntar grupos iguais. 5×0 é juntar cinco grupos vazios: 0+0+0+0+0=0. Pela distributiva: 5×(1−1)=5−5=0.",
    232: "Truque do 11: para multiplicar um número de dois algarismos por 11, põe a soma dos algarismos no meio: 23×11 vira 2 | 2+3 | 3 = 253. Se passar de 9, leva 1: 78×11 = 858.",
    233: "Truque do 9 com dedos: para 9×n, dobra o n-ésimo dedo. Os dedos à esquerda dão dezenas e à direita unidades. Exemplo 9×4: três à esquerda e seis à direita = 36.",
    234: "Na tabuada do 9, os múltiplos até 9×10 têm soma dos algarismos igual a 9 porque 9 é congruente a 0 módulo 9; seus múltiplos preservam esse resto.",
    237: "A forma rápida de somar 1 a 100 é formar pares: 1+100=101, 2+99=101, ... há 50 pares. Resultado: 50×101=5050.",
    238: "7×8=56. Truque: a sequência 5,6,7,8 ajuda a lembrar que 56=7×8.",
    245: "O problema do caixeiro viajante procura a rota mais curta que visita várias cidades uma vez e volta ao início. Cresce muito rápido em número de possibilidades.",
    247: "Grafo é uma estrutura de pontos e ligações. Serve para modelar redes, rotas, amizades, circuitos e dependências.",
    272: "Transformada de Fourier decompõe um sinal em frequências. Serve em som, imagem, telecomunicações, compressão e análise de vibrações.",
    274: "RSA usa uma chave pública baseada no produto de dois primos grandes. Multiplicar os primos é fácil; descobrir os primos a partir do produto é difícil para métodos clássicos conhecidos.",
    277: "O GPS usa geometria, tempo e relatividade: satélites enviam sinais com horários; o receptor calcula distâncias pelo tempo de chegada e resolve a posição por trilateração.",
    279: "A equação mais famosa de Einstein é E=mc².",
    280: "E=mc² significa que massa e energia são equivalentes: uma massa m corresponde a energia E igual a m vezes a velocidade da luz ao quadrado.",
    281: "Na IA, a Matemática aparece em vetores, matrizes, probabilidade, otimização, funções de perda e ajuste de parâmetros por erro.",
    282: "Backpropagation calcula como o erro final muda quando cada peso da rede muda. Depois usa esses sinais para corrigir os pesos.",
    283: "Gradiente descendente é método de ajuste: olha a direção em que o erro cresce e anda no sentido contrário para reduzir o erro.",
    287: "O modelo SIR divide a população em Suscetíveis, Infetados e Recuperados, e usa taxas de passagem entre esses grupos para estudar epidemias.",
    289: "Juros compostos: M = C(1+i)^n, onde C é capital inicial, i é taxa por período e n é número de períodos.",
    294: "Navier-Stokes são equações que descrevem movimento de fluidos, relacionando velocidade, pressão, viscosidade e forças externas.",
    295: "Previsão do tempo é caótica porque pequenas diferenças na medição inicial podem crescer e gerar previsões muito diferentes depois.",
    300: "Computadores quânticos usam álgebra linear e probabilidade quântica: estados são vetores, portas são transformações e medições produzem resultados probabilísticos.",
    # --- Expansão prioritária da Fase 7 (plano contextual) ---
    28: "A identidade de Euler é e^(iπ) + 1 = 0. É considerada bela porque liga numa só igualdade cinco constantes fundamentais: e, i, π, 1 e 0.",
    85: "O teorema de Gauss-Wantzel diz que um polígono regular de n lados é construtível com régua e compasso exatamente quando n é produto de uma potência de 2 por primos de Fermat distintos (3, 5, 17, 257, 65537).",
    88: "Os sólidos de Arquimedes são poliedros convexos com faces regulares de mais de um tipo e vértices todos iguais entre si — por exemplo, o cuboctaedro e o icosaedro truncado (padrão da bola de futebol clássica).",
    89: "Existem 13 sólidos de Arquimedes.",
    106: "Arquimedes de Siracusa (c. 287–212 a.C.) foi matemático, físico e engenheiro grego. Contribuições principais: princípio da hidrostática (empuxo), lei das alavancas, cálculo de áreas e volumes por exaustão (esfera e cilindro), estimativa de π e máquinas de defesa de Siracusa.",
    107: "Segundo a tradição, Arquimedes gritou 'Eureka!' ('descobri!') ao perceber, no banho, que o volume de água deslocada mede o volume do corpo submerso — a chave do princípio da hidrostática.",
    108: "Arquimedes estimou π encaixando o círculo entre polígonos regulares inscritos e circunscritos, dobrando os lados até 96. Concluiu que π está entre 3 + 10/71 e 3 + 1/7 (entre ~3,1408 e ~3,1429).",
    109: "A história dos espelhos incendiando navios romanos é lenda antiga sem confirmação: reconstruções modernas mostram que seria muito difícil na prática. É contada sobre Arquimedes, mas não há prova histórica.",
    118: "Leonhard Euler (1707–1783) foi um matemático suíço, um dos mais produtivos da história: as suas obras completas passam de 800 trabalhos e dezenas de volumes. Criou ou fixou notações como e, i, f(x) e Σ, fundou a teoria dos grafos (pontes de Königsberg) e trabalhou em quase todas as áreas da matemática do seu tempo.",
    119: "Sim. Euler perdeu a visão quase por completo nos últimos anos de vida e continuou a produzir intensamente, ditando cálculos e artigos de memória — parte substancial da sua obra é desse período.",
    120: "Carl Friedrich Gauss (1777–1855) foi um matemático alemão chamado 'Princeps mathematicorum' (Príncipe dos Matemáticos) pela profundidade e alcance da obra: teoria dos números (Disquisitiones Arithmeticae), método dos mínimos quadrados, distribuição normal, previsão da órbita de Ceres e contribuições em geometria e magnetismo.",
    135: "Maryam Mirzakhani (1977–2017) foi uma matemática iraniana, professora em Stanford, especialista em geometria e dinâmica de superfícies de Riemann e espaços de módulos. Em 2014 tornou-se a primeira mulher a receber a Medalha Fields. Morreu em 2017, de cancro.",
    136: "A Medalha Fields de Maryam Mirzakhani (2014) foi histórica porque foi a primeira vez, desde a criação do prémio em 1936, que uma mulher o recebeu — pelo trabalho em dinâmica e geometria de superfícies de Riemann.",
    217: "Quasicristais são sólidos com estrutura ordenada mas não periódica — a ordem não se repete por translação, e aparecem simetrias 'proibidas' em cristais clássicos, como a de ordem 5. Foram descobertos por Dan Shechtman em 1982 (publicado em 1984), o que lhe valeu o Nobel de Química de 2011. Têm ligação matemática com os ladrilhos de Penrose.",
}


def _resposta_generica(item_numero: int, pergunta: str, categoria: str) -> str:
    p = normalizar(pergunta)
    if "o que e" in p or "quem foi" in p or "qual e" in p:
        return (
            f"Esta pergunta está registada na base de curiosidades como item {item_numero} ({categoria}). "
            f"Resposta curta: trata do conceito/pergunta '{pergunta}'. O PSF deve explicar em linguagem simples, dar exemplo, indicar se é facto estável, história, curiosidade ou problema aberto, e não fingir atualidade quando depender de dados que mudam."
        )
    if "porque" in p or "por que" in p or "como" in p:
        return (
            f"Esta pergunta está registada na base de curiosidades como item {item_numero} ({categoria}). "
            f"Resposta curta: o caminho PSF é explicar a causa ou mecanismo de '{pergunta}', montar por passos, dar exemplo e testar a ideia com um caso pequeno."
        )
    return (
        f"Item vivo {item_numero} da base de curiosidades ({categoria}): {pergunta}. "
        "Resposta curta disponível no modo vivo; para aprofundar, pedir 'aula detalhada' ou 'passo a passo'."
    )


def _aula(pergunta: str, resposta: str) -> str:
    return (
        "Aula rápida PSF: primeiro identifico a ideia, depois explico com exemplo simples, "
        "depois mostro o teste.\n"
        f"Ideia: {pergunta}\n"
        f"Explicação: {resposta}\n"
        "Teste: tenta explicar com um exemplo teu; se a explicação pular um passo, o modo cientista marca lacuna."
    )


def _teste(pergunta: str) -> str:
    return f"Teste PSF: responder sem decorar: '{pergunta}' em 2 frases e com 1 exemplo."


def _carregar() -> list[PerguntaCuriosidade]:
    itens: list[PerguntaCuriosidade] = []
    for linha in PERGUNTAS_RAW.strip().splitlines():
        if not linha.strip():
            continue
        numero_s, categoria, pergunta = linha.split("|", 2)
        numero = int(numero_s)
        tem_real = numero in RESPOSTAS_ESPECIFICAS
        resposta = RESPOSTAS_ESPECIFICAS.get(numero) or _resposta_generica(numero, pergunta, categoria)
        itens.append(PerguntaCuriosidade(numero, categoria, pergunta, resposta, _aula(pergunta, resposta), _teste(pergunta), tem_real))
    return itens


PERGUNTAS = _carregar()
POR_NUMERO = {p.numero: p for p in PERGUNTAS}


def total() -> int:
    return len(PERGUNTAS)


def obter(numero: int) -> PerguntaCuriosidade:
    return POR_NUMERO[numero]


def _tokens_relevantes(texto: str) -> set[str]:
    stop = {"o", "a", "os", "as", "de", "do", "da", "dos", "das", "e", "em", "que", "qual", "quais", "como", "porque", "por", "para", "um", "uma", "no", "na", "nos", "nas", "se", "sao", "ser", "com", "quanto", "quantos", "onde", "quando", "dê", "de", "quem", "foi", "sobre", "hoje", "achas", "escreve", "escreva", "poema", "piada", "conta"}
    return {tok for tok in normalizar(texto).split() if len(tok) > 2 and tok not in stop}


def procurar(texto: str) -> PerguntaCuriosidade | None:
    """Busca por ID, por texto exato aproximado e por tokens importantes."""
    t = normalizar(texto)
    m = re.search(r"\b(?:q|pergunta|item)\s*0*(\d{1,3})\b", t)
    if m:
        n = int(m.group(1))
        if n in POR_NUMERO:
            return POR_NUMERO[n]
    melhor: tuple[float, PerguntaCuriosidade | None] = (0.0, None)
    tokens = _tokens_relevantes(texto)
    for item in PERGUNTAS:
        qn = normalizar(item.pergunta)
        if t == qn or t in qn or qn in t:
            return item
        qt = _tokens_relevantes(item.pergunta)
        inter = len(tokens & qt)
        if inter == 0:
            # Sem nenhuma palavra-chave real em comum, a similaridade de
            # caracteres (SequenceMatcher) sozinha é ruído: uma frase curta e
            # sem relação de sentido podia bater por acaso num item qualquer
            # da base. Sem token partilhado não é candidato.
            continue
        uniao = len(tokens | qt) or 1
        jacc = inter / uniao
        seq = SequenceMatcher(None, t, qn).ratio()
        score = max(jacc, seq * 0.82)
        if score > melhor[0]:
            melhor = (score, item)
    if melhor[0] >= 0.38:
        return melhor[1]
    return None


def responder(texto: str, incluir_aula: bool = False) -> str | None:
    item = procurar(texto)
    if item is None:
        return None
    base = f"{item.resposta}\n\nFonte interna: base de curiosidades, item {item.numero}, categoria {item.categoria}."
    if incluir_aula:
        base += "\n\n" + item.aula
    return base


def auto_teste() -> dict:
    casos = {
        "O que são os padrões de Turing na natureza?": "reagem",
        "Como é que as riscas das zebras se formam": "reação-difusão",
        "O que é a filotaxia e como se relaciona com Fibonacci?": "Fibonacci",
        "Porque é que os girassóis têm espirais de Fibonacci?": "ângulo áureo",
        "O que é a proporção áurea no corpo humano?": "não é uma lei universal",
        "Porque é que multiplicar por zero dá sempre zero?": "0+0",
        "Qual é o truque para multiplicar por 11 rapidamente?": "23×11",
    }
    falhas = []
    for entrada, esperado in casos.items():
        saida = responder(entrada) or ""
        if esperado not in saida:
            falhas.append((entrada, esperado, saida[:200]))
    return {"ok": not falhas, "falhas": falhas, "total": len(casos), "base_total": total()}
