"""Expansão interna do léxico português do PSF-IAminy.

Não é um dicionário externo importado. É uma semente grande, auditável e
extensível, escrita em código simples para o motor reconhecer pedidos naturais,
termos de estudo, linguagem técnica, matemática e conversa humana.
"""
from __future__ import annotations

from .tipos import ClasseGramatical, EntradaLexical, Genero, Numero, Pessoa
from .conhecimento_puro import ALIASES_CONCEITOS_PORTUGUES, CONCEITOS_PORTUGUES_PURO


def _plural_substantivo(lema: str) -> str:
    """Achado real ao adicionar candidatos do corpus ("intenção",
    "construção", "validação" já existentes geravam "intençãos" etc., forma
    que não existe em português): substantivo terminado em "-ção" pluraliza
    em "-ções" (nunca "+s") -- sub-padrão de "-ão" quase sem exceção. O
    restante da classe "-ão" (mão -> mãos, pão -> pães, irmão -> irmãos) é
    genuinamente irregular e fica de fora por ora, não coberto às cegas.

    Segundo achado real, mesmo padrão de erro ("item" já existente gerava
    "items"): substantivo terminado em "-m" pluraliza trocando "m" por
    "ns" (item -> itens, som -> sons, linguagem -> linguagens, contagem ->
    contagens), nunca "+s"."""
    if lema.endswith("ção"):
        return lema[: -len("ção")] + "ções"
    if lema.endswith("m"):
        return lema[:-1] + "ns"
    if lema.endswith(("r", "z")):
        return lema + "es"
    return lema + "s"


def _forma_nome(lema: str, genero: Genero, definicao: str) -> list[EntradaLexical]:
    entradas = [
        EntradaLexical(lema, lema, ClasseGramatical.SUBSTANTIVO, (definicao,), genero, Numero.SINGULAR)
    ]
    if not lema.endswith("s"):
        plural = _plural_substantivo(lema)
        entradas.append(
            EntradaLexical(lema, plural, ClasseGramatical.SUBSTANTIVO, (definicao,), genero, Numero.PLURAL)
        )
    return entradas


def _forma_adj(lema: str, definicao: str) -> list[EntradaLexical]:
    """Regra achada quebrada ao adicionar candidatos reais do corpus ("real",
    "natural" já existentes geravam plural "reals"/"naturals", formas que não
    existem em português): adjetivo terminado em "-al" pluraliza em "-ais"
    (real -> reais, natural -> naturais, nominal -> nominais), nunca "+s".
    As demais terminações em "-el"/"-ol"/"-ul" seguem a mesma família (papel
    -> papéis, farol -> faróis) mas ficam de fora por ora -- regra mais
    irregular (acento muda conforme a tonicidade), não coberta ainda."""
    formas = {lema}
    if lema.endswith("o"):
        formas.update({lema[:-1] + "a", lema[:-1] + "os", lema[:-1] + "as"})
    elif lema.endswith("al"):
        formas.add(lema[:-1] + "is")
    elif not lema.endswith("s"):
        formas.add(lema + "s")
    return [EntradaLexical(lema, forma, ClasseGramatical.ADJETIVO, (definicao,)) for forma in sorted(formas)]


def _corrigir_ortografia_raiz(formas: dict, raiz: str, infinitivo: str) -> dict:
    """Achado real ao adicionar "nascer" como candidato do corpus: verbo
    terminado em "-cer"/"-cir" gerava "nasco"/"nasca" em vez de
    "nasço"/"nasça" -- português preserva o som de "c" (=/s/) trocando por
    "ç" sempre que a próxima vogal é "a" ou "o" (senão "c" soaria /k/).
    Mesma disciplina já usada para os plurais em "-al"/"-ção"."""
    corrigidas = {}
    for forma, dado in formas.items():
        proxima = forma[len(raiz):len(raiz) + 1] if forma.startswith(raiz) else ""
        if infinitivo.endswith(("cer", "cir")) and proxima in ("a", "o"):
            forma = raiz[:-1] + "ç" + forma[len(raiz):]
        elif infinitivo.endswith("car") and proxima == "e":
            forma = raiz[:-1] + "qu" + forma[len(raiz):]
        elif infinitivo.endswith("gar") and proxima == "e":
            forma = raiz[:-1] + "gu" + forma[len(raiz):]
        elif infinitivo.endswith("çar") and proxima == "e":
            forma = raiz[:-1] + "c" + forma[len(raiz):]
        elif infinitivo.endswith(("ger", "gir")) and proxima in ("a", "o"):
            forma = raiz[:-1] + "j" + forma[len(raiz):]
        elif infinitivo.endswith("guir") and proxima in ("a", "o"):
            forma = raiz[:-1] + forma[len(raiz):]
        corrigidas[forma] = dado
    return corrigidas


