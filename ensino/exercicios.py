"""Gerador de exercícios com variação automática do PSF-IAminy.

Os pacotes em `curriculos.py` trazem exercícios fixos, escritos à mão --
bons para a primeira aula, mas sempre os mesmos a cada repetição. Este
módulo gera variações determinísticas a partir de modelos com lacunas:
para uma dada semente, o gerador escolhe sempre a mesma combinação, então
o exercício é reprodutível em testes e reaparece igual se o aluno pedir
de novo com a mesma semente.

Cada lacuna é preenchida por uma frase pronta, não por um número e um
substantivo escolhidos separadamente -- assim toda combinação sai
gramaticalmente correta em português (concordância de número e gênero já
embutida na frase), sem precisar de um flexionador que o motor ainda não
tem.

Nem todo pacote precisa ter modelo. Sem modelo registrado, o gerador
devolve os exercícios fixos do próprio pacote -- ninguém fica sem
exercício só porque a variação ainda não chegou até lá.
"""
from __future__ import annotations

import random
from dataclasses import dataclass

from .tipos import PacoteConhecimento


@dataclass(frozen=True, slots=True)
class ModeloExercicio:
    texto: str
    bancos: tuple[tuple[str, ...], ...]

    def sortear(self, sorteio: random.Random) -> str:
        valores = [sorteio.choice(banco) for banco in self.bancos]
        return self.texto.format(*valores)


