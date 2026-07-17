# Nota científica — PSF-IAminy

Resumo curto do que o projeto estuda, como tenta demonstrar isso e onde reconhece não ter chegado ainda. Não substitui `PLANO_PSF_IAMINY.md` (histórico completo) nem `RELATORIO_UNICO.md` (estado corrente); é um resumo de apresentação.

## Problema estudado

Sistemas que respondem com resultado pronto — seja uma calculadora que chama uma biblioteca, seja um modelo de linguagem que produz texto plausível — normalmente não expõem a construção que leva ao resultado, nem distinguem com clareza o que sabem do que estão inferindo. Isso dificulta auditoria, ensino e confiança: um erro de fundamento pode ficar escondido atrás de um resultado correto por coincidência, e uma lacuna real pode ficar escondida atrás de uma resposta fluente.

O PSF-IAminy estuda se é possível construir conhecimento (inicialmente em Matemática e Português) exigindo, para cada conceito, uma **ponte explícita** até conhecimento anterior já construído — de modo que todo resultado venha acompanhado do caminho que o gerou, e que a ausência desse caminho seja tratada como ausência de conhecimento, não como detalhe omitido.

## Hipótese geral do método PSF

Conhecimento construído com ponte obrigatória (cada conceito depende explicitamente de conceitos mais simples já construídos, a partir de um mínimo declarado) é mais auditável e menos propenso a alegações falsas do que conhecimento aceito por autoridade externa (biblioteca, fórmula citada, resposta de terceiro) sem reconstrução própria.

Esta é a hipótese de trabalho do projeto, não um resultado provado. O projeto não afirma que o método é superior em desempenho, cobertura ou corretude a alternativas estabelecidas (SymPy, correctores ortográficos consolidados, etc.) — apenas que a exigência de ponte torna mais fácil detectar quando algo foi fingido.

## Princípios (ver `REGRA_INTEGRIDADE.md` para o texto completo)

1. Nunca fingir: nada é declarado sabido, provado, testado ou construído sem estar materializado, auditável ou marcado como hipótese.
2. Conhecimento puro nasce de construção PSF, do mínimo possível, sem antecipar por fórmula ou biblioteca externa.
3. Dependências externas só comparam, medem, validam ou otimizam — nunca são fundamento.
4. Hipótese autoral permanece hipótese até prova ou falsificação.
5. Sem ponte de dependências reais até conhecimento anterior, não é conhecimento PSF — é material, candidato, referência ou lacuna.

## Arquitetura

Ver `docs/ARQUITETURA.md` para o diagrama e a descrição de cada componente (motores de Matemática e Português, motor comum, auditoria/pureza/rastreabilidade, validação externa, interface).

## Metodologia

- Cada conceito matemático ou linguístico novo entra com: construção própria, teste automatizado, e ponte declarada até dependências já existentes.
- Verificadores automáticos (`motor/coerencia.py`, `motor/pureza.py`, `motor/rastreabilidade.py`, `verificar_integridade.py`) comparam o que os documentos afirmam contra o estado real do código — não confiam em prosa não verificada.
- Hipóteses autorais (ex.: técnica de divisão por níveis relacionada a primalidade, em `matematica/hipoteses.py`) são preservadas com autoria, exemplos e contraexemplos, mas não entram na tabela de capacidades como conhecimento implementado.
- Dependências científicas de terceiros (NumPy, SymPy, SciPy etc.) são isoladas no subprojeto `cao_de_caca/PSF-Calculadora/`, desligado do grafo de conhecimento PSF, e só consultado por decisão explícita (`motor/decisao_auxiliar.py`).

## Resultados atuais (verificáveis)

- 1106 testes automatizados passam localmente (`python3 -m pytest -q`).
- 203 documentos conceituais de Matemática auditados, todos com ponte de dependências fechada.
- 1141 conceitos puros de Português numa única linha canónica, 2545 relações de dependência, 0 lacunas internas conhecidas (124 fronteiras abertas e 179 limites operacionais declarados à parte — ver `README.md`).
- Divisão reconstruída como fração exata + expansão decimal explícita (quociente, resto, transporte por 10), incluindo divisão por zero tratada como não definida por construção, não como problema aberto nem exceção silenciosa.

## Limitações

- O domínio matemático coberto é finito e racional; não há afirmação de completude sobre os números reais (a "lei geradora de aproximação real", ETAPA 1035, é o esforço mais avançado nessa direção e continua com equivalência/ordem entre leis pendente).
- A hipótese de primalidade por divisão em níveis não foi integrada nem falsificada — está preservada, não validada.
- Houve uma primeira comparação matemática de sete casos com SymPy 1.14.0, mas não comparação sistemática ampla, comparação linguística com correctores consolidados nem avaliação por terceiros independentes do autor.
- A cobertura de linhas foi medida localmente em 63% (`docs/COBERTURA.md`); o número de testes e a cobertura ainda não demonstram, por si só, profundidade científica nem cobertura completa dos casos extremos.
- O projeto tem um único mantenedor até o momento; não houve revisão por pares externos.

## Possibilidades de falsificação

Por regra (`REGRA_INTEGRIDADE.md`, item 14), toda hipótese autoral permanece hipótese até prova ou falsificação. Concretamente:

- A hipótese de primalidade por divisão em níveis seria falsificada por um contraexemplo verificável: um número onde a técnica declare "primo"/"não primo" de forma divergente do resultado já estabelecido pela primalidade PSF existente.
- Qualquer capacidade listada como "Implementada" na tabela de `README.md` seria falsificada por um teste reproduzível que produza resultado incorreto ou contraditório com a própria justificativa apresentada pelo motor.
- A alegação central do método (ponte obrigatória reduz conhecimento fingido) seria enfraquecida se se encontrasse conhecimento marcado como "implementado" sem ponte real, ou com ponte que não resista a auditoria (`motor/rastreabilidade.py`, `motor/coerencia.py`).

## Trabalho futuro

- Aprofundar a cobertura já medida e a classificação já criada, revisando força de oráculos e duplicação semântica dos testes.
- Ampliar a comparação inicial com SymPy e criar validação linguística externa, com relatório de divergências (itens 41-42).
- Obter a primeira execução pública verde do CI; a execução `29505936596` falhou e as correções locais ainda precisam ser publicadas.
- Extensão da lei geradora de aproximação real até completude dos racionais/reais, e revisão de geometria plana/espacial como bloco pleno (ver `RELATORIO_UNICO.md`).