def _verbo(infinitivo: str, definicao: str) -> list[EntradaLexical]:
    """Gera as formas do presente, pretérito perfeito, pretérito
    imperfeito, futuro do presente, presente do subjuntivo, futuro do
    pretérito (condicional) e imperativo afirmativo, cada uma já
    etiquetada com sua própria pessoa/número/tempo -- validação em
    pequena escala da "geração real de paradigma" (Fase 2 do plano de
    corretor), antes de crescer para um motor de geração morfológica
    completo (Fase 3). Só verbos regulares -- os 11 irregulares comuns
    continuam vindo do JSON (`lexico_base.json`), não desta geração.

    Achado real ao construir o imperativo afirmativo: ele não introduz
    NENHUMA string nova. "tu" é o presente do indicativo 2ª singular sem
    o "s" final (mesma string que o presente indicativo 3ª singular já
    usa -- "fala" serve às duas); "você"/"nós"/"vocês" repetem
    exatamente o presente do subjuntivo. Por isso as entradas de
    imperativo abaixo não entram no dicionário `formas` (que é indexado
    por string e sobrescreveria a leitura já existente) -- entram como
    leituras adicionais para formas que já existem, aproveitando que
    `Dicionario` já guarda múltiplas leituras por forma (o mesmo
    mecanismo que já resolve "foi" entre "ir"/"ser"). Sem "eu" (não se
    comanda a si mesmo) nem "vós" (arcaico, já fora de escopo em todo o
    resto deste módulo). Imperativo negativo fica de fora: usa sempre o
    subjuntivo em TODAS as pessoas (incluindo "tu"), regra diferente do
    afirmativo -- próximo corte, não este."""
    raiz = infinitivo[:-2]
    formas: dict[str, tuple[Pessoa | None, Numero | None, str | None]] = {
        infinitivo: (None, None, None)
    }
    if infinitivo.endswith("ar"):
        formas.update(
            {
                raiz + "o": (Pessoa.PRIMEIRA, Numero.SINGULAR, "presente"),
                raiz + "as": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente"),
                raiz + "a": (Pessoa.TERCEIRA, Numero.SINGULAR, "presente"),
                raiz + "amos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente"),
                raiz + "am": (Pessoa.TERCEIRA, Numero.PLURAL, "presente"),
                raiz + "ei": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "ou": (Pessoa.TERCEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "ava": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "avas": (Pessoa.SEGUNDA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "ávamos": (Pessoa.PRIMEIRA, Numero.PLURAL, "pretérito imperfeito"),
                raiz + "avam": (Pessoa.TERCEIRA, Numero.PLURAL, "pretérito imperfeito"),
                # Subjuntivo presente troca a vogal temática para "e" nos
                # -ar. 1ª e 3ª singular são a mesma forma na língua real
                # ("que eu fale" / "que ele fale") -- pessoa=None em vez
                # de fingir uma pessoa única, mesmo critério já usado
                # para "quis"/"soube"/"disse" no pretérito dos irregulares.
                raiz + "e": (None, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "es": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "emos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente do subjuntivo"),
                raiz + "em": (Pessoa.TERCEIRA, Numero.PLURAL, "presente do subjuntivo"),
            }
        )
    elif infinitivo.endswith("er"):
        formas.update(
            {
                raiz + "o": (Pessoa.PRIMEIRA, Numero.SINGULAR, "presente"),
                raiz + "es": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente"),
                raiz + "e": (Pessoa.TERCEIRA, Numero.SINGULAR, "presente"),
                raiz + "emos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente"),
                raiz + "em": (Pessoa.TERCEIRA, Numero.PLURAL, "presente"),
                raiz + "i": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "eu": (Pessoa.TERCEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "ia": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "ias": (Pessoa.SEGUNDA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "íamos": (Pessoa.PRIMEIRA, Numero.PLURAL, "pretérito imperfeito"),
                raiz + "iam": (Pessoa.TERCEIRA, Numero.PLURAL, "pretérito imperfeito"),
                # Subjuntivo presente troca a vogal temática para "a" nos
                # -er/-ir (mesma vogal para os dois). 1ª/3ª singular
                # ambíguas -- mesmo critério do bloco -ar acima.
                raiz + "a": (None, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "as": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "amos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente do subjuntivo"),
                raiz + "am": (Pessoa.TERCEIRA, Numero.PLURAL, "presente do subjuntivo"),
            }
        )
    elif infinitivo.endswith("ir"):
        formas.update(
            {
                raiz + "o": (Pessoa.PRIMEIRA, Numero.SINGULAR, "presente"),
                raiz + "es": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente"),
                raiz + "e": (Pessoa.TERCEIRA, Numero.SINGULAR, "presente"),
                raiz + "imos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente"),
                raiz + "em": (Pessoa.TERCEIRA, Numero.PLURAL, "presente"),
                raiz + "i": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "iu": (Pessoa.TERCEIRA, Numero.SINGULAR, "pretérito perfeito"),
                raiz + "ia": (Pessoa.PRIMEIRA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "ias": (Pessoa.SEGUNDA, Numero.SINGULAR, "pretérito imperfeito"),
                raiz + "íamos": (Pessoa.PRIMEIRA, Numero.PLURAL, "pretérito imperfeito"),
                raiz + "iam": (Pessoa.TERCEIRA, Numero.PLURAL, "pretérito imperfeito"),
                raiz + "a": (None, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "as": (Pessoa.SEGUNDA, Numero.SINGULAR, "presente do subjuntivo"),
                raiz + "amos": (Pessoa.PRIMEIRA, Numero.PLURAL, "presente do subjuntivo"),
                raiz + "am": (Pessoa.TERCEIRA, Numero.PLURAL, "presente do subjuntivo"),
            }
        )
    formas = _corrigir_ortografia_raiz(formas, raiz, infinitivo)
    # Imperativo afirmativo: "tu" tira o "s" final do presente indicativo
    # 2ª singular; "você"/"nós"/"vocês" repetem o presente do subjuntivo
    # (mesma pessoa morfológica) -- ver achado completo no docstring.
    if infinitivo.endswith("ar"):
        imperativo = {
            raiz + "a": (Pessoa.SEGUNDA, Numero.SINGULAR),
            raiz + "e": (None, Numero.SINGULAR),
            raiz + "emos": (Pessoa.PRIMEIRA, Numero.PLURAL),
            raiz + "em": (Pessoa.TERCEIRA, Numero.PLURAL),
        }
    else:
        # -er e -ir compartilham a mesma derivação de imperativo, assim
        # como já compartilham a mesma vogal temática do subjuntivo.
        imperativo = {
            raiz + "e": (Pessoa.SEGUNDA, Numero.SINGULAR),
            raiz + "a": (None, Numero.SINGULAR),
            raiz + "amos": (Pessoa.PRIMEIRA, Numero.PLURAL),
            raiz + "am": (Pessoa.TERCEIRA, Numero.PLURAL),
        }
    imperativo = _corrigir_ortografia_raiz(imperativo, raiz, infinitivo)
    entradas_imperativo = [
        EntradaLexical(
            infinitivo, forma, ClasseGramatical.VERBO, (definicao,),
            pessoa=pessoa, numero=numero,
            atributos={"tempo": "imperativo afirmativo"},
        )
        for forma, (pessoa, numero) in sorted(imperativo.items())
    ]
    # Futuro do presente e futuro do pretérito (condicional): infinitivo
    # inteiro + sufixo, igual nas três conjugações -- não depende da
    # raiz, ao contrário dos tempos acima. 1ª/3ª singular do condicional
    # também são a mesma forma ("eu falaria" / "ele falaria").
    formas.update(
        {
            infinitivo + "ei": (Pessoa.PRIMEIRA, Numero.SINGULAR, "futuro do presente"),
            infinitivo + "ás": (Pessoa.SEGUNDA, Numero.SINGULAR, "futuro do presente"),
            infinitivo + "á": (Pessoa.TERCEIRA, Numero.SINGULAR, "futuro do presente"),
            infinitivo + "emos": (Pessoa.PRIMEIRA, Numero.PLURAL, "futuro do presente"),
            infinitivo + "ão": (Pessoa.TERCEIRA, Numero.PLURAL, "futuro do presente"),
            infinitivo + "ia": (None, Numero.SINGULAR, "futuro do pretérito"),
            infinitivo + "ias": (Pessoa.SEGUNDA, Numero.SINGULAR, "futuro do pretérito"),
            infinitivo + "íamos": (Pessoa.PRIMEIRA, Numero.PLURAL, "futuro do pretérito"),
            infinitivo + "iam": (Pessoa.TERCEIRA, Numero.PLURAL, "futuro do pretérito"),
        }
    )
    return [
        EntradaLexical(
            infinitivo, forma, ClasseGramatical.VERBO, (definicao,),
            pessoa=pessoa, numero=numero,
            atributos={"tempo": tempo} if tempo else {},
        )
        for forma, (pessoa, numero, tempo) in sorted(formas.items())
    ] + entradas_imperativo


_PALAVRAS_FUNCIONAIS: tuple[EntradaLexical, ...] = (
    # Achado real ao investigar os candidatos mais frequentes do corpus
    # amplo (Fase 3/4 do plano de léxico): o léxico nunca teve cobertura de
    # classe fechada (pronome/preposição/conjunção/determinante) -- só
    # vocabulário técnico/de conteúdo. Este bloco começa a fechar essa
    # lacuna real, palavra por palavra, curada à mão -- não é lista
    # exaustiva de toda a gramática fechada do português, é o núcleo mais
    # frequente na prosa que o próprio projeto já escreveu.
    #
    # Palavra polissêmica (classe muda com o uso) ganha mais de uma
    # entrada com a MESMA forma -- nunca uma classe única forçada. Ex.:
    # "que" é conjunção integrante ("sei que vens") e pronome relativo
    # ("o livro que li"); "mesmo" é adjetivo ("o mesmo carro"), pronome
    # intensificador ("eu mesmo") e advérbio ("mesmo assim").
    #
    # Preposições (invariáveis) -- "até"/"com"/"desde"/"para"/"sem"/"sobre"
    # já existiam em lexico_base.json (lemas próprios); não duplicados aqui.
    EntradaLexical("a", "a", ClasseGramatical.PREPOSICAO, ("Introduz destino, distância, modo ou complemento; distinto do artigo/pronome \"a\".",)),
    EntradaLexical("contra", "contra", ClasseGramatical.PREPOSICAO, ("Marca oposição ou direção contrária.",)),
    EntradaLexical("entre", "entre", ClasseGramatical.PREPOSICAO, ("Marca posição intermédia entre dois ou mais termos.",)),
    EntradaLexical("perante", "perante", ClasseGramatical.PREPOSICAO, ("Marca presença de alguém diante de outro termo.",)),
    EntradaLexical("por", "por", ClasseGramatical.PREPOSICAO, ("Marca causa, meio, troca ou trajeto.",)),
    EntradaLexical("sob", "sob", ClasseGramatical.PREPOSICAO, ("Marca posição abaixo de algo.",)),
    # Conjunções -- "e"/"mas"/"portanto"/"porque"/"se"/"quando"/"então" já
    # existiam em lexico_base.json; não duplicados aqui.
    EntradaLexical("ou", "ou", ClasseGramatical.CONJUNCAO, ("Liga termos apresentando alternativa (alternativa).",)),
    EntradaLexical("pois", "pois", ClasseGramatical.CONJUNCAO, ("Liga orações indicando causa ou conclusão.",)),
    EntradaLexical("porém", "porém", ClasseGramatical.CONJUNCAO, ("Liga orações opondo uma ideia à anterior (adversativa).",)),
    EntradaLexical("contudo", "contudo", ClasseGramatical.CONJUNCAO, ("Liga orações opondo uma ideia à anterior (adversativa).",)),
    EntradaLexical("entretanto", "entretanto", ClasseGramatical.CONJUNCAO, ("Liga orações opondo uma ideia à anterior (adversativa).",)),
    EntradaLexical("logo", "logo", ClasseGramatical.CONJUNCAO, ("Liga orações indicando consequência (conclusiva).",)),
    EntradaLexical("caso", "caso", ClasseGramatical.CONJUNCAO, ("Liga orações indicando condição.",)),
    EntradaLexical("embora", "embora", ClasseGramatical.CONJUNCAO, ("Liga orações indicando concessão.",)),
    EntradaLexical("que", "que", ClasseGramatical.CONJUNCAO, ("Liga oração subordinada ao verbo da principal (\"sei que vens\").",)),
    EntradaLexical("que", "que", ClasseGramatical.PRONOME, ("Retoma um termo anterior dentro da oração seguinte (\"o livro que li\").",)),
    EntradaLexical("quem", "quem", ClasseGramatical.PRONOME, ("Retoma pessoa já referida, ou introduz pergunta sobre pessoa.",)),
    EntradaLexical("qual", "qual", ClasseGramatical.PRONOME, ("Retoma termo já referido, ou introduz pergunta de escolha.",), numero=Numero.SINGULAR),
    EntradaLexical("qual", "quais", ClasseGramatical.PRONOME, ("Retoma termo já referido, ou introduz pergunta de escolha.",), numero=Numero.PLURAL),
    EntradaLexical("quanto", "quanto", ClasseGramatical.PRONOME, ("Introduz pergunta ou referência de quantidade.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("quanto", "quanta", ClasseGramatical.PRONOME, ("Introduz pergunta ou referência de quantidade.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("quanto", "quantos", ClasseGramatical.PRONOME, ("Introduz pergunta ou referência de quantidade.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("quanto", "quantas", ClasseGramatical.PRONOME, ("Introduz pergunta ou referência de quantidade.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    # Pronomes pessoais retos -- "eu"/"tu"/"ele"/"ela"/"eles"/"elas"/"nós"
    # já existiam em lexico_base.json; só "vós" faltava.
    EntradaLexical("vós", "vós", ClasseGramatical.PRONOME, ("2ª pessoa do plural, com quem se fala.",), numero=Numero.PLURAL, pessoa=Pessoa.SEGUNDA),
    # Pronomes possessivos (só forma de base masculino/feminino singular) --
    # "meu"/"minha" já existiam em lexico_base.json.
    EntradaLexical("teu", "teu", ClasseGramatical.PRONOME, ("Indica posse pertencente à 2ª pessoa do singular.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("tua", "tua", ClasseGramatical.PRONOME, ("Indica posse pertencente à 2ª pessoa do singular.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("seu", "seu", ClasseGramatical.PRONOME, ("Indica posse pertencente à 3ª pessoa (ou a \"você\").",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("sua", "sua", ClasseGramatical.PRONOME, ("Indica posse pertencente à 3ª pessoa (ou a \"você\").",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("nosso", "nosso", ClasseGramatical.PRONOME, ("Indica posse pertencente à 1ª pessoa do plural.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("nossa", "nossa", ClasseGramatical.PRONOME, ("Indica posse pertencente à 1ª pessoa do plural.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    # Plurais dos possessivos (achado real: o lote anterior só tinha o
    # singular -- "teus"/"seus"/"nossas" etc. ficavam de fora do léxico).
    EntradaLexical("teu", "teus", ClasseGramatical.PRONOME, ("Indica posse pertencente à 2ª pessoa do singular.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("teu", "tuas", ClasseGramatical.PRONOME, ("Indica posse pertencente à 2ª pessoa do singular.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("seu", "seus", ClasseGramatical.PRONOME, ("Indica posse pertencente à 3ª pessoa (ou a \"você\").",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("seu", "suas", ClasseGramatical.PRONOME, ("Indica posse pertencente à 3ª pessoa (ou a \"você\").",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("nosso", "nossos", ClasseGramatical.PRONOME, ("Indica posse pertencente à 1ª pessoa do plural.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("nosso", "nossas", ClasseGramatical.PRONOME, ("Indica posse pertencente à 1ª pessoa do plural.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    # Pronomes demonstrativos
    EntradaLexical("este", "este", ClasseGramatical.PRONOME, ("Indica algo próximo de quem fala.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("esta", "esta", ClasseGramatical.PRONOME, ("Indica algo próximo de quem fala.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("este", "estes", ClasseGramatical.PRONOME, ("Indica algo próximo de quem fala.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("este", "estas", ClasseGramatical.PRONOME, ("Indica algo próximo de quem fala.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("esse", "esse", ClasseGramatical.PRONOME, ("Indica algo próximo de com quem se fala.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("essa", "essa", ClasseGramatical.PRONOME, ("Indica algo próximo de com quem se fala.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("esse", "esses", ClasseGramatical.PRONOME, ("Indica algo próximo de com quem se fala.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("esse", "essas", ClasseGramatical.PRONOME, ("Indica algo próximo de com quem se fala.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("aquele", "aquele", ClasseGramatical.PRONOME, ("Indica algo distante de quem fala e de com quem se fala.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("aquela", "aquela", ClasseGramatical.PRONOME, ("Indica algo distante de quem fala e de com quem se fala.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("aquele", "aqueles", ClasseGramatical.PRONOME, ("Indica algo distante de quem fala e de com quem se fala.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("aquele", "aquelas", ClasseGramatical.PRONOME, ("Indica algo distante de quem fala e de com quem se fala.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    # "aquilo" já existia em lexico_base.json.
    # Pronomes/determinantes indefinidos
    EntradaLexical("algum", "algum", ClasseGramatical.PRONOME, ("Indica quantidade ou identidade não especificada, de forma afirmativa.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("algum", "alguma", ClasseGramatical.PRONOME, ("Indica quantidade ou identidade não especificada, de forma afirmativa.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("algum", "alguns", ClasseGramatical.PRONOME, ("Indica quantidade ou identidade não especificada, de forma afirmativa.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("algum", "algumas", ClasseGramatical.PRONOME, ("Indica quantidade ou identidade não especificada, de forma afirmativa.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("nenhum", "nenhum", ClasseGramatical.PRONOME, ("Indica ausência de quantidade ou identidade.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("nenhum", "nenhuma", ClasseGramatical.PRONOME, ("Indica ausência de quantidade ou identidade.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("todo", "todo", ClasseGramatical.PRONOME, ("Indica totalidade ou generalidade (\"todo dia\"); também adjetivo (\"o dia todo\").",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("todo", "toda", ClasseGramatical.PRONOME, ("Indica totalidade ou generalidade.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("todo", "todos", ClasseGramatical.PRONOME, ("Indica totalidade ou generalidade, incluindo todos os elementos de um grupo.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("todo", "todas", ClasseGramatical.PRONOME, ("Indica totalidade ou generalidade, incluindo todos os elementos de um grupo.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("cada", "cada", ClasseGramatical.PRONOME, ("Indica cada elemento tratado individualmente dentro de um conjunto.",)),
    EntradaLexical("outro", "outro", ClasseGramatical.PRONOME, ("Indica identidade distinta da já referida.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("outro", "outra", ClasseGramatical.PRONOME, ("Indica identidade distinta da já referida.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("outro", "outros", ClasseGramatical.PRONOME, ("Indica identidade distinta da já referida.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("outro", "outras", ClasseGramatical.PRONOME, ("Indica identidade distinta da já referida.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("mesmo", "mesmo", ClasseGramatical.ADJETIVO, ("Indica identidade com algo já referido (\"o mesmo carro\").",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("mesmo", "mesma", ClasseGramatical.ADJETIVO, ("Indica identidade com algo já referido.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("mesmo", "mesmos", ClasseGramatical.ADJETIVO, ("Indica identidade com algo já referido.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("mesmo", "mesmas", ClasseGramatical.ADJETIVO, ("Indica identidade com algo já referido.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("mesmo", "mesmo", ClasseGramatical.PRONOME, ("Reforça a identidade do sujeito (\"eu mesmo fiz\").",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("mesmo", "mesma", ClasseGramatical.PRONOME, ("Reforça a identidade do sujeito.",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("mesmo", "mesmos", ClasseGramatical.PRONOME, ("Reforça a identidade do sujeito.",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("mesmo", "mesmas", ClasseGramatical.PRONOME, ("Reforça a identidade do sujeito.",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("mesmo", "mesmo", ClasseGramatical.ADVERBIO, ("Reforça uma afirmação (\"mesmo assim\").",)),
    EntradaLexical("tudo", "tudo", ClasseGramatical.PRONOME, ("Indica a totalidade das coisas, sem nome próprio.",)),
    EntradaLexical("nada", "nada", ClasseGramatical.PRONOME, ("Indica ausência total de coisa.",)),
    EntradaLexical("alguém", "alguém", ClasseGramatical.PRONOME, ("Indica uma pessoa não identificada.",)),
    EntradaLexical("ninguém", "ninguém", ClasseGramatical.PRONOME, ("Indica ausência de qualquer pessoa.",)),
    # Advérbios de uso muito frequente (função gramatical, não conteúdo) --
    # "muito"/"pouco"/"sempre"/"nunca"/"já"/"ainda"/"também"/"não"/"agora"/
    # "bem"/"mal"/"aqui"/"ali" já existiam em lexico_base.json.
    EntradaLexical("mais", "mais", ClasseGramatical.ADVERBIO, ("Marca grau superior numa comparação.",)),
    EntradaLexical("menos", "menos", ClasseGramatical.ADVERBIO, ("Marca grau inferior numa comparação.",)),
    EntradaLexical("só", "só", ClasseGramatical.ADVERBIO, ("Marca exclusividade (\"só isso\").",)),
    EntradaLexical("apenas", "apenas", ClasseGramatical.ADVERBIO, ("Marca exclusividade ou restrição.",)),
    EntradaLexical("antes", "antes", ClasseGramatical.ADVERBIO, ("Marca momento anterior de referência.",)),
    EntradaLexical("depois", "depois", ClasseGramatical.ADVERBIO, ("Marca momento posterior de referência.",)),
    EntradaLexical("onde", "onde", ClasseGramatical.PRONOME, ("Retoma ou pergunta sobre lugar.",)),
    EntradaLexical("como", "como", ClasseGramatical.CONJUNCAO, ("Introduz comparação (\"forte como um touro\").",)),
    EntradaLexical("como", "como", ClasseGramatical.ADVERBIO, ("Introduz pergunta sobre modo (\"como você está\").",)),
    EntradaLexical("dentro", "dentro", ClasseGramatical.ADVERBIO, ("Marca posição interna em relação a um limite.",)),
    EntradaLexical("nem", "nem", ClasseGramatical.CONJUNCAO, ("Liga termos negando ambos (\"nem um nem outro\").",)),
    EntradaLexical("qualquer", "qualquer", ClasseGramatical.PRONOME, ("Indica identidade não específica entre várias possibilidades.",)),
    EntradaLexical("fora", "fora", ClasseGramatical.ADVERBIO, ("Marca posição externa em relação a um limite.",)),
    EntradaLexical("segundo", "segundo", ClasseGramatical.NUMERAL, ("Indica a posição imediatamente após a primeira numa ordem.",), genero=Genero.MASCULINO),
    EntradaLexical("segundo", "segundo", ClasseGramatical.PREPOSICAO, ("Indica a fonte ou o critério de uma afirmação (\"segundo o autor\").",)),
    EntradaLexical("conforme", "conforme", ClasseGramatical.PREPOSICAO, ("Indica critério ou fonte de acordo (\"conforme o combinado\").",)),
    EntradaLexical("conforme", "conforme", ClasseGramatical.CONJUNCAO, ("Introduz oração de acordo com o que se afirma (\"faça conforme eu disser\").",)),
    # Contrações (preposição + artigo/pronome, fundidas na escrita) --
    # "dos"/"pela"/"nesta"/"pelo"/"numa" estavam entre os candidatos mais
    # frequentes do corpus amplo; completadas aqui com as formas irmãs
    # óbvias da mesma família, não uma lista inventada à parte. "do"/"da"/
    # "no"/"na" (singular) já existiam em lexico_base.json como formas dos
    # lemas "de"/"em" -- só os plurais "dos"/"das"/"nos"/"nas" faltavam.
    EntradaLexical("dos", "dos", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"os\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("das", "das", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"as\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("nos", "nos", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"os\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("nas", "nas", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"as\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("ao", "ao", ClasseGramatical.PREPOSICAO, ("Contração de \"a\" + \"o\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("à", "à", ClasseGramatical.PREPOSICAO, ("Contração de \"a\" + \"a\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("aos", "aos", ClasseGramatical.PREPOSICAO, ("Contração de \"a\" + \"os\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("às", "às", ClasseGramatical.PREPOSICAO, ("Contração de \"a\" + \"as\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("pelo", "pelo", ClasseGramatical.PREPOSICAO, ("Contração de \"por\" + \"o\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("pela", "pela", ClasseGramatical.PREPOSICAO, ("Contração de \"por\" + \"a\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("pelos", "pelos", ClasseGramatical.PREPOSICAO, ("Contração de \"por\" + \"os\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("pelas", "pelas", ClasseGramatical.PREPOSICAO, ("Contração de \"por\" + \"as\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("num", "num", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"um\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("numa", "numa", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"uma\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("nuns", "nuns", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"uns\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("numas", "numas", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"umas\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("neste", "neste", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"este\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("nesta", "nesta", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"esta\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("nestes", "nestes", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"estes\".",), genero=Genero.MASCULINO, numero=Numero.PLURAL),
    EntradaLexical("nestas", "nestas", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"estas\".",), genero=Genero.FEMININO, numero=Numero.PLURAL),
    EntradaLexical("nesse", "nesse", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"esse\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("nessa", "nessa", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"essa\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("desse", "desse", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"esse\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("dessa", "dessa", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"essa\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("deste", "deste", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"este\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("desta", "desta", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"esta\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("daquele", "daquele", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"aquele\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("daquela", "daquela", ClasseGramatical.PREPOSICAO, ("Contração de \"de\" + \"aquela\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
    EntradaLexical("naquele", "naquele", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"aquele\".",), genero=Genero.MASCULINO, numero=Numero.SINGULAR),
    EntradaLexical("naquela", "naquela", ClasseGramatical.PREPOSICAO, ("Contração de \"em\" + \"aquela\".",), genero=Genero.FEMININO, numero=Numero.SINGULAR),
)


_NOMES: tuple[tuple[str, Genero, str], ...] = (
    ("motor", Genero.MASCULINO, "Parte do sistema que executa uma responsabilidade específica."),
    ("conversa", Genero.FEMININO, "Troca de mensagens com continuidade e contexto."),
    ("pedido", Genero.MASCULINO, "Aquilo que uma pessoa solicita em linguagem natural."),
    ("intenção", Genero.FEMININO, "Sentido prático por trás de uma frase ou comando."),
    ("contexto", Genero.MASCULINO, "Informação anterior que ajuda a entender o próximo pedido."),
    ("aula", Genero.FEMININO, "Explicação organizada para ensinar um conceito a uma pessoa."),
    ("professor", Genero.MASCULINO, "Pessoa ou papel que transforma conhecimento em aprendizagem."),
    ("aluno", Genero.MASCULINO, "Pessoa que aprende, pratica e avança por etapas."),
    ("exemplo", Genero.MASCULINO, "Caso concreto usado para tornar uma ideia visível."),
    ("exercício", Genero.MASCULINO, "Tarefa curta usada para testar e fixar aprendizagem."),
    ("resumo", Genero.MASCULINO, "Versão curta que conserva a ideia principal."),
    ("fronteira", Genero.FEMININO, "Limite atual entre o que já foi construído e o que ainda precisa ser construído."),
    ("conceito", Genero.MASCULINO, "Unidade de entendimento que pode ser definida, usada e testada."),
    ("conhecimento", Genero.MASCULINO, "Conjunto de conceitos, relações e métodos já construídos."),
    ("construção", Genero.FEMININO, "Processo de formar uma ideia a partir de partes anteriores."),
    ("validação", Genero.FEMININO, "Teste usado para confirmar se uma construção funciona."),
    ("prova", Genero.FEMININO, "Caminho controlado que mostra por que uma afirmação se sustenta."),
    ("fórmula", Genero.FEMININO, "Expressão simbólica que só pode entrar como resultado ou validação, não como fundamento pronto."),
    ("matemática", Genero.FEMININO, "Construção de objetos, relações, operações, estruturas e provas."),
    ("infinito", Genero.MASCULINO, "Abertura sem último nível; no PSF é tratado por regra de continuidade, não por lista pronta."),
    ("número", Genero.MASCULINO, "Marca de quantidade ou posição construída por distinção e repetição."),
    ("operação", Genero.FEMININO, "Transformação controlada aplicada a objetos."),
    ("relação", Genero.FEMININO, "Ligação reconhecida entre objetos ou estados."),
    ("estrutura", Genero.FEMININO, "Organização estável de objetos, relações e operações."),
    ("modelo", Genero.MASCULINO, "Representação usada para testar uma teoria ou construção."),
    ("teoria", Genero.FEMININO, "Sistema organizado de conceitos, regras e consequências."),
    ("algoritmo", Genero.MASCULINO, "Sequência finita de passos para resolver uma tarefa."),
    ("função", Genero.FEMININO, "Relação que associa cada entrada permitida a uma saída determinada."),
    ("sequência", Genero.FEMININO, "Objetos postos em ordem por uma regra."),
    ("conjunto", Genero.MASCULINO, "Coleção de objetos tratados como uma unidade."),
    ("grafo", Genero.MASCULINO, "Estrutura formada por vértices e ligações."),
    ("matriz", Genero.FEMININO, "Arranjo retangular de valores usado para representar transformações ou dados."),
    ("vetor", Genero.MASCULINO, "Objeto com componentes ordenadas ou direção estrutural."),
    ("português", Genero.MASCULINO, "Língua usada pelo motor para conversar, explicar e ensinar."),
    ("dicionário", Genero.MASCULINO, "Índice de palavras, formas, classes gramaticais e definições."),
    ("palavra", Genero.FEMININO, "Forma linguística com som, grafia e significado possível."),
    ("frase", Genero.FEMININO, "Unidade de texto com sentido comunicável."),
    ("texto", Genero.MASCULINO, "Sequência organizada de frases com intenção."),
    ("gramática", Genero.FEMININO, "Regras de organização das palavras e frases."),
    ("vocabulário", Genero.MASCULINO, "Conjunto de palavras reconhecidas por uma pessoa ou sistema."),
    ("sinónimo", Genero.MASCULINO, "Palavra de sentido próximo de outra."),
    ("antónimo", Genero.MASCULINO, "Palavra de sentido oposto a outra."),
    ("fluidez", Genero.FEMININO, "Qualidade de uma conversa que mantém continuidade, naturalidade e ritmo."),
    ("clareza", Genero.FEMININO, "Qualidade de uma explicação fácil de seguir."),
    ("dificuldade", Genero.FEMININO, "Grau de esforço necessário para entender ou resolver algo."),
    ("futuro", Genero.MASCULINO, "Parte ainda não construída do trilho de conhecimento."),
    ("lacuna", Genero.FEMININO, "Ponto que falta construir, testar ou documentar."),
    ("hipótese", Genero.FEMININO, "Ideia provisória que precisa ser testada."),
    ("observação", Genero.FEMININO, "Dado ou facto percebido antes da conclusão."),
    ("regra", Genero.FEMININO, "Condição estável que orienta uma construção ou decisão."),
    ("etapa", Genero.FEMININO, "Nível numerado de construção do conhecimento PSF."),
    ("nível", Genero.MASCULINO, "Posição de avanço dentro de uma sequência de aprendizagem."),

    ("diferença", Genero.FEMININO, "Separação mínima que permite reconhecer que uma ocorrência não é outra."),
    ("som", Genero.MASCULINO, "Ocorrência audível ou abstrata que pode iniciar a fala antes da palavra."),
    ("pausa", Genero.FEMININO, "Corte ou intervalo que separa sons, palavras, frases e intenções."),
    ("marca", Genero.FEMININO, "Sinal visível que conserva uma diferença na escrita."),
    ("grafema", Genero.MASCULINO, "Unidade escrita: letra, acento, algarismo, espaço ou pontuação."),
    ("letra", Genero.FEMININO, "Grafema usado para representar som ou parte da forma escrita de uma palavra."),
    ("vogal", Genero.FEMININO, "Unidade sonora/gráfica que pode sustentar núcleo de sílaba."),
    ("consoante", Genero.FEMININO, "Unidade sonora/gráfica que se articula com vogal ou combinação."),
    ("sílaba", Genero.FEMININO, "Agrupamento pronunciável de sons ou grafemas dentro de uma palavra."),
    ("dígrafo", Genero.MASCULINO, "Combinação de duas letras tratada como uma unidade funcional."),
    ("acento", Genero.MASCULINO, "Marca gráfica que altera ou orienta a leitura de uma letra."),
    ("cedilha", Genero.FEMININO, "Marca gráfica usada sob a letra c para indicar som específico em português."),
    ("lema", Genero.MASCULINO, "Forma-base usada para reunir variantes de uma palavra."),
    ("sentido", Genero.MASCULINO, "Função interpretável que nasce da relação entre palavra, contexto e construção."),
    ("oração", Genero.FEMININO, "Construção frasal organizada em torno de verbo ou estrutura equivalente."),
    ("sujeito", Genero.MASCULINO, "Parte que ocupa o ponto de referência daquilo que se declara."),
    ("predicado", Genero.MASCULINO, "Parte que declara algo sobre o sujeito ou organiza o acontecimento verbal."),
    ("pontuação", Genero.FEMININO, "Conjunto de marcas que regula pausa, limite e intenção na escrita."),
    ("espaço", Genero.MASCULINO, "Marca vazia que separa palavras e blocos escritos."),
    ("encontro vocálico", Genero.MASCULINO, "Sequência de vogais observada dentro de uma palavra."),
    ("encontro consonantal", Genero.MASCULINO, "Sequência de consoantes observada dentro de uma palavra."),
    ("tonicidade", Genero.FEMININO, "Diferença de força entre sílabas de uma palavra."),
    ("sílaba tônica", Genero.FEMININO, "Sílaba que recebe maior força relativa dentro da palavra."),
    ("morfema", Genero.MASCULINO, "Parte mínima de palavra com função ou sentido."),
    ("radical", Genero.MASCULINO, "Parte que conserva o núcleo de família de uma palavra."),
    ("prefixo", Genero.MASCULINO, "Morfema colocado antes do radical."),
    ("sufixo", Genero.MASCULINO, "Morfema colocado depois do radical."),
    ("flexão", Genero.FEMININO, "Variação formal de palavra por gênero, número, pessoa, tempo ou modo."),
    ("gênero", Genero.MASCULINO, "Traço de concordância que organiza masculino, feminino ou comum."),
    ("número gramatical", Genero.MASCULINO, "Traço que distingue singular e plural na construção linguística."),
    ("pessoa gramatical", Genero.FEMININO, "Traço que organiza quem fala, com quem se fala e de quem se fala."),
    ("nome", Genero.MASCULINO, "Palavra que aponta para entidade, coisa, ideia, lugar ou conceito."),
    ("substantivo", Genero.MASCULINO, "Classe de palavra que nomeia entidade, coisa, ideia, lugar ou conceito."),
    ("verbo", Genero.MASCULINO, "Classe de palavra que organiza ação, estado, existência, ocorrência ou ligação."),
    ("adjetivo", Genero.MASCULINO, "Classe de palavra que atribui característica a um nome."),
    ("pronome", Genero.MASCULINO, "Classe de palavra que retoma, aponta ou substitui referência."),
    ("determinante", Genero.MASCULINO, "Classe de palavra que acompanha nome e limita referência."),
    ("advérbio", Genero.MASCULINO, "Classe de palavra que modifica verbo, adjetivo, outro advérbio ou frase."),
    ("concordância", Genero.FEMININO, "Ajuste formal entre palavras relacionadas."),
    ("parágrafo", Genero.MASCULINO, "Bloco de texto que agrupa frases em torno de continuidade local."),
    ("coerência", Genero.FEMININO, "Continuidade de sentido entre partes do texto."),
    ("coesão", Genero.FEMININO, "Ligação visível entre partes do texto."),
    ("funcionamento", Genero.MASCULINO, "Caminho interno pelo qual uma construção opera do mínimo até uma forma viva."),
    ("enunciado", Genero.MASCULINO, "Unidade comunicativa dita ou escrita numa situação."),
    ("referência", Genero.FEMININO, "Ligação entre palavra ou expressão e aquilo para que aponta."),
    ("referente", Genero.MASCULINO, "Alvo textual ou situacional construído pela referência."),
    ("campo", Genero.MASCULINO, "Agrupamento ou zona de relação entre elementos."),
    ("campo semântico", Genero.MASCULINO, "Agrupamento de palavras por proximidade de sentido."),
    ("polissemia", Genero.FEMININO, "Possibilidade de uma palavra ter sentidos diferentes conforme o contexto."),
    ("sinonímia", Genero.FEMININO, "Proximidade de sentido entre palavras em certo contexto."),
    ("antonímia", Genero.FEMININO, "Oposição de sentido entre palavras ou expressões."),
    ("conectivo", Genero.MASCULINO, "Palavra ou expressão que liga partes do texto."),
    ("retomada", Genero.FEMININO, "Retorno a um referente já construído no texto."),
    ("elipse", Genero.FEMININO, "Ausência controlada de parte recuperável pela construção."),
    ("inferência", Genero.FEMININO, "Sentido obtido pela relação entre o dito e o implicado."),
    ("período", Genero.MASCULINO, "Unidade formada por uma ou mais orações e limitada por pontuação final."),
    ("coordenação", Genero.FEMININO, "Ligação de unidades de mesmo nível funcional."),
    ("subordinação", Genero.FEMININO, "Ligação em que uma unidade depende de outra."),
    ("termo", Genero.MASCULINO, "Parte funcional de uma oração ou frase."),
    ("núcleo", Genero.MASCULINO, "Parte central de um termo ou construção."),
    ("complemento", Genero.MASCULINO, "Termo que completa sentido de nome, verbo ou construção."),
    ("adjunto", Genero.MASCULINO, "Termo que acrescenta informação sem completar exigência central."),
    ("transitividade", Genero.FEMININO, "Modo como um verbo pede ou dispensa complemento."),
    ("regência", Genero.FEMININO, "Relação de exigência ou orientação entre palavras."),
    ("colocação", Genero.FEMININO, "Posição relativa de palavras na frase."),
    ("norma", Genero.FEMININO, "Regularidade aceita para uso controlado da língua."),
    ("uso", Genero.MASCULINO, "Prática concreta de aplicar a língua numa situação."),
    ("variação", Genero.FEMININO, "Diferença de uso conforme pessoa, lugar, tempo ou situação."),
    ("variação linguística", Genero.FEMININO, "Diferença de uso entre comunidades, lugares, tempos e situações."),
    ("registro", Genero.MASCULINO, "Ajuste de linguagem conforme situação e formalidade."),
    ("fala", Genero.FEMININO, "Realização oral ou concreta da língua em uso."),
    ("escrita", Genero.FEMININO, "Realização gráfica da língua por marcas organizadas."),
    ("emissor", Genero.MASCULINO, "Participante que produz um enunciado."),
    ("receptor", Genero.MASCULINO, "Participante que recebe ou interpreta um enunciado."),
    ("modalidade", Genero.FEMININO, "Orientação do enunciado quanto a afirmar, negar, perguntar, ordenar ou avaliar."),
    ("afirmação", Genero.FEMININO, "Modalidade que apresenta algo como posto ou sustentado."),
    ("negação", Genero.FEMININO, "Marca de recusa, ausência, oposição ou cancelamento de uma afirmação possível."),
    ("interrogação", Genero.FEMININO, "Modalidade que busca informação, confirmação ou escolha."),
    ("exclamação", Genero.FEMININO, "Modalidade que aumenta força expressiva, surpresa, emoção ou ênfase."),
    ("tempo verbal", Genero.MASCULINO, "Traço verbal que situa ocorrência em relação a antes, agora, depois ou referência interna."),
    ("aspecto verbal", Genero.MASCULINO, "Modo de observar a ocorrência como concluída, em curso, repetida, habitual ou iniciada."),
    ("modo verbal", Genero.MASCULINO, "Orientação do verbo quanto a certeza, hipótese, desejo, ordem ou condição."),
    ("voz verbal", Genero.FEMININO, "Organização que mostra como sujeito e predicado se relacionam com a ação."),
    ("preposição", Genero.FEMININO, "Palavra relacional que aproxima termos e orienta dependência de sentido."),
    ("conjunção", Genero.FEMININO, "Palavra relacional que liga termos ou orações."),
    ("interjeição", Genero.FEMININO, "Palavra ou emissão que manifesta reação, chamado, dor, surpresa ou contacto comunicativo."),
    ("numeral", Genero.MASCULINO, "Classe que introduz contagem, ordem, fração ou multiplicação na língua."),
    ("artigo", Genero.MASCULINO, "Determinante que apresenta nome como definido, indefinido ou introduzido na referência."),
    ("locução", Genero.FEMININO, "Combinação estável de palavras que funciona como unidade de classe ou função."),
    ("perífrase verbal", Genero.FEMININO, "Locução em que verbos combinados expressam tempo, aspecto, modalidade ou ação composta."),
    ("discurso direto", Genero.MASCULINO, "Modo textual que apresenta fala ou pensamento como enunciado preservado."),
    ("discurso indireto", Genero.MASCULINO, "Modo textual que reconstrói fala ou pensamento dentro de outra enunciação."),
    ("tema", Genero.MASCULINO, "Aquilo sobre que um texto, parágrafo ou enunciado se organiza."),
    ("progressão temática", Genero.FEMININO, "Avanço controlado do tema ao longo do texto."),
    ("ambiguidade", Genero.FEMININO, "Abertura de mais de uma leitura possível para uma forma, frase ou texto."),
    ("pragmática", Genero.FEMININO, "Observação do sentido em uso, considerando intenção, contexto, participantes e efeito."),
    ("estilo", Genero.MASCULINO, "Modo recorrente de escolher palavras, ritmo, ordem, tom e construção textual."),
    ("revisão", Genero.FEMININO, "Retorno controlado ao texto para verificar coerência, coesão, norma, clareza e intenção."),
    ("interpretação", Genero.FEMININO, "Construção de sentido a partir de texto, contexto, relações e inferências limitadas."),
    # Lote extraído do corpus amplo (Fase 3/4 do plano de léxico), palavras de
    # alta frequência na prosa já autoral do projeto, ainda ausentes do
    # léxico antes desta entrada.
    ("consulta", Genero.FEMININO, "Ato de perguntar ou verificar informação já registrada."),
    ("dependência", Genero.FEMININO, "Aquilo de que um conceito ou construção precisa para existir."),
    ("forma", Genero.FEMININO, "Aspecto ou configuração que algo assume."),
    ("ocorrência", Genero.FEMININO, "Caso concreto em que algo acontece ou aparece."),
    ("definição", Genero.FEMININO, "Enunciado que fixa o sentido preciso de um conceito."),
    ("domínio", Genero.MASCULINO, "Área ou conjunto sobre o qual uma construção ou regra se aplica."),
    ("análise", Genero.FEMININO, "Exame que separa um todo nas suas partes para entender a construção."),
    ("linguística", Genero.FEMININO, "Área que estuda a estrutura e o funcionamento da língua."),
    ("bloco", Genero.MASCULINO, "Conjunto de partes tratadas como unidade dentro de uma organização maior."),
    ("posição", Genero.FEMININO, "Lugar que um elemento ocupa dentro de uma ordem ou estrutura."),
    ("fluxo", Genero.MASCULINO, "Caminho contínuo que avança de um conceito para o seguinte sem saltos."),
    ("unidade", Genero.FEMININO, "Elemento tratado como um todo dentro de uma contagem ou estrutura."),
    ("projeto", Genero.MASCULINO, "Empreendimento organizado com objetivo e construção definidos."),
    ("limite", Genero.MASCULINO, "Ponto além do qual uma construção ou regra deixa de valer."),
    ("base", Genero.FEMININO, "Fundamento sobre o qual uma construção se apoia."),
    ("igualdade", Genero.FEMININO, "Relação entre dois valores ou formas que são exatamente o mesmo."),
    ("busca", Genero.FEMININO, "Percurso controlado para encontrar um elemento ou caminho."),
    ("grau", Genero.MASCULINO, "Nível ou medida numa escala ordenada."),
    ("implementação", Genero.FEMININO, "Construção concreta em código de uma ideia já especificada."),
    # Segundo lote do corpus amplo (Fase 3/4, corte seguinte).
    ("raiz", Genero.FEMININO, "Origem ou fundamento de onde algo nasce."),
    ("lógica", Genero.FEMININO, "Disciplina que estuda a validade do raciocínio."),
    ("classe", Genero.FEMININO, "Categoria que agrupa elementos com propriedade comum."),
    ("pessoa", Genero.FEMININO, "Indivíduo humano, ou categoria gramatical que marca quem fala."),
    ("valor", Genero.MASCULINO, "Quantidade ou grandeza atribuída a algo."),
    ("zero", Genero.MASCULINO, "Ausência de quantidade; ponto de partida da contagem."),
    ("modo", Genero.MASCULINO, "Maneira como algo acontece ou é feito."),
    ("verdade", Genero.FEMININO, "Aquilo que corresponde exatamente ao que é."),
    ("ponte", Genero.FEMININO, "Ligação explícita entre um conceito novo e outro já construído."),
    ("erro", Genero.MASCULINO, "Desvio entre o esperado e o que aconteceu de fato."),
    ("autor", Genero.MASCULINO, "Pessoa que cria ou constrói uma obra ou ideia."),
    ("parte", Genero.FEMININO, "Porção de um todo maior."),
    ("objeto", Genero.MASCULINO, "Aquilo sobre que uma ação ou pensamento recai."),
    ("mudança", Genero.FEMININO, "Passagem de um estado para outro diferente."),
    ("produto", Genero.MASCULINO, "Resultado de uma construção ou operação."),
    ("lei", Genero.FEMININO, "Regra permanente que rege um domínio."),
    ("expressão", Genero.FEMININO, "Forma que representa um valor ou ideia."),
    ("item", Genero.MASCULINO, "Elemento individual dentro de uma lista ou conjunto."),
    ("linguagem", Genero.FEMININO, "Sistema usado para comunicar ou representar sentido."),
    ("padrão", Genero.MASCULINO, "Forma recorrente que se repete de modo reconhecível."),
    ("passo", Genero.MASCULINO, "Etapa individual dentro de uma construção maior."),
    ("distinção", Genero.FEMININO, "Marca que separa dois conceitos próximos."),
    ("voz", Genero.FEMININO, "Som produzido pela fala, ou organização gramatical sujeito-ação."),
    ("vez", Genero.FEMININO, "Ocasião ou repetição contada de um evento."),
    ("fechamento", Genero.MASCULINO, "Conclusão que fecha uma construção ou etapa."),
    ("equivalência", Genero.FEMININO, "Relação em que dois elementos valem exatamente o mesmo."),
    ("grupo", Genero.MASCULINO, "Conjunto de elementos tratados como unidade."),
    # Terceiro lote do corpus amplo (Fase 3/4, corte seguinte).
    ("variedade", Genero.FEMININO, "Conjunto de formas ou versões diferentes dentro de uma mesma categoria."),
    ("caminho", Genero.MASCULINO, "Percurso ou sequência de passos até um destino."),
    ("informação", Genero.FEMININO, "Conteúdo que reduz incerteza sobre algo."),
    ("lista", Genero.FEMININO, "Sequência ordenada de elementos."),
    ("auditoria", Genero.FEMININO, "Verificação sistemática que confere se algo está correto ou completo."),
    ("aritmética", Genero.FEMININO, "Ramo que trata de números e das operações entre eles."),
    ("corpo", Genero.MASCULINO, "Conjunto principal de um texto ou estrutura, sem as partes periféricas."),
    ("condição", Genero.FEMININO, "Circunstância que precisa se cumprir para algo acontecer."),
    ("contagem", Genero.FEMININO, "Ato de determinar quantos elementos existem num conjunto."),
    ("conteúdo", Genero.MASCULINO, "Aquilo que está contido dentro de uma forma ou estrutura."),
    ("realização", Genero.FEMININO, "Ato de tornar concreto algo que antes era só ideia."),
    ("catálogo", Genero.MASCULINO, "Lista organizada que inventaria itens de um conjunto."),
    ("ligação", Genero.FEMININO, "Conexão estabelecida entre duas partes ou conceitos."),
    ("propriedade", Genero.FEMININO, "Característica que pertence a um objeto ou estrutura."),
    ("elemento", Genero.MASCULINO, "Unidade individual que compõe um conjunto maior."),
    ("ausência", Genero.FEMININO, "Estado de não estar presente."),
    ("módulo", Genero.MASCULINO, "Parte independente que compõe um sistema maior."),
    ("alvo", Genero.MASCULINO, "Aquilo que se pretende atingir ou identificar."),
    ("ação", Genero.FEMININO, "Ato realizado por alguém ou algo."),
    # Quarto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("caso", Genero.MASCULINO, "Ocorrência particular usada como exemplo ou instância."),
    ("narrativa", Genero.FEMININO, "Relato organizado de acontecimentos."),
    ("repetição", Genero.FEMININO, "Ocorrência de novo do mesmo elemento ou padrão."),
    ("organização", Genero.FEMININO, "Disposição ordenada de partes dentro de um todo."),
    ("participante", Genero.MASCULINO, "Pessoa ou elemento que toma parte numa situação ou interação."),
    ("avaliação", Genero.FEMININO, "Julgamento sobre o valor, a qualidade ou a correção de algo."),
    ("documento", Genero.MASCULINO, "Registro escrito que preserva informação ou conhecimento."),
    ("grafia", Genero.FEMININO, "Modo como uma palavra é escrita."),
    ("código", Genero.MASCULINO, "Sistema de instruções escrito para ser executado por um sistema."),
    ("marcador", Genero.MASCULINO, "Elemento que assinala ou identifica uma posição ou categoria."),
    ("conclusão", Genero.FEMININO, "Ideia final alcançada a partir do que veio antes."),
    ("decisão", Genero.FEMININO, "Escolha feita entre alternativas possíveis."),
    ("continuidade", Genero.FEMININO, "Manutenção de uma ligação sem interrupção ao longo do tempo."),
    ("tipo", Genero.MASCULINO, "Categoria que agrupa elementos com característica comum."),
    ("plano", Genero.MASCULINO, "Conjunto organizado de passos para alcançar um objetivo."),
    # Quinto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("discurso", Genero.MASCULINO, "Uso organizado da língua numa situação real de comunicação."),
    ("pretérito", Genero.MASCULINO, "Tempo verbal que situa a ocorrência antes do momento de referência."),
    ("linha", Genero.FEMININO, "Sequência contínua de texto, marca ou elementos numa direção."),
    ("fonte", Genero.FEMININO, "Origem de onde algo vem ou é obtido."),
    ("produção", Genero.FEMININO, "Ato de gerar ou construir algo a partir de partes ou processo."),
    ("razão", Genero.FEMININO, "Motivo que explica ou justifica algo."),
    ("dado", Genero.MASCULINO, "Informação básica usada como ponto de partida para análise ou construção."),
    ("plural", Genero.MASCULINO, "Forma que indica mais de um elemento."),
    ("par", Genero.MASCULINO, "Conjunto de dois elementos associados."),
    # Sexto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("criança", Genero.FEMININO, "Ser humano na primeira fase da vida, antes da idade adulta."),
    ("autoridade", Genero.FEMININO, "Poder reconhecido para decidir ou validar algo dentro de um domínio."),
    ("efeito", Genero.MASCULINO, "Consequência produzida por uma causa."),
    ("fato", Genero.MASCULINO, "Acontecimento real, verificável, distinto de opinião ou suposição."),
    ("achado", Genero.MASCULINO, "Descoberta feita ao investigar ou testar algo."),
    ("constituinte", Genero.MASCULINO, "Elemento que entra na composição de uma estrutura maior."),
    ("agente", Genero.MASCULINO, "Quem ou o que realiza uma ação."),
    # Sétimo lote do corpus amplo (Fase 3/4, corte seguinte).
    ("área", Genero.FEMININO, "Domínio ou extensão dentro do qual algo se aplica ou existe."),
)

_ADJETIVOS: tuple[tuple[str, str], ...] = (
    ("fluido", "Que corre com naturalidade e continuidade."),
    ("natural", "Próximo do modo como uma pessoa fala ou pensa."),
    ("humano", "Explicado para uma pessoa real, com chão, exemplo e ritmo."),
    ("técnico", "Relacionado a método, sistema, ciência ou construção especializada."),
    ("perfeito", "Completo para o objetivo definido, sem lacuna essencial naquele contexto."),
    ("amplo", "Grande em alcance e variedade."),
    ("grande", "De tamanho, alcance ou quantidade elevados."),
    ("infinito", "Sem último elemento dentro da regra de continuação."),
    ("real", "Tratado com honestidade operacional e não apenas como palavra bonita."),
    ("futuro", "Ainda por construir, testar ou integrar."),
    ("construído", "Já formado por etapas anteriores e documentado."),
    ("pendente", "Ainda em falta ou à espera de construção."),
    ("claro", "Fácil de perceber."),
    ("simples", "Reduzido ao essencial sem perder verdade."),
    ("profundo", "Que vai até fundamentos e consequências."),
    ("aberto", "Preparado para continuar além do estado atual."),
    ("finito", "Com limite definido e manipulável."),
    ("simbólico", "Expresso por sinais, letras ou fórmulas."),
    ("conceitual", "Baseado no conceito antes da fórmula."),
    ("lexical", "Relacionado à palavra como unidade reconhecida."),
    ("morfologico", "Relacionado à forma interna das palavras."),
    ("morfológico", "Relacionado à forma interna das palavras."),
    ("sintático", "Relacionado à organização das palavras na frase."),
    ("semântico", "Relacionado ao sentido construído."),
    ("gramatical", "Relacionado ao funcionamento organizado da língua."),
    ("tônico", "Que recebe força relativa maior na palavra."),
    ("comunicativo", "Relacionado à intenção ou ato de comunicar."),
    ("referencial", "Relacionado à referência ou ao alvo indicado."),
    ("polissêmico", "Que admite mais de um sentido conforme contexto."),
    ("sinonímico", "Relacionado à proximidade de sentido."),
    ("antonímico", "Relacionado à oposição de sentido."),
    ("coordenado", "Ligado em mesmo nível funcional."),
    ("subordinado", "Dependente de outra unidade na construção."),
    ("normativo", "Relacionado à norma de uso controlado."),
    ("variável", "Que pode mudar conforme uso, situação ou relação."),
    ("formal", "Adequado a contexto de maior controlo ou cerimónia."),
    ("informal", "Adequado a contexto familiar ou espontâneo."),
    ("afirmativo", "Relacionado a afirmação ou declaração sustentada."),
    ("negativo", "Relacionado a negação ou cancelamento de uma afirmação possível."),
    ("interrogativo", "Relacionado a pergunta ou busca de informação."),
    ("exclamativo", "Relacionado a força expressiva ou exclamação."),
    ("pragmático", "Relacionado ao sentido em uso e ao contexto comunicativo."),
    ("estilístico", "Relacionado ao modo de expressão de um texto."),
    ("interpretativo", "Relacionado à construção de sentido com limites claros."),
    # Lote extraído do corpus amplo (Fase 3/4 do plano de léxico).
    ("mínimo", "O menor valor ou caso ainda válido dentro de uma regra."),
    ("verbal", "Relacionado ao verbo ou à fala."),
    ("compatível", "Que pode coexistir ou funcionar junto sem conflito."),
    ("operacional", "Que já funciona de verdade, não só em teoria."),
    ("nominal", "Relacionado ao nome ou substantivo."),
    ("adverbial", "Relacionado ao advérbio ou à sua função."),
    ("puro", "Construído desde o fundamento, sem atalho nem fórmula pronta importada."),
    # Segundo lote do corpus amplo (Fase 3/4, corte seguinte).
    ("inicial", "Que está no começo de algo."),
    ("final", "Que está no fim de algo."),
    ("explícito", "Dito de forma clara e direta, sem ficar implícito."),
    ("geral", "Que se aplica ao conjunto todo, não a um caso só."),
    ("primeiro", "Que ocupa a posição inicial numa ordem."),
    ("próprio", "Que pertence especificamente a algo ou alguém."),
    ("direto", "Que vai ao ponto sem desvio ou intermediário."),
    ("gráfico", "Relacionado à representação visual ou escrita."),
    ("próximo", "Que está perto no espaço, tempo ou relação."),
    ("comum", "Que é compartilhado ou frequente."),
    ("externo", "Que vem ou está fora de um limite dado."),
    ("necessário", "Que é preciso para que algo aconteça ou exista."),
    ("textual", "Relacionado ao texto como unidade organizada."),
    ("permitido", "Que tem autorização para acontecer ou ser usado."),
    ("proibido", "Que não tem autorização para acontecer ou ser usado."),
    # Terceiro lote do corpus amplo (Fase 3/4, corte seguinte).
    ("diferente", "Que não é igual a outra coisa comparada."),
    ("parcial", "Que cobre só uma parte, não o todo."),
    ("exato", "Que corresponde precisamente ao esperado, sem erro."),
    ("linguístico", "Relacionado à língua ou ao seu estudo."),
    ("ordenado", "Que segue uma sequência ou critério de organização."),
    ("modular", "Que pode ser dividido em partes independentes e combináveis."),
    ("booleano", "Relacionado a valores lógicos de verdadeiro ou falso."),
    ("linear", "Que segue uma progressão direta, sem ramificação."),
    ("maior", "Que tem tamanho, grau ou quantidade acima de outro na comparação."),
    ("principal", "Que tem mais importância entre os elementos comparados."),
    ("racional", "Que pode ser expresso como razão entre dois números inteiros, ou que segue raciocínio lógico."),
    ("anterior", "Que vem antes na ordem ou no tempo."),
    ("automático", "Que acontece sem intervenção manual repetida."),
    ("histórico", "Relacionado a fatos ou período já ocorridos."),
    ("ortográfico", "Relacionado às regras de escrita correta das palavras."),
    # Quarto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("abstrato", "Que não tem existência física concreta, tratado por conceito."),
    ("temporal", "Relacionado ao tempo ou à sua passagem."),
    ("universal", "Que se aplica a todos os casos dentro do seu domínio, sem exceção conhecida."),
    ("honesto", "Que não esconde nem finge o que realmente é ou sabe."),
    ("menor", "Que tem tamanho, grau ou quantidade abaixo de outro na comparação."),
    ("sonoro", "Que produz ou envolve som."),
    ("único", "Que não tem outro igual dentro do conjunto considerado."),
    ("interno", "Que está ou vem de dentro de um limite dado."),
    ("indireto", "Que passa por um intermediário em vez de ir direto ao ponto."),
    # Quinto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("pronto", "Que já está preparado ou concluído para uso ou apresentação."),
    ("funcional", "Que cumpre de verdade a função a que se destina."),
    ("limitado", "Que tem alcance restrito, não total."),
    ("nativo", "Que já nasce construído dentro do sistema, sem depender de fonte externa."),
    ("regular", "Que segue um padrão previsível, sem exceção."),
    ("social", "Relacionado à convivência ou organização entre pessoas."),
    # Sexto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("central", "Que ocupa a posição principal ou mais importante."),
)

_VERBOS: tuple[tuple[str, str], ...] = (
    ("conversar", "Trocar mensagens com contexto e continuidade."),
    ("entender", "Captar a intenção e o conteúdo de um pedido."),
    ("explicar", "Tornar uma ideia clara para outra pessoa."),
    ("ensinar", "Organizar conhecimento em caminho de aprendizagem."),
    ("aprender", "Transformar explicação e prática em domínio."),
    ("construir", "Formar algo a partir de partes anteriores."),
    ("reconstruir", "Refazer uma ideia desde o fundamento."),
    ("validar", "Testar se uma construção funciona."),
    ("melhorar", "Remover falhas e aumentar qualidade."),
    ("aprimorar", "Ajustar e elevar o nível de um sistema ou ideia."),
    ("desmontar", "Separar uma ideia em partes menores."),
    ("resumir", "Dizer o essencial em menos palavras."),
    ("exemplificar", "Mostrar uma ideia por caso concreto."),
    ("praticar", "Treinar por exercícios."),
    ("continuar", "Avançar a partir do ponto atual."),
    ("perguntar", "Solicitar informação, aula, exemplo ou ação."),
    ("responder", "Devolver uma resposta ao pedido recebido."),
    ("comparar", "Ver semelhanças, diferenças e consequências."),
    ("testar", "Submeter uma ideia a casos para verificar estabilidade."),
    ("formalizar", "Dar forma precisa a uma construção."),
    ("flexionar", "Variar uma palavra por gênero, número, pessoa, tempo ou modo."),
    ("concordar", "Ajustar palavras relacionadas dentro da construção."),
    ("acentuar", "Marcar graficamente uma palavra quando a construção exigir."),
    ("pontuar", "Inserir marcas que regulam limite, pausa e intenção."),
    ("segmentar", "Separar uma forma em partes menores para análise."),
    ("relacionar", "Ligar partes da construção por função ou sentido."),
    ("referir", "Apontar para um alvo textual ou situacional."),
    ("retomar", "Voltar a um referente já construído."),
    ("inferir", "Obter sentido por relação entre o dito e o implicado."),
    ("coordenar", "Ligar unidades de mesmo nível funcional."),
    ("subordinar", "Ligar uma unidade a outra da qual depende."),
    ("complementar", "Completar sentido de uma construção."),
    ("reger", "Orientar ou exigir uma relação gramatical."),
    ("variar", "Mudar forma ou uso conforme condição."),
    ("registrar", "Ajustar ou fixar uma forma de linguagem em certo contexto."),
    ("afirmar", "Apresentar algo como sustentado ou posto."),
    ("negar", "Marcar recusa, ausência ou cancelamento de uma afirmação possível."),
    ("interrogar", "Construir pergunta ou busca de informação."),
    ("exclamar", "Marcar força expressiva, surpresa ou emoção."),
    ("interpretar", "Construir sentido a partir de texto, contexto e relações limitadas."),
    ("revisar", "Retornar ao texto para verificar e melhorar coerência, coesão, norma e clareza."),
    # Lote extraído do corpus amplo (Fase 3/4 do plano de léxico).
    ("permitir", "Dar possibilidade ou abertura para algo acontecer ou ser feito."),
    ("reconhecer", "Identificar algo como já conhecido ou válido."),
    ("confundir", "Tratar por engano uma coisa como se fosse outra."),
    ("verificar", "Conferir se algo é verdadeiro ou está correto."),
    ("ligar", "Estabelecer conexão entre duas partes ou conceitos."),
    ("organizar", "Dispor partes numa ordem clara e funcional."),
    ("distinguir", "Perceber e marcar a diferença entre duas coisas."),
    # Segundo lote do corpus amplo (Fase 3/4, corte seguinte).
    ("existir", "Ter presença real dentro de um domínio."),
    ("pertencer", "Fazer parte de um conjunto ou categoria."),
    ("precisar", "Ter necessidade de algo para continuar."),
    ("apresentar", "Mostrar algo pela primeira vez a alguém."),
    ("implementar", "Construir em código uma ideia já especificada."),
    ("exigir", "Pedir como condição necessária."),
    ("usar", "Empregar algo para um fim."),
    ("depender", "Precisar de outra coisa para existir ou funcionar."),
    # Terceiro lote do corpus amplo (Fase 3/4, corte seguinte).
    ("significar", "Ter determinado sentido ou valor."),
    ("expressar", "Tornar visível ou comunicável um sentido ou sentimento."),
    ("partir", "Sair de um ponto de origem em direção a outro."),
    ("fingir", "Simular algo que não é real ou verdadeiro."),
    ("materializar", "Tornar concreto algo que antes era só ideia ou possibilidade."),
    ("nascer", "Passar a existir a partir de uma origem."),
    ("dever", "Ter obrigação de fazer algo."),
    # Quarto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("separar", "Colocar partes distintas fora de contacto ou de um mesmo grupo."),
    ("criar", "Fazer existir algo que antes não existia."),
    ("chegar", "Alcançar um destino ou ponto de referência."),
    ("fechar", "Encerrar ou concluir algo que estava aberto ou em curso."),
    ("aprovar", "Confirmar que algo está correto ou aceitável."),
    # Sexto lote do corpus amplo (Fase 3/4, corte seguinte).
    ("corrigir", "Ajustar algo para remover erro ou falha."),
    # Sétimo lote do corpus amplo (Fase 3/4, corte seguinte).
    ("ficar", "Permanecer num estado ou lugar."),
    ("aparecer", "Passar a ser visível ou perceptível."),
)

# Estes lemas não seguem integralmente o paradigma mecânico de `_verbo`.
# Mantemos o lema e a definição já curados, mas não fabricamos flexões com a
# raiz invariável. As formas irregulares serão materializadas em lote próprio.
_VERBOS_FORA_DO_PARADIGMA_REGULAR = frozenset({
    "construir",
    "reconstruir",
    "referir",
    "inferir",
})


def entradas_expandidas() -> tuple[EntradaLexical, ...]:
    entradas: list[EntradaLexical] = []
    lemas_manuais: set[str] = set()
    for lema, genero, definicao in _NOMES:
        lemas_manuais.add(lema.casefold())
        entradas.extend(_forma_nome(lema, genero, definicao))
    for lema, definicao in _ADJETIVOS:
        entradas.extend(_forma_adj(lema, definicao))
    for infinitivo, definicao in _VERBOS:
        if infinitivo in _VERBOS_FORA_DO_PARADIGMA_REGULAR:
            entradas.append(
                EntradaLexical(infinitivo, infinitivo, ClasseGramatical.VERBO, (definicao,))
            )
        else:
            entradas.extend(_verbo(infinitivo, definicao))
    entradas.extend(_PALAVRAS_FUNCIONAIS)

    # Todo conceito puro precisa ser consultável no léxico interno. Conceitos já
    # materializados manualmente não são duplicados; os demais entram como
    # substantivos técnicos, sem género inventado e sem dependência externa.
    conceitos_por_nome = {conceito.nome.casefold(): conceito for conceito in CONCEITOS_PORTUGUES_PURO}
    for conceito in CONCEITOS_PORTUGUES_PURO:
        if conceito.nome.casefold() in lemas_manuais:
            continue
        entradas.append(
            EntradaLexical(
                lema=conceito.nome,
                forma=conceito.nome,
                classe=ClasseGramatical.SUBSTANTIVO,
                definicoes=(conceito.construcao,),
                atributos={"tema_consulta_psf": conceito.tema_consulta, "ordem_psf": conceito.ordem, "camada_psf": conceito.camada},
            )
        )

    # Termos equivalentes são formas de acesso, não conceitos duplicados.
    for alias, alvo in ALIASES_CONCEITOS_PORTUGUES.items():
        conceito = conceitos_por_nome[alvo.casefold()]
        entradas.append(
            EntradaLexical(
                lema=alias,
                forma=alias,
                classe=ClasseGramatical.SUBSTANTIVO,
                definicoes=(f"Termo equivalente a {conceito.nome}: {conceito.construcao}",),
                atributos={"alias_psf": conceito.nome, "ordem_psf": conceito.ordem},
            )
        )
    return tuple(entradas)
