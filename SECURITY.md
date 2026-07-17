# Política de Segurança

[English](docs/en/SECURITY.md)

A segurança, a integridade científica e a proteção de dados fazem parte dos princípios do PSF-IAminy-Open.

Versões suportadas

Atualmente, apenas a versão mais recente disponível na branch `main` recebe correções de segurança.

Como comunicar uma vulnerabilidade

Não publiques vulnerabilidades graves em issues públicas antes de permitir que o problema seja analisado e corrigido.

Para comunicar uma vulnerabilidade de forma responsável:

1. Acede ao separador **Security** deste repositório.
2. Procura a opção **Report a vulnerability**.
3. Descreve o problema, os ficheiros afetados e uma forma segura de reproduzi-lo.
4. Não incluas senhas, tokens, chaves, dados pessoais ou documentos privados.

Caso a opção de comunicação privada ainda não esteja disponível, abre uma issue contendo apenas uma descrição geral, sem revelar detalhes que permitam explorar a vulnerabilidade.

## Informações úteis no relatório

Inclui, quando possível:

* descrição clara do problema;
* componente ou ficheiro afetado;
* passos mínimos para reprodução;
* comportamento esperado;
* comportamento observado;
* impacto possível;
* versão do Python e do sistema operativo;
* proposta de correção, caso exista.

## Conteúdos sensíveis

Nunca publiques no repositório:

* senhas;
* tokens de acesso;
* chaves de API;
* credenciais do GitHub;
* dados pessoais;
* conversas privadas;
* documentos confidenciais;
* ficheiros da edição privada do PSF;
* conteúdos da pasta privada original;
* caminhos locais que revelem informações pessoais.

## Dependências externas

Dependências externas usadas para comparação, validação ou otimização devem ser verificadas antes da integração.

Não devem ser adicionadas dependências desconhecidas, abandonadas ou desnecessárias sem uma análise do risco.

## Integridade científica

Também são considerados problemas de integridade:

* apresentar capacidades inexistentes como concluídas;
* ocultar falhas removendo testes;
* transformar hipóteses em conhecimento validado sem evidência;
* adulterar resultados de testes ou avaliações;
* remover rastreabilidade para esconder a origem de uma conclusão;
* introduzir dependências externas como fundamento oculto do conhecimento PSF.

## Processo de correção

Depois de receber um relatório, o mantenedor poderá:

1. confirmar o problema;
2. avaliar o impacto;
3. preparar uma correção;
4. adicionar testes de regressão;
5. publicar a correção;
6. reconhecer o responsável pelo relatório, caso ele autorize.

Não existe garantia de prazo específico para a correção, pois o projeto é mantido de forma independente.

Uso responsável

O PSF-IAminy-Open é um projeto científico e experimental. Os utilizadores devem verificar resultados importantes de forma independente antes de utilizá-los em contextos críticos.
