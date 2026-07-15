# Como rodar o PSF-IAminy

Projeto oficial: `PSF-IAminy/`.

## Entrar na pasta

```bash
cd PSF-IAminy
```

## Verificar integridade básica

```bash
python3 verificar_integridade.py
```

## Rodar todos os testes atuais

```bash
python3 -m pytest -q
```

Resultado atual esperado:

```text
660 passed
```

## Verificar conhecimento puro de Português

```bash
python3 -m pytest -q testes/test_portugues_conhecimento_puro.py
```

## Inspecionar funcionamento de Português

```bash
python3 -c "from lingua_portuguesa import MotorPortugues; motor=MotorPortugues(); print('\n'.join(motor.funcionamento_portugues()))"
```

## Rodar pergunta simples

```bash
python3 psf_chat.py "quem é você?"
```

Observação: `dados/base_canonica.jsonl` foi limpo porque continha perguntas, respostas e aulas prontas. O chat pode responder de forma mais limitada até a base pura ser reconstruída por materialização PSF.

## Abrir interface local

```bash
python3 -m interface.servidor
```

Depois abrir no navegador:

```text
http://127.0.0.1:8765/
```

## Regra deste pacote

Este pacote preserva o conhecimento puro, o núcleo, Matemática, Português, motor interno, motor de busca e área privada.

Foram removidas conversas salvas, aulas prontas antigas, perguntas prontas antigas, respostas prontas antigas, baterias didáticas órfãs, auditorias/dossiês, índices antigos, monografias, resultados temporários e logs que não eram conhecimento puro.

A pasta `privado/` é sagrada e pessoal. O arquivo `privado/avalmath.docx` foi preservado.

## Verificar o aproveitamento da Matemática no Português

```bash
python3 - <<'PY'
from lingua_portuguesa import MotorPortugues

motor = MotorPortugues()
print(motor.auditar_estrutura_portugues())
print(motor.caminho_minimo_conceito_puro("interpretação"))
print(motor.comparar_padrao_gramatical_finito("As meninas estudam rapidamente."))
print(motor.provar_equivalencia_terminologica("variação diatópica"))
PY
```

Esses recursos validam e comparam. Eles não substituem o conhecimento puro de Português.

## Usar os três motores

```bash
python3 - <<'PY'
from motor import MotorGeralIAMiny

psf = MotorGeralIAMiny()
print(psf.calcular_matematica("2+2*3"))
print(psf.reconstruir_matematica("fatorial natural"))
print(psf.analisar_portugues("As meninas estudam."))
print(psf.buscar_conhecimento("fatorial", "matemática"))
print(psf.auditar_motores())
PY
```

`ETAPA` em Matemática e os antigos nomes de camada em Português são somente marcadores históricos/temáticos. A validade vem da construção, das dependências, das implementações e dos testes.

## Verificar a nova divisão PSF

```bash
python3 - <<'PY'
from matematica import MotorMatematica
m = MotorMatematica()
for r in (
    m.calcular("12:5"),
    m.calcular("12:5", casas_decimais=3),
    m.calcular("2:3", casas_decimais=3, modo="arredondar"),
    m.calcular("12:0"),
):
    print(r.estado, r.resultado, r.resultado_exato)
    for passo in r.passos:
        print(passo.ordem, passo.operacao, passo.justificacao)
PY
```

## Consultar a hipótese pendente

```bash
python3 - <<'PY'
from matematica import MotorMatematica
for h in MotorMatematica().hipoteses_pendentes():
    print(h.titulo, h.estado, h.autor)
PY
```

