# Português — conhecimento puro PSF

Este documento é materializado a partir da linha canónica em `lingua_portuguesa/conhecimento_puro.py`.

## Estado

- Conceitos puros: **1139**
- Temas de consulta: **20**
- Relações de dependência: **2541**
- Conceitos com exemplo mínimo: **1139**
- Lacunas internas conhecidas: **0**
- Fronteiras abertas: **124**
- Limites operacionais: **179**
- Equivalências terminológicas: **9**

## Distinção de integridade

- **Lacuna interna:** falta dentro da definição canónica. Estado atual: zero conhecida.
- **Fronteira aberta:** depende de dados vivos, variedade, contexto, história ou investigação.
- **Limite operacional:** conceito construído cuja automatização ainda pode ser parcial.

## Linha canónica

### 1. diferença

**Construção:** O primeiro conhecimento é perceber que uma ocorrência pode ser separada de outra.

**Função:** Permite distinguir silêncio de som, letra de letra e palavra de palavra.

**Dependências:** nenhuma anterior

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer diferença numa ocorrência compatível com a definição e verificar as suas dependências.

### 2. som

**Construção:** Um som é uma ocorrência audível ou abstrata separada pela diferença.

**Função:** Serve como matéria inicial da fala antes de existir palavra.

**Dependências:** diferença

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer som numa ocorrência compatível com a definição e verificar as suas dependências.

### 3. pausa

**Construção:** A pausa é ausência ou corte entre ocorrências sonoras.

**Função:** Permite separar ritmos, palavras, frases e intenções.

**Dependências:** diferença, som

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer pausa numa ocorrência compatível com a definição e verificar as suas dependências.

### 4. marca

**Construção:** Uma marca é um sinal visível que conserva uma diferença.

**Função:** Permite levar o som e a pausa para a escrita.

**Dependências:** diferença

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer marca numa ocorrência compatível com a definição e verificar as suas dependências.

### 5. grafema

**Construção:** Um grafema é uma marca escrita tratada como unidade: letra, acento, algarismo, espaço ou pontuação.

**Função:** Serve para formar a camada gráfica da língua.

**Dependências:** marca

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer grafema numa ocorrência compatível com a definição e verificar as suas dependências.

### 6. letra

**Construção:** Letra é grafema usado para representar parte estável da palavra escrita.

**Função:** Permite nomear e ordenar marcas alfabéticas.

**Dependências:** grafema

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer letra numa ocorrência compatível com a definição e verificar as suas dependências.

### 7. espaço

**Construção:** Espaço é marca vazia que separa combinações escritas sem ser som próprio.

**Função:** Ajuda a separar palavras e blocos no texto.

**Dependências:** grafema, pausa

**Tema de consulta:** `fundamento`

**Exemplo mínimo:** Aplicação mínima: reconhecer espaço numa ocorrência compatível com a definição e verificar as suas dependências.

### 8. vogal

**Construção:** Vogal é grafema sonoro que pode sustentar núcleo de emissão na palavra.

**Função:** Ajuda a formar sílabas e ritmo interno da palavra.

**Dependências:** som, grafema

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer vogal numa ocorrência compatível com a definição e verificar as suas dependências.

### 9. consoante

**Construção:** Consoante é grafema sonoro que se apoia em vogal ou em combinação para circular na palavra.

**Função:** Ajuda a desenhar limites e articulações da palavra.

**Dependências:** som, grafema, vogal

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer consoante numa ocorrência compatível com a definição e verificar as suas dependências.

### 10. acento

**Construção:** Acento é marca acrescentada ao grafema para orientar abertura, nasalidade, tonicidade ou distinção escrita.

**Função:** Permite diferenciar formas como avo, avó e avô.

**Dependências:** grafema, letra

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer acento numa ocorrência compatível com a definição e verificar as suas dependências.

### 11. cedilha

**Construção:** Cedilha é marca sob o c que altera a leitura funcional desse grafema em português.

**Função:** Permite reconhecer formas como criança e ação.

**Dependências:** grafema, letra, acento

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer cedilha numa ocorrência compatível com a definição e verificar as suas dependências.

### 12. combinação

**Construção:** Combinação é aproximação de grafemas para formar uma unidade maior.

**Função:** Permite criar dígrafo, sílaba e palavra-forma.

**Dependências:** grafema

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer combinação numa ocorrência compatível com a definição e verificar as suas dependências.

### 13. dígrafo

**Construção:** Dígrafo é combinação de duas letras tratada como uma unidade funcional de escrita/leitura.

**Função:** Ajuda a reconhecer ch, lh, nh, rr, ss, qu e gu sem dividir de modo falso.

**Dependências:** combinação, letra

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer dígrafo numa ocorrência compatível com a definição e verificar as suas dependências.

### 14. encontro vocálico

**Construção:** Encontro vocálico nasce quando duas ou mais vogais aparecem em sequência na palavra.

**Função:** Ajuda a investigar ditongo, hiato e tritongo sem antecipar regra total.

**Dependências:** vogal, combinação

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer encontro vocálico numa ocorrência compatível com a definição e verificar as suas dependências.

### 15. encontro consonantal

**Construção:** Encontro consonantal nasce quando duas ou mais consoantes aparecem próximas na palavra.

**Função:** Ajuda a observar articulação e divisão aproximada de sílabas.

**Dependências:** consoante, combinação

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer encontro consonantal numa ocorrência compatível com a definição e verificar as suas dependências.

### 16. sílaba

**Construção:** Sílaba é agrupamento de sons/grafemas que pode ser pronunciado como bloco.

**Função:** Serve como ponte entre letra isolada e palavra pronunciável.

**Dependências:** vogal, consoante, combinação

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer sílaba numa ocorrência compatível com a definição e verificar as suas dependências.

### 17. tonicidade

**Construção:** Tonicidade é diferença de força entre sílabas de uma palavra.

**Função:** Permite observar sílaba mais forte e orientar acentuação futura.

**Dependências:** sílaba, som, acento

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer tonicidade numa ocorrência compatível com a definição e verificar as suas dependências.

### 18. sílaba tônica

**Construção:** Sílaba tônica é a sílaba que recebe maior força relativa dentro da palavra.

**Função:** Ajuda a classificar oxítona, paroxítona e proparoxítona quando houver regra suficiente.

**Dependências:** sílaba, tonicidade

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Aplicação mínima: reconhecer sílaba tônica numa ocorrência compatível com a definição e verificar as suas dependências.

### 19. palavra

**Construção:** Palavra é combinação estável que pode receber forma, classe e sentido.

**Função:** Permite que a língua deixe de ser só som e vire unidade de significado.

**Dependências:** sílaba, combinação, espaço

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer palavra numa ocorrência compatível com a definição e verificar as suas dependências.

### 20. lema

**Construção:** Lema é a forma-base usada para reunir variantes de uma palavra.

**Função:** Permite reconhecer que formas diferentes podem apontar para uma mesma unidade lexical.

**Dependências:** palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer lema numa ocorrência compatível com a definição e verificar as suas dependências.

### 21. morfema

**Construção:** Morfema é parte mínima de palavra que carrega função ou sentido dentro da forma.

**Função:** Permite separar radical, prefixo, sufixo e flexão sem tratar a palavra como bloco cego.

**Dependências:** palavra, lema

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer morfema numa ocorrência compatível com a definição e verificar as suas dependências.

### 22. radical

**Construção:** Radical é parte que conserva o núcleo de família de uma palavra.

**Função:** Ajuda a ligar palavras aparentadas.

**Dependências:** morfema

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer radical numa ocorrência compatível com a definição e verificar as suas dependências.

### 23. prefixo

**Construção:** Prefixo é morfema colocado antes do radical para alterar ou orientar sentido.

**Função:** Permite observar formações como refazer e desfazer.

**Dependências:** morfema, radical

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer prefixo numa ocorrência compatível com a definição e verificar as suas dependências.

### 24. sufixo

**Construção:** Sufixo é morfema colocado depois do radical para formar palavra ou variar função.

**Função:** Permite observar formações como construção, clareza e rapidamente.

**Dependências:** morfema, radical

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer sufixo numa ocorrência compatível com a definição e verificar as suas dependências.

### 25. flexão

**Construção:** Flexão é variação de forma que ajusta gênero, número, pessoa, tempo ou modo sem trocar totalmente a unidade.

**Função:** Permite reconhecer menina/meninas, estudar/estudam e bonito/bonita.

**Dependências:** morfema, lema

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer flexão numa ocorrência compatível com a definição e verificar as suas dependências.

### 26. gênero

**Construção:** Gênero é traço de concordância que organiza formas masculinas, femininas ou comuns no sistema.

**Função:** Ajuda a verificar relações entre determinante, nome e adjetivo.

**Dependências:** flexão, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer gênero numa ocorrência compatível com a definição e verificar as suas dependências.

### 27. número gramatical

**Construção:** Número gramatical é traço que distingue singular e plural dentro da construção.

**Função:** Ajuda a verificar concordância e quantidade linguística.

**Dependências:** flexão, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer número gramatical numa ocorrência compatível com a definição e verificar as suas dependências.

### 28. pessoa gramatical

**Construção:** Pessoa gramatical organiza quem fala, com quem se fala e de quem se fala.

**Função:** Ajuda a ligar pronome, verbo e ponto de vista.

**Dependências:** flexão, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer pessoa gramatical numa ocorrência compatível com a definição e verificar as suas dependências.

### 29. classe gramatical

**Construção:** Classe gramatical é o papel básico que uma palavra pode assumir na construção.

**Função:** Ajuda a separar nome, verbo, adjetivo, pronome, determinante e outros papéis.

**Dependências:** palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer classe gramatical numa ocorrência compatível com a definição e verificar as suas dependências.

### 30. nome

**Construção:** Nome é palavra que pode apontar para entidade, coisa, ideia, lugar ou conceito.

**Função:** Serve de base para sujeito, núcleo nominal e referência.

**Dependências:** classe gramatical, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer nome numa ocorrência compatível com a definição e verificar as suas dependências.

### 31. verbo

**Construção:** Verbo é palavra que organiza ação, estado, existência, ocorrência ou ligação.

**Função:** Serve como eixo de oração quando aparece explicitamente.

**Dependências:** classe gramatical, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer verbo numa ocorrência compatível com a definição e verificar as suas dependências.

### 32. adjetivo

**Construção:** Adjetivo é palavra que atribui característica a nome ou construção nominal.

**Função:** Ajuda a qualificar e verificar concordância.

**Dependências:** classe gramatical, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer adjetivo numa ocorrência compatível com a definição e verificar as suas dependências.

### 33. pronome

**Construção:** Pronome é palavra que retoma, aponta ou substitui referência no texto.

**Função:** Ajuda a manter continuidade sem repetir sempre o nome.

**Dependências:** classe gramatical, palavra

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer pronome numa ocorrência compatível com a definição e verificar as suas dependências.

### 34. determinante

**Construção:** Determinante é palavra que acompanha nome para limitar, apresentar ou localizar referência.

**Função:** Ajuda a formar grupo nominal e concordância.

**Dependências:** classe gramatical, nome

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer determinante numa ocorrência compatível com a definição e verificar as suas dependências.

### 35. advérbio

**Construção:** Advérbio é palavra que modifica verbo, adjetivo, outro advérbio ou frase.

**Função:** Ajuda a expressar modo, tempo, lugar, intensidade e negação.

**Dependências:** classe gramatical, verbo

**Tema de consulta:** `palavra_e_morfologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer advérbio numa ocorrência compatível com a definição e verificar as suas dependências.

### 36. sentido

**Construção:** Sentido é a função interpretável que nasce quando palavra, contexto e relação se encontram.

**Função:** Permite sair da forma escrita para aquilo que a frase quer comunicar.

**Dependências:** palavra, lema, classe gramatical

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer sentido numa ocorrência compatível com a definição e verificar as suas dependências.

### 37. relação

**Construção:** Relação é ligação reconhecida entre palavras ou partes do texto.

**Função:** Permite construir concordância, dependência, sujeito, predicado e coerência.

**Dependências:** sentido

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer relação numa ocorrência compatível com a definição e verificar as suas dependências.

### 38. concordância

**Construção:** Concordância é ajuste de forma entre palavras relacionadas.

**Função:** Permite verificar se determinante, nome, adjetivo e verbo combinam de modo estável.

**Dependências:** relação, gênero, número gramatical, classe gramatical

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer concordância numa ocorrência compatível com a definição e verificar as suas dependências.

### 39. frase

**Construção:** Frase é sequência de palavras com unidade comunicável.

**Função:** Permite comunicar afirmação, pedido, dúvida, ordem ou expressão.

**Dependências:** palavra, sentido, relação

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer frase numa ocorrência compatível com a definição e verificar as suas dependências.

### 40. oração

**Construção:** Oração é construção de frase organizada em torno de verbo explícito ou estrutura equivalente.

**Função:** Permite reconhecer ação, estado, sujeito e predicado quando eles aparecem.

**Dependências:** frase, classe gramatical, relação, verbo

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer oração numa ocorrência compatível com a definição e verificar as suas dependências.

### 41. sujeito

**Construção:** Sujeito é parte que ocupa o ponto de referência daquilo que se declara.

**Função:** Ajuda a saber de quem ou do que a oração trata.

**Dependências:** oração, relação

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer sujeito numa ocorrência compatível com a definição e verificar as suas dependências.

### 42. predicado

**Construção:** Predicado é parte que declara algo sobre o sujeito ou organiza o acontecimento verbal.

**Função:** Ajuda a reconhecer o que é dito, feito, sentido ou atribuído.

**Dependências:** oração, sujeito, relação

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer predicado numa ocorrência compatível com a definição e verificar as suas dependências.

### 43. pontuação

**Construção:** Pontuação é marca que regula pausa, limite, pergunta, exclamação e encadeamento.

**Função:** Ajuda a separar unidades e orientar a leitura do texto.

**Dependências:** marca, frase

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer pontuação numa ocorrência compatível com a definição e verificar as suas dependências.

### 44. parágrafo

**Construção:** Parágrafo é bloco de texto que agrupa frases em torno de continuidade local.

**Função:** Ajuda a organizar pensamento maior em partes manejáveis.

**Dependências:** frase, pontuação

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer parágrafo numa ocorrência compatível com a definição e verificar as suas dependências.

### 45. texto

**Construção:** Texto é encadeamento de frases com continuidade e intenção.

**Função:** Permite conservar pensamento maior que uma frase isolada.

**Dependências:** frase, pontuação, sentido, parágrafo

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer texto numa ocorrência compatível com a definição e verificar as suas dependências.

### 46. coerência

**Construção:** Coerência é continuidade de sentido entre partes do texto.

**Função:** Ajuda a verificar se o texto mantém direção compreensível.

**Dependências:** texto, sentido, relação

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer coerência numa ocorrência compatível com a definição e verificar as suas dependências.

### 47. coesão

**Construção:** Coesão é ligação visível entre partes do texto por repetição controlada, retomada, conectivo ou referência.

**Função:** Ajuda a manter fluxo entre frases e parágrafos.

**Dependências:** texto, relação, pronome

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer coesão numa ocorrência compatível com a definição e verificar as suas dependências.

### 48. gramática

**Construção:** Gramática é conjunto de regras observáveis que organiza palavras, relações, frases e textos.

**Função:** Serve para verificar forma, concordância, ordem, função e coerência.

**Dependências:** palavra, relação, frase, texto, concordância

**Tema de consulta:** `frase_texto_gramatica`

**Exemplo mínimo:** Aplicação mínima: reconhecer gramática numa ocorrência compatível com a definição e verificar as suas dependências.

### 49. enunciado

**Construção:** Enunciado é uma frase ou conjunto curto usado numa situação de comunicação.

**Função:** Permite tratar aquilo que foi dito como unidade com contexto e intenção.

**Dependências:** frase, sentido

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer enunciado numa ocorrência compatível com a definição e verificar as suas dependências.

### 50. intenção comunicativa

**Construção:** Intenção comunicativa é a direção prática do enunciado: informar, pedir, ordenar, perguntar, negar, afirmar ou expressar.

**Função:** Ajuda a distinguir forma parecida com função diferente.

**Dependências:** enunciado, sentido

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer intenção comunicativa numa ocorrência compatível com a definição e verificar as suas dependências.

### 51. referência

**Construção:** Referência é a ligação entre uma palavra ou expressão e aquilo para que ela aponta no texto.

**Função:** Permite saber de quem ou do que se fala sem confundir forma com coisa.

**Dependências:** palavra, sentido

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer referência numa ocorrência compatível com a definição e verificar as suas dependências.

### 52. referente

**Construção:** Referente é o alvo construído pela referência dentro do texto ou situação.

**Função:** Ajuda a manter continuidade entre nomes, pronomes e retomadas.

**Dependências:** referência

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer referente numa ocorrência compatível com a definição e verificar as suas dependências.

### 53. campo semântico

**Construção:** Campo semântico é agrupamento de palavras por proximidade de sentido construído.

**Função:** Permite observar famílias de sentido dentro de um texto.

**Dependências:** palavra, sentido

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer campo semântico numa ocorrência compatível com a definição e verificar as suas dependências.

### 54. polissemia

**Construção:** Polissemia nasce quando uma mesma palavra pode carregar mais de um sentido conforme a relação em que aparece.

**Função:** Impede o motor de assumir sentido único sem contexto.

**Dependências:** palavra, sentido, relação

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer polissemia numa ocorrência compatível com a definição e verificar as suas dependências.

### 55. sinonímia

**Construção:** Sinonímia é proximidade de sentido entre palavras ou expressões em certo contexto.

**Função:** Permite reconhecer alternativas sem fingir igualdade perfeita.

**Dependências:** sentido, relação

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer sinonímia numa ocorrência compatível com a definição e verificar as suas dependências.

### 56. antonímia

**Construção:** Antonímia é oposição de sentido construída entre palavras ou expressões.

**Função:** Ajuda a reconhecer contraste e negação de qualidade, ação ou estado.

**Dependências:** sentido, relação

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer antonímia numa ocorrência compatível com a definição e verificar as suas dependências.

### 57. conectivo

**Construção:** Conectivo é palavra ou expressão que liga partes do texto e mostra relação entre elas.

**Função:** Permite construir adição, contraste, causa, conclusão e sequência.

**Dependências:** palavra, relação, coesão

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer conectivo numa ocorrência compatível com a definição e verificar as suas dependências.

### 58. retomada

**Construção:** Retomada é retorno a um referente já construído por repetição, pronome, sinónimo ou elipse.

**Função:** Ajuda a manter coesão sem repetir tudo sempre.

**Dependências:** referente, pronome, coesão

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer retomada numa ocorrência compatível com a definição e verificar as suas dependências.

### 59. elipse

**Construção:** Elipse é ausência controlada de uma parte que pode ser recuperada pela relação no texto.

**Função:** Permite reconhecer sentido mesmo quando algo não aparece escrito.

**Dependências:** relação, sentido, coesão

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer elipse numa ocorrência compatível com a definição e verificar as suas dependências.

### 60. inferência

**Construção:** Inferência é sentido obtido por relação entre o que está dito e o que fica implicado.

**Função:** Permite avançar além da palavra isolada sem inventar fora do texto.

**Dependências:** sentido, coerência

**Tema de consulta:** `semantica_e_coesao`

**Exemplo mínimo:** Aplicação mínima: reconhecer inferência numa ocorrência compatível com a definição e verificar as suas dependências.

### 61. período

**Construção:** Período é unidade textual formada por uma ou mais orações limitada por pontuação final.

**Função:** Permite agrupar orações num bloco sintático maior.

**Dependências:** oração, pontuação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer período numa ocorrência compatível com a definição e verificar as suas dependências.

### 62. coordenação

**Construção:** Coordenação é ligação de unidades de mesmo nível funcional sem uma depender totalmente da outra.

**Função:** Ajuda a organizar orações e termos paralelos.

**Dependências:** período, oração, relação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer coordenação numa ocorrência compatível com a definição e verificar as suas dependências.

### 63. subordinação

**Construção:** Subordinação é ligação em que uma unidade depende de outra para completar função ou sentido.

**Função:** Ajuda a reconhecer encaixe entre orações e termos.

**Dependências:** período, oração, relação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer subordinação numa ocorrência compatível com a definição e verificar as suas dependências.

### 64. termo

**Construção:** Termo é parte funcional de uma oração ou frase considerada pelo papel que exerce.

**Função:** Permite separar núcleo, complemento, adjunto e outras funções.

**Dependências:** oração, relação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer termo numa ocorrência compatível com a definição e verificar as suas dependências.

### 65. núcleo

**Construção:** Núcleo é a parte central de um termo, da qual outras partes podem depender.

**Função:** Ajuda a encontrar o centro de um sujeito, predicado ou grupo nominal.

**Dependências:** termo

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer núcleo numa ocorrência compatível com a definição e verificar as suas dependências.

### 66. complemento

**Construção:** Complemento é termo que completa o sentido de nome, verbo ou construção incompleta.

**Função:** Permite diferenciar verbo que basta de verbo que pede continuação.

**Dependências:** termo, núcleo, predicado

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer complemento numa ocorrência compatível com a definição e verificar as suas dependências.

### 67. adjunto

**Construção:** Adjunto é termo que acrescenta informação sem completar uma exigência central do núcleo.

**Função:** Permite observar circunstância, caracterização e expansão de sentido.

**Dependências:** termo, núcleo, relação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer adjunto numa ocorrência compatível com a definição e verificar as suas dependências.

### 68. transitividade verbal

**Construção:** Transitividade verbal é o modo como um verbo pede ou dispensa complemento.

**Função:** Ajuda a reconhecer verbos intransitivos, transitivos e de ligação sem antecipar tabela completa.

**Dependências:** verbo, predicado, complemento

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer transitividade verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 69. regência

**Construção:** Regência é relação em que uma palavra exige ou orienta outra, muitas vezes por preposição.

**Função:** Ajuda a verificar ligações entre verbo, nome e complemento.

**Dependências:** relação, verbo, complemento

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer regência numa ocorrência compatível com a definição e verificar as suas dependências.

### 70. colocação

**Construção:** Colocação é posição relativa de palavras na frase segundo função, clareza e uso.

**Função:** Permite observar ordem sem fingir uma única ordem fixa.

**Dependências:** palavra, frase, relação

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer colocação numa ocorrência compatível com a definição e verificar as suas dependências.

### 71. norma

**Construção:** Norma é conjunto de regularidades aceitas para um uso controlado da língua.

**Função:** Ajuda a separar funcionamento observado de correção normativa.

**Dependências:** gramática, texto

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer norma numa ocorrência compatível com a definição e verificar as suas dependências.

### 72. uso

**Construção:** Uso é prática real de aplicar a língua numa situação concreta.

**Função:** Permite reconhecer que a língua vive em contexto e não só em regra abstrata.

**Dependências:** texto, intenção comunicativa

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer uso numa ocorrência compatível com a definição e verificar as suas dependências.

### 73. variação linguística

**Construção:** Variação linguística é diferença de uso entre pessoas, lugares, tempos, situações e comunidades.

**Função:** Impede tratar uma única forma como todo o português possível.

**Dependências:** uso, norma

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer variação linguística numa ocorrência compatível com a definição e verificar as suas dependências.

### 74. registro

**Construção:** Registro é ajuste de linguagem conforme situação, formalidade e relação entre participantes.

**Função:** Ajuda a escolher forma mais simples, técnica, formal ou familiar sem mudar o conhecimento.

**Dependências:** uso, intenção comunicativa, variação linguística

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** Aplicação mínima: reconhecer registro numa ocorrência compatível com a definição e verificar as suas dependências.

### 75. contexto

**Construção:** Contexto é o conjunto de marcas, relações e situação que limita como um sentido deve ser lido.

**Função:** Impede interpretar palavra, frase ou texto como se existissem isolados.

**Dependências:** texto, uso, intenção comunicativa

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer contexto numa ocorrência compatível com a definição e verificar as suas dependências.

### 76. modalidade

**Construção:** Modalidade é a orientação do enunciado quanto a afirmar, negar, perguntar, ordenar, desejar ou avaliar.

**Função:** Permite reconhecer a força comunicativa sem confundir forma com intenção total.

**Dependências:** enunciado, intenção comunicativa, contexto

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer modalidade numa ocorrência compatível com a definição e verificar as suas dependências.

### 77. afirmação

**Construção:** Afirmação é modalidade em que o enunciado apresenta algo como posto ou sustentado.

**Função:** Ajuda a separar declaração de pergunta, negação ou ordem.

**Dependências:** modalidade, enunciado

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer afirmação numa ocorrência compatível com a definição e verificar as suas dependências.

### 78. negação

**Construção:** Negação é modalidade que marca recusa, ausência, oposição ou cancelamento de uma afirmação possível.

**Função:** Permite entender formas como não, nunca e sem como operadores de sentido.

**Dependências:** modalidade, advérbio

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer negação numa ocorrência compatível com a definição e verificar as suas dependências.

### 79. interrogação

**Construção:** Interrogação é modalidade que transforma o enunciado em busca explícita de informação, confirmação ou escolha.

**Função:** Ajuda a reconhecer pergunta pela intenção, ordem das palavras e pontuação.

**Dependências:** modalidade, pontuação

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer interrogação numa ocorrência compatível com a definição e verificar as suas dependências.

### 80. exclamação

**Construção:** Exclamação é modalidade que aumenta força expressiva, surpresa, emoção ou ênfase do enunciado.

**Função:** Permite diferenciar simples declaração de expressão marcada.

**Dependências:** modalidade, pontuação

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer exclamação numa ocorrência compatível com a definição e verificar as suas dependências.

### 81. tempo verbal

**Construção:** Tempo verbal é flexão ou construção que situa ocorrência em relação a antes, agora, depois ou referência interna.

**Função:** Ajuda a localizar ação, estado ou processo dentro do texto.

**Dependências:** verbo, flexão

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer tempo verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 82. aspecto verbal

**Construção:** Aspecto verbal é modo de observar a ocorrência como concluída, em curso, repetida, habitual ou iniciada.

**Função:** Permite separar tempo de forma de desenvolvimento da ação.

**Dependências:** verbo, tempo verbal

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer aspecto verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 83. modo verbal

**Construção:** Modo verbal é orientação do verbo quanto a certeza, hipótese, desejo, ordem ou condição.

**Função:** Liga verbo à modalidade do enunciado sem tratar toda forma como fato.

**Dependências:** verbo, modalidade, flexão

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer modo verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 84. voz verbal

**Construção:** Voz verbal é organização que mostra como sujeito e predicado se relacionam com a ação: agir, receber ou participar reflexivamente.

**Função:** Ajuda a interpretar quem faz, sofre ou se envolve no acontecimento verbal.

**Dependências:** verbo, oração, sujeito, predicado

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer voz verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 85. preposição

**Construção:** Preposição é palavra relacional que aproxima termos e orienta dependência de sentido.

**Função:** Permite construir ligações como de, em, com, para e por sem fingir lista total.

**Dependências:** palavra, relação, regência

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer preposição numa ocorrência compatível com a definição e verificar as suas dependências.

### 86. conjunção

**Construção:** Conjunção é palavra relacional que liga termos ou orações dentro de coordenação ou subordinação.

**Função:** Ajuda a marcar adição, oposição, causa, condição e consequência.

**Dependências:** conectivo, palavra, relação

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer conjunção numa ocorrência compatível com a definição e verificar as suas dependências.

### 87. interjeição

**Construção:** Interjeição é palavra ou emissão que manifesta reação, chamado, dor, surpresa ou contacto comunicativo.

**Função:** Permite reconhecer enunciado expressivo mesmo sem estrutura sintática completa.

**Dependências:** palavra, intenção comunicativa, enunciado

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer interjeição numa ocorrência compatível com a definição e verificar as suas dependências.

### 88. numeral

**Construção:** Numeral é classe que introduz contagem, ordem, fração ou multiplicação dentro da língua.

**Função:** Liga quantidade construída a forma linguística.

**Dependências:** classe gramatical, palavra

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer numeral numa ocorrência compatível com a definição e verificar as suas dependências.

### 89. artigo

**Construção:** Artigo é determinante que apresenta nome como definido, indefinido ou introduzido na referência.

**Função:** Ajuda a construir grupo nominal e acompanhar gênero e número.

**Dependências:** determinante, nome

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer artigo numa ocorrência compatível com a definição e verificar as suas dependências.

### 90. locução

**Construção:** Locução é combinação estável de palavras que funciona como uma unidade de classe ou função.

**Função:** Permite tratar mais de uma palavra como bloco funcional sem apagar suas partes.

**Dependências:** palavra, combinação, classe gramatical

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer locução numa ocorrência compatível com a definição e verificar as suas dependências.

### 91. perífrase verbal

**Construção:** Perífrase verbal é locução em que verbos combinados expressam tempo, aspecto, modalidade ou ação composta.

**Função:** Ajuda a interpretar formas como vai estudar, está lendo e pode resolver.

**Dependências:** locução, verbo, tempo verbal

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer perífrase verbal numa ocorrência compatível com a definição e verificar as suas dependências.

### 92. discurso direto

**Construção:** Discurso direto é modo de texto que apresenta fala ou pensamento como enunciado preservado por marcas próprias.

**Função:** Permite reconhecer vozes dentro do texto sem confundir autor, narrador e fala citada.

**Dependências:** texto, enunciado, pontuação

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer discurso direto numa ocorrência compatível com a definição e verificar as suas dependências.

### 93. discurso indireto

**Construção:** Discurso indireto é modo de texto que reconstrói fala ou pensamento dentro de outra enunciação.

**Função:** Permite transformar voz citada em relato sem perder a relação entre vozes.

**Dependências:** discurso direto, texto, relação

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer discurso indireto numa ocorrência compatível com a definição e verificar as suas dependências.

### 94. tema

**Construção:** Tema é aquilo sobre que um texto, parágrafo ou enunciado se organiza.

**Função:** Ajuda a manter foco e perceber desvio, repetição ou desenvolvimento.

**Dependências:** texto, sentido

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer tema numa ocorrência compatível com a definição e verificar as suas dependências.

### 95. progressão temática

**Construção:** Progressão temática é avanço controlado do tema ao longo do texto.

**Função:** Permite ver se o texto cresce, repete, salta ou se contradiz.

**Dependências:** tema, coerência, coesão

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer progressão temática numa ocorrência compatível com a definição e verificar as suas dependências.

### 96. ambiguidade

**Construção:** Ambiguidade é abertura de mais de uma leitura possível para uma forma, frase ou texto.

**Função:** Ajuda a marcar dúvida interpretativa sem fingir escolha única.

**Dependências:** sentido, polissemia, contexto

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer ambiguidade numa ocorrência compatível com a definição e verificar as suas dependências.

### 97. pragmática

**Construção:** Pragmática é observação do sentido em uso, considerando intenção, contexto, participantes e efeito.

**Função:** Permite estudar o que a frase faz, não só o que ela diz literalmente.

**Dependências:** uso, contexto, intenção comunicativa

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer pragmática numa ocorrência compatível com a definição e verificar as suas dependências.

### 98. estilo

**Construção:** Estilo é modo recorrente de escolher palavras, ritmo, ordem, tom e construção textual.

**Função:** Permite reconhecer forma de expressão sem confundir estilo com verdade do conteúdo.

**Dependências:** texto, registro, uso

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer estilo numa ocorrência compatível com a definição e verificar as suas dependências.

### 99. revisão

**Construção:** Revisão é retorno controlado ao texto para verificar coerência, coesão, norma, clareza e intenção.

**Função:** Permite melhorar texto sem alterar o conhecimento puro que o sustenta.

**Dependências:** texto, norma, coerência

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer revisão numa ocorrência compatível com a definição e verificar as suas dependências.

### 100. interpretação

**Construção:** Interpretação é construção de sentido a partir de texto, contexto, relações e inferências limitadas.

**Função:** Permite compreender sem inventar fora do que foi dado ou construído.

**Dependências:** texto, sentido, inferência, contexto

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** Aplicação mínima: reconhecer interpretação numa ocorrência compatível com a definição e verificar as suas dependências.

### 101. produção da fala

**Construção:** A produção da fala nasce quando corrente de ar, articulação e intenção se combinam para criar ocorrências sonoras controladas.

**Função:** Liga o som abstrato ao ato físico de falar.

**Dependências:** som, intenção comunicativa

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** falar uma palavra

**Não confundir com:** Não é o mesmo que escrita.

### 102. corrente de ar

**Construção:** Corrente de ar é o deslocamento que fornece energia para a maioria dos sons da fala.

**Função:** Permite distinguir silêncio, emissão e bloqueio articulatório.

**Dependências:** som, produção da fala

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** expiração durante a fala

**Não confundir com:** Não é som por si só.

### 103. articulação

**Construção:** Articulação é a modificação controlada da corrente de ar por partes móveis e fixas do aparelho fonador.

**Função:** Explica por que sons diferentes podem nascer da mesma corrente de ar.

**Dependências:** corrente de ar, produção da fala

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** fechar os lábios em /p/

**Não confundir com:** Não é sinónimo de pronúncia inteira.

### 104. aparelho fonador

**Construção:** Aparelho fonador é o conjunto funcional de estruturas usadas para respirar, vibrar e articular a fala.

**Função:** Organiza a origem física dos sons sem reduzir língua a anatomia.

**Dependências:** produção da fala, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pulmões, laringe, boca e nariz

**Não confundir com:** É suporte físico, não gramática.

### 105. vozeamento

**Construção:** Vozeamento é a presença de vibração laríngea durante parte da emissão sonora.

**Função:** Ajuda a distinguir pares sonoros como /p/ e /b/.

**Dependências:** aparelho fonador, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /b/ é vozeado em contraste com /p/

**Não confundir com:** Não é volume.

### 106. oralidade

**Construção:** Oralidade é o modo de produção e circulação da língua pela fala e pela escuta.

**Função:** Permite estudar ritmo, entoação, turnos e recursos não escritos.

**Dependências:** produção da fala, uso

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** uma conversa falada

**Não confundir com:** Não é ausência de gramática.

### 107. nasalidade

**Construção:** Nasalidade é a participação da cavidade nasal na ressonância de um som.

**Função:** Ajuda a compreender vogais nasais e consoantes nasais.

**Dependências:** aparelho fonador, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** som nasal em mãe

**Não confundir com:** Não é igual ao uso do til.

### 108. fonema

**Construção:** Fonema é unidade sonora abstrata capaz de distinguir palavras ou formas numa língua.

**Função:** Separa função distintiva de realização física concreta.

**Dependências:** som, diferença, palavra

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/ distingue pato de bato

**Não confundir com:** Não é letra nem gravação concreta.

### 109. alofone

**Construção:** Alofone é realização diferente de um mesmo fonema que não muda a identidade lexical naquele contexto.

**Função:** Permite reconhecer variação de pronúncia sem criar palavra nova.

**Dependências:** fonema, variação linguística

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** realizações diferentes de /r/

**Não confundir com:** Não é fonema novo.

### 110. oposição fonológica

**Construção:** Oposição fonológica é uma diferença sonora que produz contraste funcional entre formas.

**Função:** Permite testar se duas realizações distinguem significado.

**Dependências:** fonema, diferença, sentido

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pato/bato

**Não confundir com:** Nem toda diferença acústica é oposição fonológica.

### 111. ponto de articulação

**Construção:** Ponto de articulação é a região onde a corrente de ar sofre o contacto ou estreitamento principal.

**Função:** Organiza consoantes pela posição articulatória.

**Dependências:** articulação, aparelho fonador

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** bilabial em /p/

**Não confundir com:** Não é modo de articulação.

### 112. modo de articulação

**Construção:** Modo de articulação é a forma como a corrente de ar é bloqueada, estreitada ou desviada.

**Função:** Organiza consoantes pelo tipo de passagem do ar.

**Dependências:** articulação, corrente de ar

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** oclusão em /t/

**Não confundir com:** Não é ponto de articulação.

### 113. oclusiva

**Construção:** Oclusiva é consoante construída por bloqueio momentâneo seguido de libertação da corrente de ar.

**Função:** Permite agrupar sons como /p/, /b/, /t/ e /d/.

**Dependências:** modo de articulação, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/

**Não confundir com:** Não é fricativa.

### 114. fricativa

**Construção:** Fricativa é consoante construída por estreitamento que gera fricção contínua da corrente de ar.

**Função:** Permite agrupar sons como /f/, /v/, /s/ e /z/.

**Dependências:** modo de articulação, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /f/

**Não confundir com:** Não é oclusiva.

### 115. nasal consonantal

**Construção:** Nasal consonantal é consoante em que a corrente de ar encontra saída principal pela cavidade nasal.

**Função:** Explica o funcionamento de /m/, /n/ e /nh/.

**Dependências:** nasalidade, consoante, modo de articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** m em mapa

**Não confundir com:** Não é vogal nasal.

### 116. lateral

**Construção:** Lateral é consoante em que o ar passa pelos lados da língua.

**Função:** Ajuda a compreender /l/ e /lh/.

**Dependências:** modo de articulação, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** l em lado

**Não confundir com:** Não é vibrante.

### 117. vibrante

**Construção:** Vibrante é consoante produzida por uma ou mais vibrações rápidas de um articulador.

**Função:** Ajuda a compreender realizações de r e rr.

**Dependências:** modo de articulação, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** r em caro

**Não confundir com:** Não é lateral.

### 118. semivogal

**Construção:** Semivogal é realização vocálica que acompanha o núcleo silábico sem ocupar o centro principal da sílaba.

**Função:** Permite construir ditongos e tritongos.

**Dependências:** vogal, sílaba, sílaba

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** i em pai

**Não confundir com:** Não é consoante nem vogal nuclear.

### 119. ditongo

**Construção:** Ditongo é encontro vocálico em que uma vogal e uma semivogal permanecem na mesma sílaba.

**Função:** Distingue união silábica de separação vocálica.

**Dependências:** encontro vocálico, semivogal, sílaba

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pai

**Não confundir com:** Não é hiato.

### 120. tritongo

**Construção:** Tritongo é encontro de semivogal, vogal nuclear e semivogal dentro da mesma sílaba.

**Função:** Expande a análise dos encontros vocálicos.

**Dependências:** ditongo, semivogal, sílaba

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Paraguai

**Não confundir com:** Não é sequência de três sílabas.

### 121. hiato

**Construção:** Hiato é encontro de vogais que pertencem a sílabas diferentes.

**Função:** Impede tratar toda sequência vocálica como ditongo.

**Dependências:** encontro vocálico, sílaba

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** sa-í-da

**Não confundir com:** Não é ditongo.

### 122. ataque silábico

**Construção:** Ataque silábico é a parte da sílaba que aparece antes do núcleo.

**Função:** Permite decompor a estrutura interna da sílaba.

**Dependências:** sílaba, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pr em pra

**Não confundir com:** Pode estar vazio.

### 123. núcleo silábico

**Construção:** Núcleo silábico é o centro obrigatório da sílaba, geralmente sustentado por vogal.

**Função:** Dá à sílaba seu ponto de maior sonoridade.

**Dependências:** sílaba, vogal

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a em mar

**Não confundir com:** Não é sílaba inteira.

### 124. coda silábica

**Construção:** Coda silábica é a parte que pode aparecer depois do núcleo dentro da sílaba.

**Função:** Ajuda a distinguir sílabas abertas e fechadas.

**Dependências:** sílaba, núcleo silábico

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** r em mar

**Não confundir com:** Pode estar vazia.

### 125. prosódia

**Construção:** Prosódia é a organização suprassegmental de força, duração, ritmo e entoação na fala.

**Função:** Liga sons isolados à forma global do enunciado oral.

**Dependências:** oralidade, tonicidade, pausa

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** subir a voz numa pergunta

**Não confundir com:** Não é uma única regra de acento.

### 126. entoação

**Construção:** Entoação é o movimento de altura percebida ao longo de uma fala.

**Função:** Ajuda a marcar pergunta, afirmação, emoção e continuidade.

**Dependências:** prosódia, modalidade

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** curva ascendente numa pergunta

**Não confundir com:** Não é pontuação escrita.

### 127. ritmo

**Construção:** Ritmo é a distribuição temporal de sílabas, acentos e pausas.

**Função:** Permite observar fluidez e organização temporal da fala.

**Dependências:** prosódia, sílaba, pausa

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** alternância de sílabas fortes e fracas

**Não confundir com:** Não é velocidade apenas.

### 128. alfabeto

**Construção:** Alfabeto é um conjunto ordenado de letras usado para registrar formas escritas.

**Função:** Organiza identificação, soletração e busca lexical.

**Dependências:** letra, relação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** a, b, c...

**Não confundir com:** Não é o conjunto de todos os grafemas.

### 129. ordem alfabética

**Construção:** Ordem alfabética é a relação convencional que posiciona letras e palavras segundo o alfabeto.

**Função:** Permite organizar dicionários, listas e índices.

**Dependências:** alfabeto, relação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa antes de dado

**Não confundir com:** Não é ordem de tamanho.

### 130. maiúscula

**Construção:** Maiúscula é variante gráfica de letra usada em posições e funções específicas.

**Função:** Ajuda a marcar início, nomes próprios e destaques controlados.

**Dependências:** letra, grafema

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Maputo

**Não confundir com:** Não muda automaticamente o som.

### 131. minúscula

**Construção:** Minúscula é variante gráfica comum de letra dentro de palavras e textos.

**Função:** Sustenta a escrita corrente sem destaque especial.

**Dependências:** letra, grafema

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** mapa

**Não confundir com:** Não é letra menos importante.

### 132. diacrítico

**Construção:** Diacrítico é marca acrescentada a uma letra para modificar leitura ou função gráfica.

**Função:** Reúne acentos, til e cedilha como operações sobre grafemas.

**Dependências:** marca, grafema, letra

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** á, â, ã, ç

**Não confundir com:** Não é letra independente.

### 133. acento agudo

**Construção:** Acento agudo é diacrítico que pode marcar tonicidade e qualidade vocálica conforme a palavra.

**Função:** Distingue formas e orienta leitura.

**Dependências:** diacrítico, acento, tonicidade

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** avó

**Não confundir com:** Não é acento circunflexo.

### 134. acento circunflexo

**Construção:** Acento circunflexo é diacrítico que pode marcar tonicidade e uma qualidade vocálica específica.

**Função:** Distingue formas como avô de avó.

**Dependências:** diacrítico, acento, tonicidade

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** avô

**Não confundir com:** Não é acento agudo.

### 135. acento grave

**Construção:** Acento grave é diacrítico usado na escrita portuguesa para marcar crase em contextos construídos.

**Função:** Sinaliza fusão funcional sem ser acento tônico.

**Dependências:** diacrítico, acento, relação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** à

**Não confundir com:** Não marca sílaba tônica.

### 136. til

**Construção:** Til é diacrítico associado à nasalidade em certas vogais e formas.

**Função:** Ajuda a representar nasalidade gráfica.

**Dependências:** diacrítico, nasalidade

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** mãe

**Não confundir com:** Não é acento de tonicidade por si só.

### 137. hífen

**Construção:** Hífen é marca que liga ou separa partes em construções ortográficas específicas.

**Função:** Representa fronteiras internas em compostos, pronomes e translineação.

**Dependências:** pontuação, marca, combinação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** guarda-chuva

**Não confundir com:** Não é travessão.

### 138. apóstrofo

**Construção:** Apóstrofo é marca que indica supressão ou ligação gráfica em usos limitados.

**Função:** Preserva a indicação de ausência de segmento ou forma histórica.

**Dependências:** pontuação, marca

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** d'água

**Não confundir com:** Não é aspas.

### 139. ortografia

**Construção:** Ortografia é o sistema de convenções que estabiliza a representação escrita das palavras.

**Função:** Permite escrita compartilhada sem confundir convenção com fundamento sonoro.

**Dependências:** grafema, palavra, norma

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** escrever ação com ç

**Não confundir com:** Não é toda a gramática.

### 140. correspondência som-grafema

**Construção:** Correspondência som-grafema é a relação entre unidades sonoras e marcas escritas.

**Função:** Explica regularidades e ambiguidades da escrita alfabética.

**Dependências:** som, grafema, relação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** /k/ pode aparecer em c ou qu

**Não confundir com:** Não é relação um-para-um universal.

### 141. regularidade ortográfica

**Construção:** Regularidade ortográfica é padrão recorrente de escrita que permite prever uma forma em certos contextos.

**Função:** Ajuda a construir regras testáveis de escrita.

**Dependências:** ortografia, correspondência som-grafema

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** m antes de p e b em muitos casos

**Não confundir com:** Não elimina exceções.

### 142. irregularidade ortográfica

**Construção:** Irregularidade ortográfica é caso em que a forma escrita não pode ser deduzida por uma regra local simples.

**Função:** Obriga o motor a registrar conhecimento lexical sem fingir regra universal.

**Dependências:** ortografia, regularidade ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** grafias históricas

**Não confundir com:** Não é erro automaticamente.

### 143. família ortográfica

**Construção:** Família ortográfica é conjunto de formas relacionadas que preservam padrões de escrita.

**Função:** Permite aprender grafia por relação entre palavras.

**Dependências:** ortografia, radical, relação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa, casinha, casarão

**Não confundir com:** Não é apenas semelhança visual.

### 144. separação silábica

**Construção:** Separação silábica é a representação das fronteiras entre sílabas de uma palavra.

**Função:** Apoia pronúncia, translineação e análise tônica.

**Dependências:** sílaba, ataque silábico, núcleo silábico, coda silábica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** sa-í-da

**Não confundir com:** Não é divisão morfológica.

### 145. oxítona

**Construção:** Oxítona é palavra cuja sílaba tônica é a última.

**Função:** Permite organizar regras de acentuação por posição tônica.

**Dependências:** sílaba tônica, palavra

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** café

**Não confundir com:** Não é toda palavra terminada em vogal.

### 146. paroxítona

**Construção:** Paroxítona é palavra cuja sílaba tônica é a penúltima.

**Função:** Permite organizar regras de acentuação por posição tônica.

**Dependências:** sílaba tônica, palavra

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa

**Não confundir com:** Não é oxítona.

### 147. proparoxítona

**Construção:** Proparoxítona é palavra cuja sílaba tônica é a antepenúltima.

**Função:** Permite reconhecer uma classe com acentuação gráfica sistemática.

**Dependências:** sílaba tônica, palavra

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** música

**Não confundir com:** Não é paroxítona.

### 148. monossílabo tônico

**Construção:** Monossílabo tônico é palavra de uma sílaba com autonomia prosódica.

**Função:** Permite tratar acentuação de uma sílaba sem aplicar classificação polissilábica.

**Dependências:** sílaba, tonicidade, palavra

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** pá

**Não confundir com:** Não é sílaba átona isolada.

### 149. acentuação gráfica

**Construção:** Acentuação gráfica é o uso normativo de diacríticos para marcar tonicidade ou distinção em classes definidas.

**Função:** Reúne posição tônica, terminação e contraste gráfico.

**Dependências:** ortografia, tonicidade, diacrítico, oxítona, paroxítona, proparoxítona, monossílabo tônico

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** café, lápis, música

**Não confundir com:** Não é pronúncia completa.

### 150. crase

**Construção:** Crase é a fusão de vogais idênticas em uma relação gramatical, marcada por acento grave em certos usos escritos.

**Função:** Permite explicar à como resultado de relação, não como sinal decorativo.

**Dependências:** preposição, artigo, relação, acento grave

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** vou à escola

**Não confundir com:** Não é qualquer encontro de a.

### 151. estrutura da palavra

**Construção:** Estrutura da palavra é a organização interna de morfemas e funções numa forma lexical.

**Função:** Permite analisar palavra sem reduzi-la ao significado global.

**Dependências:** palavra, morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** infeliz = in + feliz

**Não confundir com:** Não é estrutura da frase.

### 152. tema morfológico

**Construção:** Tema morfológico é a base formada pelo radical e, quando existe, pela vogal temática.

**Função:** Serve de suporte a flexões e formação de formas.

**Dependências:** radical, morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cant-a-

**Não confundir com:** Não é lema inteiro.

### 153. vogal temática

**Construção:** Vogal temática é elemento que liga radical verbal ou nominal a desinências em certas classes.

**Função:** Ajuda a organizar paradigmas de conjugação e flexão.

**Dependências:** tema morfológico, verbo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** a em cantar

**Não confundir com:** Não é vogal tônica obrigatória.

### 154. desinência

**Construção:** Desinência é morfema final que expressa traços flexionais.

**Função:** Marca pessoa, número, tempo, modo ou gênero conforme a classe.

**Dependências:** flexão, morfema, tema morfológico

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mos em cantamos

**Não confundir com:** Não é sufixo derivacional.

### 155. afixo

**Construção:** Afixo é morfema ligado a uma base para formar ou modificar uma palavra.

**Função:** Reúne prefixos e sufixos sob uma relação comum.

**Dependências:** morfema, radical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** in- em infeliz

**Não confundir com:** Não é radical.

### 156. derivação

**Construção:** Derivação é formação de palavra nova a partir de uma base e de operação morfológica.

**Função:** Explica expansão lexical sem tratar toda forma como flexão.

**Dependências:** estrutura da palavra, afixo, lema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** feliz → felicidade

**Não confundir com:** Não é flexão.

### 157. derivação prefixal

**Construção:** Derivação prefixal acrescenta prefixo a uma base.

**Função:** Permite construir novos sentidos antes do radical.

**Dependências:** derivação, prefixo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** fazer → refazer

**Não confundir com:** Não é composição.

### 158. derivação sufixal

**Construção:** Derivação sufixal acrescenta sufixo a uma base.

**Função:** Pode alterar classe ou criar novo sentido.

**Dependências:** derivação, sufixo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** claro → clareza

**Não confundir com:** Não é flexão.

### 159. derivação parassintética

**Construção:** Derivação parassintética forma palavra com acréscimo conjunto de prefixo e sufixo necessários.

**Função:** Explica construções que não sobrevivem apenas com uma das partes.

**Dependências:** derivação prefixal, derivação sufixal

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** triste → entristecer

**Não confundir com:** Não é simples soma de duas derivações independentes.

### 160. derivação regressiva

**Construção:** Derivação regressiva cria forma lexical por redução aparente da base.

**Função:** Explica nomes de ação formados a partir de verbos em certos casos.

**Dependências:** derivação, verbo, nome

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** atacar → ataque

**Não confundir com:** Não é abreviação livre.

### 161. derivação imprópria

**Construção:** Derivação imprópria ocorre quando uma forma muda de classe pelo uso sem alteração gráfica necessária.

**Função:** Mostra que função sintática pode criar nova leitura lexical.

**Dependências:** derivação, classe gramatical, uso

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o jantar

**Não confundir com:** Não é erro de classe.

### 162. composição

**Construção:** Composição forma unidade lexical pela união de duas ou mais bases.

**Função:** Explica palavras complexas sem reduzi-las a afixos.

**Dependências:** estrutura da palavra, combinação, palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** guarda-chuva

**Não confundir com:** Não é derivação.

### 163. justaposição

**Construção:** Justaposição é composição em que as bases preservam forma reconhecível.

**Função:** Distingue união sem forte alteração fonográfica.

**Dependências:** composição

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** passatempo

**Não confundir com:** Não é aglutinação.

### 164. aglutinação

**Construção:** Aglutinação é composição em que bases sofrem fusão ou alteração formal.

**Função:** Explica unidade resultante menos segmentável.

**Dependências:** composição

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** planalto

**Não confundir com:** Não é justaposição.

### 165. abreviação

**Construção:** Abreviação reduz uma forma escrita mantendo referência recuperável.

**Função:** Economiza espaço sem criar necessariamente palavra nova.

**Dependências:** palavra, ortografia

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** pág.

**Não confundir com:** Não é sigla.

### 166. sigla

**Construção:** Sigla é forma construída pelas letras iniciais de uma expressão.

**Função:** Permite referir expressões longas de modo compacto.

**Dependências:** abreviação, letra, combinação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** ONU

**Não confundir com:** Não é sempre pronunciada como palavra.

### 167. acrônimo

**Construção:** Acrônimo é sigla ou combinação inicial pronunciada como palavra.

**Função:** Distingue forma soletrada de unidade lexical pronunciável.

**Dependências:** sigla, palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** Unesco

**Não confundir com:** Não é toda sigla.

### 168. onomatopeia

**Construção:** Onomatopeia é palavra ou forma que imita ou evoca um som.

**Função:** Liga percepção sonora e criação lexical.

**Dependências:** som, palavra, sentido

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** tic-tac

**Não confundir com:** Não é cópia perfeita do som real.

### 169. neologismo

**Construção:** Neologismo é forma ou sentido novo introduzido no uso.

**Função:** Permite reconhecer crescimento lexical sem fingir estabilidade imediata.

**Dependências:** palavra, uso, variação linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** uma criação lexical recente

**Não confundir com:** Não é automaticamente erro.

### 170. empréstimo linguístico

**Construção:** Empréstimo linguístico é forma ou sentido incorporado por contacto entre línguas.

**Função:** Explica parte do crescimento lexical e da variação histórica.

**Dependências:** palavra, uso, variação linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** software

**Não confundir com:** Não é dependência técnica do motor.

### 171. família lexical

**Construção:** Família lexical reúne palavras relacionadas por base morfológica e história interna reconhecível.

**Função:** Permite ligar radical, derivação e sentido.

**Dependências:** radical, derivação, relação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** pedra, pedreiro, pedregulho

**Não confundir com:** Não é campo semântico.

### 172. campo lexical

**Construção:** Campo lexical reúne palavras associadas a uma atividade, domínio ou situação.

**Função:** Organiza vocabulário por contexto de uso.

**Dependências:** palavra, contexto, relação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mar, barco, onda, porto

**Não confundir com:** Não exige mesma raiz.

### 173. lexema

**Construção:** Lexema é unidade lexical abstrata que reúne suas formas flexionadas.

**Função:** Distingue identidade lexical de ocorrência escrita concreta.

**Dependências:** lema, flexão, palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** CANTAR reúne canto, cantas, cantamos

**Não confundir com:** Não é token.

### 174. forma lexical

**Construção:** Forma lexical é realização concreta de um lexema numa ocorrência.

**Função:** Liga o lexema abstrato ao texto real.

**Dependências:** lexema, palavra, flexão

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cantamos

**Não confundir com:** Não é lema necessariamente.

### 175. substantivo próprio

**Construção:** Substantivo próprio nomeia referente individualizado dentro de uma convenção de uso.

**Função:** Ajuda a construir referência específica e maiúscula inicial.

**Dependências:** nome, referente, maiúscula

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** Maputo

**Não confundir com:** Não é toda palavra com maiúscula.

### 176. substantivo comum

**Construção:** Substantivo comum nomeia membros de uma classe ou espécie.

**Função:** Permite referência geral ou particular conforme determinantes.

**Dependências:** nome, referência

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cidade

**Não confundir com:** Não é substantivo próprio.

### 177. substantivo concreto

**Construção:** Substantivo concreto apresenta entidade concebida com existência própria no enunciado.

**Função:** Ajuda a distinguir entidade de qualidade ou processo abstraído.

**Dependências:** nome, referente

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mesa

**Não confundir com:** Não significa apenas objeto físico visível.

### 178. substantivo abstrato

**Construção:** Substantivo abstrato nomeia qualidade, estado, ação ou conceito dependente de abstração.

**Função:** Permite transformar processos e propriedades em referentes linguísticos.

**Dependências:** nome, sentido

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** beleza

**Não confundir com:** Não é sinónimo de palavra difícil.

### 179. substantivo coletivo

**Construção:** Substantivo coletivo designa conjunto por uma forma singular.

**Função:** Mostra que número gramatical e quantidade conceptual podem divergir.

**Dependências:** nome, número gramatical, sentido

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cardume

**Não confundir com:** Não é plural morfológico.

### 180. conjugação

**Construção:** Conjugação é organização das formas verbais segundo pessoa, número, tempo, modo e aspecto.

**Função:** Permite reconstruir paradigmas sem decorar tabela como fundamento.

**Dependências:** verbo, flexão, pessoa gramatical, tempo verbal, modo verbal, aspecto verbal

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** eu estudo, nós estudamos

**Não confundir com:** Não é derivação.

### 181. infinitivo

**Construção:** Infinitivo é forma verbal não finita que apresenta o processo sem ancoragem plena de pessoa e tempo.

**Função:** Serve como forma de citação verbal e base de perífrases.

**Dependências:** verbo, conjugação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudar

**Não confundir com:** Não é substantivo automaticamente.

### 182. gerúndio

**Construção:** Gerúndio é forma verbal não finita associada a desenvolvimento ou simultaneidade conforme a construção.

**Função:** Participa de perífrases aspectuais e orações reduzidas.

**Dependências:** verbo, conjugação, aspecto verbal

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudando

**Não confundir com:** Não significa sempre ação presente.

### 183. particípio

**Construção:** Particípio é forma verbal não finita usada em tempos compostos, voz passiva e funções adjetivais.

**Função:** Liga verbo, aspecto e concordância em construções específicas.

**Dependências:** verbo, conjugação, voz verbal

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudado

**Não confundir com:** Não é adjetivo em todo uso.

### 184. presente

**Construção:** Presente é valor temporal que ancora ou aproxima a ocorrência do momento de enunciação, podendo também expressar hábito ou generalidade.

**Função:** Evita reduzir forma presente a instante exato.

**Dependências:** tempo verbal, contexto, enunciado

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudo agora; a água ferve

**Não confundir com:** Não é um único uso temporal.

### 185. passado

**Construção:** Passado é valor temporal que situa ocorrência antes do ponto de referência.

**Função:** Organiza anterioridade sem antecipar todos os tempos verbais.

**Dependências:** tempo verbal, contexto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudei ontem

**Não confundir com:** Não é uma forma única.

### 186. futuro

**Construção:** Futuro é valor temporal que situa ocorrência depois do ponto de referência ou exprime projeção/modalidade.

**Função:** Liga tempo, hipótese e intenção.

**Dependências:** tempo verbal, modalidade, contexto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudarei amanhã

**Não confundir com:** Não garante que o evento ocorrerá.

### 187. indicativo

**Construção:** Indicativo é modo verbal usado para apresentar ocorrência como situada ou assumida no quadro do enunciado.

**Função:** Organiza afirmações sem garantir verdade externa.

**Dependências:** modo verbal, afirmação, contexto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** ele estuda

**Não confundir com:** Não transforma frase em fato comprovado.

### 188. conjuntivo

**Construção:** Conjuntivo é modo verbal associado a hipótese, desejo, possibilidade, condição ou dependência.

**Função:** Permite separar ocorrência afirmada de ocorrência projetada.

**Dependências:** modo verbal, modalidade, subordinação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** talvez ele estude

**Não confundir com:** Também é chamado subjuntivo em outras variedades.

### 189. imperativo

**Construção:** Imperativo é modo ou construção usada para orientar ação, pedido, conselho ou ordem.

**Função:** Liga verbo a ato de fala diretivo.

**Dependências:** modo verbal, intenção comunicativa, pragmática

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estuda com atenção

**Não confundir com:** Não é sempre ordem autoritária.

### 190. pronome pessoal

**Construção:** Pronome pessoal marca participantes ou entidades ligadas às pessoas do discurso.

**Função:** Organiza referência a locutor, interlocutor e terceiros.

**Dependências:** pronome, pessoa gramatical, referência

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** eu, tu, ele

**Não confundir com:** Não é nome próprio.

### 191. pronome possessivo

**Construção:** Pronome possessivo relaciona referente a uma pessoa do discurso por posse ou vínculo.

**Função:** Constrói relações como meu, teu e nosso.

**Dependências:** pronome, pessoa gramatical, relação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** meu livro

**Não confundir com:** Não exprime apenas propriedade material.

### 192. pronome demonstrativo

**Construção:** Pronome demonstrativo localiza referente no espaço, tempo ou discurso.

**Função:** Liga referência a dêixis e contexto.

**Dependências:** pronome, referência, contexto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** este texto

**Não confundir com:** Não é artigo.

### 193. pronome relativo

**Construção:** Pronome relativo retoma antecedente e introduz oração dependente.

**Função:** Une coesão referencial e subordinação.

**Dependências:** pronome, retomada, subordinação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o livro que li

**Não confundir com:** Não é conjunção sem referente.

### 194. pronome interrogativo

**Construção:** Pronome interrogativo ocupa posição desconhecida numa pergunta.

**Função:** Permite buscar pessoa, coisa, quantidade ou escolha.

**Dependências:** pronome, interrogação, referência

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** quem chegou?

**Não confundir com:** Não é pronome relativo em todo contexto.

### 195. pronome indefinido

**Construção:** Pronome indefinido refere quantidade ou identidade não determinada.

**Função:** Representa referência aberta ou imprecisa sem inventar referente.

**Dependências:** pronome, referência, ambiguidade

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** alguém chegou

**Não confundir com:** Não é erro de precisão necessariamente.

### 196. sintagma

**Construção:** Sintagma é grupo de palavras organizado em torno de um núcleo e com função dentro de unidade maior.

**Função:** Cria ponte entre palavra isolada e oração.

**Dependências:** palavra, núcleo, termo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** as meninas

**Não confundir com:** Não é frase completa necessariamente.

### 197. sintagma nominal

**Construção:** Sintagma nominal é sintagma cujo núcleo é nome, pronome ou unidade equivalente.

**Função:** Pode funcionar como sujeito, objeto ou complemento.

**Dependências:** sintagma, nome, pronome

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** as meninas estudiosas

**Não confundir com:** Não é apenas substantivo.

### 198. sintagma verbal

**Construção:** Sintagma verbal é sintagma organizado por verbo e seus dependentes.

**Função:** Estrutura predicados e acontecimentos.

**Dependências:** sintagma, verbo, predicado

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** estudam rapidamente

**Não confundir com:** Não é toda oração sozinho.

### 199. sintagma adjetival

**Construção:** Sintagma adjetival é sintagma cujo núcleo é adjetivo.

**Função:** Organiza qualificação e complementos de adjetivo.

**Dependências:** sintagma, adjetivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** muito feliz

**Não confundir com:** Não é sintagma nominal.

### 200. sintagma adverbial

**Construção:** Sintagma adverbial é sintagma cujo núcleo é advérbio.

**Função:** Organiza circunstância, intensidade ou orientação enunciativa.

**Dependências:** sintagma, advérbio

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** muito longe

**Não confundir com:** Não é adjunto adverbial em todo contexto.

### 201. sintagma preposicional

**Construção:** Sintagma preposicional é grupo introduzido por preposição e ligado a outro termo.

**Função:** Realiza complementos e adjuntos relacionais.

**Dependências:** sintagma, preposição, regência

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** de matemática

**Não confundir com:** Não é preposição isolada.

### 202. concordância nominal

**Construção:** Concordância nominal é ajuste de gênero e número entre elementos de um sintagma nominal.

**Função:** Verifica relações entre nome, artigo, determinante e adjetivo.

**Dependências:** concordância, sintagma nominal, gênero, número gramatical

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** as meninas estudiosas

**Não confundir com:** Não é concordância verbal.

### 203. concordância verbal

**Construção:** Concordância verbal é ajuste de pessoa e número entre verbo e referente sintático relevante.

**Função:** Liga sujeito e forma verbal em construções controladas.

**Dependências:** concordância, verbo, sujeito, pessoa gramatical, número gramatical

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** as meninas estudam

**Não confundir com:** Não é regência verbal.

### 204. sujeito simples

**Construção:** Sujeito simples possui um núcleo principal expresso ou recuperável.

**Função:** Permite análise de concordância em estrutura básica.

**Dependências:** sujeito, núcleo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A menina estuda.

**Não confundir com:** Não significa sujeito curto.

### 205. sujeito composto

**Construção:** Sujeito composto possui mais de um núcleo coordenado.

**Função:** Explica concordância com múltiplos referentes.

**Dependências:** sujeito, núcleo, coordenação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ana e Paulo estudam.

**Não confundir com:** Não é duas orações necessariamente.

### 206. sujeito oculto

**Construção:** Sujeito oculto não aparece como sintagma expresso, mas é recuperado pela forma verbal ou contexto.

**Função:** Evita declarar ausência quando há referência implícita.

**Dependências:** sujeito, elipse, contexto, conjugação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudamos.

**Não confundir com:** Não é sujeito indeterminado.

### 207. sujeito indeterminado

**Construção:** Sujeito indeterminado existe semanticamente, mas não é identificado pelo enunciado.

**Função:** Marca limite de referência sem inventar agente.

**Dependências:** sujeito, referência, contexto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Disseram que viria.

**Não confundir com:** Não é oração sem sujeito.

### 208. oração sem sujeito

**Construção:** Oração sem sujeito organiza predicação sem atribuir o processo a um sujeito gramatical.

**Função:** Trata construções impessoais sem fabricar referente.

**Dependências:** oração, sujeito, verbo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Há problemas.

**Não confundir com:** Não é sujeito oculto.

### 209. predicado verbal

**Construção:** Predicado verbal tem verbo significativo como núcleo principal.

**Função:** Organiza ação, processo ou ocorrência ligada ao sujeito.

**Dependências:** predicado, sintagma verbal, verbo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A menina estudou.

**Não confundir com:** Não é predicado nominal.

### 210. predicado nominal

**Construção:** Predicado nominal atribui estado ou característica por meio de ligação e predicativo.

**Função:** Organiza relação entre sujeito e propriedade.

**Dependências:** predicado, adjetivo, sujeito

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A menina está feliz.

**Não confundir com:** Não é todo predicado com verbo.

### 211. predicado verbo-nominal

**Construção:** Predicado verbo-nominal combina processo verbal e predicação nominal.

**Função:** Representa ação e característica simultaneamente.

**Dependências:** predicado verbal, predicado nominal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A menina chegou cansada.

**Não confundir com:** Não são necessariamente duas orações.

### 212. objeto direto

**Construção:** Objeto direto é complemento verbal não introduzido por preposição exigida na construção básica.

**Função:** Completa verbo transitivo direto.

**Dependências:** complemento, transitividade verbal, sintagma nominal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** leu o livro

**Não confundir com:** Não é sujeito pós-verbal automaticamente.

### 213. objeto indireto

**Construção:** Objeto indireto é complemento verbal ligado por preposição exigida.

**Função:** Completa verbo transitivo indireto.

**Dependências:** complemento, transitividade verbal, preposição

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** gosta de música

**Não confundir com:** Não é qualquer sintagma preposicional.

### 214. complemento nominal

**Construção:** Complemento nominal completa sentido de nome, adjetivo ou advérbio por relação preposicional.

**Função:** Distingue dependência lexical nominal de circunstância livre.

**Dependências:** complemento, sintagma preposicional, nome, adjetivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** necessidade de apoio

**Não confundir com:** Não é objeto indireto.

### 215. predicativo do sujeito

**Construção:** Predicativo do sujeito atribui propriedade ao sujeito dentro do predicado.

**Função:** Liga estado ou qualidade ao referente do sujeito.

**Dependências:** predicado nominal, sujeito, adjetivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A casa é grande.

**Não confundir com:** Não é adjunto adnominal.

### 216. predicativo do objeto

**Construção:** Predicativo do objeto atribui propriedade ao objeto dentro da predicação.

**Função:** Mostra segunda relação predicativa na mesma oração.

**Dependências:** objeto direto, predicado verbo-nominal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** considero o plano correto

**Não confundir com:** Não é adjetivo meramente interno ao nome.

### 217. agente da passiva

**Construção:** Agente da passiva expressa participante que realiza a ação em construção passiva.

**Função:** Recupera agente sem colocá-lo como sujeito gramatical.

**Dependências:** voz verbal, sujeito, preposição

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o texto foi escrito pelo aluno

**Não confundir com:** Não é sujeito da oração passiva.

### 218. adjunto adnominal

**Construção:** Adjunto adnominal modifica ou determina um nome sem completar exigência lexical obrigatória.

**Função:** Organiza atributos, posse e delimitação no sintagma nominal.

**Dependências:** adjunto, sintagma nominal, nome

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** meu livro novo

**Não confundir com:** Não é complemento nominal.

### 219. adjunto adverbial

**Construção:** Adjunto adverbial acrescenta circunstância de tempo, lugar, modo, causa ou outra relação ao predicado ou enunciado.

**Função:** Amplia informação sem ser complemento exigido em muitos casos.

**Dependências:** adjunto, advérbio, sintagma adverbial

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** estuda de manhã

**Não confundir com:** Não é todo advérbio isolado.

### 220. aposto

**Construção:** Aposto acrescenta explicação, identificação, enumeração ou resumo a um termo.

**Função:** Expande referência sem criar necessariamente nova oração.

**Dependências:** termo, pontuação, referência

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Maputo, capital de Moçambique, ...

**Não confundir com:** Não é vocativo.

### 221. vocativo

**Construção:** Vocativo chama ou interpela o interlocutor fora da estrutura argumental do predicado.

**Função:** Marca participante comunicativo diretamente convocado.

**Dependências:** enunciado, intenção comunicativa, pontuação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Maria, venha aqui.

**Não confundir com:** Não é sujeito.

### 222. voz ativa

**Construção:** Voz ativa organiza sujeito como participante apresentado na posição de agente ou origem do processo.

**Função:** Fornece uma configuração básica entre sujeito, verbo e objeto.

**Dependências:** voz verbal, sujeito, predicado

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** O aluno escreveu o texto.

**Não confundir com:** Não garante agente semântico em todo verbo.

### 223. voz passiva

**Construção:** Voz passiva organiza sujeito como participante afetado e pode apresentar agente separadamente.

**Função:** Permite mudar foco informacional sem mudar necessariamente o acontecimento central.

**Dependências:** voz verbal, sujeito, objeto direto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** O texto foi escrito pelo aluno.

**Não confundir com:** Não é simples troca de ordem.

### 224. voz reflexiva

**Construção:** Voz reflexiva apresenta participante ligado simultaneamente ao início e ao alvo do processo.

**Função:** Representa ação voltada ao próprio referente.

**Dependências:** voz verbal, pronome pessoal, sujeito

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ela se penteou.

**Não confundir com:** Nem todo se é reflexivo.

### 225. oração coordenada

**Construção:** Oração coordenada liga-se a outra sem depender dela como termo sintático.

**Função:** Constrói período composto por unidades de nível semelhante.

**Dependências:** oração, coordenação, período

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou e passou.

**Não confundir com:** Pode haver relação semântica forte sem subordinação.

### 226. oração subordinada

**Construção:** Oração subordinada exerce função ou relação dependente dentro de outra construção.

**Função:** Constrói períodos em que uma oração integra ou modifica outra.

**Dependências:** oração, subordinação, período

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Disse que viria.

**Não confundir com:** Não é simplesmente oração posterior.

### 227. oração subordinada substantiva

**Construção:** Oração subordinada substantiva ocupa função típica de sintagma nominal.

**Função:** Pode atuar como sujeito, objeto ou complemento.

**Dependências:** oração subordinada, sintagma nominal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** É necessário que estudes.

**Não confundir com:** Não é substantivo lexical.

### 228. oração subordinada adjetiva

**Construção:** Oração subordinada adjetiva modifica um nome por meio de relação relativa.

**Função:** Expande referente com propriedade ou identificação.

**Dependências:** oração subordinada, pronome relativo, adjetivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o livro que li

**Não confundir com:** Não é qualquer oração com adjetivo.

### 229. oração subordinada adverbial

**Construção:** Oração subordinada adverbial estabelece circunstância ou relação lógica com outra oração.

**Função:** Expressa causa, condição, tempo, concessão e outras relações.

**Dependências:** oração subordinada, advérbio, conjunção

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Se estudar, aprenderá.

**Não confundir com:** Não é adjunto adverbial simples.

### 230. período composto

**Construção:** Período composto contém duas ou mais orações articuladas.

**Função:** Permite analisar coordenação, subordinação e relações entre eventos.

**Dependências:** período, oração coordenada, oração subordinada

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou porque queria aprender.

**Não confundir com:** Não é definido pelo tamanho gráfico.

### 231. denotação

**Construção:** Denotação é uso de sentido mais diretamente referencial e estabilizado no contexto.

**Função:** Serve como ponto de partida para distinguir leitura literal de efeitos figurados.

**Dependências:** sentido, referência, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A pedra caiu.

**Não confundir com:** Não garante um único sentido universal.

### 232. conotação

**Construção:** Conotação é conjunto de associações e valores evocados além da referência direta.

**Função:** Permite interpretar efeitos culturais, afetivos e figurados.

**Dependências:** sentido, contexto, denotação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** coração como afeto

**Não confundir com:** Não é erro ou mentira.

### 233. homonímia

**Construção:** Homonímia ocorre quando formas iguais ou próximas correspondem a lexemas distintos.

**Função:** Impede fundir sentidos sem relação apenas porque a forma coincide.

**Dependências:** palavra, lexema, sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** manga da camisa / manga fruta

**Não confundir com:** Não é polissemia quando não há unidade lexical comum reconhecida.

### 234. paronímia

**Construção:** Paronímia é proximidade formal entre palavras diferentes.

**Função:** Ajuda a evitar confusões de escrita e sentido.

**Dependências:** palavra, diferença, ortografia

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** descrição / discrição

**Não confundir com:** Não é sinonímia.

### 235. hiperonímia

**Construção:** Hiperonímia é relação em que um termo expressa classe mais geral.

**Função:** Organiza hierarquias de sentido.

**Dependências:** sentido, relação, campo semântico

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** animal é hiperónimo de cão

**Não confundir com:** Não é parte-todo.

### 236. hiponímia

**Construção:** Hiponímia é relação em que um termo expressa membro ou subclasse mais específica.

**Função:** Permite descer de categoria geral para categoria particular.

**Dependências:** hiperonímia, sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** cão é hipónimo de animal

**Não confundir com:** Não é sinónimo.

### 237. metáfora

**Construção:** Metáfora constrói sentido por aproximação entre domínios sem marca explícita de comparação.

**Função:** Permite transferência controlada de propriedades e imagens.

**Dependências:** conotação, relação, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** tempo é rio

**Não confundir com:** Não é afirmação literal.

### 238. metonímia

**Construção:** Metonímia constrói sentido por contiguidade entre entidades, partes, autores, obras ou relações associadas.

**Função:** Permite referir um elemento por outro ligado a ele.

**Dependências:** conotação, referência, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** ler Machado de Assis

**Não confundir com:** Não é metáfora por semelhança.

### 239. ironia

**Construção:** Ironia produz sentido em tensão com o significado literal e depende de contexto, intenção e expectativa.

**Função:** Permite reconhecer que o enunciado pode comunicar oposição implícita.

**Dependências:** pragmática, contexto, intenção comunicativa, conotação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Que pontual!, dito a quem chegou tarde.

**Não confundir com:** Não deve ser inferida sem sinais suficientes.

### 240. pressuposição

**Construção:** Pressuposição é conteúdo tratado como pano de fundo para que um enunciado funcione.

**Função:** Ajuda a separar o que é afirmado do que é tomado como já válido no discurso.

**Dependências:** enunciado, inferência, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Ele voltou pressupõe que esteve antes.

**Não confundir com:** Não é necessariamente verdade externa.

### 241. implicatura

**Construção:** Implicatura é sentido sugerido pelo uso e pela cooperação comunicativa sem ser dito literalmente.

**Função:** Permite inferir intenção mantendo possibilidade de cancelamento.

**Dependências:** pragmática, inferência, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Está frio pode sugerir fechar a janela.

**Não confundir com:** Não é consequência lógica obrigatória.

### 242. dêixis

**Construção:** Dêixis é referência dependente da posição de participantes, tempo ou espaço da enunciação.

**Função:** Explica formas como eu, aqui e agora.

**Dependências:** referência, contexto, enunciado

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** eu aqui agora

**Não confundir com:** Não é referência fixa fora do contexto.

### 243. anáfora

**Construção:** Anáfora retoma elemento anterior no texto ou discurso.

**Função:** Constrói cadeia referencial e coesão.

**Dependências:** retomada, referente, coesão

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Maria chegou. Ela sentou.

**Não confundir com:** Não é catáfora.

### 244. catáfora

**Construção:** Catáfora anuncia ou aponta para elemento que aparecerá depois.

**Função:** Permite referência prospectiva dentro do texto.

**Dependências:** referência, coesão, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Só digo isto: estudem.

**Não confundir com:** Não é anáfora.

### 245. gênero textual

**Construção:** Gênero textual é forma social recorrente de texto ligada a finalidade, situação e participantes.

**Função:** Organiza expectativas sobre estrutura e linguagem sem congelar textos reais.

**Dependências:** texto, uso, intenção comunicativa, contexto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** carta, notícia, receita

**Não confundir com:** Não é tipo textual.

### 246. tipo textual

**Construção:** Tipo textual é modo predominante de organização linguística, como narrar, descrever, expor, argumentar ou instruir.

**Função:** Analisa operação textual interna independentemente do gênero social.

**Dependências:** texto, relação, intenção comunicativa

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** narração

**Não confundir com:** Não é gênero textual.

### 247. narração

**Construção:** Narração organiza acontecimentos, participantes e mudanças no tempo.

**Função:** Constrói sequência de eventos e relações causais ou temporais.

**Dependências:** tipo textual, tempo verbal, texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** contar uma viagem

**Não confundir com:** Não é apenas texto no passado.

### 248. descrição

**Construção:** Descrição organiza propriedades, partes e estados de um referente.

**Função:** Permite tornar entidade ou situação observável por linguagem.

**Dependências:** tipo textual, referente, adjetivo

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** descrever uma casa

**Não confundir com:** Não é lista sem relação.

### 249. exposição

**Construção:** Exposição organiza conceitos, relações e explicações para tornar um assunto compreensível.

**Função:** Serve à apresentação estruturada de conhecimento.

**Dependências:** tipo textual, coerência, tema

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** explicar fotossíntese

**Não confundir com:** Não é argumentação necessariamente.

### 250. argumentação

**Construção:** Argumentação organiza tese, razões, evidências e respostas a objeções para sustentar uma posição.

**Função:** Permite avaliar se uma conclusão está apoiada por relações explícitas.

**Dependências:** tipo textual, afirmação, inferência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** defender uma tese com razões

**Não confundir com:** Não é discussão agressiva.

### 251. instrução

**Construção:** Instrução organiza ações em sequência orientada para um resultado.

**Função:** Permite produzir procedimentos, regras e comandos verificáveis.

**Dependências:** tipo textual, imperativo, coerência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** receita ou manual

**Não confundir com:** Não é mera descrição.

### 252. diálogo

**Construção:** Diálogo organiza alternância de enunciados entre participantes.

**Função:** Torna visíveis turnos, respostas e negociação de sentido.

**Dependências:** texto, enunciado, intenção comunicativa

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A: Olá. B: Olá.

**Não confundir com:** Não é qualquer texto com aspas.

### 253. título

**Construção:** Título é unidade que identifica e orienta o tema ou função de um texto.

**Função:** Cria expectativa inicial e facilita referência ao documento.

**Dependências:** texto, tema

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Conhecimento puro de Português

**Não confundir com:** Não é resumo completo.

### 254. tópico frasal

**Construção:** Tópico frasal é enunciado que apresenta ou concentra a ideia central de um parágrafo.

**Função:** Ajuda a construir progressão e unidade local.

**Dependências:** parágrafo, tema, enunciado

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A leitura amplia o vocabulário.

**Não confundir com:** Não precisa ser sempre a primeira frase.

### 255. introdução

**Construção:** Introdução é parte textual que apresenta tema, contexto, objetivo ou problema.

**Função:** Prepara o leitor para o desenvolvimento.

**Dependências:** texto, tema, contexto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** apresentação do assunto

**Não confundir com:** Não é prefácio obrigatório.

### 256. desenvolvimento textual

**Construção:** Desenvolvimento textual é parte em que tema, argumentos, explicações ou eventos são expandidos.

**Função:** Sustenta o corpo principal do texto.

**Dependências:** texto, progressão temática, coerência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** parágrafos centrais

**Não confundir com:** Não é repetição da introdução.

### 257. conclusão textual

**Construção:** Conclusão textual fecha ou reorienta o percurso construído pelo texto.

**Função:** Retoma resultados, sínteses ou consequências sem acrescentar base não sustentada.

**Dependências:** texto, coerência, desenvolvimento textual

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** síntese final

**Não confundir com:** Não é verdade automática do texto.

### 258. tese

**Construção:** Tese é posição central defendida numa argumentação.

**Função:** Orienta seleção de argumentos e conclusão.

**Dependências:** argumentação, tema, afirmação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A leitura diária melhora a escrita.

**Não confundir com:** Não é fato comprovado por si só.

### 259. argumento

**Construção:** Argumento é razão apresentada para sustentar ou contestar uma tese.

**Função:** Liga afirmações a justificações examináveis.

**Dependências:** argumentação, relação, inferência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A prática amplia repertório.

**Não confundir com:** Não é exemplo isolado necessariamente.

### 260. premissa

**Construção:** Premissa é afirmação usada como ponto de partida de uma inferência ou argumento.

**Função:** Permite verificar se a conclusão depende de bases aceitas.

**Dependências:** argumento, inferência, afirmação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Todos os mamíferos respiram.

**Não confundir com:** Não é conclusão.

### 261. evidência

**Construção:** Evidência é dado, observação ou fonte apresentada para apoiar uma afirmação.

**Função:** Distingue suporte observável de opinião nua.

**Dependências:** argumento, contexto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** resultado de teste

**Não confundir com:** Não garante conclusão sem análise.

### 262. contra-argumento

**Construção:** Contra-argumento é razão que contesta tese ou argumento anterior.

**Função:** Permite testar resistência da posição defendida.

**Dependências:** argumento, relação, negação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma objeção fundamentada

**Não confundir com:** Não é ataque pessoal.

### 263. refutação

**Construção:** Refutação responde a um contra-argumento mostrando erro, limite ou insuficiência.

**Função:** Fortalece ou corrige a tese por confronto racional.

**Dependências:** contra-argumento, argumento, inferência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** mostrar que a objeção não cobre o caso

**Não confundir com:** Não é simples negação.

### 264. fato textual

**Construção:** Fato textual é conteúdo apresentado como verificável dentro de critérios e fontes definidos.

**Função:** Ajuda a separar afirmação verificável de avaliação pessoal.

**Dependências:** texto, afirmação, evidência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o teste registrou 58 aprovações

**Não confundir com:** Não é verdade eterna; depende de escopo e fonte.

### 265. opinião

**Construção:** Opinião é avaliação ou posição de um locutor.

**Função:** Permite marcar subjetividade sem apresentá-la como fato.

**Dependências:** enunciado, intenção comunicativa, modalidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** considero o método claro

**Não confundir com:** Não é evidência por si só.

### 266. paráfrase

**Construção:** Paráfrase reconstrói conteúdo com outras palavras preservando o núcleo de sentido.

**Função:** Permite explicar e verificar compreensão sem copiar forma.

**Dependências:** texto, sentido, interpretação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** dizer a mesma ideia de outra maneira

**Não confundir com:** Não é citação literal.

### 267. citação

**Construção:** Citação incorpora forma ou conteúdo atribuído a outra fonte ou voz.

**Função:** Preserva rastreabilidade e separa voz própria de voz trazida.

**Dependências:** texto, discurso direto, referência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** trecho atribuído a autor

**Não confundir com:** Não entra como conhecimento puro sem reconstrução.

### 268. resumo

**Construção:** Resumo reduz extensão preservando ideias centrais e relações essenciais.

**Função:** Permite condensar sem substituir análise profunda.

**Dependências:** texto, tema, coerência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** síntese curta de capítulo

**Não confundir com:** Não é lista aleatória.

### 269. síntese

**Construção:** Síntese integra elementos de uma ou mais fontes numa construção unificada.

**Função:** Cria visão conjunta mantendo relações e diferenças relevantes.

**Dependências:** resumo, relação, interpretação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** unir resultados de vários trechos

**Não confundir com:** Não é colagem.

### 270. resenha

**Construção:** Resenha apresenta, resume e avalia uma obra ou texto com critérios explícitos.

**Função:** Combina exposição e avaliação sem esconder opinião.

**Dependências:** resumo, opinião, argumento

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** resenha de um livro

**Não confundir com:** Não é apenas resumo.

### 271. coesão referencial

**Construção:** Coesão referencial liga menções que apontam para o mesmo referente ou referentes relacionados.

**Função:** Sustenta continuidade por pronomes, nomes, elipses e substituições.

**Dependências:** coesão, referência, retomada

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Maria... ela... a estudante

**Não confundir com:** Não é coerência global.

### 272. coesão sequencial

**Construção:** Coesão sequencial organiza avanço entre enunciados por conectores, tempos e relações.

**Função:** Marca adição, oposição, causa, consequência e ordem.

**Dependências:** coesão, conectivo, progressão temática

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** primeiro, depois, portanto

**Não confundir com:** Não é ordem cronológica obrigatória.

### 273. cadeia referencial

**Construção:** Cadeia referencial é sequência de expressões que mantém ou transforma um referente ao longo do texto.

**Função:** Permite rastrear quem ou o que está sendo mencionado.

**Dependências:** coesão referencial, anáfora, catáfora

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o aluno → ele → o jovem

**Não confundir com:** Não é repetição idêntica obrigatória.

### 274. tópico discursivo

**Construção:** Tópico discursivo é foco sobre o qual uma parte da interação ou texto se organiza.

**Função:** Permite observar mudanças, retomadas e desvios temáticos.

**Dependências:** tema, contexto, diálogo

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** falar sobre educação

**Não confundir com:** Não é título necessariamente.

### 275. informação dada

**Construção:** Informação dada é conteúdo tratado como já acessível no contexto ou discurso.

**Função:** Ajuda a explicar ordem, pronomes e elipses.

**Dependências:** contexto, referência, pressuposição

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** retomar algo já mencionado

**Não confundir com:** Não é fato universal.

### 276. informação nova

**Construção:** Informação nova é conteúdo introduzido ou destacado como ainda não acessível ao interlocutor.

**Função:** Orienta foco, progressão e escolha de formas.

**Dependências:** informação dada, contexto, enunciado

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** apresentar novo referente

**Não confundir com:** Não é palavra inédita necessariamente.

### 277. modalidade oral

**Construção:** Modalidade oral é realização da língua pela fala, com prosódia, interação e contexto imediato.

**Função:** Permite analisar recursos próprios da oralidade.

**Dependências:** oralidade, uso, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** conversa presencial

**Não confundir com:** Não é português incorreto.

### 278. modalidade escrita

**Construção:** Modalidade escrita é realização da língua por marcas gráficas relativamente persistentes.

**Função:** Permite planejamento, revisão e leitura fora do momento de produção.

**Dependências:** grafema, texto, uso

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** uma carta

**Não confundir com:** Não é simples transcrição da fala.

### 279. norma-padrão

**Construção:** Norma-padrão é modelo codificado usado como referência em certos contextos formais de escrita e ensino.

**Função:** Permite adequação institucional sem negar outras variedades.

**Dependências:** norma, modalidade escrita, registro

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** convenção de documento oficial

**Não confundir com:** Não é a língua inteira nem medida de inteligência.

### 280. dialeto

**Construção:** Dialeto é variedade linguística associada a região, grupo ou história, com padrões próprios.

**Função:** Reconhece organização sistemática da variação.

**Dependências:** variação linguística, uso, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** variedade regional

**Não confundir com:** Não é erro coletivo.

### 281. sotaque

**Construção:** Sotaque é conjunto de traços de pronúncia associados a origem, grupo ou percurso individual.

**Função:** Localiza variação fonética sem julgar competência.

**Dependências:** variação linguística, fonema, prosódia

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** realizações diferentes de r

**Não confundir com:** Não é dialeto inteiro.

### 282. socioleto

**Construção:** Socioleto é variedade associada a grupo social ou profissional.

**Função:** Explica escolhas compartilhadas de vocabulário e construção.

**Dependências:** variação linguística, registro, uso

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** vocabulário técnico de programadores

**Não confundir com:** Não é idioleto.

### 283. idioleto

**Construção:** Idioleto é conjunto de hábitos linguísticos recorrentes de uma pessoa.

**Função:** Permite reconhecer estilo individual sem separá-lo da língua compartilhada.

**Dependências:** variação linguística, estilo, uso

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** preferências de palavras de um falante

**Não confundir com:** Não é língua privada completa.

### 284. regionalismo

**Construção:** Regionalismo é forma ou sentido fortemente ligado a uma região.

**Função:** Registra diversidade lexical e cultural sem apagá-la.

**Dependências:** variação linguística, contexto, palavra

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** uma palavra típica de certa região

**Não confundir com:** Não é erro padrão.

### 285. variação regional

**Construção:** Variação regional é mudança sistemática conforme localização geográfica e contacto linguístico.

**Função:** Organiza diferenças de pronúncia, léxico e gramática entre regiões.

**Dependências:** variação linguística, dialeto, regionalismo

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** português de Moçambique e de Portugal

**Não confundir com:** Não implica hierarquia de valor.

### 286. variação social

**Construção:** Variação social é mudança ligada a grupos, profissões, redes e condições sociais.

**Função:** Explica socioletos e escolhas de identidade.

**Dependências:** variação linguística, socioleto, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** jargão profissional

**Não confundir com:** Não é falha individual.

### 287. variação histórica

**Construção:** Variação histórica é mudança da língua ao longo do tempo.

**Função:** Explica arcaísmos, neologismos e transformações gramaticais.

**Dependências:** variação linguística, uso, neologismo

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** formas antigas e atuais

**Não confundir com:** Não é evolução para melhor ou pior.

### 288. variação situacional

**Construção:** Variação situacional é mudança de linguagem conforme atividade, relação e objetivo comunicativo.

**Função:** Permite adequar registro ao contexto.

**Dependências:** variação linguística, registro, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** falar diferente em entrevista e com amigos

**Não confundir com:** Não é fingimento de identidade.

### 289. formalidade

**Construção:** Formalidade é grau de controlo, distância e convenção numa situação comunicativa.

**Função:** Orienta escolhas lexicais, sintáticas e de tratamento.

**Dependências:** registro, contexto, variação situacional

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** pedido institucional

**Não confundir com:** Não é qualidade moral.

### 290. informalidade

**Construção:** Informalidade é grau de espontaneidade e proximidade numa situação comunicativa.

**Função:** Permite linguagem mais elíptica, coloquial e contextual.

**Dependências:** registro, contexto, variação situacional

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** conversa entre amigos

**Não confundir com:** Não é ausência de regras.

### 291. cortesia

**Construção:** Cortesia é conjunto de estratégias para gerir respeito, proximidade, pedido e desacordo.

**Função:** Liga forma linguística à relação entre participantes.

**Dependências:** pragmática, intenção comunicativa, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** por favor

**Não confundir com:** Não é apenas uso de palavras fixas.

### 292. adequação linguística

**Construção:** Adequação linguística é escolha de formas compatíveis com objetivo, participantes, gênero e contexto.

**Função:** Substitui julgamento absoluto por avaliação contextual.

**Dependências:** uso, registro, contexto, gênero textual

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** usar linguagem técnica num relatório

**Não confundir com:** Não é submissão cega à norma-padrão.

### 293. leitura

**Construção:** Leitura é construção de sentido a partir de marcas escritas, conhecimentos internos e contexto controlado.

**Função:** Liga decodificação, interpretação e verificação.

**Dependências:** modalidade escrita, interpretação, texto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** ler um parágrafo

**Não confundir com:** Não é pronunciar letras apenas.

### 294. compreensão literal

**Construção:** Compreensão literal recupera informações explicitamente apresentadas no texto.

**Função:** Forma base verificável antes de inferências mais abertas.

**Dependências:** leitura, denotação, texto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** identificar quem realizou a ação

**Não confundir com:** Não é interpretação total.

### 295. compreensão inferencial

**Construção:** Compreensão inferencial constrói informação não dita diretamente a partir de relações sustentadas pelo texto e contexto.

**Função:** Permite avançar além do literal sem inventar.

**Dependências:** leitura, inferência, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** deduzir causa por conectores

**Não confundir com:** Não é adivinhação.

### 296. leitura crítica

**Construção:** Leitura crítica examina tese, evidência, pressupostos, linguagem, fonte e limites.

**Função:** Impede aceitar texto apenas por aparência de autoridade.

**Dependências:** leitura, argumento, evidência, interpretação

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** questionar se a prova sustenta a conclusão

**Não confundir com:** Não é rejeitar tudo.

### 297. escrita

**Construção:** Escrita é produção de texto por marcas gráficas organizadas para um objetivo comunicativo.

**Função:** Integra planejamento, textualização, revisão e adequação.

**Dependências:** modalidade escrita, texto, intenção comunicativa

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** redigir uma explicação

**Não confundir com:** Não é copiar palavras.

### 298. planejamento textual

**Construção:** Planejamento textual define objetivo, leitor, gênero, tema e organização antes ou durante a escrita.

**Função:** Reduz saltos e contradições na produção.

**Dependências:** escrita, contexto, gênero textual, tema

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** esboçar tópicos

**Não confundir com:** Não precisa ser documento separado.

### 299. textualização

**Construção:** Textualização transforma planejamento e ideias em sequência efetiva de frases e parágrafos.

**Função:** Materializa o texto mantendo coesão e progressão.

**Dependências:** planejamento textual, frase, parágrafo, coesão

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** redigir o primeiro rascunho

**Não confundir com:** Não é revisão final.

### 300. edição textual

**Construção:** Edição textual altera organização, conteúdo e forma para melhorar adequação e consistência.

**Função:** Permite mudanças estruturais além da correção local.

**Dependências:** textualização, revisão, coerência

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** mover um parágrafo

**Não confundir com:** Não é apenas corrigir ortografia.

### 301. reescrita

**Construção:** Reescrita produz nova formulação preservando ou ajustando objetivo e sentido.

**Função:** Permite reconstruir texto após análise.

**Dependências:** edição textual, paráfrase, escrita

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** reescrever uma explicação confusa

**Não confundir com:** Não é apagar conhecimento.

### 302. correção ortográfica

**Construção:** Correção ortográfica verifica grafia, acentuação, hífen e segmentação segundo convenções assumidas.

**Função:** Remove desvios gráficos sem fingir que corrige sentido.

**Dependências:** ortografia, revisão, acentuação gráfica

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** corrigir ação

**Não confundir com:** Não é correção gramatical inteira.

### 303. correção gramatical

**Construção:** Correção gramatical verifica relações de flexão, concordância, regência e construção sintática.

**Função:** Ajusta estrutura sem substituir avaliação de coerência.

**Dependências:** gramática, revisão, concordância, regência

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** as meninas estudam

**Não confundir com:** Não é garantia de texto claro.

### 304. clareza

**Construção:** Clareza é facilidade de reconstruir o sentido pretendido com ambiguidades controladas.

**Função:** Orienta escolha lexical, ordem e explicitação suficiente.

**Dependências:** texto, interpretação, ambiguidade

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** frase com referente explícito

**Não confundir com:** Não é simplificação excessiva.

### 305. precisão lexical

**Construção:** Precisão lexical é escolha de palavra compatível com o conceito e o contexto.

**Função:** Reduz vagueza e confusão entre termos próximos.

**Dependências:** palavra, sentido, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** usar hipótese em vez de certeza

**Não confundir com:** Não é vocabulário rebuscado.

### 306. concisão

**Construção:** Concisão é redução do excesso mantendo informação necessária e relações essenciais.

**Função:** Melhora eficiência textual sem amputar conhecimento.

**Dependências:** texto, revisão, clareza

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** remover repetição inútil

**Não confundir com:** Não é escrever o mínimo possível.

### 307. fluidez

**Construção:** Fluidez é continuidade perceptível entre unidades linguísticas sem rupturas desnecessárias.

**Função:** Liga ritmo, coesão e facilidade de processamento.

**Dependências:** coesão, ritmo, texto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** transições naturais entre frases

**Não confundir com:** Não é velocidade.

### 308. escuta

**Construção:** Escuta é construção de sentido a partir da fala, do contexto e de sinais prosódicos.

**Função:** Complementa oralidade e diálogo.

**Dependências:** oralidade, prosódia, interpretação

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** acompanhar uma explicação oral

**Não confundir com:** Não é ouvir som passivamente.

### 309. fala

**Construção:** Fala é produção situada de enunciados por meio sonoro.

**Função:** Materializa conhecimento linguístico na interação oral.

**Dependências:** produção da fala, oralidade, enunciado

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** explicar uma ideia em voz alta

**Não confundir com:** Não é língua inteira.

### 310. competência comunicativa

**Construção:** Competência comunicativa é capacidade de compreender e produzir linguagem adequada, coerente e eficaz em contextos diversos.

**Função:** Integra gramática, uso, variação, leitura, escrita, fala e escuta.

**Dependências:** gramática, adequação linguística, leitura, escrita, fala, escuta

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** adaptar uma explicação ao interlocutor

**Não confundir com:** Não é apenas correção normativa.

### 311. dicionário

**Construção:** Dicionário é estrutura que organiza formas, lemas, classes, sentidos e relações lexicais.

**Função:** Permite consulta e expansão controlada do léxico.

**Dependências:** lema, forma lexical, sentido

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** entrada para palavra

**Não confundir com:** Não é a língua inteira.

### 312. entrada lexical

**Construção:** Entrada lexical é registro estruturado de uma forma ou lexema no dicionário.

**Função:** Liga grafia, lema, classe, traços e definições.

**Dependências:** dicionário, lexema, classe gramatical

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** lema=casa, classe=nome

**Não confundir com:** Não é ocorrência textual.

### 313. verbete

**Construção:** Verbete é apresentação consultável de uma entrada lexical ou conceito.

**Função:** Organiza informação para leitura humana.

**Dependências:** entrada lexical, texto

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** verbete de casa

**Não confundir com:** Não é conhecimento puro por si só; é apresentação.

### 314. acepção

**Construção:** Acepção é sentido específico de uma palavra dentro de um conjunto de leituras.

**Função:** Permite representar polissemia sem misturar usos.

**Dependências:** sentido, polissemia, entrada lexical

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** banco como assento ou instituição

**Não confundir com:** Não é sinónimo de definição inteira.

### 315. definição lexical

**Construção:** Definição lexical descreve uma acepção por relações e propriedades suficientes.

**Função:** Permite consultar significado mantendo limites.

**Dependências:** acepção, sentido, relação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** casa: edifício para habitação

**Não confundir com:** Não prova existência do referente.

### 316. exemplo de uso

**Construção:** Exemplo de uso mostra uma forma ou construção em contexto mínimo.

**Função:** Testa se definição e função podem ser aplicadas.

**Dependências:** uso, contexto, entrada lexical

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** A casa é grande.

**Não confundir com:** Não substitui regra geral.

### 317. corpus local

**Construção:** Corpus local é conjunto delimitado de textos internos usado para observação e comparação.

**Função:** Permite encontrar padrões sem depender de fonte externa como fundamento.

**Dependências:** texto, uso, dicionário

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** textos aprovados do projeto

**Não confundir com:** Não é conhecimento puro automaticamente.

### 318. frequência lexical

**Construção:** Frequência lexical é contagem de ocorrências de formas ou lemas num corpus delimitado.

**Função:** Ajuda a priorizar estudo e reconhecer padrões de uso.

**Dependências:** corpus local, forma lexical, lema

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** casa aparece 12 vezes

**Não confundir com:** Não mede importância universal.

### 319. produtividade linguística

**Construção:** Produtividade linguística é capacidade de uma regra ou padrão formar novos casos aceitáveis.

**Função:** Distingue padrão vivo de lista fechada.

**Dependências:** gramática, uso, derivação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** sufixo -mente formando advérbios

**Não confundir com:** Não significa ausência de restrições.

### 320. gramaticalidade

**Construção:** Gramaticalidade é compatibilidade de uma construção com regras de uma variedade ou modelo definidos.

**Função:** Permite testar estrutura sem confundir com verdade ou elegância.

**Dependências:** gramática, relação, variação linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** As meninas estudam.

**Não confundir com:** Não é aceitabilidade total.

### 321. aceitabilidade

**Construção:** Aceitabilidade é grau em que falantes ou um modelo consideram uma construção utilizável num contexto.

**Função:** Inclui efeitos de frequência, sentido, processamento e situação.

**Dependências:** gramaticalidade, uso, contexto

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma frase rara mas compreensível

**Não confundir com:** Não é regra fixa universal.

### 322. competência linguística

**Construção:** Competência linguística é conhecimento interno de formas e relações que permite produzir e compreender construções.

**Função:** Separa capacidade estrutural de execução concreta.

**Dependências:** gramática, dicionário, sentido

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** saber formar frases

**Não confundir com:** Não é competência comunicativa completa.

### 323. desempenho linguístico

**Construção:** Desempenho linguístico é realização concreta da competência sob condições de memória, atenção e contexto.

**Função:** Explica falhas de execução sem concluir ausência de conhecimento.

**Dependências:** competência linguística, uso, contexto

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** hesitar ao falar

**Não confundir com:** Não é conhecimento puro.

### 324. metalinguagem

**Construção:** Metalinguagem é linguagem usada para descrever a própria língua.

**Função:** Permite definir verbo, sujeito, sentido e regra com precisão.

**Dependências:** texto, gramática, sentido

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** verbo é uma classe gramatical

**Não confundir com:** Não é a língua-objeto em uso direto.

### 325. análise linguística

**Construção:** Análise linguística decompõe ocorrência em unidades, relações e funções explícitas.

**Função:** Permite investigar sem reduzir tudo a correção normativa.

**Dependências:** metalinguagem, diferença, relação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** separar palavra, classe e função

**Não confundir com:** Não é apenas classificar nomes.

### 326. descrição linguística

**Construção:** Descrição linguística registra como formas e relações funcionam numa variedade ou corpus delimitado.

**Função:** Conserva observação antes de prescrever.

**Dependências:** análise linguística, uso, variação linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** descrever uma construção usada

**Não confundir com:** Não é autorização normativa.

### 327. prescrição linguística

**Construção:** Prescrição linguística estabelece formas recomendadas para objetivo ou norma específicos.

**Função:** Permite orientar escrita formal mantendo escopo explícito.

**Dependências:** norma, descrição linguística, adequação linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** recomendação para documento oficial

**Não confundir com:** Não é verdade absoluta sobre a língua.

### 328. reconstrução linguística PSF

**Construção:** Reconstrução linguística PSF desmonta uma forma, regra ou explicação e refaz suas dependências desde unidades já construídas.

**Função:** Garante que conhecimento de Português seja compreendido por como e porquê, não por citação cega.

**Dependências:** análise linguística, diferença, relação, revisão

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** reconstruir crase a partir de preposição, artigo e relação

**Não confundir com:** Não inventa fatos históricos ou externos.

### 329. ponto final

**Construção:** Ponto final é marca que encerra uma unidade declarativa ou um bloco textual completo.

**Função:** Sinaliza fechamento gráfico e separa enunciados.

**Dependências:** pontuação, frase

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** O estudo terminou.

**Não confundir com:** Não prova que o assunto acabou.

### 330. vírgula

**Construção:** Vírgula é marca interna que separa ou delimita unidades segundo relações sintáticas e discursivas.

**Função:** Ajuda a organizar enumerações, deslocamentos, vocativos e explicações.

**Dependências:** pontuação, oração, relação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Maria, venha aqui.

**Não confundir com:** Não representa qualquer pausa da fala.

### 331. ponto e vírgula

**Construção:** Ponto e vírgula é marca intermediária entre vírgula e ponto final em certas organizações textuais.

**Função:** Separa unidades extensas ou itens complexos mantendo continuidade.

**Dependências:** pontuação, período, coesão

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** um item; outro item

**Não confundir com:** Não é vírgula forte universal.

### 332. dois-pontos

**Construção:** Dois-pontos é marca que anuncia explicação, enumeração, consequência apresentada ou fala citada.

**Função:** Cria relação prospectiva entre duas partes.

**Dependências:** pontuação, catáfora, relação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Só falta isto: testar.

**Não confundir com:** Não encerra necessariamente o período.

### 333. reticências

**Construção:** Reticências são três pontos que marcam suspensão, continuação aberta, hesitação ou omissão controlada.

**Função:** Representam incompletude discursiva sem obrigar uma única interpretação.

**Dependências:** pontuação, modalidade, contexto

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Eu pensei que...

**Não confundir com:** Não autorizam inventar o conteúdo omitido.

### 334. ponto de interrogação

**Construção:** Ponto de interrogação é marca terminal associada a enunciado interrogativo direto.

**Função:** Torna visível a modalidade interrogativa na escrita.

**Dependências:** pontuação, interrogação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Quem chegou?

**Não confundir com:** Não transforma pergunta indireta em direta.

### 335. ponto de exclamação

**Construção:** Ponto de exclamação é marca terminal associada a força expressiva ou injuntiva.

**Função:** Torna visível intensidade enunciativa na escrita.

**Dependências:** pontuação, exclamação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Cuidado!

**Não confundir com:** Não mede emoção objetivamente.

### 336. aspas

**Construção:** Aspas são marcas que delimitam citação, menção, palavra destacada ou uso distanciado.

**Função:** Separam voz, forma citada ou sentido especial do texto circundante.

**Dependências:** pontuação, citação, discurso direto

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Ele disse: “volto”.

**Não confundir com:** Não provam fidelidade da fonte.

### 337. parênteses

**Construção:** Parênteses delimitam informação encaixada ou comentário secundário.

**Função:** Permitem inserir explicação sem quebrar totalmente a estrutura principal.

**Dependências:** pontuação, texto, relação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** O teste (já aprovado) continua.

**Não confundir com:** Não tornam conteúdo irrelevante.

### 338. colchetes

**Construção:** Colchetes delimitam inserção editorial, informação dentro de parênteses ou ajuste em citação.

**Função:** Marcam intervenção ou segundo nível de encaixe.

**Dependências:** pontuação, citação, parênteses

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** [explicação adicionada]

**Não confundir com:** Não são parênteses equivalentes em todo uso.

### 339. travessão

**Construção:** Travessão é marca longa usada para fala, inciso, mudança de voz ou destaque estrutural.

**Função:** Organiza diálogo e encaixes com fronteira gráfica forte.

**Dependências:** pontuação, diálogo, discurso direto

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** — Vamos estudar.

**Não confundir com:** Não é hífen.

### 340. barra

**Construção:** Barra é marca usada para alternativa, separação técnica, verso ou abreviação em contextos definidos.

**Função:** Representa relação compacta entre formas.

**Dependências:** pontuação, relação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** e/ou

**Não confundir com:** Não substitui conectivo em todo texto.

### 341. artigo definido

**Construção:** Artigo definido apresenta referente como identificável ou recuperável no contexto.

**Função:** Ajuda a construir referência determinada.

**Dependências:** artigo, referência, contexto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** o livro

**Não confundir com:** Não garante que todos conheçam o referente.

### 342. artigo indefinido

**Construção:** Artigo indefinido introduz referente não identificado como único no contexto.

**Função:** Ajuda a apresentar entidade nova ou não especificada.

**Dependências:** artigo, referência, informação nova

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** um livro

**Não confundir com:** Não significa ausência total de referência.

### 343. numeral cardinal

**Construção:** Numeral cardinal expressa quantidade contável.

**Função:** Liga número matemático a forma linguística de quantidade.

**Dependências:** numeral, número gramatical

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** três livros

**Não confundir com:** Não é numeral ordinal.

### 344. numeral ordinal

**Construção:** Numeral ordinal expressa posição numa sequência.

**Função:** Liga ordem a forma linguística.

**Dependências:** numeral, relação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** terceiro capítulo

**Não confundir com:** Não expressa quantidade pura.

### 345. advérbio de tempo

**Construção:** Advérbio de tempo localiza ou relaciona ocorrência temporalmente.

**Função:** Modifica verbo, frase ou enunciado quanto ao tempo.

**Dependências:** advérbio, tempo verbal, contexto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** ontem

**Não confundir com:** Não é tempo verbal.

### 346. advérbio de lugar

**Construção:** Advérbio de lugar localiza ocorrência ou referente no espaço discursivo ou situacional.

**Função:** Contribui para dêixis espacial e circunstância.

**Dependências:** advérbio, contexto, dêixis

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** aqui

**Não confundir com:** Não é nome de lugar necessariamente.

### 347. advérbio de modo

**Construção:** Advérbio de modo caracteriza a maneira de uma ocorrência ou avaliação.

**Função:** Modifica processo, propriedade ou enunciado.

**Dependências:** advérbio, verbo, sentido

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** rapidamente

**Não confundir com:** Não é adjetivo em todo uso.

### 348. advérbio de intensidade

**Construção:** Advérbio de intensidade altera grau de propriedade, processo ou outro advérbio.

**Função:** Constrói escalas relativas.

**Dependências:** advérbio, adjetivo, relação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** muito claro

**Não confundir com:** Não exprime quantidade exata necessariamente.

### 349. advérbio de negação

**Construção:** Advérbio de negação marca cancelamento ou rejeição de conteúdo no seu escopo.

**Função:** Realiza negação em construções frequentes.

**Dependências:** advérbio, negação, relação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** não veio

**Não confundir com:** Não nega sempre a frase inteira.

### 350. advérbio de afirmação

**Construção:** Advérbio de afirmação reforça ou confirma conteúdo assumido pelo locutor.

**Função:** Marca posicionamento afirmativo.

**Dependências:** advérbio, afirmação, modalidade

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** sim, certamente

**Não confundir com:** Não prova verdade externa.

### 351. preposição simples

**Construção:** Preposição simples é preposição realizada por uma palavra.

**Função:** Introduz relações sintáticas e semânticas compactas.

**Dependências:** preposição, palavra

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** de, em, com

**Não confundir com:** Não é locução prepositiva.

### 352. locução prepositiva

**Construção:** Locução prepositiva é combinação de palavras que funciona como preposição.

**Função:** Introduz relação por unidade composta.

**Dependências:** locução, preposição, relação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** por causa de

**Não confundir com:** Não é qualquer sequência terminada em preposição.

### 353. conjunção coordenativa

**Construção:** Conjunção coordenativa liga unidades de nível sintático semelhante.

**Função:** Materializa relações de coordenação.

**Dependências:** conjunção, coordenação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** e, mas, ou

**Não confundir com:** Não cria dependência sintática subordinada.

### 354. conjunção subordinativa

**Construção:** Conjunção subordinativa introduz relação em que uma oração depende de outra.

**Função:** Materializa causa, condição, tempo e outras relações subordinadas.

**Dependências:** conjunção, subordinação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** porque, se, quando

**Não confundir com:** Não é pronome relativo.

### 355. verbo auxiliar

**Construção:** Verbo auxiliar participa de perífrase ou tempo composto e carrega parte de tempo, aspecto, modalidade ou voz.

**Função:** Distribui informação verbal entre mais de uma forma.

**Dependências:** verbo, perífrase verbal, conjugação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** tem estudado

**Não confundir com:** Não perde todo sentido em qualquer contexto.

### 356. verbo de ligação

**Construção:** Verbo de ligação conecta sujeito a predicativo em construção nominal.

**Função:** Organiza estado, qualidade ou identificação.

**Dependências:** verbo, predicado nominal, predicativo do sujeito

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** A casa é grande.

**Não confundir com:** Não é categoria fixa para todo uso do verbo.

### 357. verbo transitivo direto

**Construção:** Verbo transitivo direto seleciona objeto direto na construção analisada.

**Função:** Explica complemento sem preposição exigida.

**Dependências:** transitividade verbal, objeto direto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** ler o livro

**Não confundir com:** A transitividade depende do uso da forma.

### 358. verbo transitivo indireto

**Construção:** Verbo transitivo indireto seleciona objeto indireto na construção analisada.

**Função:** Explica complemento com preposição exigida.

**Dependências:** transitividade verbal, objeto indireto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** gostar de música

**Não confundir com:** Não é qualquer verbo seguido de preposição.

### 359. verbo transitivo direto e indireto

**Construção:** Verbo transitivo direto e indireto seleciona dois complementos de tipos diferentes na construção analisada.

**Função:** Representa transferência ou relação com objeto e destinatário.

**Dependências:** verbo transitivo direto, verbo transitivo indireto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** dar o livro ao aluno

**Não confundir com:** Não exige sempre ordem fixa.

### 360. verbo intransitivo

**Construção:** Verbo intransitivo forma predicação completa sem objeto exigido naquela construção.

**Função:** Distingue complemento necessário de adjunto opcional.

**Dependências:** transitividade verbal, predicado verbal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** A criança dormiu.

**Não confundir com:** Pode receber adjuntos.

### 361. pronome clítico

**Construção:** Pronome clítico é forma pronominal átona dependente de verbo ou hospedeiro sintático.

**Função:** Permite representar objetos e relações pronominais compactas.

**Dependências:** pronome pessoal, verbo, colocação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** vi-o; me disse

**Não confundir com:** Não é pronome tônico.

### 362. próclise

**Construção:** Próclise é colocação do pronome clítico antes do verbo.

**Função:** Representa uma posição possível condicionada pela construção e variedade.

**Dependências:** pronome clítico, colocação, verbo

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** não me diga

**Não confundir com:** Não é única posição correta em todo português.

### 363. ênclise

**Construção:** Ênclise é colocação do pronome clítico depois do verbo.

**Função:** Representa ligação pós-verbal em contextos definidos.

**Dependências:** pronome clítico, colocação, verbo

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** diga-me

**Não confundir com:** Não é hífen livre.

### 364. mesóclise

**Construção:** Mesóclise é colocação do pronome clítico dentro de forma verbal futura em registros específicos.

**Função:** Registra uma construção formal e limitada.

**Dependências:** pronome clítico, colocação, futuro

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** dir-lhe-ei

**Não confundir com:** Não é uso geral de todas as variedades.

### 365. infinitivo pessoal

**Construção:** Infinitivo pessoal é infinitivo com marca ou referência de pessoa em certas construções.

**Função:** Permite explicitar participante sem verbo finito completo.

**Dependências:** infinitivo, pessoa gramatical, conjugação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** para estudarmos

**Não confundir com:** Não é tempo verbal finito.

### 366. infinitivo impessoal

**Construção:** Infinitivo impessoal apresenta processo sem flexão pessoal explícita.

**Função:** Serve a formas de citação, perífrases e construções gerais.

**Dependências:** infinitivo, conjugação

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** estudar é importante

**Não confundir com:** Não implica ausência semântica de agente.

### 367. coordenação aditiva

**Construção:** Coordenação aditiva soma unidades ou conteúdos.

**Função:** Materializa relação de adição entre termos ou orações.

**Dependências:** oração coordenada, conjunção coordenativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** estudou e praticou

**Não confundir com:** Não garante equivalência entre as partes.

### 368. coordenação adversativa

**Construção:** Coordenação adversativa contrapõe conteúdos ou expectativas.

**Função:** Materializa contraste sem subordinação sintática.

**Dependências:** oração coordenada, conjunção coordenativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** estudou, mas errou

**Não confundir com:** Não é negação total da primeira parte.

### 369. coordenação alternativa

**Construção:** Coordenação alternativa apresenta escolha, alternância ou exclusão contextual.

**Função:** Organiza possibilidades coordenadas.

**Dependências:** oração coordenada, conjunção coordenativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** estuda ou trabalha

**Não confundir com:** O ou pode ser inclusivo ou exclusivo conforme contexto.

### 370. coordenação conclusiva

**Construção:** Coordenação conclusiva apresenta resultado inferido da unidade anterior.

**Função:** Marca conclusão discursiva coordenada.

**Dependências:** oração coordenada, inferência, conjunção coordenativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** estudou; portanto, passou

**Não confundir com:** Não prova validade da inferência.

### 371. coordenação explicativa

**Construção:** Coordenação explicativa acrescenta justificativa ou explicação à unidade anterior.

**Função:** Liga enunciados por razão apresentada.

**Dependências:** oração coordenada, conjunção coordenativa, argumento

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** saia, porque é tarde

**Não confundir com:** Não é sempre oração causal subordinada; a análise depende da construção.

### 372. subordinação causal

**Construção:** Subordinação causal apresenta causa proposta para outra ocorrência.

**Função:** Organiza relação causa–efeito no período.

**Dependências:** oração subordinada adverbial, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** ficou porque chovia

**Não confundir com:** A frase pode alegar causa sem prová-la.

### 373. subordinação condicional

**Construção:** Subordinação condicional estabelece condição para ocorrência ou conclusão.

**Função:** Constrói dependência hipotética.

**Dependências:** oração subordinada adverbial, modalidade, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** se estudar, aprenderá

**Não confundir com:** Não afirma que a condição ocorreu.

### 374. subordinação concessiva

**Construção:** Subordinação concessiva apresenta obstáculo que não impede a ocorrência principal.

**Função:** Organiza contraste com manutenção do resultado.

**Dependências:** oração subordinada adverbial, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** embora chovesse, saiu

**Não confundir com:** Não é coordenação adversativa.

### 375. subordinação temporal

**Construção:** Subordinação temporal localiza uma ocorrência em relação temporal a outra.

**Função:** Organiza simultaneidade, anterioridade ou posterioridade.

**Dependências:** oração subordinada adverbial, tempo verbal, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** quando chegou, sentou

**Não confundir com:** Não determina tempo cronológico sem contexto.

### 376. subordinação final

**Construção:** Subordinação final apresenta objetivo ou finalidade.

**Função:** Liga ação a propósito declarado.

**Dependências:** oração subordinada adverbial, intenção comunicativa, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** estuda para aprender

**Não confundir com:** Finalidade não garante resultado.

### 377. subordinação consecutiva

**Construção:** Subordinação consecutiva apresenta consequência relacionada a grau ou causa expressa.

**Função:** Organiza resultado discursivo dependente.

**Dependências:** oração subordinada adverbial, relação, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** falou tanto que cansou

**Não confundir com:** Não é coordenação conclusiva.

### 378. subordinação comparativa

**Construção:** Subordinação comparativa relaciona duas construções por semelhança, diferença ou escala.

**Função:** Permite comparar processos e propriedades.

**Dependências:** oração subordinada adverbial, relação, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** corre como o irmão corre

**Não confundir com:** Não é metáfora necessariamente.

### 379. subordinação conformativa

**Construção:** Subordinação conformativa apresenta acordo com regra, fala ou modo de referência.

**Função:** Relaciona ocorrência a um modelo declarado.

**Dependências:** oração subordinada adverbial, relação, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** fez conforme combinámos

**Não confundir com:** Não prova correção do modelo.

### 380. subordinação proporcional

**Construção:** Subordinação proporcional relaciona variação de duas grandezas ou processos.

**Função:** Constrói crescimento ou diminuição correlacionados.

**Dependências:** oração subordinada adverbial, relação, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** quanto mais estuda, mais aprende

**Não confundir com:** Não é proporcionalidade matemática exata necessariamente.

### 381. oração completiva

**Construção:** Oração completiva preenche posição exigida por verbo, nome ou adjetivo.

**Função:** Generaliza subordinadas que completam sentido de um núcleo.

**Dependências:** oração subordinada, complemento, regência

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** sei que ele veio

**Não confundir com:** Não é adjunto livre.

### 382. oração relativa

**Construção:** Oração relativa modifica ou identifica referente por elemento relativo.

**Função:** Constrói descrição dependente ligada a antecedente.

**Dependências:** oração subordinada adjetiva, pronome relativo, referente

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** o livro que li

**Não confundir com:** Não é oração completiva.

### 383. oração relativa restritiva

**Construção:** Oração relativa restritiva limita o conjunto de referentes sem isolamento explicativo.

**Função:** Seleciona subconjunto relevante.

**Dependências:** oração relativa, referência

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** os alunos que estudaram passaram

**Não confundir com:** Não é comentário parentético.

### 384. oração relativa explicativa

**Construção:** Oração relativa explicativa acrescenta informação sobre referente já identificado.

**Função:** Insere comentário descritivo normalmente delimitado por pontuação.

**Dependências:** oração relativa, pontuação, referência

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** os alunos, que estudaram, passaram

**Não confundir com:** Não restringe necessariamente o conjunto.

### 385. transformação de discurso

**Construção:** Transformação de discurso reconstrói fala direta ou indireta ajustando pessoa, tempo, dêixis e pontuação.

**Função:** Permite preservar relações essenciais ao mudar a forma de apresentação da voz.

**Dependências:** discurso direto, discurso indireto, dêixis, conjugação

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** “Vou” → disse que iria

**Não confundir com:** Não é substituição mecânica universal.

### 386. sequência de tempos

**Construção:** Sequência de tempos é relação entre tempos verbais de orações conectadas.

**Função:** Ajuda a manter coerência temporal em relato e subordinação.

**Dependências:** tempo verbal, oração subordinada, contexto

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** disse que viria

**Não confundir com:** Não é regra única para todas as variedades.

### 387. agente semântico

**Construção:** Agente semântico é participante concebido como iniciador ou controlador de uma ocorrência.

**Função:** Separa papel de sentido da função sintática de sujeito.

**Dependências:** referente, verbo, sentido

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** O aluno abriu a porta.

**Não confundir com:** Nem todo sujeito é agente.

### 388. paciente semântico

**Construção:** Paciente semântico é participante afetado ou transformado pela ocorrência.

**Função:** Ajuda a interpretar objetos e sujeitos passivos.

**Dependências:** referente, verbo, sentido

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** a porta em abriu a porta

**Não confundir com:** Não é função sintática fixa.

### 389. experienciador

**Construção:** Experienciador é participante que sente, percebe ou vivencia estado.

**Função:** Explica verbos de percepção, emoção e cognição.

**Dependências:** referente, verbo, sentido

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Ana gosta de música.

**Não confundir com:** Não é agente controlador necessariamente.

### 390. instrumento semântico

**Construção:** Instrumento semântico é entidade usada para realizar uma ocorrência.

**Função:** Representa meio participante do processo.

**Dependências:** referente, verbo, relação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** cortou com a faca

**Não confundir com:** Não é adjunto adverbial como conceito de sentido.

### 391. beneficiário

**Construção:** Beneficiário é participante em favor ou prejuízo de quem algo ocorre.

**Função:** Explica destinatários e interesses na predicação.

**Dependências:** referente, verbo, relação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** fez o trabalho para Ana

**Não confundir com:** Não é objeto indireto em todo caso.

### 392. origem semântica

**Construção:** Origem semântica é ponto de partida espacial, temporal ou abstrato de uma relação.

**Função:** Organiza movimentos e transferências.

**Dependências:** referência, relação, contexto

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** veio de Maputo

**Não confundir com:** Não é causa necessariamente.

### 393. destino semântico

**Construção:** Destino semântico é ponto de chegada ou orientação de uma relação.

**Função:** Organiza movimento, transferência e finalidade espacial.

**Dependências:** referência, relação, contexto

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** foi para casa

**Não confundir com:** Não é beneficiário automaticamente.

### 394. localização semântica

**Construção:** Localização semântica situa entidade ou ocorrência num espaço real, textual ou conceptual.

**Função:** Constrói relações de lugar.

**Dependências:** referência, contexto, dêixis

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** está na sala

**Não confundir com:** Não é advérbio de lugar como classe.

### 395. comparação figurada

**Construção:** Comparação figurada aproxima domínios por marca explícita de semelhança.

**Função:** Cria imagem mantendo sinal de comparação.

**Dependências:** conotação, relação, metáfora

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** forte como pedra

**Não confundir com:** Não é metáfora sem marcador.

### 396. personificação

**Construção:** Personificação atribui traço humano a entidade não humana ou abstrata.

**Função:** Produz efeito figurado por transferência de propriedades.

**Dependências:** conotação, metáfora, referente

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** o vento cantou

**Não confundir com:** Não é descrição literal.

### 397. hipérbole

**Construção:** Hipérbole amplia ou reduz excessivamente uma ideia para efeito expressivo.

**Função:** Marca intensidade figurada.

**Dependências:** conotação, contexto, modalidade

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** esperei uma eternidade

**Não confundir com:** Não deve ser lida como medida exata.

### 398. eufemismo

**Construção:** Eufemismo substitui expressão direta por formulação percebida como menos dura.

**Função:** Gere impacto social e afetivo do enunciado.

**Dependências:** pragmática, cortesia, conotação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** partiu em vez de morreu

**Não confundir com:** Não apaga o referente.

### 399. antítese

**Construção:** Antítese aproxima ideias opostas para produzir contraste.

**Função:** Torna oposição visível na estrutura textual.

**Dependências:** antonímia, conotação, relação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** amor e ódio

**Não confundir com:** Não é contradição lógica obrigatória.

### 400. paradoxo

**Construção:** Paradoxo reúne formulações aparentemente incompatíveis que exigem nova interpretação.

**Função:** Produz tensão conceptual ou expressiva.

**Dependências:** antítese, ambiguidade, interpretação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** é ferida que dói e não se sente

**Não confundir com:** Não deve ser aceito como verdade sem reconstrução.

### 401. ato de fala

**Construção:** Ato de fala é uma ação realizada por meio de um enunciado em uma situação comunicativa.

**Função:** Permite distinguir informar, pedir, prometer, agradecer e declarar sem reduzir linguagem a forma gramatical.

**Dependências:** enunciado, intenção comunicativa, modalidade, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Feche a porta, por favor. | Prometo voltar.

**Não confundir com:** Não é apenas tipo de frase.

### 402. meronímia

**Construção:** Meronímia é relação de sentido em que uma unidade é parte constitutiva de outra.

**Função:** Organiza relações parte–todo no léxico e no texto.

**Dependências:** sentido, relação, campo semântico

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** roda é parte de carro

**Não confundir com:** Não é hiponímia: parte não é espécie.

### 403. holonímia

**Construção:** Holonímia é a relação inversa da meronímia: uma unidade nomeia o todo que contém outra como parte.

**Função:** Permite reconstruir relações todo–parte sem confundir classificação com composição.

**Dependências:** meronímia, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** carro é todo em relação a roda

**Não confundir com:** Não é hiperonímia.

### 404. intertextualidade

**Construção:** Intertextualidade é relação em que um texto retoma, cita, transforma, responde ou alude a outro texto.

**Função:** Ajuda a identificar memória textual e dependência entre discursos.

**Dependências:** texto, referência, citação, paráfrase

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma paródia retoma outro texto

**Não confundir com:** Não exige sempre citação explícita.

### 405. multimodalidade

**Construção:** Multimodalidade é construção de sentido pela combinação de palavra, imagem, som, gesto, espaço ou disposição gráfica.

**Função:** Impede tratar toda comunicação como texto verbal isolado.

**Dependências:** texto, gênero textual, contexto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** cartaz com palavras e imagem

**Não confundir com:** Não é apenas decoração visual.

### 406. aquisição da linguagem

**Construção:** Aquisição da linguagem é o processo pelo qual uma pessoa constrói capacidade de compreender e produzir língua por exposição, interação e reorganização interna.

**Função:** Distingue conhecimento linguístico construído de lista de regras memorizadas.

**Dependências:** uso, competência linguística, competência comunicativa

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** criança amplia formas e sentidos pelo uso

**Não confundir com:** Não é simples cópia de frases.

### 407. bilinguismo

**Construção:** Bilinguismo é uso funcional de duas línguas por uma pessoa ou comunidade, com domínio que pode variar por tarefa e contexto.

**Função:** Permite compreender contacto linguístico sem exigir equilíbrio perfeito entre línguas.

**Dependências:** aquisição da linguagem, variação linguística, competência comunicativa

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** uma língua em casa e outra no trabalho

**Não confundir com:** Não significa domínio idêntico em todas as áreas.

### 408. tradução

**Construção:** Tradução é reconstrução controlada de sentido e função de um texto em outra língua.

**Função:** Distingue equivalência comunicativa de substituição mecânica palavra por palavra.

**Dependências:** texto, sentido, contexto, interpretação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** reformular uma instrução noutra língua

**Não confundir com:** Não é cópia literal obrigatória.

### 409. sociolinguística

**Construção:** Sociolinguística é investigação das relações entre língua, comunidade, situação, identidade social e mudança.

**Função:** Integra variação regional, social, histórica e situacional sem transformar uma variedade em erro absoluto.

**Dependências:** variação regional, variação social, variação histórica, variação situacional, registro

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** formas diferentes em comunidades diferentes

**Não confundir com:** Não é licença para ignorar adequação ao contexto.

### 410. psicolinguística

**Construção:** Psicolinguística é investigação de processos humanos de compreensão, produção, memória e aquisição da linguagem.

**Função:** Liga estrutura linguística a processamento humano sem confundir modelo do motor com mente humana.

**Dependências:** aquisição da linguagem, compreensão literal, compreensão inferencial, fala, escuta

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** reconhecer uma palavra durante a escuta

**Não confundir com:** O motor não é modelo completo da mente.

### 411. arcaísmo

**Construção:** Arcaísmo é forma, sentido ou construção associada a estado anterior da língua e pouco corrente em determinado uso atual.

**Função:** Ajuda a interpretar textos antigos sem classificar automaticamente a forma como erro.

**Dependências:** palavra, variação histórica, uso

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** forma antiga preservada em texto histórico

**Não confundir com:** Antigo não significa necessariamente incorreto.

### 412. vogal oral

**Construção:** Vogal oral é vogal cuja corrente de ar se organiza principalmente pela cavidade oral.

**Função:** Distingue realização oral de realização nasal.

**Dependências:** vogal, oralidade, fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a em casa

**Não confundir com:** Não é sinónimo de vogal aberta.

### 413. vogal nasal

**Construção:** Vogal nasal é vogal produzida com participação funcional da cavidade nasal.

**Função:** Explica contraste de nasalidade em sílabas e palavras.

**Dependências:** vogal, nasalidade, fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** ã em lã

**Não confundir com:** Não é apenas vogal seguida da letra n.

### 414. vogal aberta

**Construção:** Vogal aberta é vogal realizada com maior abertura relativa do trato oral.

**Função:** Ajuda a distinguir timbres vocálicos.

**Dependências:** vogal, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** é em pé

**Não confundir com:** Não é o mesmo que sílaba tônica.

### 415. vogal fechada

**Construção:** Vogal fechada é vogal realizada com menor abertura relativa do trato oral.

**Função:** Contrasta timbres e apoia relações entre fala e acento gráfico.

**Dependências:** vogal aberta, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** ê em você

**Não confundir com:** Não significa ausência de som.

### 416. vogal tônica

**Construção:** Vogal tônica é vogal situada no núcleo da sílaba que recebe maior proeminência na palavra.

**Função:** Liga qualidade vocálica a tonicidade.

**Dependências:** vogal, sílaba tônica, núcleo silábico

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a de casa

**Não confundir com:** Não é necessariamente acentuada graficamente.

### 417. vogal átona

**Construção:** Vogal átona é vogal situada em sílaba sem a proeminência principal da palavra.

**Função:** Permite observar redução e variação de realização.

**Dependências:** vogal tônica, tonicidade

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a final de casa

**Não confundir com:** Não é vogal sem som.

### 418. consoante surda

**Construção:** Consoante surda é consoante produzida sem vibração laríngea funcional durante o segmento.

**Função:** Distingue pares por vozeamento.

**Dependências:** consoante, vozeamento, fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** p em pato

**Não confundir com:** Não significa ausência de corrente de ar.

### 419. consoante sonora

**Construção:** Consoante sonora é consoante produzida com vibração laríngea funcional durante o segmento.

**Função:** Contrasta com consoante surda.

**Dependências:** consoante surda, vozeamento

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** b em bato

**Não confundir com:** Não significa maior volume.

### 420. bilabial

**Construção:** Bilabial é articulação produzida com participação dos dois lábios.

**Função:** Classifica consoantes por ponto de articulação.

**Dependências:** ponto de articulação, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** p, b, m

**Não confundir com:** Não é modo de articulação.

### 421. labiodental

**Construção:** Labiodental é articulação produzida entre lábio inferior e dentes superiores.

**Função:** Classifica parte das fricativas.

**Dependências:** ponto de articulação, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** f, v

**Não confundir com:** Não é dental.

### 422. dental

**Construção:** Dental é articulação produzida com aproximação ou contacto da língua junto aos dentes.

**Função:** Permite localizar realizações consonantais.

**Dependências:** ponto de articulação, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer dental numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** A realização concreta pode ser alveolar em certas variedades.

### 423. alveolar

**Construção:** Alveolar é articulação produzida junto à região alveolar atrás dos dentes superiores.

**Função:** Classifica consoantes por localização articulatória.

**Dependências:** dental, ponto de articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** s em muitas variedades

**Não confundir com:** Não é uma letra específica.

### 424. palatal

**Construção:** Palatal é articulação produzida pela aproximação da língua ao palato duro.

**Função:** Ajuda a classificar sons como os associados a nh e lh em muitas descrições.

**Dependências:** ponto de articulação, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** nh, lh

**Não confundir com:** Grafia e realização não são idênticas.

### 425. velar

**Construção:** Velar é articulação produzida pela aproximação da parte posterior da língua ao véu palatino.

**Função:** Classifica sons posteriores.

**Dependências:** ponto de articulação, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** k em casa

**Não confundir com:** Não é sinónimo de palatal.

### 426. glotal

**Construção:** Glotal é articulação localizada na glote.

**Função:** Permite descrever realizações laríngeas quando ocorrerem.

**Dependências:** ponto de articulação, aparelho fonador

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer glotal numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não corresponde obrigatoriamente a uma letra.

### 427. assimilação fonológica

**Construção:** Assimilação fonológica é processo em que um segmento se torna mais semelhante a outro próximo.

**Função:** Explica ajustes de fala sem tratá-los automaticamente como erro.

**Dependências:** fonema, relação, contexto

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** um som adapta vozeamento ao vizinho

**Não confundir com:** Não é mudança ortográfica obrigatória.

### 428. elisão

**Construção:** Elisão é ausência de realização de segmento previsível em determinado contexto de fala.

**Função:** Ajuda a analisar redução sem confundir fala fluida com escrita incompleta.

**Dependências:** fonema, contexto, fala

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer elisão numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é apagamento arbitrário.

### 429. epêntese

**Construção:** Epêntese é inserção de segmento para facilitar ou reorganizar uma sequência sonora.

**Função:** Explica formas de adaptação fonológica.

**Dependências:** fonema, sílaba, articulação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer epêntese numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é acréscimo ortográfico obrigatório.

### 430. metátese

**Construção:** Metátese é mudança de ordem entre segmentos numa realização ou evolução de palavra.

**Função:** Permite distinguir reordenação sonora de simples troca de letras.

**Dependências:** fonema, ordem alfabética, variação histórica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer metátese numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é regra geral de pronúncia.

### 431. redução vocálica

**Construção:** Redução vocálica é diminuição de contraste ou alteração de qualidade em vogal átona.

**Função:** Liga tonicidade a variação de fala.

**Dependências:** vogal átona, tonicidade, fala

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer redução vocálica numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não significa desaparecimento necessário da vogal.

### 432. encadeamento fônico

**Construção:** Encadeamento fônico é ligação de unidades sonoras através de fronteiras de palavra na fala contínua.

**Função:** Explica por que a fala não respeita sempre espaços gráficos como cortes absolutos.

**Dependências:** fala, espaço, sílaba, ritmo

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Aplicação mínima: reconhecer encadeamento fônico numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não apaga a separação lexical na escrita.

### 433. regra de oxítona

**Construção:** Regra de oxítona é família de decisões de acentuação aplicada a palavras cuja última sílaba é tônica.

**Função:** Liga classificação tônica a marca gráfica.

**Dependências:** oxítona, acentuação gráfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** café, avó

**Não confundir com:** Nem toda oxítona recebe acento.

### 434. regra de paroxítona

**Construção:** Regra de paroxítona é família de decisões de acentuação aplicada a palavras cuja penúltima sílaba é tônica.

**Função:** Organiza a maior família tônica sem assumir que todas recebem acento.

**Dependências:** paroxítona, acentuação gráfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** fácil, táxi

**Não confundir com:** Paroxítona não significa palavra sem acento.

### 435. regra de proparoxítona

**Construção:** Regra de proparoxítona estabelece que palavras proparoxítonas recebem marca gráfica de tonicidade.

**Função:** Fecha uma família regular de acentuação.

**Dependências:** proparoxítona, acentuação gráfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** música, lâmpada

**Não confundir com:** A divisão silábica precisa estar correta.

### 436. regra de monossílabo tônico

**Construção:** Regra de monossílabo tônico organiza quando uma palavra de uma sílaba recebe acento gráfico.

**Função:** Liga tonicidade, terminação e marca gráfica.

**Dependências:** monossílabo tônico, acentuação gráfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** pá, pé, só

**Não confundir com:** Nem todo monossílabo tônico recebe acento.

### 437. acento em hiato

**Construção:** Acento em hiato é marca usada em certas vogais tônicas que formam sílaba própria após outra vogal.

**Função:** Relaciona hiato, tonicidade e ortografia.

**Dependências:** hiato, sílaba tônica, acentuação gráfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** saída, baú

**Não confundir com:** Nem todo hiato recebe acento.

### 438. acento diferencial

**Construção:** Acento diferencial distingue graficamente certas formas que seriam iguais na escrita.

**Função:** Evita ambiguidade em um conjunto restrito de palavras.

**Dependências:** acento, ambiguidade, forma lexical

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** pôde/pode, pôr/por

**Não confundir com:** Não é regra produtiva para qualquer homógrafo.

### 439. uso de s

**Construção:** Uso de s é família ortográfica que relaciona o grafema s a posições, morfemas e famílias lexicais.

**Função:** Permite construir regularidades sem adivinhar cada palavra isoladamente.

**Dependências:** ortografia, grafema, família ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa, análise

**Não confundir com:** O mesmo som pode ter outras grafias.

### 440. uso de ss

**Construção:** Uso de ss é família ortográfica em que duas letras s representam um valor consonantal entre vogais.

**Função:** Distingue padrão gráfico interno de palavra.

**Dependências:** uso de s, dígrafo

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** massa, possível

**Não confundir com:** ss não inicia palavra portuguesa comum.

### 441. uso de c

**Construção:** Uso de c é família ortográfica ligada a valores consonantais diferentes conforme o grafema seguinte e a família lexical.

**Função:** Ajuda a reconstruir alternâncias como c/qu e c/ç.

**Dependências:** ortografia, grafema, família ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa, cedo

**Não confundir com:** Uma letra pode representar mais de um som.

### 442. uso de ç

**Construção:** Uso de ç é família ortográfica em que c com cedilha representa valor consonantal antes de a, o ou u.

**Função:** Relaciona cedilha a ambiente gráfico.

**Dependências:** cedilha, uso de c

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** ação, açúcar

**Não confundir com:** ç não aparece antes de e ou i no padrão ortográfico.

### 443. uso de z

**Construção:** Uso de z é família ortográfica ligada a raízes, sufixos e posições específicas.

**Função:** Ajuda a diferenciar z de s com valor sonoro semelhante.

**Dependências:** ortografia, grafema, sufixo

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** beleza, feliz

**Não confundir com:** Som semelhante não garante mesma grafia.

### 444. uso de x

**Construção:** Uso de x é família ortográfica de múltiplos valores sonoros e origens lexicais.

**Função:** Marca uma área em que escrita depende de família e história da palavra.

**Dependências:** ortografia, grafema, família lexical

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** texto, exame, xícara

**Não confundir com:** x não tem um único valor sonoro.

### 445. uso de ch

**Construção:** Uso de ch é família ortográfica em que c e h formam dígrafo.

**Função:** Distingue ch de x em palavras de som aproximado.

**Dependências:** dígrafo, ortografia, família lexical

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** chave, chuva

**Não confundir com:** Som semelhante não permite escolher grafia sem base lexical.

### 446. uso de g

**Construção:** Uso de g é família ortográfica em que o grafema varia de valor conforme vogal seguinte e composição gráfica.

**Função:** Relaciona g, gu e famílias lexicais.

**Dependências:** ortografia, grafema, família ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** gato, gelo

**Não confundir com:** g não representa sempre o mesmo fonema.

### 447. uso de j

**Construção:** Uso de j é família ortográfica de palavras e formações em que o grafema representa valor consonantal específico.

**Função:** Distingue j de g antes de e e i.

**Dependências:** ortografia, grafema, família lexical

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** janela, jeito

**Não confundir com:** Som semelhante não basta para escolher j ou g.

### 448. uso de qu

**Construção:** Uso de qu é combinação gráfica que conserva valor consonantal de q diante de e ou i e pode incluir ou não realização de u conforme a palavra.

**Função:** Relaciona dígrafo, vogal e ortografia.

**Dependências:** dígrafo, uso de c, ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** que, quinto

**Não confundir com:** A letra u pode não ter realização própria.

### 449. uso de gu

**Construção:** Uso de gu é combinação gráfica que conserva valor consonantal de g diante de e ou i e pode incluir ou não realização de u.

**Função:** Relaciona g, dígrafo e ambiente gráfico.

**Dependências:** dígrafo, uso de g, ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** guerra, guitarra

**Não confundir com:** A letra u pode não ter realização própria.

### 450. maiúscula inicial

**Construção:** Maiúscula inicial é uso de letra maiúscula no início de período e em certas unidades nominais convencionadas.

**Função:** Liga estrutura textual e distinção gráfica.

**Dependências:** maiúscula, período, substantivo próprio

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Maputo; A língua cresce.

**Não confundir com:** Maiúscula não significa maior importância sem regra.

### 451. abreviatura

**Construção:** Abreviatura é redução gráfica convencional de palavra ou expressão, geralmente conservando marcas de corte.

**Função:** Distingue abreviatura, sigla e acrônimo.

**Dependências:** palavra, marca, sigla, acrônimo

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** pág. para página

**Não confundir com:** Não é qualquer corte informal.

### 452. translineação

**Construção:** Translineação é divisão gráfica de palavra na mudança de linha segundo sua estrutura silábica e ortográfica.

**Função:** Aplica separação silábica à disposição do texto.

**Dependências:** separação silábica, hífen, escrita

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Aplicação mínima: reconhecer translineação numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é divisão morfológica livre.

### 453. plural regular

**Construção:** Plural regular é flexão de número formada por padrão produtivo sem alteração imprevisível do radical.

**Função:** Fornece base antes dos plurais especiais.

**Dependências:** número gramatical, flexão, nome

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa/casas

**Não confundir com:** Regularidade não elimina ajustes ortográficos.

### 454. plural em -ão

**Construção:** Plural em -ão é família de flexão de nomes terminados em -ão, com resultados que podem ocorrer em -ões, -ães ou -ãos.

**Função:** Marca uma família que exige organização lexical e morfológica.

**Dependências:** plural regular, forma lexical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** nação/nações; pão/pães; mão/mãos

**Não confundir com:** Não há uma única terminação para todas as palavras.

### 455. plural de palavra em -m

**Construção:** Plural de palavra terminada em -m substitui m final por ns no padrão produtivo.

**Função:** Materializa uma regra ortográfico-morfológica estável.

**Dependências:** plural regular, grafema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** homem/homens; viagem/viagens

**Não confundir com:** Aplica-se a palavras terminadas em m, não a qualquer ocorrência interna.

### 456. plural de palavra em -l

**Construção:** Plural de palavra terminada em -l reorganiza a terminação conforme o tipo de final da palavra.

**Função:** Marca família produtiva que envolve alteração gráfica.

**Dependências:** plural regular, sílaba tônica

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** animal/animais; papel/papéis

**Não confundir com:** A tonicidade e a terminação influenciam o resultado.

### 457. feminino regular

**Construção:** Feminino regular é flexão de gênero formada por padrão produtivo, frequentemente com alternância final.

**Função:** Fornece base antes de formas comuns, sobrecomuns e epicenas.

**Dependências:** gênero, flexão, nome

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** menino/menina

**Não confundir com:** Gênero gramatical não é identidade humana total.

### 458. substantivo comum de dois

**Construção:** Substantivo comum de dois conserva uma forma e distingue referência de gênero por determinante ou contexto.

**Função:** Explica concordância sem inventar duas formas lexicais.

**Dependências:** substantivo comum, gênero, determinante

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o estudante/a estudante

**Não confundir com:** Não é substantivo sobrecomum.

### 459. substantivo sobrecomum

**Construção:** Substantivo sobrecomum mantém um único gênero gramatical para referências humanas de sexos diferentes.

**Função:** Distingue gênero da palavra e características do referente.

**Dependências:** substantivo comum, gênero, referente

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** a criança

**Não confundir com:** Não alterna artigo apenas para indicar sexo.

### 460. substantivo epiceno

**Construção:** Substantivo epiceno designa animal com um gênero gramatical estável, podendo usar macho ou fêmea para especificar sexo.

**Função:** Materializa uma relação entre gênero lexical e referente biológico.

**Dependências:** substantivo comum, gênero, referente

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** a cobra macho/a cobra fêmea

**Não confundir com:** Não é substantivo comum de dois.

### 461. grau aumentativo

**Construção:** Grau aumentativo expressa aumento, intensidade ou avaliação por morfema ou construção sintática.

**Função:** Mostra que grau pode ser morfológico ou analítico.

**Dependências:** nome, adjetivo, sufixo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa grande/casarão

**Não confundir com:** Nem todo aumentativo é apenas tamanho.

### 462. grau diminutivo

**Construção:** Grau diminutivo expressa diminuição, aproximação ou avaliação afetiva por morfema ou construção.

**Função:** Liga forma, sentido e contexto.

**Dependências:** nome, adjetivo, sufixo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa pequena/casinha

**Não confundir com:** Nem todo diminutivo indica tamanho real.

### 463. grau comparativo

**Construção:** Grau comparativo relaciona duas referências quanto a uma propriedade.

**Função:** Organiza igualdade, superioridade e inferioridade.

**Dependências:** adjetivo, relação, comparação figurada

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mais claro que; tão claro como

**Não confundir com:** Comparação gramatical não é necessariamente figura.

### 464. grau superlativo

**Construção:** Grau superlativo apresenta uma propriedade em intensidade elevada ou máxima dentro de um conjunto.

**Função:** Distingue intensificação absoluta de relação comparativa.

**Dependências:** adjetivo, grau comparativo, advérbio de intensidade

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** muito claro; claríssimo

**Não confundir com:** Superlativo não prova avaliação objetiva.

### 465. pretérito perfeito

**Construção:** Pretérito perfeito apresenta ocorrência passada como delimitada ou concluída em relação ao ponto de referência.

**Função:** Distingue fechamento de desenvolvimento passado.

**Dependências:** passado, aspecto verbal, indicativo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudei ontem

**Não confundir com:** O valor pode mudar conforme contexto e variedade.

### 466. pretérito imperfeito

**Construção:** Pretérito imperfeito apresenta ocorrência passada em desenvolvimento, habitual ou não delimitada.

**Função:** Contrasta com pretérito perfeito.

**Dependências:** pretérito perfeito, aspecto verbal, indicativo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudava todos os dias

**Não confundir com:** Não significa ação necessariamente incompleta no mundo.

### 467. pretérito mais-que-perfeito

**Construção:** Pretérito mais-que-perfeito situa ocorrência antes de outra referência já passada.

**Função:** Constrói anterioridade dentro do passado.

**Dependências:** pretérito perfeito, sequência de tempos

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** quando cheguei, ele já partira

**Não confundir com:** A forma simples e a composta diferem em frequência e registro.

### 468. futuro do presente

**Construção:** Futuro do presente situa ocorrência posterior ao ponto de fala ou expressa valor modal associado.

**Função:** Liga tempo e modalidade.

**Dependências:** futuro, indicativo, modalidade

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudarei amanhã

**Não confundir com:** Forma futura pode expressar hipótese ou ordem em contexto.

### 469. futuro do pretérito

**Construção:** Futuro do pretérito situa ocorrência posterior a referência passada ou apresenta condição, hipótese e cortesia.

**Função:** Liga sequência temporal a modalidade.

**Dependências:** passado, futuro, modalidade, sequência de tempos

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** disse que estudaria

**Não confundir com:** Também é chamado condicional em certas descrições.

### 470. presente do conjuntivo

**Construção:** Presente do conjuntivo organiza ocorrência não afirmada como facto pleno, frequentemente ligada a desejo, dúvida, avaliação ou dependência.

**Função:** Materializa uma forma do modo conjuntivo.

**Dependências:** conjuntivo, presente, subordinação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** espero que estude

**Não confundir com:** O gatilho não é apenas tempo cronológico.

### 471. pretérito imperfeito do conjuntivo

**Construção:** Pretérito imperfeito do conjuntivo organiza hipótese, condição ou dependência em relação passada ou não realizada.

**Função:** Apoia construções condicionais e subordinadas.

**Dependências:** conjuntivo, passado, subordinação condicional

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** se estudasse, aprenderia

**Não confundir com:** Não equivale ao pretérito imperfeito do indicativo.

### 472. futuro do conjuntivo

**Construção:** Futuro do conjuntivo apresenta condição ou eventualidade futura dependente de outra construção.

**Função:** Materializa relação entre futuro e subordinação.

**Dependências:** conjuntivo, futuro, subordinação temporal, subordinação condicional

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** quando estudar, compreenderá

**Não confundir com:** Não é o futuro do indicativo.

### 473. oração principal

**Construção:** Oração principal é oração que serve de base sintática ou discursiva para uma oração subordinada.

**Função:** Permite localizar dependência sem afirmar independência absoluta de sentido.

**Dependências:** oração, subordinação, período composto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Espero que venhas: espero é a oração principal.

**Não confundir com:** Principal não significa sempre mais importante no conteúdo.

### 474. oração reduzida

**Construção:** Oração reduzida é oração dependente construída com forma nominal do verbo e sem conectivo finito explícito típico.

**Função:** Reúne formas reduzidas de infinitivo, gerúndio e particípio.

**Dependências:** oração subordinada, infinitivo, gerúndio, particípio

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ao chegar, telefonou.

**Não confundir com:** Reduzida não significa incompleta.

### 475. oração reduzida de infinitivo

**Construção:** Oração reduzida de infinitivo tem verbo no infinitivo e função subordinada no período.

**Função:** Permite analisar dependência sem verbo finito.

**Dependências:** oração reduzida, infinitivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** É necessário estudar.

**Não confundir com:** Nem todo infinitivo forma oração autônoma.

### 476. oração reduzida de gerúndio

**Construção:** Oração reduzida de gerúndio tem verbo no gerúndio e expressa relação circunstancial ou descritiva.

**Função:** Liga forma verbal a função subordinada.

**Dependências:** oração reduzida, gerúndio

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudando, aprenderás.

**Não confundir com:** A relação semântica precisa do contexto.

### 477. oração reduzida de particípio

**Construção:** Oração reduzida de particípio tem verbo no particípio e expressa estado resultante ou relação circunstancial.

**Função:** Materializa uma forma de redução oracional.

**Dependências:** oração reduzida, particípio

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Terminada a tarefa, saiu.

**Não confundir com:** Nem todo particípio constitui oração.

### 478. oração subordinada substantiva subjetiva

**Construção:** Oração subordinada substantiva subjetiva ocupa função de sujeito em relação à oração principal.

**Função:** Liga oração a função nominal de sujeito.

**Dependências:** oração subordinada substantiva, sujeito, oração principal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** É necessário que estudes.

**Não confundir com:** Não é oração adjetiva.

### 479. oração subordinada substantiva objetiva direta

**Construção:** Oração subordinada substantiva objetiva direta ocupa função de objeto direto de um verbo da oração principal.

**Função:** Aplica transitividade direta a uma oração inteira.

**Dependências:** oração subordinada substantiva, objeto direto, oração principal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Desejo que venhas.

**Não confundir com:** Não exige preposição regida.

### 480. oração subordinada substantiva objetiva indireta

**Construção:** Oração subordinada substantiva objetiva indireta ocupa função de objeto indireto exigido por verbo da oração principal.

**Função:** Aplica regência verbal a uma oração inteira.

**Dependências:** oração subordinada substantiva, objeto indireto, oração principal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Lembro-me de que chegaste.

**Não confundir com:** A preposição depende da regência.

### 481. oração subordinada substantiva completiva nominal

**Construção:** Oração subordinada substantiva completiva nominal completa sentido de um nome, adjetivo ou advérbio da oração principal.

**Função:** Aplica complemento nominal a uma oração.

**Dependências:** oração subordinada substantiva, complemento nominal, oração principal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Tenho certeza de que virá.

**Não confundir com:** Não completa diretamente um verbo.

### 482. oração subordinada substantiva predicativa

**Construção:** Oração subordinada substantiva predicativa ocupa função de predicativo em construção com verbo de ligação.

**Função:** Liga oração a predicado nominal.

**Dependências:** oração subordinada substantiva, predicativo do sujeito, verbo de ligação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A verdade é que estudou.

**Não confundir com:** Não é oração subjetiva.

### 483. oração subordinada substantiva apositiva

**Construção:** Oração subordinada substantiva apositiva explica ou desenvolve um termo anterior como aposto.

**Função:** Liga oração a função explicativa nominal.

**Dependências:** oração subordinada substantiva, aposto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Só desejo isto: que estudes.

**Não confundir com:** Não é simples citação.

### 484. adjunto adverbial de tempo

**Construção:** Adjunto adverbial de tempo situa ocorrência em relação temporal.

**Função:** Especializa a função circunstancial do adjunto adverbial.

**Dependências:** adjunto adverbial, tempo verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudo hoje.

**Não confundir com:** Tempo sintático não é apenas tempo verbal.

### 485. adjunto adverbial de lugar

**Construção:** Adjunto adverbial de lugar situa ocorrência ou referência no espaço.

**Função:** Especializa relação locativa.

**Dependências:** adjunto adverbial, advérbio de lugar, localização semântica

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudo em casa.

**Não confundir com:** Pode ser expresso por sintagma preposicional.

### 486. adjunto adverbial de modo

**Construção:** Adjunto adverbial de modo caracteriza como uma ocorrência se realiza.

**Função:** Especializa circunstância modal de ação.

**Dependências:** adjunto adverbial, advérbio de modo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Falou claramente.

**Não confundir com:** Não é o mesmo que modo verbal.

### 487. adjunto adverbial de causa

**Construção:** Adjunto adverbial de causa apresenta motivo associado à ocorrência.

**Função:** Liga circunstância sintática a papel causal.

**Dependências:** adjunto adverbial, subordinação causal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Tremeu de frio.

**Não confundir com:** Causa inferida precisa de contexto.

### 488. ambiguidade lexical

**Construção:** Ambiguidade lexical ocorre quando uma palavra ou forma admite mais de uma leitura relevante no contexto.

**Função:** Especializa polissemia e homonímia na interpretação.

**Dependências:** ambiguidade, polissemia, homonímia

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** banco pode indicar assento ou instituição

**Não confundir com:** Não é necessariamente erro.

### 489. ambiguidade estrutural

**Construção:** Ambiguidade estrutural ocorre quando a organização sintática permite mais de uma relação entre os mesmos elementos.

**Função:** Distingue problema de estrutura de multiplicidade lexical.

**Dependências:** ambiguidade, sintagma, oração

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** vi o homem com o telescópio

**Não confundir com:** Não depende obrigatoriamente de palavra polissêmica.

### 490. acarretamento

**Construção:** Acarretamento é relação em que a verdade de um enunciado exige a verdade de outro em uma interpretação controlada.

**Função:** Permite testar consequência semântica.

**Dependências:** afirmação, inferência, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** João corre acarreta João se move.

**Não confundir com:** Não é simples associação provável.

### 491. contradição semântica

**Construção:** Contradição semântica ocorre quando duas leituras afirmadas sob o mesmo escopo não podem ser verdadeiras juntas.

**Função:** Ajuda a detectar incompatibilidade de sentido.

**Dependências:** negação, afirmação, acarretamento

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Está vivo e não está vivo no mesmo sentido e tempo.

**Não confundir com:** Diferença de contexto pode desfazer aparente contradição.

### 492. ato assertivo

**Construção:** Ato assertivo compromete o enunciador com uma descrição, afirmação ou avaliação apresentada como sustentada.

**Função:** Especializa atos de fala de informar e afirmar.

**Dependências:** ato de fala, afirmação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A porta está aberta.

**Não confundir com:** Pode ser falso sem deixar de ser assertivo.

### 493. ato diretivo

**Construção:** Ato diretivo procura levar o interlocutor a realizar uma ação.

**Função:** Reúne pedido, ordem, conselho e convite por função comunicativa.

**Dependências:** ato de fala, intenção comunicativa

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Por favor, sente-se.

**Não confundir com:** Forma interrogativa pode realizar pedido.

### 494. ato compromissivo

**Construção:** Ato compromissivo vincula o enunciador a uma ação futura ou responsabilidade.

**Função:** Explica promessas, ofertas e compromissos.

**Dependências:** ato de fala, futuro, pessoa gramatical

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Prometo concluir.

**Não confundir com:** Não é previsão neutra.

### 495. ato expressivo

**Construção:** Ato expressivo manifesta avaliação, sentimento ou reação do enunciador diante de uma situação.

**Função:** Explica agradecimento, desculpa, felicitação e lamento.

**Dependências:** ato de fala, exclamação, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Obrigado pela ajuda.

**Não confundir com:** Não se reduz a interjeição.

### 496. ato declarativo

**Construção:** Ato declarativo produz mudança institucional quando realizado por pessoa, contexto e procedimento reconhecidos.

**Função:** Mostra que certos enunciados fazem algo por convenção social.

**Dependências:** ato de fala, contexto, registro

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Declaro aberta a sessão.

**Não confundir com:** Sem autoridade e contexto adequados, a mudança pode não ocorrer.

### 497. alternância de código

**Construção:** Alternância de código é mudança entre línguas ou variedades dentro da mesma interação.

**Função:** Descreve prática de falantes bilíngues sem tratá-la automaticamente como falha.

**Dependências:** bilinguismo, contexto, registro

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** Aplicação mínima: reconhecer alternância de código numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é mistura aleatória obrigatória.

### 498. contacto linguístico

**Construção:** Contacto linguístico é convivência entre línguas ou variedades que possibilita influência mútua.

**Função:** Liga empréstimo, bilinguismo, alternância e mudança.

**Dependências:** bilinguismo, empréstimo linguístico, variação linguística

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** Aplicação mínima: reconhecer contacto linguístico numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não implica desaparecimento de uma língua.

### 499. diglossia

**Construção:** Diglossia é distribuição social relativamente estável de variedades ou línguas por funções e contextos diferentes.

**Função:** Distingue domínio funcional de simples diferença individual de estilo.

**Dependências:** contacto linguístico, registro, variação situacional

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** Aplicação mínima: reconhecer diglossia numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Não é sinónimo de bilinguismo individual.

### 500. equivalência tradutória

**Construção:** Equivalência tradutória é relação construída entre segmentos de línguas diferentes que preservam função relevante em determinado contexto.

**Função:** Fornece critério para tradução sem exigir identidade formal.

**Dependências:** tradução, intenção comunicativa, contexto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Aplicação mínima: reconhecer equivalência tradutória numa ocorrência compatível com a definição e verificar as suas dependências.

**Não confundir com:** Equivalência não é igualdade absoluta.

### 501. numeral multiplicativo

**Construção:** Numeral multiplicativo expressa multiplicação de quantidade.

**Função:** Completa família funcional de numerais.

**Dependências:** numeral, numeral cardinal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** dobro, triplo

**Não confundir com:** Não é numeral cardinal.

### 502. numeral fracionário

**Construção:** Numeral fracionário expressa divisão de uma unidade em partes.

**Função:** Liga quantidade linguística a fração.

**Dependências:** numeral, numeral cardinal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** meio, um terço

**Não confundir com:** Não é numeral ordinal.

### 503. numeral coletivo

**Construção:** Numeral coletivo expressa quantidade organizada como conjunto convencional.

**Função:** Distingue grupo nomeado de contagem isolada.

**Dependências:** numeral, numeral cardinal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** dúzia, centena

**Não confundir com:** Nem todo substantivo coletivo é numeral coletivo.

### 504. locução adverbial

**Construção:** Locução adverbial é combinação estável que desempenha função de advérbio.

**Função:** Permite reconhecer função acima da palavra isolada.

**Dependências:** locução, advérbio

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** de manhã, com cuidado

**Não confundir com:** Nem todo sintagma preposicional é locução fixa.

### 505. locução conjuntiva

**Construção:** Locução conjuntiva é combinação estável que liga orações ou termos com função de conjunção.

**Função:** Amplia conectivos além de uma palavra.

**Dependências:** locução, conjunção, conectivo

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** ainda que, visto que

**Não confundir com:** A relação depende da construção completa.

### 506. locução adjetiva

**Construção:** Locução adjetiva é combinação que atribui característica a nome como um adjetivo.

**Função:** Liga sintagma preposicional a função qualificadora.

**Dependências:** locução, adjetivo, sintagma nominal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** amor de mãe

**Não confundir com:** Nem toda expressão com de é locução adjetiva.

### 507. locução substantiva

**Construção:** Locução substantiva é combinação estável que funciona como unidade nominal.

**Função:** Permite reconhecer nomes compostos por várias palavras.

**Dependências:** locução, nome, sintagma nominal

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** fim de semana

**Não confundir com:** Estabilidade lexical precisa de uso repetido.

### 508. locução interjetiva

**Construção:** Locução interjetiva é combinação estável com função expressiva ou apelativa semelhante a interjeição.

**Função:** Amplia a classe interjetiva para unidades multipalavra.

**Dependências:** locução, interjeição, ato expressivo

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** meu Deus!

**Não confundir com:** A interpretação depende de contexto e entoação.

### 509. preposição essencial

**Construção:** Preposição essencial é palavra cuja função básica no sistema é estabelecer relação preposicional.

**Função:** Distingue núcleo da classe de usos ocasionais de outras classes.

**Dependências:** preposição, classe gramatical

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** a, de, em, por

**Não confundir com:** Inventários normativos podem variar na classificação.

### 510. preposição acidental

**Construção:** Preposição acidental é palavra de outra origem categorial usada em certo contexto com função preposicional.

**Função:** Mostra que função e classe histórica podem divergir.

**Dependências:** preposição essencial, uso, contexto

**Tema de consulta:** `classes_funcionais`

**Exemplo mínimo:** conforme, durante, exceto

**Não confundir com:** A classificação depende da construção concreta.

### 511. oração coordenada sindética

**Construção:** Oração coordenada sindética liga-se a outra por conectivo explícito.

**Função:** Distingue coordenação com marca formal.

**Dependências:** oração coordenada, conjunção coordenativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** Estudou e aprendeu.

**Não confundir com:** O conectivo pode ter mais de um valor contextual.

### 512. oração coordenada assindética

**Construção:** Oração coordenada assindética liga-se a outra sem conjunção explícita, usando justaposição e pontuação.

**Função:** Explica coordenação sem conectivo lexical.

**Dependências:** oração coordenada, pontuação

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** Cheguei, vi, venci.

**Não confundir com:** Ausência de conjunção não elimina relação.

### 513. oração subordinada desenvolvida

**Construção:** Oração subordinada desenvolvida apresenta verbo finito e normalmente conectivo ou relativo explícito.

**Função:** Contrasta com oração reduzida.

**Dependências:** oração subordinada, oração reduzida, conjunção subordinativa

**Tema de consulta:** `relacoes_oracionais`

**Exemplo mínimo:** Espero que venhas.

**Não confundir com:** Nem toda oração finita é subordinada.

### 514. período simples

**Construção:** Período simples contém uma oração no recorte sintático adotado.

**Função:** Distingue período simples de período composto.

**Dependências:** período, oração

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança estuda.

**Não confundir com:** Locuções verbais não criam automaticamente duas orações.

### 515. frase nominal

**Construção:** Frase nominal é frase sem verbo explícito, mas com função comunicativa completa no contexto.

**Função:** Impede identificar toda frase com oração verbal.

**Dependências:** frase, nome, contexto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Que beleza!

**Não confundir com:** Não é oração no critério verbal tradicional.

### 516. frase verbal

**Construção:** Frase verbal é frase organizada com verbo explícito ou locução verbal.

**Função:** Relaciona frase e oração sem torná-las idênticas em todos os casos.

**Dependências:** frase, verbo, oração

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança estuda.

**Não confundir com:** Uma frase pode conter mais de uma oração.

### 517. coesão lexical

**Construção:** Coesão lexical é continuidade textual construída por repetição, substituição e relações de sentido entre palavras.

**Função:** Complementa coesão referencial e sequencial.

**Dependências:** coesão, campo lexical, cadeia referencial

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** casa... moradia... edifício

**Não confundir com:** Sem coerência, repetição lexical isolada não basta.

### 518. repetição lexical

**Construção:** Repetição lexical retoma a mesma palavra ou radical para manter tema, ênfase ou precisão.

**Função:** Materializa um mecanismo básico de coesão lexical.

**Dependências:** coesão lexical, retomada, radical

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** O estudo exige tempo. O estudo exige prática.

**Não confundir com:** Repetição pode ser necessária ou excessiva conforme função.

### 519. substituição lexical

**Construção:** Substituição lexical retoma referência por palavra de sentido relacionado ou expressão equivalente.

**Função:** Evita repetição mantendo cadeia temática.

**Dependências:** coesão lexical, sinonímia, hiperonímia, retomada

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o cão... o animal

**Não confundir com:** A substituição precisa conservar o referente.

### 520. paralelismo sintático

**Construção:** Paralelismo sintático repete ou alinha estruturas gramaticais equivalentes em sequência.

**Função:** Aumenta clareza, ritmo e comparabilidade textual.

**Dependências:** sintagma, coordenação, estilo

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** estudar com método, testar com rigor e escrever com clareza

**Não confundir com:** Não exige palavras idênticas.

### 521. sequência de fonemas

**Construção:** Sequência de fonemas é uma ordem explícita de unidades fonológicas tratadas como cadeia.

**Função:** Permite analisar combinações sem confundir som, letra e palavra.

**Dependências:** fonema, combinação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/ + /r/ + /a/

**Não confundir com:** Não é sequência de letras por necessidade.

### 522. foco informacional

**Construção:** Foco informacional é a parte do enunciado apresentada como informação selecionada, nova ou contrastiva.

**Função:** Liga estrutura informacional, prosódia e ordem.

**Dependências:** informação nova, enunciado, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Foi O LIVRO que ela leu.

**Não confundir com:** Não é sinónimo de tópico.

### 523. enumeração

**Construção:** Enumeração é organização de duas ou mais unidades em série reconhecível.

**Função:** Sustenta listas, coordenação e pontuação.

**Dependências:** relação, texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** pão, água e fruta

**Não confundir com:** Não é simples repetição.

### 524. paradigma

**Construção:** Paradigma é conjunto organizado de formas relacionadas por posições e contrastes de uma mesma unidade ou classe.

**Função:** Permite construir flexão e irregularidade por comparação interna.

**Dependências:** relação, forma lexical, flexão

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** canto, cantas, canta...

**Não confundir com:** Não é lista sem relações.

### 525. oposição

**Construção:** Oposição é relação em que duas unidades se distinguem por propriedade relevante num domínio.

**Função:** Generaliza contrastes fonológicos, morfológicos e semânticos.

**Dependências:** diferença, relação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** singular / plural

**Não confundir com:** Não é conflito social.

### 526. variante

**Construção:** Variante é uma forma alternativa relacionada a outra dentro de um sistema, contexto ou comunidade explicitada.

**Função:** Permite registrar diferença sem duplicar conceito canónico.

**Dependências:** variação linguística, forma lexical

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** duas formas usadas em contextos diferentes

**Não confundir com:** Não é erro por definição.

### 527. segmentação

**Construção:** Segmentação é operação de separar uma cadeia em unidades segundo critérios explícitos.

**Função:** Fornece base comum para segmentação sonora, gráfica, morfológica e textual.

**Dependências:** diferença, combinação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** texto → frases → palavras

**Não confundir com:** Não é cortar arbitrariamente.

### 528. ordem

**Construção:** Ordem é relação que posiciona unidades antes, depois ou em hierarquia definida.

**Função:** Sustenta sequência, sintaxe, narrativa e procedimento.

**Dependências:** relação, diferença

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** A antes de B

**Não confundir com:** Não é valor moral.

### 529. existência

**Construção:** Existência é a apresentação de uma entidade ou situação como pertencente ao domínio considerado.

**Função:** Apoia construções existenciais e quantificação.

**Dependências:** referência, afirmação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Há um livro na mesa.

**Não confundir com:** Não é posse.

### 530. estrutura informacional

**Construção:** Estrutura informacional é a organização do enunciado em tópico, foco, informação dada e informação nova.

**Função:** Liga forma, prosódia e contexto discursivo.

**Dependências:** tópico discursivo, informação dada, informação nova, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** tema conhecido + informação nova

**Não confundir com:** Não é estrutura sintática completa.

### 531. sintaxe

**Construção:** Sintaxe é o conhecimento das combinações e dependências entre palavras, sintagmas e orações.

**Função:** Integra constituintes, funções e ordem sem depender de aula pronta.

**Dependências:** gramática, relação, oração, sintagma

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** sujeito + predicado

**Não confundir com:** Não é apenas ordem linear.

### 532. situação

**Construção:** Situação é estado, processo ou evento considerado como unidade de interpretação.

**Função:** Fornece base para tempo, aspecto e predicação.

**Dependências:** sentido, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** uma porta estar aberta

**Não confundir com:** Não é necessariamente acontecimento dinâmico.

### 533. relação temporal

**Construção:** Relação temporal posiciona duas situações por anterioridade, simultaneidade ou posterioridade.

**Função:** Liga tempos verbais, narrativa e inferência.

**Dependências:** situação, tempo verbal, ordem

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A ocorreu antes de B.

**Não confundir com:** Não é causa.

### 534. quantidade

**Construção:** Quantidade é propriedade que permite contar, medir ou comparar extensão num domínio.

**Função:** Apoia numerais e quantificação linguística.

**Dependências:** diferença, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** três livros; muita água

**Não confundir com:** Não é apenas número exato.

### 535. domínio contextual

**Construção:** Domínio contextual é o conjunto de entidades ou situações relevantes para interpretar uma expressão num contexto.

**Função:** Limita quantificadores e referências sem universalizar.

**Dependências:** contexto, referência, texto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** todos os alunos desta turma

**Não confundir com:** Não é o universo inteiro.

### 536. estrutura semântica

**Construção:** Estrutura semântica é a organização de predicados, argumentos, operadores e relações de sentido.

**Função:** Permite representar composição e escopo.

**Dependências:** sentido, relação, inferência

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** negação aplicada a uma afirmação

**Não confundir com:** Não é árvore sintática por necessidade.

### 537. explicação

**Construção:** Explicação é texto ou relação que torna uma afirmação compreensível por causas, razões, partes ou funcionamento.

**Função:** Apoia elaboração, ensino e argumentação.

**Dependências:** exposição, relação, coerência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** mostrar como e por quê

**Não confundir com:** Não é apenas repetir a afirmação.

### 538. exemplificação

**Construção:** Exemplificação é relação em que um caso concreto materializa uma classe, regra ou ideia.

**Função:** Liga conceito abstrato a ocorrência observável.

**Dependências:** exemplo de uso, relação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** “casa” como exemplo de nome

**Não confundir com:** Não é definição completa.

### 539. causa

**Construção:** Causa é uma situação tratada como produtora ou condição explicativa de outra.

**Função:** Sustenta relações causais e argumentos.

**Dependências:** situação, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** chuva causando piso molhado em contexto controlado

**Não confundir com:** Não é simples anterioridade.

### 540. hipótese

**Construção:** Hipótese é afirmação provisória proposta para teste.

**Função:** Permite investigar sem fingir conclusão.

**Dependências:** afirmação, inferência, evidência

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** tal forma pode depender deste contexto

**Não confundir com:** Não é fato aprovado.

### 541. voz discursiva

**Construção:** Voz discursiva é a fonte textual ou enunciativa a que uma fala, avaliação ou posição é atribuída.

**Função:** Distingue narrador, autor citado e personagem.

**Dependências:** texto, citação, referência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** voz do narrador e voz da personagem

**Não confundir com:** Não é voz verbal.

### 542. progressão

**Construção:** Progressão é mudança ordenada pela qual texto, argumento ou narrativa avança.

**Função:** Generaliza progressão temática e sequencial.

**Dependências:** ordem, coerência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** problema → análise → conclusão

**Não confundir com:** Não exige crescimento linear.

### 543. comunidade de fala

**Construção:** Comunidade de fala é grupo cujos participantes partilham ou negociam padrões de uso e interpretação.

**Função:** Apoia descrição de variedades sem homogeneizar pessoas.

**Dependências:** uso, variação linguística, contexto

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** falantes ligados por práticas comuns

**Não confundir com:** Não significa fala idêntica.

### 544. repertório linguístico

**Construção:** Repertório linguístico é o conjunto de línguas, variedades, registros e recursos disponíveis a uma pessoa ou comunidade.

**Função:** Apoia bilinguismo, alternância e aquisição.

**Dependências:** competência comunicativa, variação linguística

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** português, outra língua e registros diversos

**Não confundir com:** Não é lista fixa de idiomas.

### 545. procedimento

**Construção:** Procedimento é sequência explícita de operações orientada a um resultado verificável.

**Função:** Baseia descrição operacional e instrução.

**Dependências:** ordem, instrução

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** observar → classificar → testar

**Não confundir com:** Não é resultado.

### 546. critério

**Construção:** Critério é condição explícita usada para decidir, classificar ou comparar.

**Função:** Impede classificação intuitiva sem fundamento declarado.

**Dependências:** diferença, relação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** presença de verbo finito como critério

**Não confundir com:** Não é resultado da decisão.

### 547. lacuna de conhecimento

**Construção:** Lacuna de conhecimento é dependência, dado ou operação ainda não construída ou validada.

**Função:** Torna explícito o que falta e impede antecipação.

**Dependências:** reconstrução linguística PSF, diferença

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** inventário regional ainda ausente

**Não confundir com:** Não é convite para inventar.

### 548. destinatário

**Construção:** Destinatário é participante a quem um enunciado ou texto é dirigido.

**Função:** Liga intenção, gênero e escolhas de registro.

**Dependências:** enunciado, intenção comunicativa, referência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** leitor de uma carta

**Não confundir com:** Não é necessariamente receptor efetivo.

### 549. gênero digital

**Construção:** Gênero digital é gênero textual cuja produção, circulação ou interação depende de ambiente digital.

**Função:** Agrupa correio eletrónico, mensagem e outros formatos sem os tornar idênticos.

**Dependências:** gênero textual, multimodalidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** email

**Não confundir com:** Não é tipo textual único.

### 550. gênero informativo

**Construção:** Gênero informativo prioriza apresentação verificável de fatos, dados ou explicações.

**Função:** Agrupa notícia e reportagem por finalidade dominante.

**Dependências:** gênero textual, exposição, evidência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** notícia

**Não confundir com:** Informativo não garante verdade.

### 551. gênero formal

**Construção:** Gênero formal segue convenções institucionais explícitas para cumprir função administrativa, académica ou profissional.

**Função:** Agrupa requerimentos, atas e relatórios por situação de uso.

**Dependências:** gênero textual, formalidade, norma

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** requerimento

**Não confundir com:** Formal não significa melhor em todo contexto.

### 552. gênero literário

**Construção:** Gênero literário organiza produção verbal estética por convenções abertas de narrativa, poesia ou drama.

**Função:** Permite relacionar obras sem impor fronteiras absolutas.

**Dependências:** gênero textual, estilo, conotação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** conto; poema; romance

**Não confundir com:** Não é garantia de ficção.

### 553. gênero dramático

**Construção:** Gênero dramático organiza ações e falas para representação ou leitura cénica.

**Função:** Sustenta peça teatral e diálogo dramático.

**Dependências:** gênero literário, diálogo, multimodalidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** peça teatral

**Não confundir com:** Não é toda conversa com conflito.

### 554. pesquisa

**Construção:** Pesquisa é procedimento sistemático de formular problema, recolher evidência, comparar e registrar conclusão provisória.

**Função:** Apoia reportagem, monografia e reconstrução PSF.

**Dependências:** hipótese, procedimento, evidência

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** pergunta → dados → teste → conclusão

**Não confundir com:** Não é busca sem critério.

### 555. turno de fala

**Construção:** Turno de fala é intervalo em que um participante detém a palavra numa interação.

**Função:** Permite analisar alternância em diálogo e entrevista.

**Dependências:** diálogo, fala, ordem

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** pergunta num turno, resposta no seguinte

**Não confundir com:** Não é parágrafo.

### 556. figura de linguagem

**Construção:** Figura de linguagem é construção que produz efeito por relação não literal, repetição, contraste ou desvio funcional.

**Função:** Generaliza metáfora, metonímia, ironia e outras figuras.

**Dependências:** conotação, estilo, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** metáfora

**Não confundir com:** Não é erro gramatical.

### 557. fonotática

**Construção:** Fonotática é o conhecimento das combinações de fonemas admitidas numa posição de sílaba ou palavra.

**Função:** Permite distinguir sequência possível, rara e ainda não validada.

**Dependências:** fonema, sílaba, combinação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** prato começa por grupo consonantal possível

**Não confundir com:** Não é ortografia: trata organização sonora.

### 558. sequência fonotática

**Construção:** Sequência fonotática é uma cadeia ordenada de unidades sonoras examinada quanto à sua posição e combinabilidade.

**Função:** Materializa o objeto que a fonotática testa.

**Dependências:** fonotática, sequência de fonemas

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /pr/ no início de prato

**Não confundir com:** Não é qualquer sequência de letras.

### 559. margem silábica

**Construção:** Margem silábica é a parte periférica da sílaba formada pelo ataque e, quando existe, pela coda.

**Função:** Separa periferia consonantal de núcleo silábico.

**Dependências:** ataque silábico, coda silábica, núcleo silábico

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pr- em pra; -r em mar

**Não confundir com:** O núcleo não pertence à margem.

### 560. rima silábica

**Construção:** Rima silábica é a unidade formada pelo núcleo da sílaba e pela coda que o segue, quando existe.

**Função:** Permite comparar sílabas pelo seu final sonoro.

**Dependências:** núcleo silábico, coda silábica, sílaba

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** -ar em mar

**Não confundir com:** Não é rima poética completa.

### 561. sílaba aberta

**Construção:** Sílaba aberta termina no núcleo, sem coda consonantal no recorte adotado.

**Função:** Distingue estruturas silábicas terminadas em vogal.

**Dependências:** sílaba, núcleo silábico, coda silábica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** má em mapa

**Não confundir com:** Aberta não significa necessariamente vogal aberta.

### 562. sílaba fechada

**Construção:** Sílaba fechada possui coda depois do núcleo no recorte adotado.

**Função:** Distingue estruturas silábicas com fechamento periférico.

**Dependências:** sílaba, núcleo silábico, coda silábica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** mar

**Não confundir com:** Fechada não significa vogal fechada.

### 563. ataque simples

**Construção:** Ataque simples contém uma unidade consonantal antes do núcleo silábico.

**Função:** Permite classificar a complexidade do início da sílaba.

**Dependências:** ataque silábico, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** p- em pá

**Não confundir com:** Não é ataque complexo.

### 564. ataque complexo

**Construção:** Ataque complexo contém mais de uma unidade consonantal antes do núcleo silábico.

**Função:** Permite investigar grupos consonantais iniciais.

**Dependências:** ataque silábico, encontro consonantal, fonotática

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pr- em prato

**Não confundir com:** Duas letras podem representar uma só unidade e não formar ataque complexo.

### 565. coda simples

**Construção:** Coda simples contém uma unidade depois do núcleo silábico.

**Função:** Permite descrever fechamento silábico elementar.

**Dependências:** coda silábica, consoante

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** -r em mar

**Não confundir com:** Não é ataque.

### 566. coda complexa

**Construção:** Coda complexa contém mais de uma unidade depois do núcleo silábico no recorte fonológico adotado.

**Função:** Permite marcar finais silábicos de maior complexidade.

**Dependências:** coda silábica, fonotática

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** estrutura final a validar por variedade

**Não confundir com:** Não deve ser inferida apenas pela escrita.

### 567. palavra fonológica

**Construção:** Palavra fonológica é unidade organizada por acento e continuidade sonora, que pode não coincidir perfeitamente com a palavra gráfica.

**Função:** Liga tonicidade, clíticos e ritmo.

**Dependências:** palavra, prosódia, tonicidade

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** um clítico pode apoiar-se na palavra vizinha

**Não confundir com:** Não é sinónimo obrigatório de palavra escrita.

### 568. grupo prosódico

**Construção:** Grupo prosódico é conjunto de unidades pronunciadas sob uma organização comum de ritmo, acento e entoação.

**Função:** Permite analisar fala acima da palavra isolada.

**Dependências:** palavra fonológica, ritmo, entoação

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** uma frase curta dita num só contorno

**Não confundir com:** Não é necessariamente uma oração.

### 569. acento lexical

**Construção:** Acento lexical é a proeminência relativa associada a uma palavra no sistema.

**Função:** Distingue posição tônica da palavra antes do enunciado completo.

**Dependências:** tonicidade, palavra fonológica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** café tem proeminência final

**Não confundir com:** Não é acento gráfico.

### 570. acento frásico

**Construção:** Acento frásico é a proeminência que uma unidade recebe dentro do enunciado.

**Função:** Permite destacar informação na fala.

**Dependências:** acento lexical, enunciado, prosódia

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** EU fiz, com destaque em eu

**Não confundir com:** Não altera necessariamente a grafia.

### 571. foco prosódico

**Construção:** Foco prosódico é destaque sonoro usado para selecionar ou contrastar uma parte do enunciado.

**Função:** Liga intenção comunicativa e realização sonora.

**Dependências:** acento frásico, intenção comunicativa, foco informacional

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** Eu disse HOJE, não amanhã.

**Não confundir com:** Nem toda intensidade é foco.

### 572. contorno entoacional

**Construção:** Contorno entoacional é o percurso relativo da altura da voz ao longo de um grupo prosódico.

**Função:** Ajuda a distinguir continuidade, pergunta, afirmação e atitude sem reduzir tudo à pontuação.

**Dependências:** entoação, grupo prosódico

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** subida final possível em pergunta

**Não confundir com:** Não é regra absoluta de interrogação.

### 573. fronteira prosódica

**Construção:** Fronteira prosódica é um limite percebido por pausa, alongamento, mudança de ritmo ou contorno.

**Função:** Permite segmentar fala contínua.

**Dependências:** pausa, grupo prosódico, contorno entoacional

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pausa entre dois grupos

**Não confundir com:** Não coincide sempre com vírgula.

### 574. assimilação regressiva

**Construção:** Assimilação regressiva ocorre quando uma unidade posterior influencia uma anterior.

**Função:** Distingue a direção de um processo de aproximação sonora.

**Dependências:** assimilação fonológica, sequência fonotática

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** influência do som seguinte

**Não confundir com:** Não é regra ortográfica automática.

### 575. assimilação progressiva

**Construção:** Assimilação progressiva ocorre quando uma unidade anterior influencia uma posterior.

**Função:** Completa a distinção direcional da assimilação.

**Dependências:** assimilação fonológica, sequência fonotática

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** influência do som anterior

**Não confundir com:** Não é simples repetição.

### 576. dissimilação

**Construção:** Dissimilação é mudança que aumenta a diferença entre unidades semelhantes numa sequência.

**Função:** Permite descrever afastamento articulatório ou fonológico.

**Dependências:** oposição fonológica, sequência fonotática

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** forma histórica a ser reconstruída, não presumida

**Não confundir com:** Não é assimilação.

### 577. síncope

**Construção:** Síncope é perda de unidade sonora no interior de uma palavra ou grupo.

**Função:** Localiza elisão interna.

**Dependências:** elisão, palavra fonológica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** perda interna em fala rápida a observar

**Não confundir com:** Não é apócope.

### 578. apócope

**Construção:** Apócope é perda de unidade sonora no final de uma palavra.

**Função:** Localiza elisão final.

**Dependências:** elisão, palavra fonológica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** redução final a observar

**Não confundir com:** Não é síncope.

### 579. prótese

**Construção:** Prótese é acréscimo de unidade no início de uma forma.

**Função:** Distingue epêntese inicial.

**Dependências:** epêntese, palavra fonológica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** acréscimo inicial a validar

**Não confundir com:** Não é prefixação morfológica.

### 580. paragoge

**Construção:** Paragoge é acréscimo de unidade no final de uma forma.

**Função:** Distingue epêntese final.

**Dependências:** epêntese, palavra fonológica

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** acréscimo final a validar

**Não confundir com:** Não é sufixação morfológica.

### 581. segmentação gráfica

**Construção:** Segmentação gráfica é a divisão da escrita em palavras, sinais e blocos visíveis.

**Função:** Permite reconstruir limites escritos sem confundi-los com limites sonoros.

**Dependências:** grafema, espaço, pontuação

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** a casa

**Não confundir com:** Não é separação silábica.

### 582. juntura vocabular

**Construção:** Juntura vocabular é a fronteira entre palavras ou formas na cadeia escrita e falada.

**Função:** Ajuda a investigar união indevida e separação indevida.

**Dependências:** segmentação gráfica, palavra, fronteira prosódica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** de repente, não derepente

**Não confundir com:** Não é apenas espaço físico.

### 583. grafia lexical

**Construção:** Grafia lexical é a forma escrita estabilizada de uma unidade lexical.

**Função:** Permite comparar pronúncia, família e convenção escrita.

**Dependências:** forma lexical, ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa

**Não confundir com:** Não é transcrição fonética.

### 584. convenção ortográfica

**Construção:** Convenção ortográfica é regularidade coletiva que estabiliza uma escolha gráfica.

**Função:** Explica por que escrita não é cópia exata de som.

**Dependências:** norma, ortografia, uso

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** uso partilhado de letras e sinais

**Não confundir com:** Não é verdade natural imutável.

### 585. variante gráfica

**Construção:** Variante gráfica é forma escrita alternativa ligada à mesma unidade em contexto, época ou norma identificada.

**Função:** Permite registrar diferença sem declarar erro automaticamente.

**Dependências:** grafia lexical, variação linguística, norma

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** forma A / forma B quando ambas forem validadas

**Não confundir com:** Não é erro por definição.

### 586. homofonia

**Construção:** Homofonia é relação entre formas de som igual ou muito próximo e grafia ou sentido diferente.

**Função:** Explica por que ouvir pode não bastar para escolher grafia.

**Dependências:** som, grafia lexical, sentido

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** cem e sem em variedades onde coincidem

**Não confundir com:** Não é homografia.

### 587. homografia

**Construção:** Homografia é relação entre formas escritas iguais que podem ter leitura, classe ou sentido diferente.

**Função:** Explica ambiguidade preservada pela escrita.

**Dependências:** grafia lexical, polissemia, homonímia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** forma escrita igual com sentidos distintos

**Não confundir com:** Não garante pronúncia igual.

### 588. uso de h

**Construção:** O uso de h é uma escolha gráfica que em muitas posições não corresponde a som próprio, mas distingue grafias e famílias.

**Função:** Impede deduzir h apenas pela audição.

**Dependências:** letra, grafia lexical, família ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** homem; hoje; nh; ch; lh

**Não confundir com:** H isolado e h em dígrafo têm funções diferentes.

### 589. uso de r

**Construção:** O uso de r registra valores e posições diferentes conforme início, interior, final e vizinhança gráfica.

**Função:** Prepara a distinção entre r e rr.

**Dependências:** letra, grafia lexical, correspondência som-grafema

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** rato; caro; mar

**Não confundir com:** Um r gráfico não tem sempre o mesmo som.

### 590. uso de rr

**Construção:** O uso de rr ocorre no interior de palavra entre vogais para conservar um valor consonantal forte na convenção escrita.

**Função:** Distingue pares gráficos como caro e carro.

**Dependências:** uso de r, dígrafo, vogal

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** carro

**Não confundir com:** RR não aparece normalmente no início da palavra.

### 591. uso de m antes de p e b

**Construção:** Na grafia portuguesa, m é usado frequentemente para marcar nasalidade antes de p e b.

**Função:** Constrói uma família ortográfica observável.

**Dependências:** nasalidade, grafia lexical, consoante

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** campo; também

**Não confundir com:** Não autoriza trocar todo n por m.

### 592. uso de n antes de consoante

**Construção:** N pode marcar nasalidade antes de diversas consoantes fora da família p/b.

**Função:** Complementa a distinção gráfica m/n em posição interna.

**Dependências:** nasalidade, grafia lexical, uso de m antes de p e b

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** canto

**Não confundir com:** Não é regra suficiente para todas as palavras.

### 593. uso de e e i átonos

**Construção:** E e i em posição átona podem aproximar-se na fala de certas variedades sem se tornarem grafias livremente intercambiáveis.

**Função:** Separa redução fonética de decisão ortográfica.

**Dependências:** vogal átona, grafia lexical, variação regional

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** grafia deve ser confirmada pela família, não apenas pelo som

**Não confundir com:** Não é licença para escrever pela pronúncia local.

### 594. uso de o e u átonos

**Construção:** O e u em posição átona podem aproximar-se na fala de certas variedades, mantendo distinções gráficas lexicais.

**Função:** Separa realização sonora e convenção escrita.

**Dependências:** vogal átona, grafia lexical, variação regional

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** grafia lexical deve ser validada

**Não confundir com:** Não é regra universal de pronúncia.

### 595. maiúscula no início de frase

**Construção:** Maiúscula no início de frase é marca gráfica convencional colocada na primeira unidade alfabética relevante após limite final.

**Função:** Ajuda a reconhecer começo de unidade escrita.

**Dependências:** maiúscula inicial, frase, ponto final

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** A criança lê.

**Não confundir com:** Não transforma a palavra em nome próprio.

### 596. maiúscula em nome próprio

**Construção:** Maiúscula em nome próprio marca convencionalmente uma referência individualizada na escrita.

**Função:** Relaciona categoria nominal e apresentação gráfica.

**Dependências:** substantivo próprio, maiúscula

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Maputo

**Não confundir com:** Maiúscula não prova que todo uso seja nome próprio.

### 597. ponto em abreviatura

**Construção:** Ponto em abreviatura pode marcar supressão gráfica de parte de uma palavra.

**Função:** Distingue abreviatura de palavra integral e de algumas siglas.

**Dependências:** abreviatura, ponto final

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** p. como forma abreviada validada em contexto

**Não confundir com:** Não é ponto final de frase por necessidade.

### 598. símbolo não alfabético

**Construção:** Símbolo não alfabético é marca convencional que representa medida, operação, moeda ou outra unidade sem funcionar como letra.

**Função:** Amplia o inventário gráfico sem confundir símbolo e palavra.

**Dependências:** grafema, marca, convenção ortográfica

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** %

**Não confundir com:** Não é sigla nem abreviatura comum.

### 599. vírgula de enumeração

**Construção:** Vírgula de enumeração separa unidades coordenadas numa série quando não há conectivo entre todas elas.

**Função:** Materializa uma função básica da vírgula.

**Dependências:** vírgula, enumeração, coordenação

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Trouxe pão, água, fruta e chá.

**Não confundir com:** Não separa automaticamente sujeito e verbo.

### 600. vírgula de vocativo

**Construção:** Vírgula de vocativo isola a unidade usada para chamar ou dirigir-se ao interlocutor.

**Função:** Liga pontuação e função sintática do vocativo.

**Dependências:** vírgula, vocativo, enunciado

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Maria, venha aqui.

**Não confundir com:** O vocativo não é sujeito por necessidade.

### 601. vírgula de aposto

**Construção:** Vírgula de aposto pode isolar aposto explicativo acrescentado a uma referência.

**Função:** Liga pontuação e explicação nominal.

**Dependências:** vírgula, aposto, retomada

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Maputo, capital de Moçambique, fica no sul.

**Não confundir com:** Nem todo aposto recebe vírgulas.

### 602. dois-pontos de citação

**Construção:** Dois-pontos de citação podem anunciar fala ou trecho citado.

**Função:** Liga pontuação e introdução do discurso de outra voz.

**Dependências:** dois-pontos, citação, discurso direto

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Ela disse: “Voltarei.”

**Não confundir com:** A citação pode ser integrada por outras construções.

### 603. travessão de diálogo

**Construção:** Travessão de diálogo pode marcar entrada de fala ou mudança de interlocutor em certos gêneros escritos.

**Função:** Organiza vozes sem depender apenas de verbos de dizer.

**Dependências:** travessão, diálogo, discurso direto

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** — Vou agora.

**Não confundir com:** Não é o único uso do travessão.

### 604. aspas de citação

**Construção:** Aspas de citação delimitam trecho reproduzido ou apresentado como expressão destacada.

**Função:** Ajuda a separar voz citada da voz que a enquadra.

**Dependências:** aspas, citação, intertextualidade

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Ele escreveu “clareza”.

**Não confundir com:** Aspas também podem marcar distância ou uso especial.

### 605. alomorfia

**Construção:** Alomorfia é a existência de formas diferentes que realizam a mesma função morfológica em ambientes distintos.

**Função:** Impede exigir uma única forma visível para cada morfema.

**Dependências:** morfema, forma lexical, variação linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** formas diferentes com a mesma função de plural

**Não confundir com:** Não é sinonímia lexical.

### 606. alomorfe

**Construção:** Alomorfe é cada realização formal pertencente a uma relação de alomorfia.

**Função:** Permite nomear as variantes de um morfema.

**Dependências:** alomorfia, morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** uma das formas de um mesmo morfema

**Não confundir com:** Não é palavra independente por necessidade.

### 607. morfema livre

**Construção:** Morfema livre pode ocorrer como palavra sem precisar ligar-se obrigatoriamente a outro morfema.

**Função:** Distingue unidades autónomas de unidades presas.

**Dependências:** morfema, palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mar

**Não confundir com:** Nem toda palavra tem apenas um morfema.

### 608. morfema preso

**Construção:** Morfema preso precisa ligar-se a uma base ou forma para ocorrer na construção.

**Função:** Abrange afixos e certas marcas flexionais.

**Dependências:** morfema, afixo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** re- em refazer

**Não confundir com:** Não é palavra livre.

### 609. morfema derivacional

**Construção:** Morfema derivacional participa da formação de nova unidade lexical ou altera classe e sentido.

**Função:** Separa derivação de flexão.

**Dependências:** morfema preso, derivação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** -mente em claramente

**Não confundir com:** Não expressa apenas concordância.

### 610. morfema flexional

**Construção:** Morfema flexional ajusta uma forma ao paradigma de gênero, número, pessoa, tempo ou modo sem criar necessariamente novo lexema.

**Função:** Materializa a função flexional.

**Dependências:** morfema preso, flexão

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** -s em casas

**Não confundir com:** Não é sempre derivacional.

### 611. morfema zero

**Construção:** Morfema zero é uma ausência formal interpretada como oposição dentro de paradigma explicitamente construído.

**Função:** Permite representar função sem marca audível ou gráfica, quando a comparação a justifica.

**Dependências:** morfema, paradigma, oposição

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** singular sem marca frente a plural marcado, em análise específica

**Não confundir com:** Não é ausência de conhecimento.

### 612. base lexical

**Construção:** Base lexical é a forma à qual se aplica uma operação de formação ou flexão.

**Função:** Generaliza radical, tema ou palavra usados como ponto de partida.

**Dependências:** lexema, estrutura da palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** feliz em infeliz e felicidade

**Não confundir com:** Base e radical podem coincidir, mas não são sempre idênticos.

### 613. palavra simples

**Construção:** Palavra simples é tratada como uma só base lexical sem processo sincrónico de composição identificado.

**Função:** Distingue estrutura simples de estrutura complexa.

**Dependências:** palavra, base lexical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa

**Não confundir com:** Simples não significa curta.

### 614. palavra complexa

**Construção:** Palavra complexa contém mais de um componente morfológico relevante na análise.

**Função:** Agrupa derivadas, compostas e flexionadas conforme o recorte.

**Dependências:** palavra, morfema, estrutura da palavra

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** infelizmente

**Não confundir com:** Complexa não significa difícil de entender.

### 615. palavra derivada

**Construção:** Palavra derivada resulta de operação derivacional aplicada a uma base.

**Função:** Liga produto e processo de derivação.

**Dependências:** derivação, base lexical, palavra complexa

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** feliz → infeliz

**Não confundir com:** Não é toda palavra flexionada.

### 616. palavra composta

**Construção:** Palavra composta resulta da combinação lexical de mais de uma base.

**Função:** Liga produto e processo de composição.

**Dependências:** composição, base lexical, palavra complexa

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** guarda-chuva

**Não confundir com:** Não é qualquer sintagma livre.

### 617. lexicalização

**Construção:** Lexicalização é o processo pelo qual uma forma ou combinação passa a funcionar como unidade lexical relativamente estável.

**Função:** Explica por que uma construção pode ganhar sentido próprio.

**Dependências:** lexema, uso, produtividade linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** combinação que passa a ter entrada lexical

**Não confundir com:** Não é apenas escrever junto.

### 618. gramaticalização

**Construção:** Gramaticalização é mudança pela qual uma forma ganha função mais gramatical e menos lexical em certos usos.

**Função:** Liga mudança histórica, uso e classe funcional.

**Dependências:** variação histórica, uso, classe gramatical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** forma lexical que passa a auxiliar construção gramatical

**Não confundir com:** Não é erro nem simples abreviação.

### 619. produtividade morfológica

**Construção:** Produtividade morfológica é a capacidade observada de um padrão formar novas palavras ou formas.

**Função:** Permite distinguir regra viva de lista fechada.

**Dependências:** produtividade linguística, derivação, flexão

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** formação recorrente com -mente

**Não confundir com:** Um único exemplo não prova produtividade.

### 620. adjetivo qualificativo

**Construção:** Adjetivo qualificativo atribui propriedade graduável ou descritiva ao nome em muitos usos.

**Função:** Distingue qualidade de relação classificatória.

**Dependências:** adjetivo, grau comparativo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa bonita

**Não confundir com:** Nem todo qualificativo é subjetivo.

### 621. adjetivo relacional

**Construção:** Adjetivo relacional liga o nome a domínio, origem, matéria ou relação e tende a resistir a graduação na leitura básica.

**Função:** Explica usos classificatórios.

**Dependências:** adjetivo, relação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** produção agrícola

**Não confundir com:** Não é sempre equivalente a “muito + adjetivo”.

### 622. adjetivo pátrio

**Construção:** Adjetivo pátrio relaciona entidade a lugar, território ou comunidade geográfica.

**Função:** Materializa uma subfamília relacional.

**Dependências:** adjetivo relacional, referência

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** moçambicano

**Não confundir com:** Não determina identidade pessoal completa.

### 623. pronome reto

**Construção:** Pronome reto é forma pessoal tipicamente associada a sujeito ou predicativo em construções básicas.

**Função:** Distingue formas pessoais por função sintática.

**Dependências:** pronome pessoal, sujeito

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** eu estudo

**Não confundir com:** Não é a única forma possível em toda construção.

### 624. pronome oblíquo

**Construção:** Pronome oblíquo é forma pessoal associada a complemento, objeto ou relação preposicionada.

**Função:** Liga paradigma pronominal e função sintática.

**Dependências:** pronome pessoal, complemento

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** vi-o; falei com ele

**Não confundir com:** Não é sinónimo automático de clítico.

### 625. pronome reflexivo

**Construção:** Pronome reflexivo indica que um participante retoma outro participante da mesma predicação, segundo a construção.

**Função:** Materializa correferência reflexiva.

**Dependências:** pronome, voz reflexiva, anáfora

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** Ela viu-se no espelho.

**Não confundir com:** Não é recíproco.

### 626. pronome recíproco

**Construção:** Pronome recíproco exprime relação mútua entre participantes plurais.

**Função:** Distingue reciprocidade de reflexividade individual.

**Dependências:** pronome, relação, sujeito composto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** Eles ajudaram-se.

**Não confundir com:** Não é necessariamente cada um a si mesmo.

### 627. determinante demonstrativo

**Construção:** Determinante demonstrativo acompanha nome e localiza a referência no espaço, tempo ou discurso.

**Função:** Liga dêixis e sintagma nominal.

**Dependências:** determinante, pronome demonstrativo, dêixis

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** este livro

**Não confundir com:** Pode haver uso pronominal sem nome expresso.

### 628. determinante possessivo

**Construção:** Determinante possessivo acompanha nome e constrói relação com pessoa discursiva ou possuidor contextual.

**Função:** Liga pessoa gramatical e referência nominal.

**Dependências:** determinante, pronome possessivo, referência

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** meu livro

**Não confundir com:** Posse é apenas uma das relações possíveis.

### 629. verbo regular

**Construção:** Verbo regular segue um paradigma sem alternâncias imprevisíveis relevantes na conjugação adotada.

**Função:** Serve de base para construir paradigmas antes das irregularidades.

**Dependências:** verbo, conjugação, paradigma

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** estudar em paradigma regular

**Não confundir com:** Regular não significa invariável.

### 630. verbo defectivo

**Construção:** Verbo defectivo não circula ou não é convencional em todas as posições de um paradigma.

**Função:** Impede inventar formas apenas por analogia.

**Dependências:** verbo, paradigma, uso

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** paradigma com posições ausentes ou raras

**Não confundir com:** Não é verbo incompreensível.

### 631. verbo abundante

**Construção:** Verbo abundante apresenta mais de uma forma aceite para uma posição do paradigma, frequentemente em particípios.

**Função:** Permite registrar concorrência sem escolher cegamente uma só forma.

**Dependências:** verbo, particípio, variante

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** duas formas participiais validadas em contexto

**Não confundir com:** Não significa que todas as formas sejam intercambiáveis.

### 632. adjunto de frase

**Construção:** Adjunto de frase modifica o enunciado ou a proposição como conjunto, expressando avaliação, enquadramento ou circunstância ampla.

**Função:** Distingue modificação global de modificação local do verbo.

**Dependências:** adjunto, frase, modalidade

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Felizmente, chegámos cedo.

**Não confundir com:** Não é argumento selecionado pelo verbo.

### 633. núcleo sintático

**Construção:** Núcleo sintático é a unidade que organiza propriedades centrais de um constituinte.

**Função:** Permite reconstruir sintagmas por dependência.

**Dependências:** núcleo, sintagma

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** livro em o livro novo

**Não confundir com:** Núcleo não é necessariamente a primeira palavra.

### 634. dependente sintático

**Construção:** Dependente sintático é unidade ligada a um núcleo por complemento, modificação, determinação ou outra relação.

**Função:** Materializa a direção de dependência no sintagma.

**Dependências:** núcleo sintático, relação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** novo depende de livro em livro novo

**Não confundir com:** Dependente não significa dispensável.

### 635. constituinte sintático

**Construção:** Constituinte sintático é grupo que funciona como unidade em alguma operação ou relação da frase.

**Função:** Permite segmentar a oração acima da palavra.

**Dependências:** sintagma, termo, relação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o livro novo

**Não confundir com:** Nem toda sequência contígua é constituinte.

### 636. fronteira de constituinte

**Construção:** Fronteira de constituinte é o limite estrutural entre unidades sintáticas.

**Função:** Ajuda a explicar ambiguidade e pontuação.

**Dependências:** constituinte sintático, segmentação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** [vi [o homem com binóculos]] em uma leitura

**Não confundir com:** Não é sempre espaço ou vírgula.

### 637. ordem básica

**Construção:** Ordem básica é o arranjo não marcado usado como referência numa construção e variedade.

**Função:** Serve de ponto de comparação para inversão e deslocamento.

**Dependências:** ordem, sujeito, verbo, complemento

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** sujeito antes do verbo em muitas declarações

**Não confundir com:** Básica não significa única nem superior.

### 638. ordem sujeito-verbo-objeto

**Construção:** Ordem sujeito-verbo-objeto dispõe esses três constituintes nessa sequência quando todos estão expressos.

**Função:** Materializa um padrão frequente de oração transitiva.

**Dependências:** ordem básica, sujeito, verbo, objeto direto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança leu o livro.

**Não confundir com:** Não descreve toda oração portuguesa.

### 639. inversão sintática

**Construção:** Inversão sintática altera a ordem de referência dos constituintes sem necessariamente alterar suas funções.

**Função:** Permite analisar ordens marcadas.

**Dependências:** ordem básica, constituinte sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Chegou a criança.

**Não confundir com:** Inverter não é trocar sujeito por objeto.

### 640. topicalização

**Construção:** Topicalização coloca uma unidade em posição de tópico para indicar sobre o que se fala.

**Função:** Liga ordem, tema e estrutura informacional.

**Dependências:** tópico discursivo, ordem básica, constituinte sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Esse livro, eu já li.

**Não confundir com:** Tópico não é sempre sujeito.

### 641. focalização

**Construção:** Focalização destaca a informação selecionada como nova, contrastiva ou corretiva.

**Função:** Liga sintaxe, prosódia e intenção.

**Dependências:** foco informacional, ordem, foco prosódico

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** FOI O LIVRO que ela leu.

**Não confundir com:** Foco não é sinónimo de tema.

### 642. deslocamento à esquerda

**Construção:** Deslocamento à esquerda coloca um constituinte antes da oração e pode retomá-lo dentro dela.

**Função:** Distingue tópico destacado de ordem argumental simples.

**Dependências:** topicalização, retomada, constituinte sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** O João, eu falei com ele.

**Não confundir com:** Não é necessariamente erro de repetição.

### 643. deslocamento à direita

**Construção:** Deslocamento à direita coloca um constituinte depois de uma oração que já contém elemento de retomada ou referência.

**Função:** Explica certos acréscimos pós-oracionais.

**Dependências:** retomada, constituinte sintático, ordem

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Eu falei com ele, com o João.

**Não confundir com:** Não é simples objeto em posição normal.

### 644. sujeito nulo

**Construção:** Sujeito nulo é participante de sujeito não realizado por sintagma expresso, mas recuperável ou estruturalmente admitido.

**Função:** Aprofunda sujeito oculto e concordância.

**Dependências:** sujeito oculto, concordância verbal, contexto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Cheguei cedo.

**Não confundir com:** Não é sujeito indeterminado por necessidade.

### 645. sujeito expresso

**Construção:** Sujeito expresso aparece por palavra ou sintagma identificável na oração.

**Função:** Contrasta com sujeito nulo.

**Dependências:** sujeito, sintagma nominal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança chegou.

**Não confundir com:** Expresso não significa enfatizado.

### 646. construção apresentativa

**Construção:** Construção apresentativa introduz uma entidade ou evento no discurso, frequentemente com ordem e verbo próprios.

**Função:** Liga sintaxe e introdução de referente.

**Dependências:** referente, estrutura informacional, ordem

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Chegou um visitante.

**Não confundir com:** Não é toda oração existencial.

### 647. predicação

**Construção:** Predicação é a relação pela qual algo é atribuído, afirmado ou organizado acerca de um participante ou situação.

**Função:** Fornece base comum a predicados verbais e nominais.

**Dependências:** predicado, relação, enunciado

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança corre; a criança está feliz.

**Não confundir com:** Não é apenas presença de verbo lexical.

### 648. oração finita

**Construção:** Oração finita possui verbo marcado por tempo ou modo finito e capaz de estabelecer relação de pessoa conforme o paradigma.

**Função:** Distingue orações desenvolvidas de formas não finitas.

**Dependências:** oração, tempo verbal, modo verbal, pessoa gramatical

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ela estuda.

**Não confundir com:** Locução verbal pode formar uma só oração finita.

### 649. oração não finita

**Construção:** Oração não finita organiza-se em torno de infinitivo, gerúndio ou particípio sem a mesma marcação finita.

**Função:** Generaliza orações reduzidas.

**Dependências:** oração, infinitivo, gerúndio, particípio

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ao chegar, telefonou.

**Não confundir com:** Não é frase sem verbo.

### 650. oração encaixada

**Construção:** Oração encaixada ocupa posição dentro da estrutura de outra unidade.

**Função:** Materializa dependência oracional interna.

**Dependências:** oração subordinada, constituinte sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** que venhas em espero que venhas

**Não confundir com:** Nem toda oração posterior está encaixada.

### 651. adjunto oracional

**Construção:** Adjunto oracional é oração que modifica outra oração ou predicação por circunstância ou enquadramento.

**Função:** Generaliza subordinadas adverbiais.

**Dependências:** oração subordinada adverbial, adjunto, predicação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Quando chegou, telefonou.

**Não confundir com:** Não é argumento selecionado em todos os casos.

### 652. oração temporal

**Construção:** Oração temporal localiza uma situação em relação temporal com outra.

**Função:** Materializa anterioridade, simultaneidade ou posterioridade discursiva.

**Dependências:** adjunto oracional, subordinação temporal, tempo verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Quando chegou, telefonou.

**Não confundir com:** Posição no texto não determina sozinha a ordem dos eventos.

### 653. oração final

**Construção:** Oração final apresenta finalidade atribuída a uma ação ou situação.

**Função:** Materializa relação de propósito.

**Dependências:** adjunto oracional, subordinação final, intenção comunicativa

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou para aprender.

**Não confundir com:** Finalidade não garante resultado.

### 654. oração comparativa

**Construção:** Oração comparativa estabelece comparação entre propriedades, quantidades ou situações.

**Função:** Materializa relação comparativa.

**Dependências:** adjunto oracional, subordinação comparativa, comparação figurada

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ela lê mais do que eu leio.

**Não confundir com:** Não é necessariamente metáfora.

### 655. oração conformativa

**Construção:** Oração conformativa apresenta uma situação segundo modelo, fonte ou maneira expressa por outra.

**Função:** Materializa relação de conformidade.

**Dependências:** adjunto oracional, subordinação conformativa, referência

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Fiz como combinámos.

**Não confundir com:** Não é oração comparativa em toda leitura.

### 656. significado lexical

**Construção:** Significado lexical é o conjunto de possibilidades de sentido associado a um lexema antes de um contexto específico.

**Função:** Distingue potencial lexical de interpretação concreta.

**Dependências:** lexema, sentido, acepção

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** banco pode ter mais de uma acepção

**Não confundir com:** Não é significado final do enunciado.

### 657. significado composicional

**Construção:** Significado composicional é o resultado construído pela combinação dos significados e das relações estruturais.

**Função:** Explica por que ordem e sintaxe alteram interpretação.

**Dependências:** significado lexical, sintaxe, relação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** cão morde homem difere de homem morde cão

**Não confundir com:** Não reduz todo sentido à soma de palavras.

### 658. significado da frase

**Construção:** Significado da frase é a interpretação estruturada disponível pela forma linguística sem fixar todo o contexto de uso.

**Função:** Separa estrutura linguística de uso concreto.

**Dependências:** significado composicional, frase

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** leitura possível de uma frase isolada

**Não confundir com:** Não é intenção real do falante.

### 659. significado do enunciado

**Construção:** Significado do enunciado é a interpretação da forma numa ocorrência contextual concreta.

**Função:** Liga frase, contexto, referência e intenção.

**Dependências:** significado da frase, enunciado, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** “Está frio” pode informar ou pedir fechamento da janela

**Não confundir com:** Não deve ser adivinhado sem evidência.

### 660. traço semântico

**Construção:** Traço semântico é uma propriedade abstrata usada para distinguir ou relacionar leituras lexicais.

**Função:** Permite testar compatibilidade entre palavras e predicados.

**Dependências:** sentido, oposição

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** animado / inanimado

**Não confundir com:** Não é necessariamente binário.

### 661. compatibilidade semântica

**Construção:** Compatibilidade semântica ocorre quando as propriedades de unidades permitem uma interpretação conjunta coerente.

**Função:** Ajuda a detectar seleção estranha sem declarar impossibilidade absoluta.

**Dependências:** traço semântico, coerência

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A criança bebe água.

**Não confundir com:** Estranheza não prova agramaticalidade.

### 662. predicado semântico

**Construção:** Predicado semântico representa propriedade ou relação atribuída a participantes ou situações.

**Função:** Permite analisar conteúdo além da forma verbal.

**Dependências:** predicação, sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** CORRER(x)

**Não confundir com:** Não exige notação lógica externa para existir.

### 663. argumento semântico

**Construção:** Argumento semântico é participante preenchendo uma posição de uma relação de sentido.

**Função:** Liga entidade, papel e predicado.

**Dependências:** predicado semântico, referente

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** a criança em “a criança corre”

**Não confundir com:** Pode não coincidir com argumento sintático em toda construção.

### 664. evento

**Construção:** Evento é ocorrência situada ou situável no tempo discursivo.

**Função:** Serve de base para aspecto, papéis e relações temporais.

**Dependências:** situação, tempo verbal

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** a abertura da porta

**Não confundir com:** Não é necessariamente instantâneo.

### 665. estado

**Construção:** Estado é situação apresentada sem mudança interna necessária no intervalo considerado.

**Função:** Contrasta leituras estáticas e dinâmicas.

**Dependências:** situação, aspecto verbal

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** saber uma resposta

**Não confundir com:** Estado pode mudar fora do intervalo.

### 666. processo

**Construção:** Processo é situação dinâmica apresentada em desenvolvimento, sem ponto final obrigatório na leitura.

**Função:** Distingue desenvolvimento de estado e resultado.

**Dependências:** evento, aspecto verbal

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** caminhar

**Não confundir com:** Pode receber limite por contexto.

### 667. mudança de estado

**Construção:** Mudança de estado é transição de uma condição para outra.

**Função:** Liga evento, resultado e aspecto.

**Dependências:** evento, estado, relação temporal

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** a porta abriu

**Não confundir com:** Não é todo processo.

### 668. telicidade

**Construção:** Telicidade é a presença de um ponto final interno que completa a situação na leitura considerada.

**Função:** Distingue eventos orientados a resultado de atividades abertas.

**Dependências:** evento, mudança de estado, aspecto verbal

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** ler o livro inteiro

**Não confundir com:** Tempo passado não garante telicidade.

### 669. quantificação

**Construção:** Quantificação constrói quantidade, extensão ou distribuição de uma referência.

**Função:** Liga numerais, determinantes e escopo.

**Dependências:** quantidade, referência, determinante

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** todos os livros; três livros

**Não confundir com:** Não é apenas numeral explícito.

### 670. quantificador universal

**Construção:** Quantificador universal apresenta a relação como aplicável a todos os membros do domínio contextual.

**Função:** Materializa leitura de totalidade.

**Dependências:** quantificação, domínio contextual

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** todas as crianças da turma

**Não confundir com:** Não prova existência do domínio.

### 671. quantificador existencial

**Construção:** Quantificador existencial apresenta pelo menos um membro do domínio contextual como participante.

**Função:** Materializa leitura de existência localizada.

**Dependências:** quantificação, existência, domínio contextual

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** alguma criança chegou

**Não confundir com:** Não identifica qual membro sem contexto.

### 672. escopo

**Construção:** Escopo é a parte da estrutura interpretativa sobre a qual um operador ou expressão exerce efeito.

**Função:** Explica ambiguidades de negação, quantificação e modalidade.

**Dependências:** relação, estrutura semântica

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** não + todos pode ter mais de uma leitura

**Não confundir com:** Não é posição linear apenas.

### 673. escopo da negação

**Construção:** Escopo da negação é a unidade cujo conteúdo é negado numa leitura.

**Função:** Distingue negação total, parcial e contrastiva.

**Dependências:** negação, escopo

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Não comprei TODOS os livros.

**Não confundir com:** A palavra não não nega sempre a frase inteira.

### 674. dêixis pessoal

**Construção:** Dêixis pessoal localiza participantes a partir de quem fala, ouve ou é referido.

**Função:** Aprofunda pessoa gramatical e pronomes.

**Dependências:** dêixis, pessoa gramatical, enunciado

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** eu, tu, nós em contexto

**Não confundir com:** A referência muda com o falante.

### 675. dêixis espacial

**Construção:** Dêixis espacial localiza entidades em relação ao ponto de referência discursivo.

**Função:** Liga demonstrativos, advérbios e contexto.

**Dependências:** dêixis, localização semântica, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** aqui; ali

**Não confundir com:** Distâncias variam por sistema de uso.

### 676. dêixis temporal

**Construção:** Dêixis temporal localiza situações em relação ao momento ou ponto temporal do enunciado.

**Função:** Liga advérbios e tempos verbais.

**Dependências:** dêixis, tempo verbal, contexto

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** hoje; amanhã

**Não confundir com:** O referente muda conforme a data do enunciado.

### 677. dêixis discursiva

**Construção:** Dêixis discursiva aponta para partes do próprio texto ou discurso.

**Função:** Ajuda a organizar referência metatextual.

**Dependências:** dêixis, texto, retomada

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** como veremos adiante

**Não confundir com:** Não aponta necessariamente para objeto externo.

### 678. cortesia linguística

**Construção:** Cortesia linguística é gestão verbal de distância, respeito, aproximação e impacto social numa interação.

**Função:** Explica escolhas de tratamento, pedido e mitigação.

**Dependências:** pragmática, registro, ato de fala

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Poderia ajudar-me?

**Não confundir com:** Cortesia formal não garante intenção benevolente.

### 679. macroestrutura textual

**Construção:** Macroestrutura textual é a organização global dos conteúdos principais de um texto.

**Função:** Permite resumir e verificar progressão além de frases isoladas.

**Dependências:** texto, tema, progressão temática

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** tema central e partes principais

**Não confundir com:** Não é apenas título.

### 680. microestrutura textual

**Construção:** Microestrutura textual é a rede local de palavras, frases, conectivos e retomadas que sustenta o texto.

**Função:** Liga coesão local à macroestrutura.

**Dependências:** texto, coesão, frase

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** relações entre frases vizinhas

**Não confundir com:** Não substitui coerência global.

### 681. organização retórica

**Construção:** Organização retórica é a disposição funcional de partes para informar, narrar, argumentar ou orientar.

**Função:** Relaciona intenção, gênero e estrutura textual.

**Dependências:** intenção comunicativa, gênero textual, tipo textual

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** problema → análise → solução

**Não confundir com:** Não é decoração estilística apenas.

### 682. relação de elaboração

**Construção:** Relação de elaboração ocorre quando um trecho desenvolve, exemplifica ou especifica outro.

**Função:** Materializa uma conexão de coerência.

**Dependências:** coerência, explicação, exemplificação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A planta cresceu. Novas folhas apareceram.

**Não confundir com:** Não é repetição idêntica.

### 683. relação de causa

**Construção:** Relação de causa liga uma situação tratada como razão para outra.

**Função:** Permite analisar conectivos e inferências causais.

**Dependências:** coerência, causa

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Choveu, por isso a rua molhou.

**Não confundir com:** Sequência temporal não prova causa.

### 684. relação de contraste

**Construção:** Relação de contraste aproxima conteúdos por diferença, oposição ou quebra de expectativa.

**Função:** Liga adversidade, concessão e antítese.

**Dependências:** coerência, oposição

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Estudou, mas não passou.

**Não confundir com:** Contraste não é contradição lógica automática.

### 685. relação de condição

**Construção:** Relação de condição apresenta uma situação como requisito, hipótese ou enquadramento de outra.

**Função:** Liga orações condicionais e raciocínio hipotético.

**Dependências:** coerência, hipótese

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Se houver tempo, iremos.

**Não confundir com:** Condição não afirma ocorrência.

### 686. relação de sequência

**Construção:** Relação de sequência ordena ações, estados ou partes no tempo ou na exposição.

**Função:** Sustenta instrução, narração e progressão.

**Dependências:** coerência, ordem

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** primeiro, depois, por fim

**Não confundir com:** Ordem textual e ordem real podem divergir.

### 687. estrutura narrativa

**Construção:** Estrutura narrativa organiza participantes, acontecimentos, tempo, espaço, conflito e desfecho.

**Função:** Aprofunda a narração como construção textual.

**Dependências:** narração, organização retórica

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** situação inicial → mudança → desfecho

**Não confundir com:** Não é fórmula obrigatória.

### 688. narrador

**Construção:** Narrador é a voz textual que apresenta a narrativa.

**Função:** Distingue voz narrativa de autor real.

**Dependências:** estrutura narrativa, voz discursiva

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** narrador em primeira pessoa

**Não confundir com:** Narrador não é automaticamente o autor.

### 689. personagem

**Construção:** Personagem é participante construído no universo narrativo.

**Função:** Permite acompanhar ações, estados e relações na narrativa.

**Dependências:** estrutura narrativa, referente

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** a protagonista do conto

**Não confundir com:** Não precisa corresponder a pessoa real.

### 690. enredo

**Construção:** Enredo é a organização dos acontecimentos narrados e de suas relações.

**Função:** Liga sequência, conflito e transformação.

**Dependências:** estrutura narrativa, evento, relação de sequência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** acontecimentos organizados numa história

**Não confundir com:** Não é simples lista cronológica.

### 691. espaço narrativo

**Construção:** Espaço narrativo é o lugar construído ou referido em que eventos da narrativa são situados.

**Função:** Liga descrição, dêixis e ação narrativa.

**Dependências:** estrutura narrativa, localização semântica

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** a aldeia onde ocorre a história

**Não confundir com:** Não é necessariamente lugar real.

### 692. tempo narrativo

**Construção:** Tempo narrativo é a organização temporal dos eventos e da sua apresentação no texto.

**Função:** Distingue ordem dos fatos, duração e momento da narração.

**Dependências:** estrutura narrativa, tempo verbal, relação temporal

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o texto começa pelo fim e retorna ao início

**Não confundir com:** Não é apenas tempo verbal.

### 693. conflito narrativo

**Construção:** Conflito narrativo é tensão entre objetivos, forças, valores ou situações que impulsiona transformação no enredo.

**Função:** Ajuda a explicar progressão de muitas narrativas.

**Dependências:** enredo, oposição

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** personagem quer partir, mas algo impede

**Não confundir com:** Não é discussão verbal por necessidade.

### 694. clímax

**Construção:** Clímax é ponto de máxima tensão ou viragem relevante numa organização narrativa.

**Função:** Localiza concentração estrutural do conflito.

**Dependências:** conflito narrativo, progressão

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** momento decisivo da história

**Não confundir com:** Não é sempre o final.

### 695. desfecho

**Construção:** Desfecho é a parte que apresenta resultado, fechamento ou nova estabilidade após a progressão narrativa.

**Função:** Relaciona conflito e conclusão.

**Dependências:** enredo, clímax, conclusão textual

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** resultado final da narrativa

**Não confundir com:** Não exige solução completa.

### 696. variedade nacional

**Construção:** Variedade nacional é conjunto de padrões associados ao uso do português num país ou comunidade nacional, sem apagar diversidade interna.

**Função:** Permite identificar contexto amplo sem declarar uma única norma total.

**Dependências:** variação regional, comunidade de fala, norma

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** português usado em Moçambique, descrito por evidência própria

**Não confundir com:** Não significa que todos os falantes usem a mesma forma.

### 697. língua primeira

**Construção:** Língua primeira é a língua ou conjunto de línguas adquirido inicialmente na vida de uma pessoa.

**Função:** Apoia análise de aquisição e repertório linguístico.

**Dependências:** aquisição da linguagem, repertório linguístico

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** duas línguas adquiridas desde cedo

**Não confundir com:** Não determina proficiência futura.

### 698. língua segunda

**Construção:** Língua segunda é língua adquirida depois ou além da primeira, em contexto social ou educativo.

**Função:** Distingue trajetória de aquisição sem hierarquizar valor.

**Dependências:** aquisição da linguagem, língua primeira, bilinguismo

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** português aprendido após outra língua inicial

**Não confundir com:** Não significa língua inferior.

### 699. texto-fonte

**Construção:** Texto-fonte é o texto tomado como ponto de partida numa operação de tradução.

**Função:** Define a origem material da reconstrução tradutória.

**Dependências:** tradução, texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** texto antes da tradução

**Não confundir com:** Não é fonte de verdade automática.

### 700. texto-alvo

**Construção:** Texto-alvo é o texto produzido na língua de chegada por uma operação de tradução.

**Função:** Define o produto que será comparado ao texto-fonte e ao objetivo.

**Dependências:** tradução, texto-fonte

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** texto depois da tradução

**Não confundir com:** Não deve copiar estrutura de origem cegamente.

### 701. unidade de tradução

**Construção:** Unidade de tradução é o trecho mínimo escolhido para resolver uma decisão tradutória sem perder relações necessárias.

**Função:** Impede traduzir sempre palavra por palavra.

**Dependências:** texto-fonte, texto-alvo, sentido

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma expressão fixa tratada como conjunto

**Não confundir com:** Não é tamanho fixo universal.

### 702. tradução literal

**Construção:** Tradução literal preserva de perto forma e ordem do texto-fonte quando isso continua funcional e fiel no texto-alvo.

**Função:** Serve como hipótese inicial controlada, não como regra absoluta.

**Dependências:** unidade de tradução, equivalência tradutória

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** tradução próxima quando as estruturas correspondem

**Não confundir com:** Literal não significa automaticamente correta.

### 703. tradução funcional

**Construção:** Tradução funcional prioriza a função e o efeito comunicativo relevante no texto-alvo, preservando o conteúdo justificável.

**Função:** Permite afastar-se da forma quando necessário e explicado.

**Dependências:** unidade de tradução, intenção comunicativa, adequação linguística

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** adaptar uma instrução para funcionar na língua-alvo

**Não confundir com:** Não é liberdade para inventar conteúdo.

### 704. interferência linguística

**Construção:** Interferência linguística é influência de uma língua ou variedade sobre o uso de outra no repertório do falante.

**Função:** Ajuda a investigar transferências sem tratar diferença como incapacidade.

**Dependências:** contacto linguístico, língua primeira, língua segunda

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** ordem transferida de outra língua, quando comprovada

**Não confundir com:** Não é sempre erro.

### 705. consciência linguística

**Construção:** Consciência linguística é capacidade de observar e refletir sobre formas, sentidos e usos da própria linguagem.

**Função:** Liga aprendizagem, revisão e metalinguagem.

**Dependências:** metalinguagem, análise linguística, revisão

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** perceber por que duas frases diferem

**Não confundir com:** Não exige decorar terminologia.

### 706. dado linguístico

**Construção:** Dado linguístico é ocorrência, forma, julgamento ou medida registrada para análise.

**Função:** Fornece matéria observável para hipóteses.

**Dependências:** corpus local, exemplo de uso, marca

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma frase registrada com contexto

**Não confundir com:** Não é interpretação pronta.

### 707. observação linguística

**Construção:** Observação linguística é descrição inicial do que aparece nos dados antes de explicar por quê.

**Função:** Separa ocorrência e hipótese.

**Dependências:** dado linguístico, descrição linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** esta forma aparece antes do nome em cinco casos

**Não confundir com:** Não é causa nem regra definitiva.

### 708. análise fonológica

**Construção:** Análise fonológica reconstrói unidades e oposições sonoras relevantes num sistema definido.

**Função:** Aplica fonema, sílaba, prosódia e processos.

**Dependências:** fonema, oposição fonológica, fonotática

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** comparar pares e posições sonoras

**Não confundir com:** Não é transcrição fonética completa.

### 709. análise morfológica

**Construção:** Análise morfológica segmenta e relaciona base, morfemas, flexão e formação de palavra.

**Função:** Aplica o conhecimento da estrutura da palavra.

**Dependências:** morfema, base lexical, flexão, derivação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** in-feliz-mente

**Não confundir com:** Não é separar letras arbitrariamente.

### 710. análise sintática

**Construção:** Análise sintática identifica constituintes, núcleos, dependências, funções e relações oracionais.

**Função:** Aplica o conhecimento estrutural da frase.

**Dependências:** constituinte sintático, núcleo sintático, dependente sintático, oração

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** identificar sujeito, verbo e complemento

**Não confundir com:** Não é apenas nomear classes de palavras.

### 711. análise pragmática

**Construção:** Análise pragmática examina o que uma forma faz numa situação comunicativa e quais inferências o contexto sustenta.

**Função:** Aplica atos de fala, dêixis, cortesia e implicatura.

**Dependências:** pragmática, ato de fala, contexto, implicatura

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** pedido indireto em situação documentada

**Não confundir com:** Não é leitura psicológica do falante.

### 712. análise textual

**Construção:** Análise textual examina coesão, coerência, estrutura, gênero, progressão e vozes num texto.

**Função:** Integra níveis linguísticos acima da frase.

**Dependências:** texto, macroestrutura textual, microestrutura textual, gênero textual

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** mapear tese, conectivos e retomadas

**Não confundir com:** Não é resumo por necessidade.

### 713. anotação linguística

**Construção:** Anotação linguística associa marcas explícitas a unidades de dado segundo um esquema definido.

**Função:** Permite tornar análises comparáveis e testáveis.

**Dependências:** dado linguístico, marca

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** marcar palavra como verbo com justificativa

**Não confundir com:** Anotação não transforma hipótese em fato.

### 714. segmentação de corpus

**Construção:** Segmentação de corpus divide dados em documentos, frases, tokens ou outras unidades preservando rastreabilidade.

**Função:** Prepara análise sem perder origem.

**Dependências:** corpus local, segmentação gráfica, dado linguístico

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** documento → frases → tokens

**Não confundir com:** Não é apagar contexto.

### 715. classificação linguística

**Construção:** Classificação linguística atribui categoria a uma unidade com critérios, evidência e possibilidade de revisão.

**Função:** Organiza análise sem fingir certeza absoluta.

**Dependências:** classe gramatical, anotação linguística, critério

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** classificar “claro” como adjetivo ou advérbio conforme construção

**Não confundir com:** Não é rotulagem sem contexto.

### 716. carta

**Construção:** Carta é gênero dirigido a destinatário, organizado por situação de comunicação, abertura, corpo e fechamento variáveis.

**Função:** Permite analisar voz, destinatário e finalidade.

**Dependências:** gênero textual, destinatário, texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** carta pessoal ou formal

**Não confundir com:** Não é formato único obrigatório.

### 717. correio eletrónico

**Construção:** Correio eletrónico é gênero digital de mensagem com destinatário, assunto, corpo e metadados de envio.

**Função:** Relaciona escrita, registro e comunicação assíncrona.

**Dependências:** gênero digital, destinatário, registro

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** mensagem de trabalho por email

**Não confundir com:** Não é sinónimo de carta em todos os usos.

### 718. aviso

**Construção:** Aviso é gênero breve que informa, alerta ou orienta um público sobre situação específica.

**Função:** Exige clareza, destinatário e ação relevante.

**Dependências:** gênero textual, intenção comunicativa, concisão

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Aviso: porta fechada.

**Não confundir com:** Não é notícia detalhada.

### 719. notícia

**Construção:** Notícia é gênero informativo que apresenta acontecimento considerado relevante com identificação de fontes, tempo, lugar e participantes quando disponíveis.

**Função:** Organiza informação factual e atribuição.

**Dependências:** gênero informativo, evidência, referência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** texto jornalístico sobre acontecimento verificado

**Não confundir com:** Não é opinião disfarçada.

### 720. reportagem

**Construção:** Reportagem é gênero informativo ampliado que investiga tema ou acontecimento por múltiplas fontes, contexto e descrição.

**Função:** Aprofunda informação além do anúncio inicial.

**Dependências:** notícia, pesquisa, citação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** reportagem com entrevistas e dados

**Não confundir com:** Não é simples notícia longa.

### 721. entrevista

**Construção:** Entrevista é gênero organizado por interação entre quem pergunta e quem responde, com finalidade e contexto definidos.

**Função:** Permite analisar turnos, perguntas, respostas e edição.

**Dependências:** diálogo, turno de fala, intenção comunicativa

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** pergunta seguida de resposta registrada

**Não confundir com:** Não transforma resposta em verdade automática.

### 722. artigo de opinião

**Construção:** Artigo de opinião é gênero em que uma voz defende tese sobre tema público por argumentos identificáveis.

**Função:** Integra tese, evidência, contra-argumento e estilo autoral.

**Dependências:** argumentação, tese, gênero textual

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** texto que defende uma posição

**Não confundir com:** Opinião não dispensa justificativa.

### 723. ensaio

**Construção:** Ensaio é gênero reflexivo que explora uma questão por argumentação, interpretação e voz autoral, podendo manter abertura.

**Função:** Permite investigação escrita sem exigir formato experimental único.

**Dependências:** argumentação, interpretação, estilo

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** ensaio sobre linguagem

**Não confundir com:** Não é ausência de rigor.

### 724. requerimento

**Construção:** Requerimento é gênero formal pelo qual alguém solicita providência a uma autoridade ou instituição identificada.

**Função:** Organiza destinatário, pedido, fundamento e identificação.

**Dependências:** gênero formal, ato diretivo, destinatário

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** pedido formal documentado

**Não confundir com:** Não garante deferimento.

### 725. instrução procedural

**Construção:** Instrução procedural é texto que ordena ações para alcançar resultado ou executar tarefa.

**Função:** Exige sequência, condições e critérios de conclusão.

**Dependências:** instrução, relação de sequência, clareza

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** abra o ficheiro; execute o teste; verifique o resultado

**Não confundir com:** Não é descrição do que já aconteceu.

### 726. receita textual

**Construção:** Receita textual é gênero procedural que relaciona materiais, quantidades e passos para produzir um resultado.

**Função:** Materializa instrução com dependências e ordem.

**Dependências:** instrução procedural, quantificação, relação de sequência

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** ingredientes e modo de preparo

**Não confundir com:** Não é prova científica do resultado.

### 727. poema

**Construção:** Poema é gênero verbal organizado por escolhas de ritmo, imagem, som, disposição e condensação de sentido, com grande variação formal.

**Função:** Permite analisar função estética sem exigir uma forma única.

**Dependências:** gênero literário, ritmo, figura de linguagem

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** texto em versos ou prosa poética

**Não confundir com:** Poema não é definido apenas por rima.

### 728. conto

**Construção:** Conto é gênero narrativo de extensão relativamente concentrada, organizado por seleção de eventos, personagens e efeito.

**Função:** Aplica estrutura narrativa em forma curta.

**Dependências:** gênero literário, estrutura narrativa, concisão

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** narrativa curta

**Não confundir com:** Curto não significa simples.

### 729. romance

**Construção:** Romance é gênero narrativo extenso capaz de desenvolver múltiplos eventos, personagens, tempos e espaços.

**Função:** Permite analisar macroestrutura narrativa complexa.

**Dependências:** gênero literário, estrutura narrativa, macroestrutura textual

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** narrativa longa

**Não confundir com:** Não é apenas história amorosa.

### 730. peça teatral

**Construção:** Peça teatral é texto concebido para representação por falas, ações, cenas e indicações cénicas.

**Função:** Liga diálogo escrito e performance.

**Dependências:** gênero dramático, diálogo, multimodalidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** falas de personagens e rubricas

**Não confundir com:** Não é diálogo cotidiano transcrito.

### 731. diálogo escrito

**Construção:** Diálogo escrito representa ou constrói alternância de vozes por falas, marcas gráficas e contexto textual.

**Função:** Permite analisar turnos sem som presente.

**Dependências:** diálogo, travessão de diálogo, discurso direto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** — Vais? — Vou.

**Não confundir com:** Não reproduz toda a prosódia da fala.

### 732. regularidade linguística

**Construção:** Regularidade linguística é comportamento recorrente que pode ser descrito por condição e padrão.

**Função:** Serve de base para regras e paradigmas.

**Dependências:** relação, uso, observação linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** formas que seguem a mesma terminação

**Não confundir com:** Não é universalidade automática.

### 733. irregularidade linguística

**Construção:** Irregularidade linguística é comportamento que diverge de uma regularidade definida dentro do mesmo domínio.

**Função:** Permite criar subclasse sem fingir ausência total de estrutura.

**Dependências:** regularidade linguística, oposição

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** forma que alterna o radical

**Não confundir com:** Não é caos.

### 734. comparação

**Construção:** Comparação é operação que aproxima unidades por semelhanças e diferenças segundo critério.

**Função:** Sustenta testes, figuras e argumentação.

**Dependências:** diferença, relação, critério

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** comparar duas frases pela ordem

**Não confundir com:** Não é equivalência automática.

### 735. papel semântico

**Construção:** Papel semântico é a relação interpretativa de um participante com um evento ou estado.

**Função:** Generaliza agente, paciente, experienciador e outros papéis.

**Dependências:** argumento semântico, situação

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** agente de abrir

**Não confundir com:** Não é função sintática.

### 736. indeterminação

**Construção:** Indeterminação é ausência de informação suficiente para escolher entre análises possíveis.

**Função:** Permite declarar limite sem fingir.

**Dependências:** ambiguidade, lacuna de conhecimento

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** contexto insuficiente

**Não confundir com:** Não é erro obrigatório.

### 737. resultado

**Construção:** Resultado é estado ou produto obtido após procedimento, teste ou transformação.

**Função:** Separa execução, observação e conclusão.

**Dependências:** procedimento, observação linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** teste passou em 10 casos

**Não confundir com:** Não é causa nem explicação.

### 738. ausência de vírgula entre sujeito e predicado

**Construção:** Na ordem contínua básica, sujeito e predicado não são separados por vírgula apenas por serem longos.

**Função:** Constrói uma restrição negativa essencial.

**Dependências:** vírgula, sujeito, predicado, ordem básica

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** A criança atenta leu o texto.

**Não confundir com:** A restrição não proíbe vírgulas que isolam intercalações.

### 739. dois-pontos explicativos

**Construção:** Dois-pontos explicativos introduzem desenvolvimento, esclarecimento, consequência anunciada ou enumeração ligada ao trecho anterior.

**Função:** Distingue uma relação de expansão textual.

**Dependências:** dois-pontos, relação de elaboração, coesão

**Tema de consulta:** `pontuacao`

**Exemplo mínimo:** Havia um problema: faltava água.

**Não confundir com:** Não substituem qualquer conectivo.

### 740. composição sintagmática

**Construção:** Composição sintagmática estabiliza uma combinação de palavras como unidade lexical, mesmo mantendo separação gráfica.

**Função:** Explica unidades complexas não reduzidas a uma palavra gráfica.

**Dependências:** composição, sintagma, lexicalização

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** fim de semana

**Não confundir com:** Não é qualquer sequência ocasional.

### 741. bloqueio morfológico

**Construção:** Bloqueio morfológico ocorre quando uma forma existente ou restrição impede uma formação esperada de circular normalmente.

**Função:** Explica por que padrão produtivo não gera toda forma imaginável.

**Dependências:** produtividade morfológica, irregularidade linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** forma concorrente já estabilizada

**Não confundir com:** Não é proibição lógica absoluta.

### 742. substantivo contável

**Construção:** Substantivo contável admite contagem por unidades discretas na construção relevante.

**Função:** Relaciona nome, numeral e quantificação.

**Dependências:** nome, numeral cardinal, quantificação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** três livros

**Não confundir com:** Não é propriedade imutável fora do uso.

### 743. substantivo massivo

**Construção:** Substantivo massivo apresenta matéria ou quantidade sem unidades discretas obrigatórias na leitura relevante.

**Função:** Distingue contagem direta de medição ou porção.

**Dependências:** nome, quantificação, contexto

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** água

**Não confundir com:** Não significa que a realidade não possa ser medida.

### 744. substantivo animado

**Construção:** Substantivo animado recebe leitura ligada a ser vivo ou agente potencial na construção.

**Função:** Apoia restrições semânticas e pronominais.

**Dependências:** nome, traço semântico

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** criança

**Não confundir com:** Animado é traço de leitura, não classe biológica completa.

### 745. substantivo inanimado

**Construção:** Substantivo inanimado recebe leitura sem vida própria no contexto comum.

**Função:** Contrasta com leitura animada em seleção semântica.

**Dependências:** nome, traço semântico

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** pedra

**Não confundir com:** Não impede uso como agente figurado.

### 746. pronome de tratamento

**Construção:** Pronome ou expressão de tratamento seleciona modo social de dirigir-se ou referir-se ao interlocutor.

**Função:** Liga pessoa gramatical, cortesia e concordância.

**Dependências:** pronome, cortesia linguística, pessoa gramatical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** você; senhor, conforme contexto

**Não confundir com:** Forma de tratamento não equivale sempre à pessoa morfológica do verbo.

### 747. verbo irregular

**Construção:** Verbo irregular apresenta alternância de radical, terminação ou forma que não segue integralmente o padrão regular de sua classe.

**Função:** Marca onde o paradigma exige memória e construção própria.

**Dependências:** verbo, conjugação, irregularidade linguística

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** ser; ir, em formas específicas

**Não confundir com:** Irregular não significa sem regra.

### 748. construção impessoal

**Construção:** Construção impessoal organiza predicação sem participante referencial funcionando como sujeito comum.

**Função:** Reúne fenômenos como certos meteorológicos e existenciais.

**Dependências:** oração sem sujeito, predicação

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Choveu.

**Não confundir com:** Não é sujeito oculto.

### 749. construção existencial

**Construção:** Construção existencial apresenta a existência ou ocorrência de uma entidade ou situação.

**Função:** Distingue apresentação de posse e ação transitiva.

**Dependências:** construção impessoal, existência, referência

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Há livros na mesa.

**Não confundir com:** Não é necessariamente construção possessiva.

### 750. predicado de estado

**Construção:** Predicado de estado apresenta condição relativamente estável ou não delimitada como ação dinâmica.

**Função:** Relaciona aspecto e tipo de predicação.

**Dependências:** predicação, estado, aspecto verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A porta está aberta.

**Não confundir com:** Estado não significa permanência eterna.

### 751. predicado de evento

**Construção:** Predicado de evento apresenta ocorrência, ação ou mudança localizada no tempo discursivo.

**Função:** Contrasta com leitura estática.

**Dependências:** predicação, evento, tempo verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A criança abriu a porta.

**Não confundir com:** Evento não é sinónimo de acontecimento público.

### 752. oração matriz

**Construção:** Oração matriz contém ou seleciona outra oração no recorte analisado.

**Função:** Distingue nível externo de encaixamento.

**Dependências:** oração principal, oração encaixada

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Espero [que venhas].

**Não confundir com:** Matriz não significa primeira na ordem linear.

### 753. oração causal

**Construção:** Oração causal apresenta situação tratada como causa ou razão de outra.

**Função:** Materializa a relação causal numa unidade oracional.

**Dependências:** adjunto oracional, subordinação causal, relação de causa

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Saiu porque estava cansado.

**Não confundir com:** Não é automaticamente prova factual da causa.

### 754. oração condicional

**Construção:** Oração condicional apresenta condição sob a qual outra situação é considerada.

**Função:** Materializa relação condicional.

**Dependências:** adjunto oracional, subordinação condicional, relação de condição

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Se chover, ficaremos.

**Não confundir com:** Condição não implica que ocorrerá.

### 755. oração concessiva

**Construção:** Oração concessiva apresenta obstáculo que não impede a situação principal.

**Função:** Materializa contraste concessivo.

**Dependências:** adjunto oracional, subordinação concessiva, relação de contraste

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Embora cansado, continuou.

**Não confundir com:** Não é simples adversidade coordenada.

### 756. oração consecutiva

**Construção:** Oração consecutiva apresenta consequência ligada a intensidade, condição ou situação anterior.

**Função:** Materializa relação de consequência.

**Dependências:** adjunto oracional, subordinação consecutiva, relação de causa

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou tanto que aprendeu.

**Não confundir com:** Consequência discursiva não prova causalidade universal.

### 757. seleção semântica

**Construção:** Seleção semântica é a restrição de leitura que um predicado exerce sobre seus participantes.

**Função:** Liga sentido verbal e papéis semânticos.

**Dependências:** compatibilidade semântica, predicado semântico, argumento semântico

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** beber seleciona algo interpretável como líquido em leitura comum

**Não confundir com:** Não é seleção sintática completa.

### 758. dêixis social

**Construção:** Dêixis social marca relações sociais por formas de tratamento, títulos ou escolhas linguísticas.

**Função:** Liga cortesia, registro e pessoa.

**Dependências:** dêixis, pronome de tratamento, registro

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** senhor em contexto formal

**Não confundir com:** Não define valor humano do interlocutor.

### 759. evidência argumentativa

**Construção:** Evidência argumentativa é dado, exemplo, observação ou resultado usado para apoiar uma afirmação.

**Função:** Liga argumento a fundamento verificável.

**Dependências:** argumentação, dado linguístico, exemplo de uso

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** resultado de teste citado com fonte

**Não confundir com:** Evidência não é garantia absoluta.

### 760. garantia argumentativa

**Construção:** Garantia argumentativa é a regra ou relação que explica por que a evidência apoia a tese.

**Função:** Torna explícita a passagem entre dado e conclusão.

**Dependências:** evidência argumentativa, inferência, tese

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** se o teste mede a capacidade, melhora no teste apoia melhora da capacidade

**Não confundir com:** Não é a evidência em si.

### 761. hipótese linguística

**Construção:** Hipótese linguística é explicação provisória sobre padrão de língua que precisa ser testada por exemplos e contraexemplos.

**Função:** Formaliza investigação sem fingir certeza.

**Dependências:** observação linguística, inferência, hipótese

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** tal posição pode favorecer esta forma

**Não confundir com:** Não é conhecimento aprovado antes do teste.

### 762. evidência linguística

**Construção:** Evidência linguística é material observável que sustenta ou enfraquece uma análise.

**Função:** Liga conhecimento a dados, testes e rastreabilidade.

**Dependências:** dado linguístico, observação linguística, exemplo de uso

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** exemplos de fala, escrita ou julgamento documentado

**Não confundir com:** Não é autoridade sem análise.

### 763. teste linguístico

**Construção:** Teste linguístico é operação controlada que compara previsão e comportamento de formas ou interpretações.

**Função:** Permite aceitar, restringir ou rejeitar hipótese.

**Dependências:** hipótese linguística, evidência linguística, comparação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** substituir um constituinte e observar a estrutura

**Não confundir com:** Um teste isolado não decide toda análise.

### 764. exemplo positivo

**Construção:** Exemplo positivo é ocorrência que satisfaz a construção ou previsão examinada.

**Função:** Mostra pelo menos um caso de funcionamento.

**Dependências:** exemplo de uso, teste linguístico

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** frase que respeita a regra construída

**Não confundir com:** Não prova universalidade.

### 765. exemplo negativo

**Construção:** Exemplo negativo é forma rejeitada, inadequada ou incompatível sob critérios e contexto explicitados.

**Função:** Ajuda a localizar limites da construção.

**Dependências:** teste linguístico, aceitabilidade, contexto

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** forma marcada como inadequada num contexto definido

**Não confundir com:** Não deve ser inventado sem julgamento ou derivação clara.

### 766. generalização linguística

**Construção:** Generalização linguística é padrão formulado a partir de múltiplas observações relacionadas.

**Função:** Transforma dados em regra provisória auditável.

**Dependências:** observação linguística, hipótese linguística, evidência linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** neste conjunto, a forma X ocorre neste ambiente

**Não confundir com:** Não é lei universal por padrão.

### 767. restrição linguística

**Construção:** Restrição linguística é condição que limita combinação, interpretação ou uso de uma forma.

**Função:** Complementa regras produtivas com fronteiras explícitas.

**Dependências:** regularidade linguística, contexto

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** esta combinação não ocorre nesta posição

**Não confundir com:** Não é proibição social necessariamente.

### 768. descrição operacional

**Construção:** Descrição operacional especifica como observar ou testar um conceito por passos reproduzíveis.

**Função:** Transforma definição em capacidade verificável.

**Dependências:** descrição linguística, teste linguístico, procedimento

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** tokenizar, identificar núcleo, verificar dependências

**Não confundir com:** Não é apenas definição verbal.

### 769. análise semântica

**Construção:** Análise semântica reconstrói sentidos, referências, papéis, escopos e relações interpretativas permitidas pela forma.

**Função:** Aplica o conhecimento de significado.

**Dependências:** significado composicional, referência, escopo, papel semântico

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** detectar duas leituras possíveis

**Não confundir com:** Não é adivinhar intenção.

### 770. confiança analítica

**Construção:** Confiança analítica expressa o grau de sustentação de uma análise pela informação disponível.

**Função:** Permite responder com medida de certeza em vez de fingir.

**Dependências:** evidência linguística, indeterminação

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** alta quando forma e contexto convergem; baixa quando faltam dados

**Não confundir com:** Não é probabilidade objetiva sem calibração.

### 771. indeterminação analítica

**Construção:** Indeterminação analítica é o estado em que mais de uma análise permanece possível ou faltam dados para decidir.

**Função:** Preserva honestidade diante de ambiguidade e ausência de contexto.

**Dependências:** ambiguidade, confiança analítica, lacuna de conhecimento

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** duas leituras possíveis sem contexto

**Não confundir com:** Não é falha a esconder.

### 772. relatório

**Construção:** Relatório é gênero que registra objetivo, procedimento, observações, resultados e pendências de uma atividade.

**Função:** Preserva rastreabilidade e continuidade.

**Dependências:** gênero textual, descrição operacional, resultado

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** relatório de teste

**Não confundir com:** Não é conhecimento puro por si só.

### 773. ata

**Construção:** Ata é gênero de registro de reunião, decisões e ocorrências em ordem verificável.

**Função:** Preserva memória institucional sem transformar decisão em verdade universal.

**Dependências:** relatório, relação de sequência, citação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** ata de reunião

**Não confundir com:** Não é transcrição integral por necessidade.

### 774. valência verbal

**Construção:** Valência verbal é o número e o tipo de participantes que um verbo pode selecionar numa leitura.

**Função:** Liga transitividade, complementos e sentido verbal.

**Dependências:** verbo, transitividade verbal, seleção semântica

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** dar pode envolver quem dá, o que é dado e a quem

**Não confundir com:** Não é apenas número de palavras depois do verbo.

### 775. argumento sintático

**Construção:** Argumento sintático é constituinte exigido ou licenciado pela estrutura de um núcleo numa leitura.

**Função:** Distingue participantes estruturais de modificadores opcionais.

**Dependências:** valência verbal, constituinte sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o livro em ler o livro

**Não confundir com:** Não é argumento lógico por necessidade.

### 776. argumento interno

**Construção:** Argumento interno é participante construído dentro do domínio do predicado, frequentemente como objeto ou complemento.

**Função:** Organiza relações entre verbo e complementos.

**Dependências:** argumento sintático, predicado

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o texto em ler o texto

**Não confundir com:** Não é sinónimo obrigatório de objeto direto.

### 777. argumento externo

**Construção:** Argumento externo é participante ligado ao predicado a partir de posição externa ao núcleo verbal, frequentemente associado ao sujeito.

**Função:** Relaciona predicação e sujeito.

**Dependências:** argumento sintático, sujeito, predicado

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** a criança em a criança leu

**Não confundir com:** Não é sempre agente semântico.

### 778. estrutura argumental

**Construção:** Estrutura argumental é a organização conjunta dos argumentos selecionados por um predicado.

**Função:** Permite comparar leituras e construções verbais.

**Dependências:** argumento interno, argumento externo, valência verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** quem faz, o que ocorre e a quem afeta

**Não confundir com:** Não é a ordem superficial completa da frase.

### 779. complemento verbal

**Construção:** Complemento verbal completa a estrutura de um verbo numa leitura, com ou sem preposição.

**Função:** Reúne objetos e outros complementos selecionados.

**Dependências:** verbo, complemento, valência verbal

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** ler o livro; gostar de música

**Não confundir com:** Não é todo termo posterior ao verbo.

### 780. complemento oracional

**Construção:** Complemento oracional é oração selecionada como argumento de verbo, nome ou adjetivo.

**Função:** Generaliza completivas em diferentes núcleos.

**Dependências:** oração encaixada, complemento, argumento sintático

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Espero que venhas.

**Não confundir com:** Não é toda oração subordinada.

### 781. interlíngua

**Construção:** Interlíngua é sistema provisório construído por quem aprende outra língua, com regularidades próprias e em mudança.

**Função:** Permite analisar aquisição sem reduzir tudo a falhas aleatórias.

**Dependências:** língua segunda, aquisição da linguagem, hipótese linguística

**Tema de consulta:** `variacao_letramento`

**Exemplo mínimo:** padrões estáveis durante aprendizagem

**Não confundir com:** Não é língua inferior nem conjunto sem regra.

### 782. contraexemplo linguístico

**Construção:** Contraexemplo linguístico é ocorrência que contradiz uma generalização ou delimita seu alcance.

**Função:** Impede regras absolutas construídas por poucos exemplos.

**Dependências:** hipótese linguística, exemplo negativo, generalização linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma frase aceite que a regra previa rejeitar

**Não confundir com:** Não invalida necessariamente toda a hipótese; pode restringi-la.

### 783. exceção linguística

**Construção:** Exceção linguística é ocorrência que fica fora de uma generalização dentro do mesmo domínio declarado.

**Função:** Obriga a restringir regra ou construir subclasse.

**Dependências:** generalização linguística, contraexemplo linguístico

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** item lexical que não segue o padrão regular

**Não confundir com:** Não é desculpa para abandonar toda regularidade.

### 784. regra linguística

**Construção:** Regra linguística é relação explícita entre condições e comportamento de formas num domínio delimitado.

**Função:** Permite prever, testar e explicar sem esconder dependências.

**Dependências:** generalização linguística, restrição linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** se condição A, então forma B neste domínio

**Não confundir com:** Não é ordem moral.

### 785. traço distintivo

**Construção:** propriedade mínima que separa fonemas ou classes de sons

**Função:** Permite reconhecer, explicar e testar traço distintivo na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/ e /b/ distinguem-se pelo vozeamento

### 786. sonoridade fonológica

**Construção:** grau relativo de abertura e ressonância usado para organizar sequências sonoras

**Função:** Permite reconhecer, explicar e testar sonoridade fonológica na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** vogais costumam formar o pico de sonoridade da sílaba

### 787. obstruinte

**Construção:** classe de consoante produzida com obstrução relevante da corrente de ar

**Função:** Permite reconhecer, explicar e testar obstruinte na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/, /t/, /k/, /f/ e /s/ são obstruintes

### 788. soante

**Construção:** classe de som com passagem relativamente livre e ressonância predominante

**Função:** Permite reconhecer, explicar e testar soante na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** vogais, nasais e laterais são soantes

### 789. labialidade

**Construção:** traço relacionado à participação dos lábios na articulação

**Função:** Permite reconhecer, explicar e testar labialidade na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /p/ e /m/ apresentam labialidade

### 790. coronalidade

**Construção:** traço relacionado à ação da ponta ou lâmina da língua

**Função:** Permite reconhecer, explicar e testar coronalidade na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /t/, /s/ e /n/ são tipicamente coronais

### 791. dorsalidade

**Construção:** traço relacionado à parte posterior da língua

**Função:** Permite reconhecer, explicar e testar dorsalidade na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /k/ e /g/ apresentam dorsalidade

### 792. altura vocálica

**Construção:** posição vertical relativa da língua na produção de vogal

**Função:** Permite reconhecer, explicar e testar altura vocálica na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /i/ é alta e /a/ é baixa

### 793. anterioridade vocálica

**Construção:** posição anterior ou posterior da língua na produção vocálica

**Função:** Permite reconhecer, explicar e testar anterioridade vocálica na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /i/ é anterior e /u/ é posterior

### 794. arredondamento vocálico

**Construção:** configuração arredondada dos lábios em certas vogais

**Função:** Permite reconhecer, explicar e testar arredondamento vocálico na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /u/ costuma ser arredondada

### 795. vogal anterior

**Construção:** vogal produzida com a língua avançada

**Função:** Permite reconhecer, explicar e testar vogal anterior na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /i/ em vida

### 796. vogal central

**Construção:** vogal produzida em posição central da cavidade oral

**Função:** Permite reconhecer, explicar e testar vogal central na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a vogal átona final de certas variedades pode centralizar-se

### 797. vogal posterior

**Construção:** vogal produzida com a língua recuada

**Função:** Permite reconhecer, explicar e testar vogal posterior na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /u/ em tudo

### 798. vogal alta

**Construção:** vogal produzida com pouca abertura oral

**Função:** Permite reconhecer, explicar e testar vogal alta na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /i/ e /u/

### 799. vogal média

**Construção:** vogal produzida com abertura intermediária

**Função:** Permite reconhecer, explicar e testar vogal média na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /e/, /ê/, /o/ e /ô/

### 800. vogal baixa

**Construção:** vogal produzida com maior abertura oral

**Função:** Permite reconhecer, explicar e testar vogal baixa na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /a/

### 801. semivogal anterior

**Construção:** elemento vocálico não nuclear aproximado de /j/

**Função:** Permite reconhecer, explicar e testar semivogal anterior na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pai contém semivogal anterior na análise comum

### 802. semivogal posterior

**Construção:** elemento vocálico não nuclear aproximado de /w/

**Função:** Permite reconhecer, explicar e testar semivogal posterior na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** pau contém semivogal posterior na análise comum

### 803. africada

**Construção:** consoante iniciada por oclusão e liberada com fricção

**Função:** Permite reconhecer, explicar e testar africada na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** certas realizações de t em tia são africadas

### 804. aproximante

**Construção:** som produzido com aproximação sem fricção forte

**Função:** Permite reconhecer, explicar e testar aproximante na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** semivogais funcionam como aproximantes

### 805. tepe

**Construção:** vibrante produzida por um contacto muito breve

**Função:** Permite reconhecer, explicar e testar tepe na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** r intervocálico de caro em muitas variedades

### 806. vibrante múltipla

**Construção:** vibrante produzida por contactos repetidos

**Função:** Permite reconhecer, explicar e testar vibrante múltipla na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** r forte pode realizar-se como vibrante múltipla em algumas variedades

### 807. retroflexão

**Construção:** articulação com a ponta da língua curvada para trás

**Função:** Permite reconhecer, explicar e testar retroflexão na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** r caipira pode apresentar retroflexão

### 808. palatalização

**Construção:** mudança articulatória em direção à região palatal

**Função:** Permite reconhecer, explicar e testar palatalização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** t pode palatalizar antes de i em certas variedades

### 809. velarização

**Construção:** articulação secundária em direção ao véu palatino

**Função:** Permite reconhecer, explicar e testar velarização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** l em final de sílaba pode velarizar-se em certas variedades

### 810. labialização

**Construção:** articulação secundária com arredondamento dos lábios

**Função:** Permite reconhecer, explicar e testar labialização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** uma consoante pode ganhar componente labial junto de vogal arredondada

### 811. nasalização

**Construção:** propagação ou atribuição de ressonância nasal

**Função:** Permite reconhecer, explicar e testar nasalização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** a vogal de canto é nasalizada

### 812. desnasalização

**Construção:** perda de nasalidade numa realização ou mudança

**Função:** Permite reconhecer, explicar e testar desnasalização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** uma forma pode perder nasalidade em uso informal

### 813. ensurdecimento

**Construção:** passagem de som sonoro para realização surda

**Função:** Permite reconhecer, explicar e testar ensurdecimento na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** consoante final pode ensurdecer em certos contactos

### 814. sonorização

**Construção:** passagem de som surdo para realização sonora

**Função:** Permite reconhecer, explicar e testar sonorização na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** /s/ pode soar [z] entre vogais

### 815. lenição

**Construção:** enfraquecimento articulatório de um segmento

**Função:** Permite reconhecer, explicar e testar lenição na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** oclusiva pode aproximar-se de fricativa em fala rápida

### 816. fortição

**Construção:** reforço articulatório de um segmento

**Função:** Permite reconhecer, explicar e testar fortição na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** uma aproximante pode tornar-se obstruinte em posição forte

### 817. neutralização fonológica

**Construção:** perda de contraste entre fonemas num ambiente definido

**Função:** Permite reconhecer, explicar e testar neutralização fonológica na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** contraste vocálico pode reduzir-se em sílaba átona

### 818. alternância fonológica

**Construção:** variação previsível de forma sonora ligada ao ambiente

**Função:** Permite reconhecer, explicar e testar alternância fonológica na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** um morfema pode ter pronúncias diferentes conforme o vizinho

### 819. processo fonológico

**Construção:** transformação regular que relaciona uma forma subjacente e sua realização

**Função:** Permite reconhecer, explicar e testar processo fonológico na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** assimilação e elisão são processos fonológicos

### 820. sândi

**Construção:** ajuste sonoro na fronteira entre unidades

**Função:** Permite reconhecer, explicar e testar sândi na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** sons de palavras vizinhas podem ligar-se

### 821. sândi externo

**Construção:** sândi que ocorre entre palavras

**Função:** Permite reconhecer, explicar e testar sândi externo na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** as amigas pode apresentar encadeamento entre palavras

### 822. ressilabificação

**Construção:** reorganização de segmentos entre sílabas na fala encadeada

**Função:** Permite reconhecer, explicar e testar ressilabificação na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** consoante final pode ligar-se à vogal seguinte

### 823. haplologia

**Construção:** apagamento de uma de duas sequências semelhantes

**Função:** Permite reconhecer, explicar e testar haplologia na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** sequências repetidas podem reduzir-se na fala

### 824. degeminação

**Construção:** redução de duas consoantes iguais adjacentes a uma realização

**Função:** Permite reconhecer, explicar e testar degeminação na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** dois sons iguais em fronteira podem fundir-se

### 825. geminação

**Construção:** alongamento ou duplicação funcional de consoante

**Função:** Permite reconhecer, explicar e testar geminação na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** contacto morfológico pode produzir duração consonantal maior

### 826. monotongação

**Construção:** redução de ditongo a uma vogal

**Função:** Permite reconhecer, explicar e testar monotongação na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** ou pode reduzir-se em fala de certas variedades

### 827. ditongação

**Construção:** formação de ditongo a partir de vogal ou sequência

**Função:** Permite reconhecer, explicar e testar ditongação na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** vogal pode ganhar deslize em certos contextos

### 828. vocalização consonantal

**Construção:** realização de consoante como elemento vocálico ou semivocálico

**Função:** Permite reconhecer, explicar e testar vocalização consonantal na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** l final pode vocalizar-se em certas variedades

### 829. peso silábico

**Construção:** propriedade que distingue sílabas leves e pesadas pela sua estrutura

**Função:** Permite reconhecer, explicar e testar peso silábico na construção do Português.

**Dependências:** fonema

**Tema de consulta:** `fonetica_fonologia`

**Exemplo mínimo:** sílaba fechada pode contar como pesada em certas análises

### 830. nome da letra

**Construção:** designação convencional atribuída a cada letra do alfabeto

**Função:** Permite reconhecer, explicar e testar nome da letra na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** a letra b chama-se bê

### 831. ordem lexicográfica

**Construção:** ordenação de palavras pela sequência de letras e sinais relevantes

**Função:** Permite reconhecer, explicar e testar ordem lexicográfica na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** casa vem antes de caso

### 832. capitalização

**Construção:** uso sistemático de maiúsculas conforme posição e função

**Função:** Permite reconhecer, explicar e testar capitalização na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Maputo começa com maiúscula

### 833. abreviatura convencional

**Construção:** forma reduzida estabilizada por convenção gráfica

**Função:** Permite reconhecer, explicar e testar abreviatura convencional na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Sr. abrevia senhor

### 834. sigla soletrada

**Construção:** sigla pronunciada pelo nome de cada letra

**Função:** Permite reconhecer, explicar e testar sigla soletrada na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** ONU pode ser lida como sequência de letras ou acrónimo conforme uso

### 835. acrónimo pronunciável

**Construção:** sigla lida como palavra única

**Função:** Permite reconhecer, explicar e testar acrónimo pronunciável na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Unesco é pronunciado como palavra

### 836. plural de abreviatura

**Construção:** marcação de plural numa forma abreviada conforme convenção

**Função:** Permite reconhecer, explicar e testar plural de abreviatura na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** págs. pode representar páginas

### 837. símbolo de unidade

**Construção:** sinal padronizado que representa unidade sem flexão comum

**Função:** Permite reconhecer, explicar e testar símbolo de unidade na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** kg representa quilograma

### 838. algarismo arábico

**Construção:** sinal decimal usado para escrever números

**Função:** Permite reconhecer, explicar e testar algarismo arábico na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 2026 usa algarismos arábicos

### 839. algarismo romano

**Construção:** sinal baseado em letras para representar número em certos contextos

**Função:** Permite reconhecer, explicar e testar algarismo romano na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** século XXI

### 840. número por extenso

**Construção:** representação verbal escrita de uma quantidade

**Função:** Permite reconhecer, explicar e testar número por extenso na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** vinte e três

### 841. grafia de data

**Construção:** organização escrita de dia, mês e ano

**Função:** Permite reconhecer, explicar e testar grafia de data na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 10 de julho de 2026

### 842. grafia de hora

**Construção:** organização escrita de uma indicação horária

**Função:** Permite reconhecer, explicar e testar grafia de hora na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 14h30

### 843. grafia de percentagem

**Construção:** associação entre número e símbolo de percentagem

**Função:** Permite reconhecer, explicar e testar grafia de percentagem na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 25%

### 844. separador decimal

**Construção:** sinal que separa parte inteira e decimal conforme convenção

**Função:** Permite reconhecer, explicar e testar separador decimal na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 3,14 em convenção portuguesa

### 845. separador de milhares

**Construção:** marca opcional que organiza grupos de três algarismos

**Função:** Permite reconhecer, explicar e testar separador de milhares na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** 1 000 000

### 846. quebra de linha

**Construção:** passagem gráfica para nova linha sem necessariamente encerrar período

**Função:** Permite reconhecer, explicar e testar quebra de linha na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** um verso termina e o seguinte começa

### 847. recuo de parágrafo

**Construção:** deslocamento inicial que marca visualmente um parágrafo

**Função:** Permite reconhecer, explicar e testar recuo de parágrafo na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** a primeira linha começa mais à direita

### 848. transcrição de fala

**Construção:** representação escrita de produção oral com critérios declarados

**Função:** Permite reconhecer, explicar e testar transcrição de fala na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** [pausa] pode marcar interrupção numa transcrição

### 849. citação curta

**Construção:** trecho citado integrado ao parágrafo e delimitado por convenção

**Função:** Permite reconhecer, explicar e testar citação curta na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Ele escreveu “volto já”.

### 850. citação longa

**Construção:** trecho citado destacado do corpo principal por formatação

**Função:** Permite reconhecer, explicar e testar citação longa na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** um parágrafo recuado pode apresentar citação extensa

### 851. parêntese explicativo

**Construção:** uso de parênteses para inserir informação acessória

**Função:** Permite reconhecer, explicar e testar parêntese explicativo na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** O projeto (iniciado ontem) continua.

### 852. colchete editorial

**Construção:** uso de colchetes para intervenção ou esclarecimento de editor

**Função:** Permite reconhecer, explicar e testar colchete editorial na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Ele [o autor] voltou.

### 853. travessão parentético

**Construção:** uso de travessões para isolar inserção explicativa

**Função:** Permite reconhecer, explicar e testar travessão parentético na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** A resposta — ainda provisória — foi registada.

### 854. ponto abreviativo

**Construção:** ponto que integra certas abreviaturas

**Função:** Permite reconhecer, explicar e testar ponto abreviativo na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Dr.

### 855. pontuação de enumeração

**Construção:** uso coordenado de sinais para separar itens

**Função:** Permite reconhecer, explicar e testar pontuação de enumeração na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** a) som; b) letra; c) palavra.

### 856. vírgula de adjunto deslocado

**Construção:** vírgula que pode delimitar adjunto antecipado ou intercalado

**Função:** Permite reconhecer, explicar e testar vírgula de adjunto deslocado na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Ontem, estudámos português.

### 857. vírgula de oração adverbial

**Construção:** vírgula que delimita oração adverbial deslocada ou marcada

**Função:** Permite reconhecer, explicar e testar vírgula de oração adverbial na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Quando chegou, começou a aula.

### 858. vírgula de oração explicativa

**Construção:** vírgulas que isolam oração relativa explicativa

**Função:** Permite reconhecer, explicar e testar vírgula de oração explicativa na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** O livro, que é antigo, foi restaurado.

### 859. vírgula de conectivo

**Construção:** vírgula que isola conectivo deslocado ou parentético

**Função:** Permite reconhecer, explicar e testar vírgula de conectivo na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Portanto, continuaremos.

### 860. ponto e vírgula em enumeração complexa

**Construção:** ponto e vírgula que separa itens já internamente pontuados

**Função:** Permite reconhecer, explicar e testar ponto e vírgula em enumeração complexa na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** vieram Ana, médica; Rui, professor; e Lia, engenheira

### 861. ponto e vírgula entre orações

**Construção:** ponto e vírgula que separa orações relacionadas com autonomia relativa

**Função:** Permite reconhecer, explicar e testar ponto e vírgula entre orações na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Estudou muito; ainda assim, revisou.

### 862. dois-pontos de enumeração

**Construção:** dois-pontos que anunciam lista ou série

**Função:** Permite reconhecer, explicar e testar dois-pontos de enumeração na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Trouxe três itens: papel, lápis e régua.

### 863. dois-pontos de conclusão

**Construção:** dois-pontos que introduzem síntese ou consequência explicativa

**Função:** Permite reconhecer, explicar e testar dois-pontos de conclusão na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Só havia uma saída: recomeçar.

### 864. reticências de suspensão

**Construção:** reticências que marcam interrupção ou suspensão

**Função:** Permite reconhecer, explicar e testar reticências de suspensão na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Eu pensei que...

### 865. reticências de omissão

**Construção:** reticências que indicam trecho omitido em citação quando a convenção o permite

**Função:** Permite reconhecer, explicar e testar reticências de omissão na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** “O método [...] foi testado.”

### 866. interrogação direta

**Construção:** uso do ponto de interrogação em pergunta direta

**Função:** Permite reconhecer, explicar e testar interrogação direta na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Onde estás?

### 867. exclamação enfática

**Construção:** uso do ponto de exclamação para marcar força expressiva

**Função:** Permite reconhecer, explicar e testar exclamação enfática na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Pare!

### 868. pontuação com aspas

**Construção:** relação entre sinal final e limite da citação

**Função:** Permite reconhecer, explicar e testar pontuação com aspas na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Ele perguntou: “Vamos?”

### 869. porquê substantivo

**Construção:** forma nominal que significa motivo

**Função:** Permite reconhecer, explicar e testar porquê substantivo na construção do Português.

**Dependências:** ortografia

**Tema de consulta:** `ortografia`

**Exemplo mínimo:** Não explicou o porquê.

### 870. raiz morfológica

**Construção:** segmento abstrato que concentra identidade lexical recorrente

**Função:** Permite reconhecer, explicar e testar raiz morfológica na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cant- em cantar e cantoria

### 871. radical verbal

**Construção:** base que recebe vogal temática e desinências verbais

**Função:** Permite reconhecer, explicar e testar radical verbal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cant- em cantamos

### 872. radical nominal

**Construção:** base que recebe marcas nominais ou derivacionais

**Função:** Permite reconhecer, explicar e testar radical nominal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** menin- em menina e meninos

### 873. tema verbal

**Construção:** união de radical e vogal temática verbal

**Função:** Permite reconhecer, explicar e testar tema verbal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** canta- em cantamos

### 874. tema nominal

**Construção:** base pronta para receber flexão nominal

**Função:** Permite reconhecer, explicar e testar tema nominal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** menina- em meninas

### 875. desinência nominal

**Construção:** morfema flexional de género ou número em nomes e adjetivos

**Função:** Permite reconhecer, explicar e testar desinência nominal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** -s em casas

### 876. desinência modo-temporal

**Construção:** morfema verbal que marca modo e tempo

**Função:** Permite reconhecer, explicar e testar desinência modo-temporal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** -va- em cantava

### 877. desinência número-pessoal

**Construção:** morfema verbal que marca pessoa e número

**Função:** Permite reconhecer, explicar e testar desinência número-pessoal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** -mos em cantamos

### 878. classe de conjugação

**Construção:** grupo verbal definido pela vogal temática do infinitivo

**Função:** Permite reconhecer, explicar e testar classe de conjugação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cantar, vender e partir representam três classes

### 879. primeira conjugação

**Construção:** classe de verbos em -ar

**Função:** Permite reconhecer, explicar e testar primeira conjugação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cantar

### 880. segunda conjugação

**Construção:** classe de verbos em -er e do verbo pôr por origem histórica

**Função:** Permite reconhecer, explicar e testar segunda conjugação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** vender

### 881. terceira conjugação

**Construção:** classe de verbos em -ir

**Função:** Permite reconhecer, explicar e testar terceira conjugação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** partir

### 882. flexão nominal

**Construção:** variação de género, número ou grau em formas nominais

**Função:** Permite reconhecer, explicar e testar flexão nominal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** meninas bonitas

### 883. flexão verbal

**Construção:** variação de pessoa, número, tempo, modo e voz no verbo

**Função:** Permite reconhecer, explicar e testar flexão verbal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** cantávamos

### 884. derivação prefixal e sufixal

**Construção:** formação com prefixo e sufixo sem exigência simultânea

**Função:** Permite reconhecer, explicar e testar derivação prefixal e sufixal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** infelizmente

### 885. cruzamento vocabular

**Construção:** formação por fusão parcial de duas palavras

**Função:** Permite reconhecer, explicar e testar cruzamento vocabular na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** portunhol combina português e espanhol

### 886. truncamento lexical

**Construção:** redução de palavra que passa a circular como forma própria

**Função:** Permite reconhecer, explicar e testar truncamento lexical na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** foto de fotografia

### 887. reduplicação

**Construção:** repetição total ou parcial com função expressiva ou gramatical

**Função:** Permite reconhecer, explicar e testar reduplicação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** corre-corre

### 888. conversão lexical

**Construção:** mudança de classe sem afixo visível

**Função:** Permite reconhecer, explicar e testar conversão lexical na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o olhar transforma verbo em nome

### 889. neologismo formal

**Construção:** palavra nova criada por processo de formação

**Função:** Permite reconhecer, explicar e testar neologismo formal na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** desvirtualizar

### 890. neologismo semântico

**Construção:** sentido novo atribuído a forma já existente

**Função:** Permite reconhecer, explicar e testar neologismo semântico na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** nuvem em computação

### 891. adaptação de empréstimo

**Construção:** ajuste gráfico, fonológico ou morfológico de palavra recebida

**Função:** Permite reconhecer, explicar e testar adaptação de empréstimo na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** futebol adaptou football

### 892. estrangeirismo não adaptado

**Construção:** forma externa mantida com grafia próxima da origem

**Função:** Permite reconhecer, explicar e testar estrangeirismo não adaptado na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** software

### 893. calque linguístico

**Construção:** tradução estrutural de expressão de outra língua

**Função:** Permite reconhecer, explicar e testar calque linguístico na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** arranha-céu corresponde a composição traduzida

### 894. lexicalização de locução

**Construção:** fixação de combinação como unidade lexical

**Função:** Permite reconhecer, explicar e testar lexicalização de locução na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** fim de semana funciona como unidade estável

### 895. deslexicalização

**Construção:** perda parcial de sentido lexical em favor de função gramatical

**Função:** Permite reconhecer, explicar e testar deslexicalização na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** ir em vou estudar funciona como auxiliar

### 896. substantivação

**Construção:** uso de elemento de outra classe como substantivo

**Função:** Permite reconhecer, explicar e testar substantivação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o belo

### 897. adjetivação

**Construção:** uso ou formação com função adjetiva

**Função:** Permite reconhecer, explicar e testar adjetivação na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** amor materno

### 898. adverbialização

**Construção:** uso de forma com função adverbial

**Função:** Permite reconhecer, explicar e testar adverbialização na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** falar baixo

### 899. pronominalização

**Construção:** substituição de expressão por pronome

**Função:** Permite reconhecer, explicar e testar pronominalização na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** Vi a Maria → vi-a

### 900. nominalização

**Construção:** formação ou uso de nome a partir de verbo ou adjetivo

**Função:** Permite reconhecer, explicar e testar nominalização na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** construção de construir

### 901. verbalização

**Construção:** formação de verbo a partir de nome ou adjetivo

**Função:** Permite reconhecer, explicar e testar verbalização na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** clarificar de claro

### 902. diminutivo sintético

**Construção:** grau diminutivo formado por sufixo

**Função:** Permite reconhecer, explicar e testar diminutivo sintético na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casinha

### 903. diminutivo analítico

**Construção:** grau diminutivo expresso por construção separada

**Função:** Permite reconhecer, explicar e testar diminutivo analítico na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa pequena

### 904. aumentativo sintético

**Construção:** grau aumentativo formado por sufixo

**Função:** Permite reconhecer, explicar e testar aumentativo sintético na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casarão

### 905. aumentativo analítico

**Construção:** grau aumentativo expresso por construção separada

**Função:** Permite reconhecer, explicar e testar aumentativo analítico na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa enorme

### 906. comparativo de igualdade

**Construção:** comparação que apresenta grau equivalente

**Função:** Permite reconhecer, explicar e testar comparativo de igualdade na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** tão claro quanto

### 907. comparativo de superioridade

**Construção:** comparação que apresenta grau maior

**Função:** Permite reconhecer, explicar e testar comparativo de superioridade na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** mais claro do que

### 908. comparativo de inferioridade

**Construção:** comparação que apresenta grau menor

**Função:** Permite reconhecer, explicar e testar comparativo de inferioridade na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** menos claro do que

### 909. superlativo absoluto analítico

**Construção:** intensidade alta expressa por advérbio

**Função:** Permite reconhecer, explicar e testar superlativo absoluto analítico na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** muito claro

### 910. superlativo absoluto sintético

**Construção:** intensidade alta expressa por sufixo ou forma própria

**Função:** Permite reconhecer, explicar e testar superlativo absoluto sintético na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** claríssimo

### 911. superlativo relativo de superioridade

**Construção:** grau máximo dentro de conjunto

**Função:** Permite reconhecer, explicar e testar superlativo relativo de superioridade na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o mais claro da turma

### 912. superlativo relativo de inferioridade

**Construção:** grau mínimo dentro de conjunto

**Função:** Permite reconhecer, explicar e testar superlativo relativo de inferioridade na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o menos claro da turma

### 913. substantivo primitivo

**Construção:** substantivo não formado de outra palavra portuguesa identificável na análise sincrónica

**Função:** Permite reconhecer, explicar e testar substantivo primitivo na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** pedra

### 914. substantivo derivado

**Construção:** substantivo formado de outra base

**Função:** Permite reconhecer, explicar e testar substantivo derivado na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** pedreiro

### 915. substantivo simples

**Construção:** substantivo com um radical principal

**Função:** Permite reconhecer, explicar e testar substantivo simples na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** casa

### 916. substantivo composto

**Construção:** substantivo formado por mais de um elemento lexical

**Função:** Permite reconhecer, explicar e testar substantivo composto na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** guarda-chuva

### 917. adjetivo simples

**Construção:** adjetivo com um radical principal

**Função:** Permite reconhecer, explicar e testar adjetivo simples na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** claro

### 918. adjetivo composto

**Construção:** adjetivo formado por mais de um elemento

**Função:** Permite reconhecer, explicar e testar adjetivo composto na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** luso-brasileiro

### 919. adjetivo uniforme

**Construção:** adjetivo com uma forma para mais de um género

**Função:** Permite reconhecer, explicar e testar adjetivo uniforme na construção do Português.

**Dependências:** morfema

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** feliz

### 920. determinante complexo

**Construção:** grupo de determinantes ou quantificadores que delimita o nome

**Função:** Permite reconhecer, explicar e testar determinante complexo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** todos os três livros

### 921. núcleo nominal

**Construção:** nome ou pronome central de sintagma nominal

**Função:** Permite reconhecer, explicar e testar núcleo nominal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** livro em o livro novo

### 922. modificador nominal

**Construção:** constituinte que restringe ou caracteriza um nome

**Função:** Permite reconhecer, explicar e testar modificador nominal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** novo em livro novo

### 923. complemento do nome

**Construção:** constituinte selecionado por nome para completar relação

**Função:** Permite reconhecer, explicar e testar complemento do nome na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** de matemática em estudo de matemática

### 924. especificador nominal

**Construção:** posição ou função que delimita a referência do nome

**Função:** Permite reconhecer, explicar e testar especificador nominal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** os em os livros

### 925. núcleo verbal

**Construção:** verbo central de sintagma verbal

**Função:** Permite reconhecer, explicar e testar núcleo verbal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** estudou em estudou muito

### 926. complemento do verbo

**Construção:** constituinte selecionado pelo verbo

**Função:** Permite reconhecer, explicar e testar complemento do verbo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o livro em leu o livro

### 927. modificador verbal

**Construção:** constituinte que acrescenta circunstância ao evento

**Função:** Permite reconhecer, explicar e testar modificador verbal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** ontem em chegou ontem

### 928. núcleo adjetival

**Construção:** adjetivo central de sintagma adjetival

**Função:** Permite reconhecer, explicar e testar núcleo adjetival na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** orgulhoso em muito orgulhoso

### 929. complemento do adjetivo

**Construção:** constituinte selecionado por adjetivo

**Função:** Permite reconhecer, explicar e testar complemento do adjetivo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** de ti em orgulhoso de ti

### 930. núcleo adverbial

**Construção:** advérbio central de sintagma adverbial

**Função:** Permite reconhecer, explicar e testar núcleo adverbial na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** longe em muito longe

### 931. complemento do advérbio

**Construção:** constituinte ligado a certos advérbios

**Função:** Permite reconhecer, explicar e testar complemento do advérbio na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** de casa em longe de casa

### 932. núcleo preposicional

**Construção:** preposição central de sintagma preposicional

**Função:** Permite reconhecer, explicar e testar núcleo preposicional na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** de em de casa

### 933. complemento da preposição

**Construção:** termo regido pela preposição

**Função:** Permite reconhecer, explicar e testar complemento da preposição na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** casa em de casa

### 934. oração interrogativa direta total

**Construção:** pergunta que solicita confirmação global

**Função:** Permite reconhecer, explicar e testar oração interrogativa direta total na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Chegaste?

### 935. oração interrogativa direta parcial

**Construção:** pergunta que solicita valor de um constituinte

**Função:** Permite reconhecer, explicar e testar oração interrogativa direta parcial na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Quem chegou?

### 936. oração interrogativa indireta total

**Construção:** oração subordinada que incorpora pergunta total

**Função:** Permite reconhecer, explicar e testar oração interrogativa indireta total na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Perguntei se chegaste.

### 937. oração interrogativa indireta parcial

**Construção:** oração subordinada que incorpora pergunta parcial

**Função:** Permite reconhecer, explicar e testar oração interrogativa indireta parcial na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Perguntei quem chegou.

### 938. oração exclamativa

**Construção:** oração com força exclamativa

**Função:** Permite reconhecer, explicar e testar oração exclamativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Como está bonito!

### 939. oração imperativa

**Construção:** oração que expressa ordem, pedido ou conselho

**Função:** Permite reconhecer, explicar e testar oração imperativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Fecha a porta.

### 940. oração optativa

**Construção:** oração que expressa desejo

**Função:** Permite reconhecer, explicar e testar oração optativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Que tudo corra bem.

### 941. oração declarativa

**Construção:** oração apresentada como afirmação ou negação

**Função:** Permite reconhecer, explicar e testar oração declarativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A aula começou.

### 942. sujeito agente

**Construção:** sujeito associado ao agente de ação

**Função:** Permite reconhecer, explicar e testar sujeito agente na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A Ana abriu a porta.

### 943. sujeito paciente

**Construção:** sujeito associado ao paciente em passiva

**Função:** Permite reconhecer, explicar e testar sujeito paciente na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A porta foi aberta.

### 944. sujeito experienciador

**Construção:** sujeito que sente ou percebe

**Função:** Permite reconhecer, explicar e testar sujeito experienciador na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** A Ana teme o escuro.

### 945. sujeito posposto

**Construção:** sujeito que aparece depois do verbo

**Função:** Permite reconhecer, explicar e testar sujeito posposto na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Chegaram os alunos.

### 946. sujeito anteposto

**Construção:** sujeito que aparece antes do verbo

**Função:** Permite reconhecer, explicar e testar sujeito anteposto na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Os alunos chegaram.

### 947. sujeito oracional

**Construção:** oração que exerce função de sujeito

**Função:** Permite reconhecer, explicar e testar sujeito oracional na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** É importante estudar.

### 948. objeto direto preposicionado

**Construção:** objeto direto introduzido por preposição em construção marcada

**Função:** Permite reconhecer, explicar e testar objeto direto preposicionado na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Amo a Deus.

### 949. objeto direto pleonástico

**Construção:** objeto retomado por pronome para efeito estrutural ou discursivo

**Função:** Permite reconhecer, explicar e testar objeto direto pleonástico na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Esse livro, eu o li.

### 950. objeto indireto pleonástico

**Construção:** objeto indireto retomado por pronome

**Função:** Permite reconhecer, explicar e testar objeto indireto pleonástico na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ao aluno, dei-lhe o livro.

### 951. complemento relativo

**Construção:** complemento preposicionado selecionado por certos verbos

**Função:** Permite reconhecer, explicar e testar complemento relativo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** gostar de música

### 952. complemento oblíquo

**Construção:** complemento preposicional selecionado sem função de objeto indireto tradicional

**Função:** Permite reconhecer, explicar e testar complemento oblíquo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** morar em Maputo

### 953. predicativo secundário

**Construção:** predicativo que se associa a participante sem ser núcleo copulativo principal

**Função:** Permite reconhecer, explicar e testar predicativo secundário na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ele chegou cansado.

### 954. predicativo depictivo

**Construção:** predicativo que descreve estado simultâneo ao evento

**Função:** Permite reconhecer, explicar e testar predicativo depictivo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ela saiu feliz.

### 955. predicativo resultativo

**Construção:** predicativo que expressa resultado do evento

**Função:** Permite reconhecer, explicar e testar predicativo resultativo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Pintou a parede azul.

### 956. aposto explicativo

**Construção:** aposto que acrescenta explicação

**Função:** Permite reconhecer, explicar e testar aposto explicativo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Maputo, capital de Moçambique, ...

### 957. aposto enumerativo

**Construção:** aposto que enumera componentes

**Função:** Permite reconhecer, explicar e testar aposto enumerativo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Trouxe tudo: pão, água e fruta.

### 958. aposto resumitivo

**Construção:** aposto que resume elementos anteriores

**Função:** Permite reconhecer, explicar e testar aposto resumitivo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Medo, dúvida, cansaço, tudo passou.

### 959. aposto especificativo

**Construção:** aposto que identifica nome genérico

**Função:** Permite reconhecer, explicar e testar aposto especificativo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** o poeta Camões

### 960. vocativo inicial

**Construção:** vocativo colocado no início do enunciado

**Função:** Permite reconhecer, explicar e testar vocativo inicial na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Maria, venha.

### 961. vocativo intercalado

**Construção:** vocativo inserido no meio

**Função:** Permite reconhecer, explicar e testar vocativo intercalado na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Venha, Maria, agora.

### 962. vocativo final

**Construção:** vocativo colocado no fim

**Função:** Permite reconhecer, explicar e testar vocativo final na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Venha agora, Maria.

### 963. adjunto adverbial de finalidade

**Construção:** adjunto que expressa propósito

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de finalidade na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou para aprender.

### 964. adjunto adverbial de condição

**Construção:** adjunto que expressa condição

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de condição na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Com esforço, conseguirás.

### 965. adjunto adverbial de concessão

**Construção:** adjunto que expressa obstáculo não impeditivo

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de concessão na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Apesar do cansaço, continuou.

### 966. adjunto adverbial de companhia

**Construção:** adjunto que expressa companhia

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de companhia na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Saiu com os amigos.

### 967. adjunto adverbial de instrumento

**Construção:** adjunto que expressa instrumento

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de instrumento na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Escreveu com lápis.

### 968. adjunto adverbial de meio

**Construção:** adjunto que expressa meio

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de meio na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Viajou de autocarro.

### 969. adjunto adverbial de assunto

**Construção:** adjunto que expressa assunto

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de assunto na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Falou sobre gramática.

### 970. adjunto adverbial de intensidade

**Construção:** adjunto que expressa grau

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de intensidade na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Estudou muito.

### 971. adjunto adverbial de afirmação

**Construção:** adjunto que reforça afirmação

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de afirmação na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Certamente virá.

### 972. adjunto adverbial de negação

**Construção:** adjunto que expressa negação

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de negação na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Nunca faltou.

### 973. adjunto adverbial de dúvida

**Construção:** adjunto que expressa incerteza

**Função:** Permite reconhecer, explicar e testar adjunto adverbial de dúvida na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Talvez chegue.

### 974. oração subordinada adverbial proporcional

**Construção:** oração que expressa variação proporcional

**Função:** Permite reconhecer, explicar e testar oração subordinada adverbial proporcional na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** À medida que estuda, aprende.

### 975. oração subordinada adverbial conformativa

**Construção:** oração que expressa conformidade

**Função:** Permite reconhecer, explicar e testar oração subordinada adverbial conformativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Fez como combinámos.

### 976. oração subordinada adverbial comparativa

**Construção:** oração que estabelece comparação

**Função:** Permite reconhecer, explicar e testar oração subordinada adverbial comparativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Trabalha como o pai trabalhava.

### 977. oração subordinada adjetiva restritiva

**Construção:** oração relativa que delimita o referente

**Função:** Permite reconhecer, explicar e testar oração subordinada adjetiva restritiva na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Os alunos que estudaram passaram.

### 978. oração subordinada adjetiva explicativa

**Construção:** oração relativa que acrescenta informação parentética

**Função:** Permite reconhecer, explicar e testar oração subordinada adjetiva explicativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Os alunos, que estudaram, passaram.

### 979. oração subordinada substantiva completiva verbal

**Construção:** oração que completa seleção de verbo

**Função:** Permite reconhecer, explicar e testar oração subordinada substantiva completiva verbal na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Espero que venhas.

### 980. oração subordinada substantiva interrogativa indireta

**Construção:** oração que incorpora conteúdo interrogativo

**Função:** Permite reconhecer, explicar e testar oração subordinada substantiva interrogativa indireta na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Não sei quem veio.

### 981. oração subordinada substantiva infinitiva

**Construção:** oração infinitiva com função nominal

**Função:** Permite reconhecer, explicar e testar oração subordinada substantiva infinitiva na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** É bom estudar.

### 982. coordenação correlativa

**Construção:** coordenação marcada por pares correlativos

**Função:** Permite reconhecer, explicar e testar coordenação correlativa na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** não só estudou, mas também praticou

### 983. coordenação distributiva

**Construção:** coordenação que distribui alternativas ou ocorrências

**Função:** Permite reconhecer, explicar e testar coordenação distributiva na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** ora ria, ora chorava

### 984. construção de controlo

**Construção:** construção em que argumento de uma oração controla sujeito não expresso de infinitiva

**Função:** Permite reconhecer, explicar e testar construção de controlo na construção do Português.

**Dependências:** sintaxe

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** Ana tentou sair.

### 985. sentido literal

**Construção:** leitura diretamente sustentada pelas convenções lexicais e sintáticas

**Função:** Permite reconhecer, explicar e testar sentido literal na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A porta está aberta descreve estado da porta

### 986. sentido figurado

**Construção:** leitura construída por extensão, comparação ou associação

**Função:** Permite reconhecer, explicar e testar sentido figurado na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Ele tem coração de pedra

### 987. ambiguidade de escopo

**Construção:** mais de uma leitura causada pela extensão de operadores

**Função:** Permite reconhecer, explicar e testar ambiguidade de escopo na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Todos não vieram pode ter leituras distintas

### 988. ambiguidade referencial

**Construção:** mais de um referente possível para expressão

**Função:** Permite reconhecer, explicar e testar ambiguidade referencial na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** João falou com Pedro quando ele chegou

### 989. vagueza

**Construção:** ausência de fronteira nítida para aplicação de termo

**Função:** Permite reconhecer, explicar e testar vagueza na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** alto varia conforme a escala

### 990. subespecificação

**Construção:** informação deixada sem valor completo na forma

**Função:** Permite reconhecer, explicar e testar subespecificação na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Vou chegar depois não fixa hora

### 991. sinonímia contextual

**Construção:** proximidade de sentido válida num contexto específico

**Função:** Permite reconhecer, explicar e testar sinonímia contextual na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** casa e lar podem aproximar-se em certo texto

### 992. antonímia complementar

**Construção:** oposição em que negar um termo favorece o outro

**Função:** Permite reconhecer, explicar e testar antonímia complementar na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** vivo e morto em leitura binária

### 993. antonímia gradual

**Construção:** oposição organizada por escala

**Função:** Permite reconhecer, explicar e testar antonímia gradual na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** quente e frio

### 994. antonímia recíproca

**Construção:** oposição entre papéis de uma mesma relação

**Função:** Permite reconhecer, explicar e testar antonímia recíproca na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** comprar e vender

### 995. homonímia perfeita

**Construção:** coincidência de forma sonora e gráfica entre lexemas distintos

**Função:** Permite reconhecer, explicar e testar homonímia perfeita na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** manga fruta e manga de camisa

### 996. homofonia lexical

**Construção:** mesma forma sonora com grafia ou sentido distinto

**Função:** Permite reconhecer, explicar e testar homofonia lexical na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** cela e sela

### 997. homografia lexical

**Construção:** mesma grafia com pronúncia ou sentido distinto

**Função:** Permite reconhecer, explicar e testar homografia lexical na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** sede de beber e sede de empresa

### 998. relação parte-todo

**Construção:** relação semântica entre componente e totalidade

**Função:** Permite reconhecer, explicar e testar relação parte-todo na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** roda é parte de carro

### 999. protótipo semântico

**Construção:** membro central usado como referência de categoria

**Função:** Permite reconhecer, explicar e testar protótipo semântico na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** pardal pode ser protótipo de ave

### 1000. categoria radial

**Construção:** categoria organizada por sentidos ligados a um núcleo

**Função:** Permite reconhecer, explicar e testar categoria radial na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** cabeça estende-se de parte do corpo a líder

### 1001. metáfora conceptual

**Construção:** mapeamento sistemático entre domínios de experiência

**Função:** Permite reconhecer, explicar e testar metáfora conceptual na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** tempo é recurso em gastar tempo

### 1002. metonímia de autor pela obra

**Construção:** uso do autor para referir a obra

**Função:** Permite reconhecer, explicar e testar metonímia de autor pela obra na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** li Camões

### 1003. metonímia de continente pelo conteúdo

**Construção:** uso do recipiente para referir o conteúdo

**Função:** Permite reconhecer, explicar e testar metonímia de continente pelo conteúdo na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** bebeu um copo

### 1004. sinédoque

**Construção:** relação figurada entre parte e todo ou espécie e género

**Função:** Permite reconhecer, explicar e testar sinédoque na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** cem cabeças de gado

### 1005. catacrese

**Construção:** extensão lexical estabilizada por falta de termo literal mais específico

**Função:** Permite reconhecer, explicar e testar catacrese na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** pé da mesa

### 1006. perífrase figurada

**Construção:** expressão descritiva que substitui nome

**Função:** Permite reconhecer, explicar e testar perífrase figurada na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Cidade das Acácias

### 1007. litote

**Construção:** afirmação por negação do contrário

**Função:** Permite reconhecer, explicar e testar litote na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** não é nada mau

### 1008. gradação

**Construção:** ordenação progressiva de ideias ou intensidades

**Função:** Permite reconhecer, explicar e testar gradação na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** sussurrou, falou, gritou

### 1009. pleonasmo expressivo

**Construção:** repetição semântica usada para ênfase

**Função:** Permite reconhecer, explicar e testar pleonasmo expressivo na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** vi com meus próprios olhos

### 1010. onomatopeia expressiva

**Construção:** forma que imita ou evoca som

**Função:** Permite reconhecer, explicar e testar onomatopeia expressiva na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** tic-tac

### 1011. modalidade epistémica

**Construção:** avaliação de possibilidade, probabilidade ou certeza

**Função:** Permite reconhecer, explicar e testar modalidade epistémica na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Ele deve estar em casa

### 1012. modalidade deôntica

**Construção:** avaliação de obrigação, permissão ou proibição

**Função:** Permite reconhecer, explicar e testar modalidade deôntica na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Deves estudar

### 1013. modalidade dinâmica

**Construção:** expressão de capacidade ou disposição do participante

**Função:** Permite reconhecer, explicar e testar modalidade dinâmica na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Ela consegue nadar

### 1014. modalidade avaliativa

**Construção:** expressão de julgamento do falante sobre situação

**Função:** Permite reconhecer, explicar e testar modalidade avaliativa na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Felizmente, chegou cedo

### 1015. evidencialidade

**Construção:** marcação da fonte ou modo de acesso à informação

**Função:** Permite reconhecer, explicar e testar evidencialidade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Segundo o relatório, houve mudança

### 1016. factividade

**Construção:** propriedade de predicado que apresenta complemento como pressuposto em leitura comum

**Função:** Permite reconhecer, explicar e testar factividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** lamentar que ocorreu pressupõe ocorrência

### 1017. contrafactualidade

**Construção:** interpretação de situação apresentada contra os fatos assumidos

**Função:** Permite reconhecer, explicar e testar contrafactualidade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Se tivesse estudado, teria passado

### 1018. genericidade

**Construção:** leitura sobre classe ou regularidade geral

**Função:** Permite reconhecer, explicar e testar genericidade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** O leão é mamífero

### 1019. habitualidade

**Construção:** leitura de ocorrência repetida como hábito

**Função:** Permite reconhecer, explicar e testar habitualidade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Ela lê todas as noites

### 1020. iteratividade

**Construção:** repetição de evento dentro de intervalo

**Função:** Permite reconhecer, explicar e testar iteratividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Bateu três vezes

### 1021. incoatividade

**Construção:** fase inicial de estado ou evento

**Função:** Permite reconhecer, explicar e testar incoatividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** começou a chover

### 1022. duratividade

**Construção:** extensão temporal interna de situação

**Função:** Permite reconhecer, explicar e testar duratividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** dormiu por horas

### 1023. perfectividade

**Construção:** visão da situação como totalidade delimitada

**Função:** Permite reconhecer, explicar e testar perfectividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** leu o livro ontem

### 1024. imperfectividade

**Construção:** visão interna ou não delimitada da situação

**Função:** Permite reconhecer, explicar e testar imperfectividade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** lia quando cheguei

### 1025. presente gnómico

**Construção:** presente usado em generalizações

**Função:** Permite reconhecer, explicar e testar presente gnómico na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** A água ferve sob condições definidas

### 1026. presente histórico

**Construção:** presente usado para narrar evento passado

**Função:** Permite reconhecer, explicar e testar presente histórico na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Em 1975, o país conquista a independência

### 1027. futuro modal

**Construção:** futuro usado para hipótese ou atenuação

**Função:** Permite reconhecer, explicar e testar futuro modal na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Será que ele vem?

### 1028. pretérito de cortesia

**Construção:** pretérito usado para atenuar pedido ou posição

**Função:** Permite reconhecer, explicar e testar pretérito de cortesia na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Queria uma informação

### 1029. pressuposição existencial

**Construção:** pressuposição associada a expressão definida ou possessiva

**Função:** Permite reconhecer, explicar e testar pressuposição existencial na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** O carro de Ana implica um carro associado a Ana

### 1030. pressuposição lexical

**Construção:** pressuposição acionada por item lexical

**Função:** Permite reconhecer, explicar e testar pressuposição lexical na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** parar de estudar sugere que estudava

### 1031. pressuposição estrutural

**Construção:** pressuposição ligada a forma sintática

**Função:** Permite reconhecer, explicar e testar pressuposição estrutural na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Quem chegou? pressupõe que alguém chegou

### 1032. implicatura conversacional

**Construção:** inferência pragmática cancelável gerada pelo uso em contexto

**Função:** Permite reconhecer, explicar e testar implicatura conversacional na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** Alguns vieram pode sugerir que nem todos vieram

### 1033. implicatura convencional

**Construção:** inferência associada convencionalmente a expressão

**Função:** Permite reconhecer, explicar e testar implicatura convencional na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** mas marca contraste além da conjunção

### 1034. máxima de quantidade

**Construção:** princípio de fornecer informação suficiente sem excesso irrelevante

**Função:** Permite reconhecer, explicar e testar máxima de quantidade na construção do Português.

**Dependências:** sentido

**Tema de consulta:** `semantica_pragmatica`

**Exemplo mínimo:** responder exatamente ao que foi perguntado

### 1035. coesão por referência pessoal

**Construção:** ligação textual por pronomes ou formas pessoais

**Função:** Permite reconhecer, explicar e testar coesão por referência pessoal na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Ana chegou. Ela sentou.

### 1036. coesão por referência demonstrativa

**Construção:** ligação textual por demonstrativos

**Função:** Permite reconhecer, explicar e testar coesão por referência demonstrativa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Este problema exige cuidado.

### 1037. coesão por referência comparativa

**Construção:** ligação por comparação entre elementos

**Função:** Permite reconhecer, explicar e testar coesão por referência comparativa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Outro método é mais simples.

### 1038. coesão por substituição nominal

**Construção:** substituição de grupo nominal por forma equivalente

**Função:** Permite reconhecer, explicar e testar coesão por substituição nominal na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Preciso de uma caneta; tens uma?

### 1039. coesão por substituição verbal

**Construção:** substituição de predicado por forma auxiliar

**Função:** Permite reconhecer, explicar e testar coesão por substituição verbal na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Ela estudou e eu também o fiz.

### 1040. coesão por elipse

**Construção:** ligação textual por omissão recuperável

**Função:** Permite reconhecer, explicar e testar coesão por elipse na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Ana escolheu português; Rui, matemática.

### 1041. coesão por conjunção

**Construção:** ligação por conectivos que explicitam relação

**Função:** Permite reconhecer, explicar e testar coesão por conjunção na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Estudou; portanto, passou.

### 1042. coesão por colocação lexical

**Construção:** ligação por palavras que costumam ocorrer no mesmo domínio

**Função:** Permite reconhecer, explicar e testar coesão por colocação lexical na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** escola, professor, aula, aluno

### 1043. parágrafo introdutório

**Construção:** parágrafo que apresenta tema, problema ou direção do texto

**Função:** Permite reconhecer, explicar e testar parágrafo introdutório na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Este relatório analisa o motor.

### 1044. parágrafo de desenvolvimento

**Construção:** parágrafo que explica, prova ou detalha ponto

**Função:** Permite reconhecer, explicar e testar parágrafo de desenvolvimento na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Primeiro, observamos os dados.

### 1045. parágrafo conclusivo

**Construção:** parágrafo que fecha percurso e sintetiza resultado

**Função:** Permite reconhecer, explicar e testar parágrafo conclusivo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Portanto, a hipótese permanece válida.

### 1046. parágrafo argumentativo

**Construção:** parágrafo organizado por tese local, razão e evidência

**Função:** Permite reconhecer, explicar e testar parágrafo argumentativo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A regra é útil porque reduz ambiguidades.

### 1047. parágrafo expositivo

**Construção:** parágrafo que organiza explicação de conceito

**Função:** Permite reconhecer, explicar e testar parágrafo expositivo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Morfema é a menor unidade funcional.

### 1048. parágrafo narrativo

**Construção:** parágrafo que organiza eventos em sequência

**Função:** Permite reconhecer, explicar e testar parágrafo narrativo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Chegou, observou e começou o teste.

### 1049. parágrafo descritivo

**Construção:** parágrafo que organiza propriedades de entidade ou cenário

**Função:** Permite reconhecer, explicar e testar parágrafo descritivo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A sala era ampla e silenciosa.

### 1050. frase-tópico

**Construção:** frase que apresenta ideia central do parágrafo

**Função:** Permite reconhecer, explicar e testar frase-tópico na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** A concordância organiza relações formais.

### 1051. frase de apoio

**Construção:** frase que explica ou demonstra a frase-tópico

**Função:** Permite reconhecer, explicar e testar frase de apoio na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Por exemplo, artigo e nome ajustam número.

### 1052. frase de transição

**Construção:** frase que liga partes do texto

**Função:** Permite reconhecer, explicar e testar frase de transição na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Depois de examinar a forma, passamos ao sentido.

### 1053. cadeia argumentativa

**Construção:** sequência conectada de premissas, garantias e conclusões

**Função:** Permite reconhecer, explicar e testar cadeia argumentativa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** dado → regra → conclusão

### 1054. argumento por exemplo

**Construção:** argumento sustentado por caso representativo

**Função:** Permite reconhecer, explicar e testar argumento por exemplo na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um caso testado ilustra a regra

### 1055. argumento por analogia

**Construção:** argumento que transfere relação entre casos comparáveis

**Função:** Permite reconhecer, explicar e testar argumento por analogia na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** assim como uma palavra tem partes, uma frase tem constituintes

### 1056. argumento causal

**Construção:** argumento que liga causa proposta a efeito

**Função:** Permite reconhecer, explicar e testar argumento causal na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** a ausência de dependência causa falha na construção

### 1057. argumento por definição

**Construção:** argumento que aplica definição explícita a um caso

**Função:** Permite reconhecer, explicar e testar argumento por definição na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** se é morfema, tem função na palavra

### 1058. argumento de autoridade documentada

**Construção:** argumento que usa fonte identificada sem torná-la infalível

**Função:** Permite reconhecer, explicar e testar argumento de autoridade documentada na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o estudo citado fornece evidência verificável

### 1059. falácia de generalização precipitada

**Construção:** erro de concluir regra ampla com poucos casos

**Função:** Permite reconhecer, explicar e testar falácia de generalização precipitada na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** dois exemplos não provam todos os usos

### 1060. falácia de falsa causa

**Construção:** erro de tratar sequência ou correlação como causa suficiente

**Função:** Permite reconhecer, explicar e testar falácia de falsa causa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** aconteceu depois, logo foi causado por isso

### 1061. falácia de falso dilema

**Construção:** erro de apresentar apenas duas opções quando há outras

**Função:** Permite reconhecer, explicar e testar falácia de falso dilema na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** ou aceita tudo ou rejeita tudo

### 1062. falácia ad hominem

**Construção:** erro de atacar pessoa em vez do argumento

**Função:** Permite reconhecer, explicar e testar falácia ad hominem na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** desqualificar o autor sem analisar a prova

### 1063. falácia de circularidade

**Construção:** erro de usar conclusão como premissa

**Função:** Permite reconhecer, explicar e testar falácia de circularidade na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** é verdadeiro porque é verdade

### 1064. narração em primeira pessoa

**Construção:** narração feita por voz participante marcada por primeira pessoa

**Função:** Permite reconhecer, explicar e testar narração em primeira pessoa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Eu entrei e observei.

### 1065. narração em terceira pessoa

**Construção:** narração feita por voz externa em terceira pessoa

**Função:** Permite reconhecer, explicar e testar narração em terceira pessoa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** Ela entrou e observou.

### 1066. narrador participante

**Construção:** narrador que atua na história

**Função:** Permite reconhecer, explicar e testar narrador participante na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um personagem conta o que viveu

### 1067. narrador observador

**Construção:** narrador que relata sem acesso total ao interior das personagens

**Função:** Permite reconhecer, explicar e testar narrador observador na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** descreve ações visíveis

### 1068. narrador omnisciente

**Construção:** narrador que apresenta conhecimento amplo de personagens e eventos

**Função:** Permite reconhecer, explicar e testar narrador omnisciente na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** revela pensamentos de várias personagens

### 1069. focalização interna

**Construção:** perspetiva limitada ao conhecimento de personagem

**Função:** Permite reconhecer, explicar e testar focalização interna na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o leitor sabe apenas o que Ana percebe

### 1070. focalização externa

**Construção:** perspetiva limitada ao observável

**Função:** Permite reconhecer, explicar e testar focalização externa na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o texto mostra gestos sem pensamentos

### 1071. focalização zero

**Construção:** perspetiva narrativa sem limitação estável a personagem

**Função:** Permite reconhecer, explicar e testar focalização zero na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o narrador conhece vários interiores

### 1072. tempo cronológico

**Construção:** ordem temporal linear dos acontecimentos

**Função:** Permite reconhecer, explicar e testar tempo cronológico na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** primeiro chegou, depois falou

### 1073. tempo psicológico

**Construção:** organização temporal pela experiência subjetiva

**Função:** Permite reconhecer, explicar e testar tempo psicológico na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um instante evoca longa memória

### 1074. analepse

**Construção:** retorno narrativo a evento anterior

**Função:** Permite reconhecer, explicar e testar analepse na construção do Português.

**Dependências:** texto

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** o capítulo relembra a infância

### 1075. variação fonética

**Construção:** diferença de realização sonora sem mudança necessária de estrutura gramatical

**Função:** Permite reconhecer, explicar e testar variação fonética na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** r pode ter realizações regionais

### 1076. variação fonológica

**Construção:** diferença sistemática no inventário ou distribuição de contrastes

**Função:** Permite reconhecer, explicar e testar variação fonológica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** certas variedades distinguem realizações em contextos diferentes

### 1077. variação morfológica

**Construção:** diferença de formas flexionais ou derivacionais entre usos

**Função:** Permite reconhecer, explicar e testar variação morfológica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** formas participiais podem variar

### 1078. variação sintática

**Construção:** diferença de construção e ordem entre variedades

**Função:** Permite reconhecer, explicar e testar variação sintática na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** posição de clítico pode variar

### 1079. variação lexical

**Construção:** diferença de palavras para referente ou situação semelhante

**Função:** Permite reconhecer, explicar e testar variação lexical na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** autocarro e ônibus

### 1080. variação semântica

**Construção:** diferença de sentido associado à mesma forma entre comunidades

**Função:** Permite reconhecer, explicar e testar variação semântica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** rapariga tem avaliações diferentes por variedade

### 1081. variação pragmática

**Construção:** diferença de estratégias de uso e cortesia

**Função:** Permite reconhecer, explicar e testar variação pragmática na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** formas de tratamento variam por comunidade

### 1082. mudança fonética

**Construção:** alteração histórica na realização de sons

**Função:** Permite reconhecer, explicar e testar mudança fonética na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** um segmento pode enfraquecer ao longo do tempo

### 1083. mudança fonológica

**Construção:** alteração histórica de contrastes sonoros

**Função:** Permite reconhecer, explicar e testar mudança fonológica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** dois fonemas podem fundir-se

### 1084. mudança morfológica

**Construção:** alteração histórica em paradigmas e formação de palavras

**Função:** Permite reconhecer, explicar e testar mudança morfológica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma flexão pode regularizar-se

### 1085. mudança sintática

**Construção:** alteração histórica em ordem ou construção

**Função:** Permite reconhecer, explicar e testar mudança sintática na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma posição pronominal pode tornar-se mais frequente

### 1086. mudança semântica

**Construção:** alteração histórica de sentido

**Função:** Permite reconhecer, explicar e testar mudança semântica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma palavra pode ampliar ou restringir significado

### 1087. ampliação semântica

**Construção:** mudança em que termo passa a cobrir domínio maior

**Função:** Permite reconhecer, explicar e testar ampliação semântica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma palavra específica ganha uso geral

### 1088. restrição semântica

**Construção:** mudança em que termo passa a cobrir domínio menor

**Função:** Permite reconhecer, explicar e testar restrição semântica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** uma palavra geral torna-se especializada

### 1089. melhoria semântica

**Construção:** mudança para avaliação social mais positiva

**Função:** Permite reconhecer, explicar e testar melhoria semântica na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** termo adquire valor favorável

### 1090. pejorização

**Construção:** mudança para avaliação social mais negativa

**Função:** Permite reconhecer, explicar e testar pejorização na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** termo adquire valor depreciativo

### 1091. dialetologia

**Construção:** estudo sistemático da distribuição geográfica de variedades

**Função:** Permite reconhecer, explicar e testar dialetologia na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** mapear formas por regiões

### 1092. geolinguística

**Construção:** estudo espacial de fenómenos linguísticos

**Função:** Permite reconhecer, explicar e testar geolinguística na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** atlas de variantes regionais

### 1093. planeamento linguístico

**Construção:** ação organizada sobre estatuto, ensino ou forma de língua

**Função:** Permite reconhecer, explicar e testar planeamento linguístico na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** definir política de ensino linguístico

### 1094. política linguística

**Construção:** decisões sociais e institucionais sobre línguas e variedades

**Função:** Permite reconhecer, explicar e testar política linguística na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** reconhecer línguas em educação

### 1095. consciência metalinguística

**Construção:** capacidade de refletir explicitamente sobre a língua

**Função:** Permite reconhecer, explicar e testar consciência metalinguística na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** explicar por que uma forma funciona

### 1096. lacuna interna

**Construção:** ausência de definição, dependência, exemplo ou teste necessário dentro do conhecimento declarado

**Função:** Permite reconhecer, explicar e testar lacuna interna na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** conceito sem base seria lacuna interna

### 1097. fronteira aberta

**Construção:** limite que depende de dados vivos, variedade, contexto ou investigação externa

**Função:** Permite reconhecer, explicar e testar fronteira aberta na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** pronúncia regional exige observação local

### 1098. limite operacional

**Construção:** capacidade que o motor ainda não executa embora o conceito esteja construído

**Função:** Permite reconhecer, explicar e testar limite operacional na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** o motor conhece elipse mas pode não recuperá-la automaticamente

### 1099. mestria conceitual

**Construção:** estado em que o domínio interno possui definição, dependências, exemplos, contraste e testes sem lacunas internas

**Função:** Permite reconhecer, explicar e testar mestria conceitual na construção do Português.

**Dependências:** análise linguística

**Tema de consulta:** `metalinguagem`

**Exemplo mínimo:** a base pode explicar cada conceito sem saltar dependências

### 1100. hibridismo

**Construção:** Hibridismo é processo de formação de palavras que combina radicais ou afixos de línguas diferentes numa mesma palavra.

**Função:** Explica por que palavras como sociologia (latim + grego) e automóvel (grego + latim) não se encaixam só em justaposição ou aglutinação de uma língua só.

**Dependências:** justaposição, aglutinação

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** sociologia; automóvel; burocracia

### 1101. verbo pronominal

**Construção:** Verbo pronominal é o verbo que exige um pronome reflexivo como parte obrigatória da sua forma, mesmo quando o sentido não é reflexivo.

**Função:** Separa verbos como arrepender-se e queixar-se, que não existem sem o pronome, de verbos que só ocasionalmente recebem pronome reflexivo.

**Dependências:** verbo, pronome reflexivo

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** arrepender-se; queixar-se; suicidar-se

### 1102. verbo reflexivo

**Construção:** Verbo reflexivo é o verbo pronominal cuja ação, praticada pelo sujeito, recai sobre o próprio sujeito.

**Função:** Distingue eu me machuquei (ação sobre si mesmo) de eu me arrependi (verbo pronominal sem ação transferível a devolver ao sujeito).

**Dependências:** verbo pronominal

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** machucar-se; pentear-se; vestir-se

### 1103. verbo impessoal

**Construção:** Verbo impessoal é o verbo usado sem sujeito gramatical algum, nem mesmo oculto ou indeterminado.

**Função:** Explica orações sem sujeito como chove e há problemas, onde não existe nada, explícito ou implícito, praticando a ação.

**Dependências:** verbo, oração sem sujeito

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** chove; há problemas; faz frio

### 1104. verbo unipessoal

**Construção:** Verbo unipessoal é o verbo conjugado só na terceira pessoa, geralmente para vozes de animais ou fenômenos específicos, mas que admite sujeito — diferente do impessoal.

**Função:** Separa o cão late (tem sujeito, só não conjuga em todas as pessoas) do impessoal chove (nunca tem sujeito nenhum).

**Dependências:** verbo, pessoa gramatical

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** o cão late; a vaca muge

### 1105. verbo anômalo

**Construção:** Verbo anômalo é o verbo irregular cuja conjugação muda de radical entre tempos, a ponto de parecer formada por mais de um verbo (supleção).

**Função:** Identifica ser e ir como o caso mais extremo de irregularidade: fui serve tanto para ser quanto para ir, e são/eram não têm nenhuma semelhança sonora com a forma ser.

**Dependências:** verbo irregular

**Tema de consulta:** `morfologia_lexico`

**Exemplo mínimo:** ser; ir

### 1106. locução verbal

**Construção:** Locução verbal é o nome tradicional escolar para a combinação de um verbo auxiliar com um verbo principal no infinitivo, gerúndio ou particípio — o mesmo fenômeno que a linguística chama perífrase verbal.

**Função:** Reconhece vai chover, está chovendo e tinha chovido como uma única unidade verbal, não dois verbos separados.

**Dependências:** verbo auxiliar, perífrase verbal

**Tema de consulta:** `discurso_e_interpretacao`

**Exemplo mínimo:** vai chover; está chovendo; tinha chovido

### 1107. regência nominal

**Construção:** Regência nominal é a relação de dependência entre um nome (substantivo, adjetivo ou advérbio) e o termo que ele exige, geralmente ligado por uma preposição fixa.

**Função:** Separa a regência do nome (respeito a, orgulho de) da regência do verbo, embora ambas usem preposição para ligar termos.

**Dependências:** regência

**Tema de consulta:** `sintaxe_e_uso`

**Exemplo mínimo:** respeito a; orgulho de; necessário a

### 1108. se apassivador

**Construção:** Se apassivador é o pronome se que transforma um verbo transitivo direto em voz passiva sintética, com o objeto virando o sujeito paciente que concorda em número com o verbo.

**Função:** Explica por que explicam-se os problemas equivale a os problemas são explicados, com o verbo no plural concordando com problemas, não com um sujeito oculto indeterminado.

**Dependências:** voz passiva, pronome reflexivo, verbo transitivo direto

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** explicam-se os problemas; explica-se o problema

### 1109. se índice de indeterminação do sujeito

**Construção:** Se índice de indeterminação do sujeito é o pronome se junto a um verbo intransitivo, de ligação ou transitivo indireto, que nunca concorda em número porque não há sujeito nenhum para concordância.

**Função:** Explica por que entende-se de livros e precisa-se de funcionários mantêm o verbo sempre na terceira pessoa do singular, mesmo com um plural depois da preposição.

**Dependências:** sujeito indeterminado, pronome reflexivo

**Tema de consulta:** `sintaxe`

**Exemplo mínimo:** entende-se de livros; precisa-se de funcionários

### 1110. sinestesia

**Construção:** Sinestesia é figura que combina impressões de sentidos diferentes numa mesma expressão.

**Função:** Explica combinações como cor quente e silêncio ensurdecedor, que misturam visão/tato ou som/ausência de som.

**Dependências:** metáfora, conotação

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** cor quente; voz doce; silêncio ensurdecedor

### 1111. antonomásia

**Construção:** Antonomásia substitui um nome próprio por uma expressão que o caracteriza, ou vice-versa.

**Função:** Explica por que a Cidade Maravilhosa identifica o Rio de Janeiro sem citar o nome, do mesmo jeito que metonímia substitui um termo por outro relacionado.

**Dependências:** metonímia

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** a Cidade Maravilhosa; o Poeta dos Escravos

### 1112. zeugma

**Construção:** Zeugma é a elipse de um termo já expresso numa oração anterior, omitido numa oração coordenada seguinte.

**Função:** Explica eu gosto de música; ele, de esportes, em que gosta fica implícito na segunda oração.

**Dependências:** elipse, oração coordenada

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Eu gosto de música; ele, de esportes.

### 1113. assíndeto

**Construção:** Assíndeto é a figura de encadear orações coordenadas sem conjunção, ligadas só por vírgula, para dar ritmo rápido à frase.

**Função:** Nomeia o efeito estilístico do mesmo fenômeno que oração coordenada assindética já constrói — vim, vi, venci.

**Dependências:** oração coordenada assindética

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Vim, vi, venci.

### 1114. polissíndeto

**Construção:** Polissíndeto é a figura de repetir a mesma conjunção antes de cada oração coordenada, para dar ênfase ou acúmulo.

**Função:** Nomeia o efeito estilístico oposto ao assíndeto, usando oração coordenada sindética repetida em vez de omitida.

**Dependências:** oração coordenada sindética, coordenação aditiva

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** E corre, e pula, e grita.

### 1115. aliteração

**Construção:** Aliteração é a repetição do mesmo som consonantal no início de palavras próximas, para efeito sonoro.

**Função:** Reconhecida de verdade contando a consoante inicial mais frequente numa sequência de palavras, não citada de memória — o rato roeu a roupa do rei de Roma repete o r cinco vezes.

**Dependências:** consoante, som

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** o rato roeu a roupa do rei de Roma

### 1116. assonância

**Construção:** Assonância é a repetição do mesmo som vocálico em palavras próximas, para efeito sonoro.

**Função:** Reconhecida de verdade contando a vogal inicial mais frequente numa sequência de palavras — Amanhã a Ana anda apressada repete o som de a cinco vezes.

**Dependências:** vogal, som

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Amanhã a Ana anda apressada.

### 1117. paronomásia

**Construção:** Paronomásia é o jogo de palavras que aproxima parônimos (palavras parecidas no som, diferentes no sentido) para efeito expressivo.

**Função:** Reaproveita paronímia já construída: quem não arrisca, não petisca aproxima arrisca e petisca pelo som.

**Dependências:** paronímia

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Quem não arrisca, não petisca.

### 1118. silepse

**Construção:** Silepse é a concordância feita com a ideia (sentido) em vez da forma gramatical explícita.

**Função:** Explica Vossa Excelência está cansado, em que o adjetivo concorda com o gênero da pessoa real, não com a forma gramatical feminina de vossa excelência.

**Dependências:** concordância nominal, concordância verbal

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Vossa Excelência está cansado.

### 1119. anacoluto

**Construção:** Anacoluto é a quebra da construção sintática iniciada numa oração, abandonada por outra estrutura antes de terminar.

**Função:** Explica eu, esse problema não me interessa, em que eu começa como se fosse sujeito mas a oração muda de estrutura sem ele.

**Dependências:** oração

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Eu, esse problema não me interessa.

### 1120. trema

**Construção:** Trema é o sinal gráfico de dois pontos sobre o u, abolido do português padrão pelo Acordo Ortográfico de 1990, mas preservado em nomes próprios estrangeiros e suas derivações.

**Função:** Explica por que Müller e Hülsmann mantêm o trema mesmo depois do acordo, que só eliminou seu uso em palavras genuinamente portuguesas como linguiça e sequência.

**Dependências:** acento, marca

**Tema de consulta:** `som_e_escrita`

**Exemplo mínimo:** Müller; Hülsmann

### 1121. paródia

**Construção:** Paródia é a reescrita de um texto conhecido que transforma seu sentido ou tom, geralmente para efeito cômico ou crítico, mantendo referência reconhecível ao original.

**Função:** Liga intertextualidade a um caso concreto: uma paródia só existe porque aponta de volta para o texto que imita e altera.

**Dependências:** intertextualidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma letra de música reescrita com sentido cômico sobre outro tema

### 1122. pastiche

**Construção:** Pastiche é a imitação do estilo de um autor ou obra, sem necessariamente alterar o sentido ou ter intenção cômica ou crítica — ao contrário da paródia.

**Função:** Distingue pastiche de paródia pela intenção: pastiche imita por admiração ou exercício de estilo, paródia imita para transformar ou criticar.

**Dependências:** paródia, intertextualidade

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um conto escrito imitando o estilo de outro autor, sem sátira nem crítica

### 1123. sátira

**Construção:** Sátira é o texto que usa ironia, exagero ou humor para criticar costumes, pessoas públicas ou instituições.

**Função:** Liga ironia e hipérbole a um gênero concreto: a sátira exagera e ironiza deliberadamente para expor uma crítica.

**Dependências:** ironia, hipérbole

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma charge política que exagera um defeito de um governante

### 1124. verso

**Construção:** Verso é cada linha de um poema, unidade rítmica organizada por contagem de sílabas e por rima.

**Função:** Serve de base para estrofe, métrica e rima.

**Dependências:** sílaba

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Amor é fogo que arde sem se ver

### 1125. estrofe

**Construção:** Estrofe é o agrupamento de versos separado por espaço em branco, unidade maior que o verso dentro do poema.

**Função:** Organiza versos em blocos, do mesmo jeito que parágrafos organizam frases em prosa.

**Dependências:** verso

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** quatro versos formando uma quadra

### 1126. métrica

**Construção:** Métrica é o estudo da contagem de sílabas poéticas de um verso e da organização rítmica que essa contagem produz.

**Função:** Não é a contagem gramatical de sílabas: a métrica poética funde vogais de palavras vizinhas (sinalefa) quando uma palavra termina e a seguinte começa em vogal. A contagem automática com sinalefa ainda não está construída; depende da tonicidade automática, já registrada como fronteira aberta em sílaba tônica.

**Dependências:** sílaba, verso

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** contar as sílabas poéticas de um verso decassílabo dá dez

### 1127. escansão

**Construção:** Escansão é o processo de contar e marcar as sílabas poéticas de um verso, aplicando sinalefa nas junções entre palavras.

**Função:** É o procedimento concreto que a métrica descreve; automatizá-lo depende da mesma contagem de sílabas poéticas ainda não construída, registrada em métrica.

**Dependências:** métrica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** separar um verso em sílabas poéticas contadas uma a uma

### 1128. decassílabo

**Construção:** Decassílabo é o verso de dez sílabas poéticas, o metro clássico da épica portuguesa e do soneto camoniano.

**Função:** Identifica versos como os de Os Lusíadas, escritos nesse metro.

**Dependências:** métrica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** As armas e os barões assinalados

### 1129. redondilha

**Construção:** Redondilha é o verso popular de cinco sílabas (redondilha menor) ou sete sílabas (redondilha maior), comum na poesia de tradição oral e em Camões.

**Função:** Identifica o metro mais próximo da fala espontânea, usado em cantigas e trovas populares.

**Dependências:** métrica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** Redondilha maior tem sete sílabas poéticas

### 1130. alexandrino

**Construção:** Alexandrino é o verso de doze sílabas poéticas, dividido em dois hemistíquios de seis, comum na poesia francesa e também usado em português.

**Função:** Identifica o metro mais longo entre os clássicos, dividido ao meio por uma pausa rítmica.

**Dependências:** métrica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** um verso de doze sílabas dividido em dois blocos de seis

### 1131. rima toante

**Construção:** Rima toante é a coincidência apenas do som da vogal tônica final entre versos, sem exigir que as consoantes seguintes também coincidam.

**Função:** Separa a rima mais solta, de som aproximado, da rima consoante, de som completo.

**Dependências:** rima silábica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** coração / paixão (mesma vogal tônica, consoantes finais diferentes)

### 1132. rima consoante

**Construção:** Rima consoante é a coincidência completa dos sons finais dos versos a partir da vogal tônica, vogais e consoantes.

**Função:** É a rima mais exata, oposta à rima toante.

**Dependências:** rima silábica

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** coração / limão (mesmo som final completo)

### 1133. rima rica

**Construção:** Rima rica é a rima entre palavras de classes gramaticais diferentes, como um substantivo com um verbo.

**Função:** Marca um efeito de rima considerado menos previsível pela gramática tradicional da poesia.

**Dependências:** rima silábica, classe gramatical

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** rima entre um substantivo e um verbo, classes diferentes

### 1134. rima pobre

**Construção:** Rima pobre é a rima entre palavras da mesma classe gramatical, como dois substantivos ou dois verbos.

**Função:** Marca um efeito de rima considerado mais previsível pela gramática tradicional da poesia.

**Dependências:** rima silábica, classe gramatical

**Tema de consulta:** `papeis_e_figuras`

**Exemplo mínimo:** rima entre dois substantivos, mesma classe

### 1135. literatura

**Construção:** Literatura é o uso da linguagem verbal com função estética predominante, organizando som, forma e sentido para produzir efeito além da informação referencial direta.

**Função:** Separa literatura de texto não literário pela função predominante da linguagem: um manual técnico informa, um poema também constrói efeito sonoro, rítmico e figurado como parte do sentido — a fronteira não é absoluta, um mesmo texto pode combinar as duas funções.

**Dependências:** gênero literário, figura de linguagem, conotação

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um poema usa som e ritmo como parte do sentido, não só a informação

### 1136. gênero lírico

**Construção:** Gênero lírico é a categoria de obras organizadas pela expressão subjetiva de um eu que sente, geralmente em verso.

**Função:** Nomeia o gênero que poema já constrói na prática, completando a tríade clássica ao lado de gênero dramático já existente.

**Dependências:** gênero literário, poema

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** um poema que expressa o sentimento de quem fala

### 1137. gênero épico

**Construção:** Gênero épico é a categoria de obras organizadas pela narração de eventos e feitos, tradicionalmente em verso, hoje também em prosa narrativa extensa.

**Função:** Completa a tríade clássica ao lado de gênero lírico e gênero dramático, ligando à narração e à estrutura narrativa que romance e conto já constroem.

**Dependências:** gênero literário, narração, estrutura narrativa

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** uma narrativa longa que conta feitos de um herói

### 1138. método de análise literária

**Construção:** Método de análise literária é o procedimento de aplicar, em sequência, as ferramentas já construídas de figura de linguagem, narrador, estrutura narrativa, coesão e coerência a um texto de função estética.

**Função:** Transforma uma lista de conceitos soltos em um roteiro: identificar gênero, localizar figuras de linguagem, reconhecer narrador (quando houver) e mapear estrutura antes de interpretar sentido.

**Dependências:** análise textual, gênero literário, figura de linguagem, narrador

**Tema de consulta:** `texto_discurso`

**Exemplo mínimo:** aplicar identificação de gênero, figuras e narrador a um mesmo texto, nessa ordem

### 1139. funcionamento

**Construção:** Funcionamento é a linha única pela qual o Português PSF cresce da diferença mínima à produção sonora, escrita, palavra, sintaxe, sentido, texto, uso, variação, aprendizagem, tradução, análise e reconstrução controlada.

**Função:** Integra o conhecimento conceptual sem lacunas internas conhecidas, conserva fronteiras abertas e separa limites operacionais do motor sem fingir capacidade.

**Dependências:** diferença, som, grafema, fonema, fonotática, palavra, morfema, sintagma, oração, predicação, sentido, significado composicional, texto, macroestrutura textual, gramática, pragmática, ato de fala, intertextualidade, sociolinguística, aquisição da linguagem, tradução, análise linguística, mestria conceitual, fronteira aberta, limite operacional, adequação linguística, leitura, escrita, competência comunicativa, reconstrução linguística PSF

**Tema de consulta:** `integracao`

**Exemplo mínimo:** diferença → forma → relação → sentido → uso → análise → reconstrução

**Não confundir com:** Não é completude absoluta do português vivo nem capacidade automática ilimitada.

## Fronteiras abertas preservadas

- **vogal:** O inventário fonético completo varia entre variedades do português e permanece aberto por variedade.
- **consoante:** O inventário fonético completo varia entre variedades do português e permanece aberto por variedade.
- **acento:** Casos especiais e diferenças normativas entre variedades continuam abertos para construção testada.
- **sílaba:** Casos excepcionais e diferenças de pronúncia entre variedades permanecem abertos.
- **coerência:** Coerência profunda depende de mundo e contexto; o motor atual só marca indícios simples.
- **intenção comunicativa:** A leitura profunda de intenção depende de contexto maior e fica marcada como crescimento.
- **antonímia:** Oposição completa depende de contexto e escala.
- **variação linguística:** A variação regional e social completa ainda deve crescer com cautela.
- **contexto:** A modelagem completa de contexto social, histórico e situacional ainda deve crescer.
- **modo verbal:** Alternâncias de modo dependentes de regência, negação e variedade continuam abertas.
- **interjeição:** A leitura pragmática de interjeições depende de contexto.
- **perífrase verbal:** Combinações menos frequentes e diferenças de variedade continuam abertas.
- **ambiguidade:** Resolver ambiguidade exige mais contexto e não deve ser fingido.
- **alofone:** O inventário regional completo permanece aberto.
- **vibrante:** A variação regional de r fica explicitamente aberta.
- **apóstrofo:** O uso atual é restrito e deve ser validado por contexto.
- **empréstimo linguístico:** A história específica de cada empréstimo exige fonte externa e fica separada.
- **evidência:** Evidência externa deve manter fonte e não virar conhecimento puro automaticamente.
- **mesóclise:** A frequência e adequação por variedade devem permanecer explícitas.
- **transformação de discurso:** Mudanças completas dependem do contexto enunciativo.
- **ato de fala:** A força exata pode depender de contexto, relação social e entoação.
- **intertextualidade:** Reconhecimento automático de fonte depende de corpus e evidência externa.
- **bilinguismo:** Perfis concretos exigem observação individual ou comunitária.
- **psicolinguística:** Processos cognitivos reais exigem evidência experimental externa.
- **arcaísmo:** A datação de cada forma exige fonte histórica externa.
- **vogal nasal:** Realizações variam entre variedades.
- **vogal aberta:** A distribuição exata varia entre variedades.
- **vogal fechada:** A distribuição exata varia entre variedades.
- **vogal átona:** A redução depende da variedade e da posição.
- **dental:** A fronteira dental–alveolar varia entre descrições e variedades.
- **alveolar:** Realizações variam entre variedades.
- **palatal:** Há variação fonética entre comunidades.
- **glotal:** A presença e função variam entre variedades.
- **assimilação fonológica:** Regras concretas dependem da variedade e do ambiente.
- **elisão:** Inventários por variedade permanecem abertos.
- **epêntese:** Ocorrências concretas dependem da variedade.
- **metátese:** Casos concretos exigem observação histórica ou regional.
- **redução vocálica:** Padrões variam fortemente entre variedades.
- **encadeamento fônico:** Padrões concretos variam entre variedades.
- **acento em hiato:** Exceções por contexto gráfico ainda precisam de regras testadas.
- **uso de x:** Muitos casos exigem memória lexical e comparação histórica.
- **pretérito mais-que-perfeito:** Uso por variedade e registro permanece aberto.
- **alternância de código:** Funções sociais concretas dependem da comunidade.
- **diglossia:** Configurações concretas dependem da comunidade.
- **equivalência tradutória:** Exige conhecimento suficiente das duas línguas e do contexto.
- **foco informacional:** A identificação depende de contexto e não deve ser adivinhada.
- **variante:** A distribuição de cada variante precisa de contexto.
- **repertório linguístico:** Disponibilidade e domínio variam por situação.
- **gênero formal:** As convenções precisam ser verificadas por instituição.
- **figura de linguagem:** A identificação depende de contexto e efeito.
- **fonotática:** O inventário concreto precisa ser construído separadamente por variedade.
- **sequência fonotática:** A aceitabilidade pode variar por palavra, empréstimo e variedade.
- **sílaba aberta:** A análise pode mudar conforme a realização fonética da variedade.
- **ataque complexo:** As combinações aceites variam por posição e variedade.
- **coda simples:** A realização concreta varia entre variedades.
- **coda complexa:** A existência e análise dependem da variedade e da fronteira morfológica.
- **palavra fonológica:** A delimitação operacional ainda precisa de regras por variedade.
- **acento lexical:** Há palavras e variedades com comportamento que exige análise própria.
- **acento frásico:** A posição depende de foco, ritmo e contexto.
- **foco prosódico:** A interpretação exige contexto e não deve ser adivinhada.
- **contorno entoacional:** A forma concreta varia por falante e variedade.
- **assimilação regressiva:** Os casos concretos precisam ser observados por variedade.
- **assimilação progressiva:** Os casos concretos precisam ser observados por variedade.
- **síncope:** A ocorrência varia por ritmo, registro e variedade.
- **apócope:** Os casos produtivos precisam ser descritos por variedade.
- **prótese:** O inventário histórico e regional permanece aberto.
- **paragoge:** O inventário histórico e regional permanece aberto.
- **convenção ortográfica:** Mudanças históricas e diferenças oficiais exigem fonte de comparação e reconstrução.
- **variante gráfica:** Cada variante precisa de contexto explícito.
- **homofonia:** A igualdade sonora depende da variedade.
- **uso de r:** A realização sonora varia entre variedades.
- **uso de e e i átonos:** A correspondência precisa ser construída por famílias lexicais e variedade.
- **uso de o e u átonos:** A correspondência precisa ser construída por famílias lexicais e variedade.
- **maiúscula no início de frase:** Casos após dois-pontos, enumeração e citação exigem contexto.
- **travessão de diálogo:** Convenções editoriais variam.
- **aspas de citação:** Tipos de aspas e convenções variam por publicação.
- **morfema derivacional:** A produtividade varia por padrão.
- **gramaticalização:** Reconstruções históricas exigem evidência externa comparada e não entram como fato sem validação.
- **produtividade morfológica:** A medida exige corpus e critérios explícitos.
- **adjetivo qualificativo:** A fronteira com adjetivo relacional depende do contexto.
- **pronome reto:** O uso real varia entre variedades e registros.
- **pronome oblíquo:** Distribuição de formas tônicas e átonas varia por variedade.
- **pronome recíproco:** A forma pode coincidir com reflexivo e depender do contexto.
- **determinante demonstrativo:** Sistemas de distância variam no uso.
- **determinante possessivo:** A presença de artigo e posição variam por variedade.
- **verbo regular:** Regularidade precisa ser definida por tempo, modo e variedade.
- **verbo defectivo:** O inventário depende de época, variedade e registro.
- **verbo abundante:** Distribuição por auxiliar, registro e variedade precisa de teste.
- **ordem básica:** A ordem de referência precisa ser identificada por variedade e tipo de oração.
- **ordem sujeito-verbo-objeto:** Clíticos, foco e variedades podem produzir outras ordens.
- **inversão sintática:** A interpretação depende de contexto, foco e variedade.
- **topicalização:** Retomada pronominal e aceitabilidade variam por construção.
- **focalização:** A fonte do foco não deve ser inferida sem contexto.
- **deslocamento à esquerda:** Os padrões variam por variedade e registro.
- **sujeito nulo:** Frequência e condições variam entre variedades.
- **construção apresentativa:** Os formatos variam entre gêneros e variedades.
- **oração temporal:** A ordem temporal pode depender de aspecto e contexto.
- **significado do enunciado:** Sem contexto suficiente, deve permanecer indeterminado.
- **compatibilidade semântica:** Metáfora e contexto podem recuperar combinações inesperadas.
- **telicidade:** A leitura depende de objeto, quantidade e contexto.
- **escopo:** O escopo pode ser ambíguo e precisa de estrutura/contexto.
- **escopo da negação:** Prosódia e contexto podem alterar a leitura.
- **cortesia linguística:** Normas de cortesia variam culturalmente e não devem ser universalizadas.
- **variedade nacional:** Cada variedade precisa de dados próprios e não pode ser inventada por comparação superficial.
- **língua segunda:** A fronteira com língua estrangeira depende do contexto de uso.
- **tradução literal:** Pode falhar em idiomatismos, sintaxe e contexto.
- **dado linguístico:** Dados precisam preservar contexto e origem.
- **análise fonológica:** Precisa de inventário por variedade.
- **análise pragmática:** Sem contexto suficiente, deve retornar indeterminação.
- **carta:** Convenções variam entre carta pessoal, formal e histórica.
- **ensaio:** Convenções dependem do contexto académico ou literário.
- **conto:** Extensão e fronteiras com outras formas variam.
- **romance:** Fronteiras históricas e formais variam.
- **substantivo contável:** Uma mesma palavra pode mudar de leitura conforme o contexto.
- **substantivo animado:** Personificação e contexto podem alterar a leitura.
- **pronome de tratamento:** Inventário e concordância variam por comunidade e registro.
- **construção impessoal:** Os critérios variam por análise e variedade.
- **construção existencial:** Verbos e concordância variam por variedade e norma.
- **predicado de estado:** A leitura depende do verbo, complemento e contexto.
- **dêixis social:** Os sistemas sociais variam por comunidade.
- **evidência linguística:** A qualidade depende de origem, contexto e representatividade.
- **exemplo negativo:** A rejeição pode variar por falante, variedade e intenção.
- **análise semântica:** Contexto externo não pode ser inventado.
- **ata:** Formato varia por instituição.

## Limites operacionais preservados

- **dígrafo:** Exceções e diferenças entre escrita e realização sonora continuam abertas por família lexical.
- **encontro consonantal:** A separação silábica de encontros depende da estrutura da palavra e conserva casos para teste.
- **tonicidade:** A identificação automática da tonicidade ainda é parcial.
- **pessoa gramatical:** A conjugação completa por pessoa ainda deve crescer.
- **concordância:** A concordância verbal profunda ainda é parcial.
- **coesão:** O reconhecimento completo de conectivos e referentes ainda deve crescer.
- **campo semântico:** O agrupamento automático ainda é pequeno e deve crescer por observação.
- **polissemia:** A escolha automática de sentido ainda é parcial.
- **sinonímia:** Sinónimo absoluto não é assumido; a proximidade depende de uso.
- **conectivo:** A lista de conectivos e valores ainda deve crescer por famílias.
- **retomada:** A retomada profunda ainda é parcial.
- **elipse:** A recuperação automática de elipse ainda é lacuna.
- **inferência:** Inferência depende de limites claros para não fingir conhecimento de mundo.
- **complemento:** A separação completa dos tipos de complemento ainda deve crescer.
- **adjunto:** A distinção fina entre adjunto e complemento ainda precisa de mais testes.
- **regência:** As regências normativas completas ainda não foram materializadas.
- **colocação:** Colocação pronominal normativa ainda fica para crescimento.
- **norma:** Norma completa não é assumida como pronta.
- **uso:** O motor ainda não modela todos os usos sociais.
- **registro:** A adaptação completa de registro ainda é parcial.
- **modalidade:** Modalidades epistémica, deôntica e avaliativa ainda precisam de famílias operacionais próprias.
- **negação:** A negação profunda com escopo ainda precisa crescer.
- **interrogação:** Perguntas indiretas e retóricas ainda exigem crescimento.
- **exclamação:** A leitura emocional completa não deve ser fingida.
- **tempo verbal:** Usos discursivos e concordância temporal complexa continuam abertos.
- **aspecto verbal:** A classificação aspectual completa ainda é lacuna.
- **voz verbal:** A análise completa de voz ativa, passiva e reflexiva ainda é parcial.
- **preposição:** Regências e usos preposicionais completos ainda devem crescer.
- **conjunção:** Locuções e valores contextuais múltiplos continuam abertos por família.
- **artigo:** Usos especiais do artigo ainda devem crescer por observação.
- **discurso direto:** A pontuação completa de discurso direto ainda deve crescer.
- **discurso indireto:** Transformações completas de pessoa, tempo e dêixis ainda são lacuna.
- **progressão temática:** A medição automática profunda da progressão ainda deve crescer.
- **pragmática:** A pragmática completa depende de situação e ainda deve crescer com cautela.
- **estilo:** A avaliação automática de estilo ainda é parcial.
- **revisão:** Critérios completos de revisão ainda devem crescer.
- **interpretação:** Interpretação profunda exige limites explícitos para não fingir mundo externo.
- **produção da fala:** A descrição anatómica completa fica fora do núcleo atual.
- **aparelho fonador:** A anatomia detalhada exige estudo próprio.
- **prosódia:** A medição acústica completa não é fingida.
- **hífen:** As regras completas de hifenização ficam por famílias.
- **separação silábica:** Exceções normativas continuam marcadas.
- **acentuação gráfica:** As famílias de regras e exceções ainda devem crescer.
- **conjugação:** Paradigmas irregulares completos ficam como crescimento contínuo.
- **concordância verbal:** Casos especiais permanecem para crescimento.
- **vírgula:** As regras completas exigem famílias de construção.
- **multimodalidade:** Análise de imagem, áudio e gesto permanece fora do núcleo verbal atual.
- **aquisição da linguagem:** Desenvolvimento humano real exige observação externa e não é simulado pelo motor.
- **tradução:** O motor atual não contém conhecimento puro de outras línguas suficiente para tradução geral.
- **regra de oxítona:** Terminações e exceções precisam de tabela operacional testada.
- **regra de paroxítona:** Terminações e exceções precisam de tabela operacional testada.
- **regra de monossílabo tônico:** Terminações e exceções precisam de tabela operacional testada.
- **acento diferencial:** O inventário normativo precisa permanecer explícito e testado.
- **uso de s:** As famílias lexicais e exceções precisam de inventário testado.
- **uso de ss:** Exceções e fronteiras morfológicas precisam de teste.
- **uso de c:** Famílias e exceções precisam de inventário testado.
- **uso de ç:** Famílias morfológicas e exceções precisam de teste.
- **uso de z:** Famílias e exceções precisam de inventário testado.
- **uso de ch:** Inventário lexical e famílias derivacionais precisam crescer.
- **uso de g:** Famílias e exceções precisam de inventário testado.
- **uso de j:** Origem e família lexical continuam relevantes.
- **uso de qu:** Casos com realização de u precisam de inventário testado.
- **uso de gu:** Casos com realização de u precisam de inventário testado.
- **maiúscula inicial:** Casos institucionais e estilísticos exigem norma explícita.
- **abreviatura:** Inventários convencionais dependem de uso e norma.
- **translineação:** Casos especiais de compostos e dígrafos permanecem para teste.
- **plural em -ão:** A escolha concreta precisa de família lexical testada.
- **plural de palavra em -l:** Subfamílias em -al, -el, -ol e -ul precisam de regras separadas.
- **presente do conjuntivo:** Regências e alternâncias modais precisam de famílias testadas.
- **acarretamento:** Depende de sentidos estabilizados e escopo explícito.
- **contacto linguístico:** Efeitos concretos exigem história e observação comunitária.
- **paradigma:** O paradigma completo de cada classe ainda precisa ser materializado.
- **segmentação:** O resultado depende do nível e do critério.
- **existência:** Existência no discurso não prova existência no mundo externo.
- **relação temporal:** O texto pode deixar a relação indeterminada.
- **domínio contextual:** O domínio pode permanecer implícito.
- **estrutura semântica:** A notação formal é opcional; a relação construída é o fundamento.
- **explicação:** Uma explicação pode ser clara e ainda falsa; precisa de evidência.
- **exemplificação:** Um exemplo não prova universalidade.
- **causa:** Causalidade no mundo exige evidência além da sequência textual.
- **voz discursiva:** A fonte pode ser implícita ou ambígua.
- **comunidade de fala:** As fronteiras são sociais e podem sobrepor-se.
- **lacuna de conhecimento:** Deve ser reduzida por construção, nunca escondida.
- **destinatário:** Pode ser múltiplo, implícito ou imaginado.
- **gênero digital:** Formatos mudam com plataformas e usos.
- **gênero informativo:** Pode conter interpretação e seleção editorial.
- **gênero literário:** Obras podem misturar gêneros.
- **pesquisa:** Resultados dependem da qualidade dos dados e métodos.
- **turno de fala:** Sobreposição e interrupção exigem marcação própria.
- **sílaba fechada:** A identificação concreta depende da pronúncia analisada.
- **grupo prosódico:** Os limites concretos exigem fala observada.
- **fronteira prosódica:** A deteção automática ainda não está implementada.
- **dissimilação:** A produtividade no português atual deve ser validada por dados.
- **segmentação gráfica:** Casos de hífen, contração e expressão fixa exigem regras próprias.
- **juntura vocabular:** A fala pode ocultar fronteiras que a escrita conserva.
- **grafia lexical:** A grafia de cada item precisa ser materializada e testada, não adivinhada.
- **homografia:** A classificação entre polissemia e homonímia pode exigir história lexical.
- **uso de h:** O inventário lexical e os casos de dígrafo precisam ser testados por família.
- **uso de rr:** Famílias derivadas e fronteiras morfológicas devem ser testadas.
- **uso de m antes de p e b:** Empréstimos, nomes próprios e fronteiras morfológicas precisam ser verificados.
- **uso de n antes de consoante:** A escolha concreta continua lexical e precisa de famílias testadas.
- **maiúscula em nome próprio:** Títulos, instituições e usos estilísticos precisam de regras específicas.
- **ponto em abreviatura:** Há abreviaturas sem o mesmo padrão e convenções especializadas.
- **símbolo não alfabético:** Cada sistema de símbolos precisa de domínio e regra próprios.
- **vírgula de aposto:** Aposto restritivo e estruturas sem pausa exigem distinção.
- **alomorfia:** A análise de cada alternância precisa de paradigma e evidência.
- **morfema livre:** A autonomia depende da análise e do uso.
- **morfema zero:** Só deve ser admitido quando o contraste do paradigma exigir, não para preencher qualquer vazio.
- **palavra simples:** A história da palavra pode divergir da análise atual.
- **palavra composta:** A grafia unida, hifenizada ou separada não decide sozinha a análise.
- **lexicalização:** A estabilidade exige observação de uso e não pode ser presumida por um exemplo.
- **adjetivo relacional:** Alguns adjetivos alternam entre leitura relacional e qualificativa.
- **adjetivo pátrio:** O inventário e as formas oficiais precisam ser construídos lexicalmente.
- **pronome reflexivo:** A interpretação pode competir com leitura lexical do verbo.
- **adjunto de frase:** A posição e o alcance podem gerar ambiguidade.
- **constituinte sintático:** Os testes de constituência precisam ser implementados e podem divergir.
- **fronteira de constituinte:** A fronteira pode não ter marca visível.
- **deslocamento à direita:** A prosódia é decisiva e precisa ser observada.
- **oração não finita:** Infinitivo pessoal exige análise de pessoa própria.
- **oração comparativa:** Pode haver elipse de elementos repetidos.
- **significado lexical:** Não é uma lista completa sem observação de uso.
- **significado composicional:** Idiomatismos e inferências exigem tratamento adicional.
- **significado da frase:** Ambiguidade pode produzir mais de uma leitura.
- **traço semântico:** Traços são ferramentas de análise, não partículas físicas da palavra.
- **quantificação:** Quantidades vagas e coletivas exigem análise própria.
- **quantificador universal:** O domínio precisa ser identificado; não é o universo inteiro por padrão.
- **macroestrutura textual:** A extração automática ainda é parcial.
- **organização retórica:** Pode haver mais de uma organização no mesmo texto.
- **relação de causa:** Texto pode alegar causa sem prová-la no mundo.
- **estrutura narrativa:** Narrativas podem quebrar ou omitir partes do padrão.
- **narrador:** A identificação pode ser ambígua.
- **tempo narrativo:** Retrocesso e antecipação exigem conceitos adicionais.
- **conflito narrativo:** Nem toda narrativa depende de conflito forte.
- **clímax:** Algumas narrativas distribuem ou evitam um único clímax.
- **desfecho:** Pode ser aberto, suspenso ou múltiplo.
- **língua primeira:** Pode haver aquisição inicial de mais de uma língua.
- **unidade de tradução:** A unidade pode ser palavra, expressão, frase ou trecho conforme o problema.
- **tradução funcional:** Exige justificar perdas, ganhos e escolhas.
- **interferência linguística:** A causa precisa ser observada, não presumida por um erro isolado.
- **análise morfológica:** Segmentações concorrentes precisam ser registradas.
- **análise sintática:** O motor automático ainda cobre apenas parte dessas operações.
- **análise textual:** Critérios dependem do objetivo de análise.
- **anotação linguística:** O esquema precisa documentar categorias e incerteza.
- **segmentação de corpus:** Unidades de fala exigem critérios prosódicos próprios.
- **classificação linguística:** Categorias podem sobrepor-se conforme nível e uso.
- **correio eletrónico:** Convenções mudam por ambiente e finalidade.
- **notícia:** A veracidade depende de apuração externa; o PSF não deve inventar fatos.
- **reportagem:** Exige fontes externas verificáveis quando trata do mundo.
- **entrevista:** A edição pode alterar ordem e extensão; deve ser declarada.
- **requerimento:** Exigências legais e administrativas precisam ser verificadas externamente.
- **receita textual:** Conteúdo culinário ou técnico específico precisa ser validado no domínio.
- **poema:** Interpretação poética permanece aberta a leituras justificadas.
- **peça teatral:** A realização cénica acrescenta elementos não contidos integralmente no texto.
- **regularidade linguística:** Recorrência precisa ser testada em dados suficientes.
- **irregularidade linguística:** Cada irregularidade exige descrição própria.
- **papel semântico:** Um participante pode receber mais de uma leitura.
- **resultado:** Resultado não é interpretação automática.
- **ausência de vírgula entre sujeito e predicado:** Elementos intercalados podem introduzir vírgulas por outra função.
- **composição sintagmática:** O grau de estabilização precisa ser verificado pelo uso.
- **bloqueio morfológico:** Cada caso precisa de evidência de uso.
- **substantivo massivo:** Pode receber leitura contável por recipiente, tipo ou porção.
- **substantivo inanimado:** Metáfora e personificação podem suspender a distinção.
- **verbo irregular:** Cada paradigma irregular deve ser materializado e testado separadamente.
- **predicado de evento:** Eventos podem ser habituais, iterados ou não delimitados.
- **oração causal:** Causa real e justificativa discursiva podem divergir.
- **seleção semântica:** Usos figurados podem ampliar a seleção.
- **evidência argumentativa:** A força depende de relevância, qualidade e ligação à tese.
- **garantia argumentativa:** Pode permanecer implícita e precisa ser reconstruída com cautela.
- **teste linguístico:** Cada teste tem limites e não deve ser universalizado.
- **generalização linguística:** Precisa declarar domínio e exceções.
- **descrição operacional:** Nem todo conceito já possui operação automática implementada.
- **confiança analítica:** A escala precisa ser calibrada por testes.
- **valência verbal:** Um mesmo verbo pode ter valências diferentes conforme a acepção.
- **argumento sintático:** A fronteira com adjunto pode ser gradual em certos casos.
- **argumento interno:** A análise depende da construção.
- **argumento externo:** Construções passivas, impessoais e não agentivas exigem análise própria.
- **estrutura argumental:** Alternâncias de construção precisam ser materializadas por verbo e sentido.
- **interlíngua:** A descrição precisa de produções reais do aprendiz.
- **regra linguística:** Toda regra permanece aberta a revisão por contraexemplo.
