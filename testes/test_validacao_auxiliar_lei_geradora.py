from nucleo.lei_geradora_real import lei_geradora_raiz_quadrada, modulo_convergencia
from nucleo.reais_intervalos_naturais import RacionalAssinado
from validacao_externa import MotorAuxiliarValidacao


def test_auxiliar_confere_intervalo_ja_construido_pelo_psf_sem_decidi_lo():
    # PSF constrói e prova o intervalo sozinho, sem qualquer ajuda externa.
    lei = lei_geradora_raiz_quadrada(2)
    epsilon = RacionalAssinado(1, 10_000)
    passo = modulo_convergencia(lei, epsilon)
    intervalo = lei.passo(passo)

    # Só depois disso o motor auxiliar (stdlib) confere e mede precisão.
    auxiliar = MotorAuxiliarValidacao()
    resultado = auxiliar.validar_aproximacao_irracional(
        "raiz quadrada de 2",
        (intervalo.inferior.numerador, intervalo.inferior.denominador),
        (intervalo.superior.numerador, intervalo.superior.denominador),
        "sqrt(2)",
    )

    assert resultado.aprovado is True
    assert resultado.estado == "REFERÊNCIA_DENTRO_DO_INTERVALO_PSF"
    assert resultado.aviso == "Motor auxiliar compara e otimiza; não cria conhecimento PSF."


def test_auxiliar_denuncia_intervalo_que_nao_contem_a_referencia():
    auxiliar = MotorAuxiliarValidacao()
    resultado = auxiliar.validar_aproximacao_irracional(
        "raiz quadrada de 2 (intervalo errado de propósito)",
        (1, 1),
        (14, 10),
        "sqrt(2)",
    )
    assert resultado.aprovado is False
    assert resultado.estado == "REFERÊNCIA_FORA_DO_INTERVALO_PSF"
