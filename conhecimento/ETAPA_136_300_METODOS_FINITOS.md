# PSF-IAminy — Etapas 136 a 300: Métodos finitos

## Posição no fluxo natural

Depois de equação quadrática finita, o próximo método geral que nasce sem violar a lei das fórmulas é a enumeração sobre domínio finito explícito.

Este bloco não introduz fórmulas fechadas. Ele constrói métodos por:

```text
domínio finito explícito
↓
predicado / relação / transição / avaliação
↓
varredura estrutural
↓
conjunto de testemunhas, contraexemplos ou objetos construídos
```

O motor expande este arquivo como etapas 136 a 300. A granularidade é registrada dentro deste documento porque todas as etapas compartilham o mesmo fundamento operacional.

## Dependências permitidas

- primitivas e estruturas finitas já usadas no núcleo;
- relações, funções, ordens, grafos, polinómios, expressões finitas e equações finitas;
- lei das fórmulas construídas.

## Dependências proibidas

- fórmulas fechadas não derivadas;
- infinitos atuais;
- análise real;
- cardinalidade infinita;
- atalhos por teoremas externos não construídos.

## Etapas registradas

| Etapa | Conceito |
|---|---|
| 136 | Equação como predicado finito |
| 137 | Conjunto de soluções |
| 138 | Todas as soluções por varredura |
| 139 | Equivalência de equações no domínio |
| 140 | Sistema finito de equações |
| 141 | Alternativa finita de equações |
| 142 | Inequação finita |
| 143 | Varredura de parâmetros |
| 144 | Restrição de domínio |
| 145 | Conjunto factível |
| 146 | Função objetivo finita |
| 147 | Minimizadores |
| 148 | Maximizadores |
| 149 | Argmin finito |
| 150 | Argmax finito |
| 151 | Produto de domínios nomeados |
| 152 | Valoração multivariável |
| 153 | Expressão multivariável finita |
| 154 | Projeção de valorações |
| 155 | Substituição em valoração |
| 156 | Testemunhas finitas |
| 157 | Contraexemplos finitos |
| 158 | Decisão finita por testemunha ou contraexemplo |
| 159 | Fechamento de método finito |
| 160 | Ponte entre equações e métodos finitos |
| 161 | Conjunto finito |
| 162 | Conjunto vazio |
| 163 | Conjunto unitário |
| 164 | Pertencimento a conjunto finito |
| 165 | Subconjunto finito |
| 166 | Igualdade extensional finita |
| 167 | União finita |
| 168 | Interseção finita |
| 169 | Diferença finita |
| 170 | Complemento relativo finito |
| 171 | Produto cartesiano finito |
| 172 | Conjunto das partes finito |
| 173 | Família finita de conjuntos |
| 174 | Cobertura finita |
| 175 | Partição finita |
| 176 | Quociente por partição |
| 177 | Transversal finito |
| 178 | Cardinal finito por enumeração |
| 179 | Imagem de conjunto finito |
| 180 | Pré-imagem de conjunto finito |
| 181 | Elementos minimais |
| 182 | Elementos maximais |
| 183 | Menor elemento |
| 184 | Maior elemento |
| 185 | Cotas inferiores |
| 186 | Cotas superiores |
| 187 | Ínfimo finito |
| 188 | Supremo finito |
| 189 | Cadeia finita |
| 190 | Anticadeia finita |
| 191 | Aplicação monótona finita |
| 192 | Rede finita |
| 193 | Topo de ordem finita |
| 194 | Base de ordem finita |
| 195 | Intervalo de ordem finito |
| 196 | Ideal finito |
| 197 | Filtro finito |
| 198 | Fechamento ordinal finito |
| 199 | Comparabilidade finita |
| 200 | Fechamento de ordens finitas |
| 201 | Topologia finita |
| 202 | Aberto finito |
| 203 | Fechado finito |
| 204 | Interior finito |
| 205 | Fecho finito |
| 206 | Fronteira finita |
| 207 | Pré-imagem de aberto |
| 208 | Continuidade finita |
| 209 | Separação T0 finita |
| 210 | Conexidade topológica finita |
| 211 | Compacidade finita |
| 212 | Subespaço finito |
| 213 | Base topológica finita |
| 214 | Produto topológico finito |
| 215 | Mapa aberto finito |
| 216 | Mapa fechado finito |
| 217 | Homeomorfismo finito |
| 218 | Componente conexa finita |
| 219 | Fechamento topológico finito |
| 220 | Ponte topologia-grafos finita |
| 221 | Alfabeto finito |
| 222 | Palavra finita |
| 223 | Concatenação de palavras |
| 224 | Tamanho de palavra por enumeração |
| 225 | Linguagem finita |
| 226 | Pertencimento a linguagem |
| 227 | Prefixo |
| 228 | Sufixo |
| 229 | Conjunto de prefixos |
| 230 | Conjunto de sufixos |
| 231 | Fechamento por prefixos |
| 232 | Linguagem concatenada finita |
| 233 | Potência finita de linguagem |
| 234 | Relação entre palavras |
| 235 | Reescrita finita |
| 236 | Forma normal por busca finita |
| 237 | Gramática finita inicial |
| 238 | Derivação finita de palavra |
| 239 | Linguagem gerada em profundidade finita |
| 240 | Fechamento de linguagens finitas |
| 241 | Automato finito determinístico |
| 242 | Estado inicial |
| 243 | Estado final |
| 244 | Transição finita |
| 245 | Transição estendida |
| 246 | Palavra aceita |
| 247 | Linguagem aceita em amostra finita |
| 248 | Complemento de automato completo |
| 249 | Produto de automatos |
| 250 | União de linguagens por automatos |
| 251 | Interseção de linguagens por automatos |
| 252 | Equivalência em amostra finita |
| 253 | Acessibilidade de estado |
| 254 | Estado morto |
| 255 | Minimização por equivalência finita |
| 256 | Reconhecimento finito |
| 257 | Decisão de aceitação |
| 258 | Contraexemplo de equivalência |
| 259 | Fechamento de automatos finitos |
| 260 | Ponte linguagens-lógica finita |
| 261 | Variável proposicional |
| 262 | Negação proposicional |
| 263 | Conjunção proposicional |
| 264 | Disjunção proposicional |
| 265 | Implicação proposicional |
| 266 | Variáveis de fórmula |
| 267 | Valoração proposicional |
| 268 | Avaliação proposicional |
| 269 | Todas as valorações |
| 270 | Tabela verdade |
| 271 | Modelos de fórmula |
| 272 | Tautologia |
| 273 | Satisfatibilidade |
| 274 | Contradição |
| 275 | Consequência semântica finita |
| 276 | Equivalência lógica finita |
| 277 | Forma disjuntiva por tabela |
| 278 | Forma conjuntiva por tabela |
| 279 | Teoria finita |
| 280 | Consistência finita |
| 281 | Completude finita relativa |
| 282 | Prova como objeto finito |
| 283 | Passo de derivação finito |
| 284 | Derivação válida por consequência |
| 285 | Refutação finita |
| 286 | Decisão proposicional finita |
| 287 | Testemunha de satisfatibilidade |
| 288 | Contraexemplo de tautologia |
| 289 | Núcleo semântico finito |
| 290 | Fechamento dedutivo finito |
| 291 | Conservatividade finita |
| 292 | Tradução finita entre linguagens |
| 293 | Correção de verificador finito |
| 294 | Completude por tabela finita |
| 295 | Decidibilidade finita |
| 296 | Busca universal finita |
| 297 | Busca existencial finita |
| 298 | Classificação finita por predicado |
| 299 | Auditoria finita de método |
| 300 | Fechamento dos métodos finitos |

## Forma operacional no projeto

Implementado em `nucleo/metodos_finitos.py` e validado em `testes/test_metodos_finitos_136_300.py`.

## Limite honesto

Este bloco não prova resultados infinitos. Ele dá métodos corretos para domínios finitos explícitos. Quando um conceito tiver versão infinita, analítica ou fechada por fórmula, essa versão ainda terá de nascer em etapa própria.