MODELOS: dict[str, tuple[ModeloExercicio, ...]] = {
    "MAT-000": (
        ModeloExercicio(
            "Mostre uma mesa vazia, depois coloque {0} em cima.",
            (("um lápis", "uma pedra", "uma borracha", "uma tampa"),),
        ),
    ),
    "MAT-001": (
        ModeloExercicio(
            "Ache dois objetos {0} e diga se são iguais ou diferentes {1}.",
            (
                ("da mesma cor", "de tamanhos diferentes", "da mesma forma"),
                ("na cor", "no tamanho", "na forma"),
            ),
        ),
    ),
    "MAT-002": (
        ModeloExercicio(
            "Separe {0} do grupo e depois devolva.",
            (("uma moeda", "um botão", "um lápis", "uma tampa"),),
        ),
    ),
    "MAT-003": (
        ModeloExercicio(
            "Pareie {0} com {1} e diga se sobrou alguma peça.",
            (
                ("três copos", "quatro colheres", "duas tampas", "cinco pratos"),
                ("três tampas", "quatro pratos", "duas colheres", "cinco copos"),
            ),
        ),
    ),
    "MAT-004": (
        ModeloExercicio(
            "Conte {0} em voz alta, sem pular nenhum.",
            (("três lápis", "quatro dedos", "cinco moedas", "duas pedras"),),
        ),
    ),
    "MAT-005": (
        ModeloExercicio(
            "Organize {0} em fila e diga qual é o primeiro e qual é o último.",
            (("três objetos", "quatro cartões", "cinco brinquedos"),),
        ),
    ),
    "MAT-006": (
        ModeloExercicio(
            "Junte {0} e conte o total.",
            (
                (
                    "1 lápis com 2 lápis",
                    "2 tampas com 2 tampas",
                    "3 moedas com 1 moeda",
                    "1 pedra com 3 pedras",
                ),
            ),
        ),
    ),
    "MAT-007": (
        ModeloExercicio(
            "Comece com {0}; conte o que sobrou.",
            (
                (
                    "4 objetos e retire 1",
                    "5 objetos e retire 2",
                    "6 lápis e retire 3",
                    "5 moedas e retire 2",
                ),
            ),
        ),
    ),
    "MAT-008": (
        ModeloExercicio(
            "Compare {0} e diga se há mais, menos ou a mesma quantidade.",
            (
                (
                    "3 lápis e 2 borrachas",
                    "4 tampas e 4 copos",
                    "5 moedas e 3 botões",
                    "2 pedras e 2 conchas",
                ),
            ),
        ),
    ),
    "MAT-009": (
        ModeloExercicio(
            "Coloque {0} da caixa e diga a posição usada.",
            (("um cubo dentro", "uma bola fora", "um lápis perto", "uma bola longe"),),
        ),
    ),
    "MAT-010": (
        ModeloExercicio(
            "Conte em voz alta até {0}.",
            (("doze", "quinze", "dezoito", "vinte"),),
        ),
    ),
    "MAT-011": (
        ModeloExercicio(
            "Agrupe {0} em dezenas e unidades.",
            (("13 lápis", "27 tampas", "34 moedas", "19 pedras"),),
        ),
    ),
    "MAT-012": (
        ModeloExercicio(
            "Junte {0} e diga se precisou de uma dezena nova.",
            (("8 e 5", "7 e 6", "9 e 9", "6 e 8"),),
        ),
    ),
    "MAT-013": (
        ModeloExercicio(
            "Calcule {0}, desfazendo uma dezena se precisar.",
            (("22 menos 5", "31 menos 8", "40 menos 6", "25 menos 9"),),
        ),
    ),
    "MAT-014": (
        ModeloExercicio(
            "Monte {0} e conte o total.",
            (("3 grupos de 4", "2 grupos de 6", "5 grupos de 2", "4 grupos de 3"),),
        ),
    ),
    "MAT-015": (
        ModeloExercicio(
            "Calcule {0}.",
            (("7 vezes 2", "7 vezes 10", "7 vezes 5", "9 vezes 2", "9 vezes 10"),),
        ),
    ),
    "MAT-016": (
        ModeloExercicio(
            "Reparta {0} e diga se sobra algo.",
            (("13 balas por 4 crianças", "10 lápis por 2 pessoas", "15 balas por 5 crianças", "17 tampas por 3 pessoas"),),
        ),
    ),
    "MAT-017": (
        ModeloExercicio(
            "Calcule {0}.",
            (("o dobro de 9", "a metade de 18", "o dobro de 12", "a metade de 20"),),
        ),
    ),
    "POR-000": (
        ModeloExercicio(
            "Faça o som {0} e diga se está separado do som anterior.",
            (("/a/", "/m/", "/s/", "/o/"),),
        ),
    ),
    "POR-001": (
        ModeloExercicio(
            "Fale {0} sons com pausa entre eles e depois sem pausa nenhuma.",
            (("2", "3"),),
        ),
    ),
    "POR-002": (
        ModeloExercicio(
            "Escreva a letra {0} e diga uma palavra que começa com ela.",
            (("A", "B", "C", "M", "S"),),
        ),
    ),
    "POR-003": (
        ModeloExercicio(
            "Compare {0} e diga o que muda no sentido ou na pergunta.",
            (("avo e avó", "avo e avô", "Vai. e Vai?"),),
        ),
    ),
    "POR-004": (
        ModeloExercicio(
            "Junte {0} e leia a parte formada.",
            (("c + a", "m + a", "n + h", "l + a"),),
        ),
    ),
    "POR-005": (
        ModeloExercicio(
            "Aponte a palavra {0} numa frase e diga onde ela começa e termina.",
            (("casa", "escola", "livro", "gato"),),
        ),
    ),
    "POR-006": (
        ModeloExercicio(
            "Use a palavra {0} em duas frases com sentidos diferentes.",
            (("manga", "banco", "capital"),),
        ),
    ),
    "POR-007": (
        ModeloExercicio(
            "Monte uma frase com a palavra {0} e depois troque a ordem das palavras.",
            (("casa", "escola", "gato"),),
        ),
    ),
    "POR-008": (
        ModeloExercicio(
            "Ache o verbo em '{0}' e separe sujeito e predicado.",
            (("Os gatos comem", "A menina estuda", "O sol brilha"),),
        ),
    ),
    "POR-009": (
        ModeloExercicio(
            "Escreva duas frases sobre {0} e ligue a segunda à primeira.",
            (("um objeto", "um animal", "um lugar"),),
        ),
    ),
    "POR-010": (
        ModeloExercicio(
            "Separe {0} em sílabas e diga qual é a tônica.",
            (("bola", "café", "sabia", "relógio"),),
        ),
    ),
    "POR-011": (
        ModeloExercicio(
            "Classifique as palavras de '{0}'.",
            (("A menina estuda muito", "O gato dorme", "Ela é feliz"),),
        ),
    ),
    "POR-012": (
        ModeloExercicio(
            "Corrija a concordância: '{0}'.",
            (("o menina bonita", "as gato preto", "um casa grande"),),
        ),
    ),
    "POR-013": (
        ModeloExercicio(
            "Diga o tempo verbal de '{0}'.",
            (("ela cantou", "eu como", "nós jogamos", "eles vão sair"),),
        ),
    ),
    "POR-014": (
        ModeloExercicio(
            "Dê um sinónimo e um antónimo de '{0}'.",
            (("bonito", "rápido", "grande", "feliz"),),
        ),
    ),
    "POR-015": (
        ModeloExercicio(
            "Escreva um parágrafo sobre {0}.",
            (("a escola", "um animal de estimação", "um dia de chuva"),),
        ),
    ),
    "POR-016": (
        ModeloExercicio(
            "Escreva uma fala de personagem sobre {0}, usando travessão.",
            (("estar com fome", "ganhar um presente", "chegar atrasado"),),
        ),
    ),
    "POR-017": (
        ModeloExercicio(
            "Pontue corretamente: '{0}'",
            (("Que susto", "Vens à festa", "Trouxe lápis borracha e caderno"),),
        ),
    ),
}


class GeradorExercicios:
    """Gera exercícios variados a partir de modelos por pacote.

    Sem modelo registrado para o código do pacote, devolve os exercícios
    fixos do próprio pacote (`pacote.exercicios`), sem erro.
    """

    def __init__(self, modelos: "dict[str, tuple[ModeloExercicio, ...]] | None" = None) -> None:
        self._modelos = modelos if modelos is not None else MODELOS

    def tem_modelo(self, codigo: str) -> bool:
        return codigo.upper() in self._modelos

    def gerar(
        self,
        pacote: PacoteConhecimento,
        quantidade: int = 3,
        semente: "int | None" = None,
    ) -> tuple[str, ...]:
        modelos = self._modelos.get(pacote.codigo.upper())
        if not modelos:
            return pacote.exercicios
        sorteio = random.Random(semente)
        return tuple(sorteio.choice(modelos).sortear(sorteio) for _ in range(quantidade))
