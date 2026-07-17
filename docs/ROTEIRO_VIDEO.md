# Roteiro de demonstração pública (2–5 minutos)

Objetivo: gravar apenas o que a versão pública realmente executa, sem edição que
esconda falhas ou substitua a saída do programa.

## 1. Apresentação — 20 segundos

- mostrar a página principal do repositório;
- dizer: “PSF-IAminy-Open é um sistema experimental para construção rastreável
  de conhecimento matemático e linguístico”;
- esclarecer que não é apresentado como conhecimento ilimitado ou concluído.

## 2. Instalação — 40 segundos

```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Não cortar erros caso ocorram; corrigir e repetir num novo registo.

## 3. Entrada oficial — 30 segundos

```bash
psf-iaminy --selftest
python -m psf_iaminy --selftest
```

Explicar que ambos usam a mesma entrada pública.

## 4. Matemática — 40 segundos

```bash
python exemplos/matematica.py
```

Mostrar uma reconstrução, a origem indicada e uma limitação reconhecida.

## 5. Português — 40 segundos

```bash
python exemplos/portugues.py
```

Mostrar correção/sugestão conservadora e um caso em que o motor não força uma
análise sem base suficiente.

## 6. Rastreabilidade — 30 segundos

```bash
python exemplos/rastreabilidade.py
```

Mostrar de onde vem a capacidade e como hipótese, validação e conhecimento
implementado permanecem separados.

## 7. Evidência — 30 segundos

```bash
python verificar_integridade.py
python -m pytest -q
```

Na gravação, usar o resultado real do commit apresentado. Não sobrepor texto com
uma quantidade diferente da saída do terminal.

## 8. Encerramento — 20 segundos

- mostrar `docs/LIMITES_OPERACIONAIS.md` e `ROADMAP.md`;
- convidar reprodução independente, issues e revisão científica;
- não pedir estrelas como substituto de validação técnica.

## Checklist antes de publicar

- [ ] gravação corresponde ao commit indicado;
- [ ] nenhum token, e-mail privado, caminho pessoal ou conversa real aparece;
- [ ] todos os comandos foram executados na gravação;
- [ ] limitações aparecem, não apenas resultados positivos;
- [ ] legenda informa sistema operativo e versão do Python;
- [ ] link aponta para uma tag/release ou commit exato.
