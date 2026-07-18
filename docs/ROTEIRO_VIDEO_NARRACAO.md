# Roteiro de narração — vídeo de apresentação do PSF-IAminy-Open

Texto para ler/falar durante a gravação descrita em `docs/ROTEIRO_VIDEO.md`.
Segue a mesma estrutura de 8 blocos e os mesmos tempos-alvo. As falas usam
apenas resultados reais, obtidos rodando os comandos indicados nesta cópia do
repositório — nada aqui foi inventado ou arredondado para soar melhor.

Antes de gravar, confira se o commit gravado ainda produz estes mesmos
resultados; se um número mudar, ajuste o texto, não a gravação.

---

## 1. Apresentação — 20 segundos

**Tela:** página principal do repositório (README.md).

**Fala:**
> "Este é o PSF-IAminy-Open. É um sistema experimental que constrói
> conhecimento de Matemática e de Português a partir do mínimo possível — por
> construção própria, chamada aqui de 'Pensador Sem Fronteiras' — em vez de
> citar bibliotecas, fórmulas prontas ou respostas de terceiros como
> fundamento. Não é um sistema completo, nem um produto pronto. É um projeto
> em construção, e o que ainda falta está declarado abertamente."

---

## 2. Instalação — 40 segundos

**Tela:** terminal.

```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

**Fala:**
> "A instalação usa um ambiente virtual comum do Python. Nada de passo
> escondido: clona o repositório, cria o ambiente, ativa e instala em modo
> editável. Se aparecer um erro aqui, ele fica na gravação — o objetivo é
> mostrar o que realmente acontece, não uma versão editada."

---

## 3. Entrada oficial — 30 segundos

```bash
psf-iaminy --selftest
python -m psf_iaminy --selftest
```

**Fala:**
> "Estes dois comandos chamam exatamente a mesma entrada pública do projeto —
> um pelo comando instalado, outro chamando o módulo diretamente. Não são dois
> caminhos diferentes disfarçados de um só."

---

## 4. Matemática — 40 segundos

```bash
python exemplos/matematica.py
```

**Tela de referência** (saída real de `exemplo_publico.py`, mesmo motor):

```
[Matemática] entrada: '12:5'
  estado: RESOLVIDO_EXATAMENTE_POR_CONSTRUÇÃO_PSF
  resultado: 2,400  (forma exata: 12/5)
  1. divisão racional — preservar quociente, resto e fração
  2. expansão decimal por resto — 12 = 5 × 2 + 2
  3. Casa 1: resto 2 → 20; 20 = 5 × 4 + 0.
  4. Casa 2 e 3: resto zero; completa com 0 para a precisão pedida.
```

**Fala:**
> "Aqui o motor recebe '12 dividido por 5'. Ele não chama uma função de
> divisão pronta: reconstrói o resultado — encontra quociente 2 e resto 2,
> depois transporta o resto multiplicando por 10 para gerar cada casa decimal,
> até chegar em 2,400, guardando também a forma exata, 12/5. Cada passo tem uma
> justificativa, não só um número final."

---

## 5. Português — 40 segundos

```bash
python exemplos/portugues.py
```

**Tela de referência** (saída real):

```
[Português] entrada: 'Ela nao sabia nda sobre o assunto.'
  sugestão para 'nao': não, na, no
  sugestão para 'nda': nada, na, da
  sugestão para 'assunto': adjunto
```

**Fala:**
> "No corretor ortográfico, 'nao' recebe as sugestões não, na e no; 'nda'
> recebe nada, na e da. E aqui está um ponto importante: mesmo para uma
> palavra correta, como 'assunto', o corretor pode sugerir 'adjunto' — é uma
> sugestão consultiva, não uma autoridade final. O projeto mostra isso em vez
> de esconder."

---

## 6. Rastreabilidade — 30 segundos

```bash
python exemplos/rastreabilidade.py
```

**Tela de referência** (saída real):

```
[Rastreabilidade] caminho mínimo até 'interpretação':
  diferença → marca → pontuação → texto → interpretação
```

**Fala:**
> "Todo conceito carrega o caminho até ele. Para chegar em 'interpretação', o
> motor mostra a cadeia real de dependências: diferença, marca, pontuação,
> texto, interpretação. Cada elo é uma dependência auditável, não uma citação
> solta."

Opcional, se quiser reforçar a regra de "nunca fingir" com o exemplo de
limite reconhecido também presente em `exemplo_publico.py`:

```
[Limitação reconhecida] entrada: '12:0'
  estado: DIVISÃO_POR_ZERO_NÃO_DEFINIDA_POR_CONSTRUÇÃO_PSF
```

> "E quando o motor não pode reconstruir algo — como divisão por zero — ele
> não finge um resultado nem lança um erro genérico. Marca como não definida
> por construção, de forma explícita."

---

## 7. Evidência — 30 segundos

```bash
python verificar_integridade.py
python -m pytest -q
```

**Fala:**
> "Isto roda a verificação de integridade e a suíte de testes automatizados.
> Nesta cópia do repositório, [dizer o número real de testes que passaram na
> gravação — a última verificação local marcou 1106 passed] — o número exato
> que aparecer na tela é o que vale, não este roteiro."

> ⚠️ Não repita "1106" de cor na narração final: rode os dois comandos no
> commit que será gravado e fale o número que a tela mostrar.

---

## 8. Encerramento — 20 segundos

**Tela:** `docs/LIMITES_OPERACIONAIS.md` e `ROADMAP.md`.

**Fala:**
> "O projeto documenta abertamente seus limites operacionais e o que ainda
> falta construir — isso está em LIMITES_OPERACIONAIS.md e no ROADMAP.md. Se
> quiser reproduzir, testar ou revisar tecnicamente, o código está aberto.
> Este vídeo não pede estrela como substituto de validação técnica — pede
> reprodução independente."

---

## Checklist antes de publicar

(mesma do `docs/ROTEIRO_VIDEO.md` — repetida aqui para conferência rápida)

- [ ] gravação corresponde ao commit indicado;
- [ ] nenhum token, e-mail privado, caminho pessoal ou conversa real aparece;
- [ ] todos os comandos foram executados na gravação (nada simulado);
- [ ] os números falados (testes, sugestões, resultados) batem com a tela;
- [ ] limitações aparecem, não apenas resultados positivos;
- [ ] legenda informa sistema operativo e versão do Python;
- [ ] link aponta para uma tag/release ou commit exato.
