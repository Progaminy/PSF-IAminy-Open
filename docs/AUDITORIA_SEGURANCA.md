# Auditoria de segurança

Complemento automatizado: `docs/ANALISE_ESTATICA.md` regista Bandit 1.9.4 com
11 alertas baixos, 0 médios e 0 altos, além da triagem de cada classe.

Auditoria manual do código do pacote principal (excluindo `cao_de_caca/PSF-Calculadora`, subprojeto externo com seu próprio ciclo), item 22/23 do plano de melhorias públicas. Não é uma auditoria de terceiros nem certificação — é o que foi verificado, o que foi corrigido e o que continua sendo hipótese de risco não testada.

## O que foi verificado

| Item | Resultado |
| --- | --- |
| `eval`/`exec` | Nenhuma ocorrência no pacote principal. |
| `subprocess`/`os.system` | Só em `motor/execucao.py`, para rodar a própria suíte de testes (`sys.executable` + lista fixa de argumentos, `shell=False`, caminhos vindos de `Path.glob()` no próprio repositório — nunca de entrada externa). |
| `pickle`/`yaml.load` (desserialização insegura) | Nenhuma ocorrência. |
| Chamadas de rede de saída | Nenhuma no pacote principal — confirmado por busca textual, não apenas por leitura de docstring. |
| Ficheiros estáticos servidos pela interface HTTP | `interface/roteador.py::arquivo_estatico` resolve o caminho absoluto e confere que continua dentro da pasta permitida antes de servir — já coberto por `testes/test_interface_e2e_http.py::test_arquivo_fora_da_pasta_estatica_fica_bloqueado`. |
| Renderização de mensagens de chat no frontend | `interface/estatico/app.js` usa `.textContent` (nunca `.innerHTML`) para o texto de mensagens do utilizador/assistente — sem risco de injeção HTML/JS pelo conteúdo da conversa. `.innerHTML` só é usado para ícones estáticos definidos no próprio código, nunca com dado de utilizador. |

## O que foi encontrado e corrigido nesta auditoria

### 1. Travessia de caminho em `interface/conversas.py` (severidade: alta)

`id_conversa`, vindo direto da URL (`/api/conversas/{id}`), era concatenado sem validação em `self.pasta / f"{id_conversa}.json"`. Um `id_conversa` como `"../arquivo_sensivel"` permitia:

- **leitura** de qualquer `.json` alcançável por travessia relativa a partir da pasta de conversas (`GET /api/conversas/../arquivo_sensivel`);
- **apagamento** de qualquer `.json` alcançável do mesmo jeito (`DELETE /api/conversas/../arquivo_sensivel`).

Confirmado explorável de verdade antes da correção (não só teoricamente): rodar `ArmazemConversas.carregar("../arquivo_sensivel")`/`.remover(...)` contra um ficheiro-irmão real leu e apagou o ficheiro de fato.

**Corrigido**: `_caminho()` agora exige que `id_conversa` bata exatamente no formato produzido por `secrets.token_hex(6)` (12 caracteres hexadecimais minúsculos); qualquer outra coisa é tratada como conversa inexistente, antes de qualquer operação de ficheiro. Testes de regressão em `testes/test_seguranca_conversas.py` (12 testes, confirmados falhando contra o código anterior à correção).

### 2. Sem limite de tamanho de corpo em `interface/servidor.py` (severidade: baixa/moderada)

`Manipulador._corpo_json()` lia `self.rfile.read(tamanho)` usando o `Content-Length` declarado pelo cliente, sem limite algum — um `Content-Length` forjado e enorme faria o servidor tentar ler um corpo arbitrariamente grande antes de qualquer validação.

**Corrigido**: `TAMANHO_MAXIMO_CORPO = 1_000_000` (1 MB); acima disso, `413` sem tocar em `rfile.read`. Teste de regressão em `testes/test_seguranca_servidor.py`.

### 3. Anexos ZIP/DOCX sem limites defensivos (severidade: moderada)

`ensino/leitura_documentos.py` abria ZIP/DOCX e lia as entradas suportadas sem
teto de tamanho compactado, quantidade de entradas, tamanho descomprimido ou
razão de compactação. Mesmo sem extrair em disco, um arquivo hostil poderia
consumir CPU/memória de forma desproporcional; nomes internos perigosos também
eram devolvidos ao chamador sem validação.

**Corrigido**: 32 MiB compactados, 512 entradas, 16 MiB por entrada, 64 MiB
de total declarado e razão máxima 200:1 a partir de 1 MiB. Caminhos absolutos,
travessia `..`, separador Windows ambíguo e nomes duplicados são rejeitados.
A leitura de cada entrada também para em 16 MiB, mesmo depois da validação dos
metadados, e um DOCX dentro de ZIP passa pela mesma política. Há 18 regressões
em `testes/test_seguranca_leitura_documentos.py`.

## O que continua como risco não testado (honesto, não escondido)

- A interface HTTP (`python3 -m interface.servidor`) não tem autenticação nem HTTPS — assume-se uso local (`127.0.0.1`), documentado em `COMO_RODAR.md`. Expor isto publicamente sem uma camada própria de autenticação/proxy reverso não é recomendado e não foi testado.
- `cao_de_caca/PSF-Calculadora` (dependências científicas de terceiros abusadas de propósito) não foi auditado nesta rodada — é um subprojeto externo com ciclo de vida próprio.
- Não houve execução de ferramenta automatizada de análise de dependências vulneráveis (`pip-audit`) nesta rodada — o pacote principal não tem dependências de terceiros em runtime (só `pytest`/`pytest-cov`/`ruff`/`bandit` como dev, declarados em `pyproject.toml`), o que reduz mas não elimina a necessidade dessa verificação no futuro.
- Bandit roda no CI (`.github/workflows/ci.yml`, job `qualidade`): severidade média/alta é bloqueante e o relatório completo de alertas baixos é informativo. Isso não substitui esta auditoria manual nem revisão externa.
