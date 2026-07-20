"""Teste do resolvedor de exercícios "modo cientista" (ensino/resolvedor_exercicios.py).

Usa as frases literais encontradas em privado/avalmath.docx (avaliações
reais de matemática por país/classe) para provar que cada padrão
reconhece e deriva a resposta certa com os métodos do próprio motor.

Roda com: python3 testes/test_resolvedor_exercicios.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino.resolvedor_exercicios import resolver

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste do resolvedor de exercícios")

    caminho_log = Path(tempfile.mktemp(suffix=".json"))
    try:
        r = resolver(
            "Conta 8 lápis e mais 5 lápis numa turma de Afghanistan. Quantos lápis há?",
            caminho_log,
        )
        ok("soma_contextual resolvida", r.resolvida, True)
        ok("soma_contextual padrao", r.padrao, "soma_contextual")
        ok("soma_contextual resposta", r.resposta, "13")

        r = resolver("Coloca em ordem crescente: 6, 2, 9, 1.", caminho_log)
        ok("ordenar crescente resolvida", r.resolvida, True)
        ok("ordenar crescente resposta", r.resposta, "1, 2, 6, 9")

        r = resolver("Coloca em ordem decrescente: 6, 2, 9, 1.", caminho_log)
        ok("ordenar decrescente resposta", r.resposta, "9, 6, 2, 1")

        r = resolver(
            "Num modelo de crescimento em Zimbabwe, P(t)=500(1,04)^t. Calcula P(3) aproximadamente.",
            caminho_log,
        )
        ok("crescimento exponencial resolvida", r.resolvida, True)
        ok("crescimento exponencial resposta", r.resposta, "70304/125 (aproximadamente 562.432)")

        r = resolver("Resolve log10(x)=2.", caminho_log)
        ok("log como potencia resolvida", r.resolvida, True)
        ok("log como potencia resposta", r.resposta, "100")

        r = resolver("Resolve log2(x)=5.", caminho_log)
        ok("log base diferente", r.resposta, "32")

        r = resolver("Calcula a soma dos 10 primeiros termos da PA 3, 7, 11, ...", caminho_log)
        ok("PA soma resolvida", r.resolvida, True)
        ok("PA soma resposta (3,7,11,... 10 termos)", r.resposta, "210")

        r = resolver("Calcula a soma dos 5 primeiros termos da PA 2, 4, 6, ...", caminho_log)
        ok("PA soma outro caso (2,4,6,... 5 termos == 30)", r.resposta, "30")

        r = resolver(
            "Numa escola de Afghanistan há 37 alunos numa sala e 24 noutra. Quantos alunos há ao todo?",
            caminho_log,
        )
        ok("soma_contextual_ao_todo resposta", r.resposta, "61")

        r = resolver("Calcula: 84 - 29.", caminho_log)
        ok("calculo_direto subtracao", r.resposta, "55")

        r = resolver("Calcula: 56 ÷ 7.", caminho_log)
        ok("calculo_direto divisao exata", r.resposta, "8")

        r = resolver("Calcula: 2 345 + 1 789.", caminho_log)
        ok("calculo_direto soma com milhares espaçados", r.resposta, "4134")

        r = resolver(
            "Um mercado em Afghanistan vende 6 caixas com 8 maçãs cada. Quantas maçãs são?", caminho_log
        )
        ok("multiplicacao_caixas resposta", r.resposta, "48")

        r = resolver("Uma horta escolar em Afghanistan mede 9 m por 6 m. Calcula a área.", caminho_log)
        ok("area_retangulo resposta", r.resposta, "54 m²")

        r = resolver("Calcula 15% de 240.", caminho_log)
        ok("percentagem resposta", r.resposta, "36")

        r = resolver("Compara: 5/8 e 3/4. Qual é maior?", caminho_log)
        ok("fracao_comparar resposta", r.resposta, "3/4")

        r = resolver("Calcula: 3/5 + 1/10.", caminho_log)
        ok("fracao_somar resposta", r.resposta, "7/10")

        r = resolver(
            "Numa turma de Afghanistan, 0,6 dos alunos trouxeram caderno. Escreve 0,6 como fração.", caminho_log
        )
        ok("decimal_para_fracao resposta", r.resposta, "3/5")

        r = resolver("A média de 6, 8, 10 e 12 é quanto?", caminho_log)
        ok("media_de_lista resposta", r.resposta, "9")

        r = resolver(
            "Interpreta um gráfico com valores 12, 18, 15 e 20: qual é o maior valor?", caminho_log
        )
        ok("maior_valor_lista resposta", r.resposta, "20")

        r = resolver(
            "Uma receita usada em Afghanistan usa razão 2:3 de farinha e água. "
            "Se há 10 copos de farinha, quantos de água?",
            caminho_log,
        )
        ok("razao_receita resposta", r.resposta, "15")

        r = resolver(
            "Dois triângulos são semelhantes com razão 3:5. Se um lado pequeno mede 12, "
            "qual é o correspondente maior?",
            caminho_log,
        )
        ok("razao_semelhanca resposta", r.resposta, "20")

        r = resolver("Um triângulo retângulo tem catetos 6 e 8. Calcula a hipotenusa.", caminho_log)
        ok("hipotenusa resolvida (quadrado perfeito)", r.resolvida, True)
        ok("hipotenusa resposta", r.resposta, "10")

        r = resolver("Um triângulo retângulo tem catetos 2 e 3. Calcula a hipotenusa.", caminho_log)
        ok("hipotenusa honesta quando não é quadrado perfeito", r.resolvida, False)
        ok("hipotenusa não inventa resposta", r.resposta, None)

        r = resolver("Fatora: x² + 5x + 6.", caminho_log)
        ok("fatorar_quadratica resposta", r.resposta, "(x + 2)(x + 3)")

        r = resolver(
            "Em Afghanistan, compara dois planos: A = 50 + 2x e B = 20 + 5x. Para que x são iguais?",
            caminho_log,
        )
        ok("planos_lineares_iguais resposta", r.resposta, "10")

        r = resolver("Num problema de Afghanistan, resolve 2x + 5 = 21.", caminho_log)
        ok("equacao_linear_simples resposta", r.resposta, "8")

        r = resolver(
            "Em Afghanistan, um autocarro percorre 180 km em 3 h. Qual é a velocidade média?", caminho_log
        )
        ok("velocidade_media resposta", r.resposta, "60 km/h")

        r = resolver("Encontra a distância entre A(2,3) e B(8,11).", caminho_log)
        ok("distancia_entre_pontos resposta", r.resposta, "10")

        r = resolver("quanto é 7 mais 8?", caminho_log)
        ok("conversacional mais", r.resposta, "15")
        r = resolver("quanto e 20 menos 5?", caminho_log)
        ok("conversacional menos (sem acento)", r.resposta, "15")
        r = resolver("Quanto é 6 vezes 7?", caminho_log)
        ok("conversacional vezes", r.resposta, "42")
        r = resolver("quanto é 20 dividido por 4?", caminho_log)
        ok("conversacional dividido exato", r.resposta, "5")
        r = resolver("quanto é 7 dividido por 2?", caminho_log)
        ok("conversacional dividido em fracao", r.resposta, "7/2")

        # pergunta de desenho: sem resposta numérica, deve ser honesto e logar.
        pergunta_sem_padrao = "Desenha um círculo, um quadrado e um triângulo."
        r = resolver(pergunta_sem_padrao, caminho_log)
        ok("pergunta sem padrão não resolvida", r.resolvida, False)
        ok("pergunta sem padrão sem resposta", r.resposta, None)
        ok("pergunta sem padrão explica honestamente", "não reconheço" in r.raciocinio, True)

        import json

        log = json.loads(caminho_log.read_text(encoding="utf-8"))
        ok("pergunta não reconhecida foi registada", pergunta_sem_padrao in log, True)

        # repetir a mesma pergunta não-reconhecida não duplica a entrada no log.
        resolver(pergunta_sem_padrao, caminho_log)
        log_de_novo = json.loads(caminho_log.read_text(encoding="utf-8"))
        ok("log não duplica a mesma pergunta", log_de_novo.count(pergunta_sem_padrao), 1)
    finally:
        if caminho_log.exists():
            caminho_log.unlink()

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()


def test_programa_principal():
    assert main() is None
