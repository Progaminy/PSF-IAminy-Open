# Inventário de dependências

Inventário do pacote principal. O subprojeto independente
`cao_de_caca/PSF-Calculadora` mantém dependências próprias no seu
`pyproject.toml` e não participa do conhecimento puro.

## Execução

Não há dependência obrigatória de terceiros. Os motores, a interface local e
os exemplos usam a biblioteca padrão do Python.

| Dependência | Uso | Versão declarada | Obrigatória | Participa do conhecimento puro | Risco principal |
| --- | --- | --- | --- | --- | --- |
| Python | execução | `>=3.10` | sim | é o ambiente, não fonte de verdade | diferenças entre versões e plataformas |
| biblioteca padrão | ficheiros, HTTP local, JSON, estruturas e CLI | acompanha Python | sim | mecanismo técnico; não autoridade externa | mudanças de comportamento entre versões |

## Build e desenvolvimento

| Dependência | Uso | Restrição atual | Obrigatória para executar | Licença a confirmar antes da release | Risco principal |
| --- | --- | --- | --- | --- | --- |
| setuptools | construir/instalar o pacote e metadados PEP 639 | `>=77` | só para build/instalação | sim | limite superior aberto pode alterar builds futuros |
| build | frontend de construção do wheel no CI | versão mais recente resolvida pelo pip | só para build | sim | mudança futura do frontend |
| pytest | executar testes | sem versão fixada | não | MIT indicada pelos metadados do ambiente | atualização incompatível da suíte |
| pytest-cov | medir cobertura | sem versão fixada | não | sim | métrica variar conforme ferramenta/configuração |
| Ruff | análise estática crítica + dívida informativa | `0.15.22` no CI | não | sim | atualizar exige rever a linha de base |
| Bandit | padrões de segurança; médio/alto bloqueante | `1.9.4` no CI | não | sim | falsos positivos/negativos e regras variáveis |

Pytest, pytest-cov, setuptools e build ainda não estão totalmente bloqueados nesta pré-release; Ruff e Bandit estão fixos no CI para tornar a linha de base estática comparável. Antes de
publicar uma release reproduzível, deve-se registar as versões usadas na
validação e confirmar licença e origem em fontes oficiais. Fixar versões sem
processo de atualização também criaria risco de vulnerabilidades antigas.

## Dependências externas como validação

Ferramentas como SymPy ou corretores conhecidos podem ser adicionadas no
futuro a um ambiente de validação separado. Elas nunca devem decidir ou
materializar conhecimento puro. Qualquer inclusão deve declarar finalidade,
versão, licença, dados enviados, comportamento offline e divergências
encontradas.

Primeira ferramenta efetivamente usada nesse ambiente separado:

| Dependência | Uso | Versão medida | Licença indicada pelos metadados | Obrigatória |
| --- | --- | --- | --- | --- |
| SymPy | comparar sete resultados em `avaliacoes/comparar_sympy.py` | 1.14.0 | BSD | não; apenas validação externa |

O script informa `BLOQUEADO_SYMPY_AUSENTE` e termina sem tocar no motor quando
a dependência opcional não está instalada.

## Processo de mudança

Uma nova dependência exige:

1. finalidade que a biblioteca padrão não cubra adequadamente;
2. separação explícita entre execução, desenvolvimento e validação;
3. licença compatível e manutenção ativa verificadas;
4. análise de segurança e privacidade;
5. teste reproduzível e entrada no changelog;
6. confirmação de que não virou fundamento oculto do PSF.
