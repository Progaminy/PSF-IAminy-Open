Como contribuir com o PSF-IAminy-Open

Obrigado pelo interesse em contribuir com o PSF-IAminy-Open.

O projeto investiga a construção rastreável de conhecimento matemático e linguístico pelo método PSF. Toda contribuição deve preservar a coerência, a transparência e a verificabilidade do sistema.

Antes de contribuir

1. Leia o `README.md`, o `PLANO_PSF_IAMINY.md` e as regras de integridade.
2. Verifique se já existe uma issue relacionada ao problema ou à proposta.
3. Para alterações grandes, abra primeiro uma issue explicando a ideia.
4. Não inclua dados privados, credenciais, conversas pessoais, chaves ou ficheiros temporários.

Princípios obrigatórios

* Não apresentar capacidades inexistentes como se estivessem concluídas.
* Diferenciar claramente conhecimento implementado, experimento, hipótese e trabalho futuro.
* Preservar a rastreabilidade das construções e decisões.
* Não introduzir dependências externas como fundamento oculto do conhecimento PSF.
* Dependências externas podem ser usadas para comparação, validação ou otimização quando isso estiver claramente identificado.
* Não remover testes ou verificações apenas para ocultar uma falha.
* Manter separadas as responsabilidades dos motores de Matemática, Português e do núcleo comum.
* Não adicionar conteúdo privado à pasta `privado/`.

Preparar o ambiente

Clone o repositório:

git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open

Execute os testes:

python -m pytest

Execute a verificação de integridade:

python verificar_integridade.py

Criar uma contribuição

Crie uma nova branch:

git checkout -b tipo/descricao-curta

Exemplos:

correcao/divisao-euclidiana
funcionalidade/analise-morfologica
documentacao/como-executar
teste/cobertura-primalidade

Faça alterações pequenas, coerentes e verificáveis.

Testes

Toda correção de erro deve, sempre que possível, incluir um teste que:

* demonstre o problema anterior;
* confirme o comportamento corrigido;
* não dependa de dados privados;
* possa ser executado por outros colaboradores.

Antes de enviar:

python -m pytest
python verificar_integridade.py

Commits

Use mensagens claras e objetivas.

Exemplos:

Corrige reconstrução da divisão euclidiana
Adiciona testes para concordância verbal
Documenta execução da interface local

Evite mensagens vagas como:

mudanças
ajustes
novo
teste

Pull requests

A descrição do pull request deve informar:

* o problema tratado;
* a solução aplicada;
* os ficheiros principais alterados;
* os testes executados;
* limitações conhecidas;
* possíveis efeitos sobre outras partes do sistema.

Não afirme que uma funcionalidade está completa se os testes ou a implementação ainda forem parciais.

Hipóteses e investigação

Hipóteses matemáticas, linguísticas ou computacionais devem ser identificadas explicitamente como hipóteses.

Uma hipótese não deve ser incorporada como conhecimento validado antes de passar por análise, tentativa de falsificação, comparação e testes reproduzíveis.

Segurança

Não publique:

* senhas;
* tokens;
* chaves de API;
* endereços privados;
* dados pessoais;
* documentos confidenciais;
* ficheiros da edição privada do projeto.

Caso encontre uma vulnerabilidade ou exposição de dados, não a divulgue publicamente antes de permitir uma correção responsável.

Licença

Ao enviar uma contribuição, você concorda que ela poderá ser distribuída sob a Apache License 2.0, adotada por este repositório.
