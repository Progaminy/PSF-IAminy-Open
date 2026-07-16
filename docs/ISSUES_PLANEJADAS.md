# Issues planejadas

Em 17 de julho de 2026, o repositório público não possuía issues. A tentativa
de criar as seis abaixo pela integração GitHub recebeu HTTP 403 (`Resource not
accessible by integration`) e o push HTTPS da branch local não encontrou
credencial. Portanto, **nenhuma destas issues está publicada ainda**.

## Publicar CI e preparar release v0.1.0

- publicar a branch de preparação por PR;
- obter CI verde em Python 3.10–3.13;
- repetir integridade, demonstração e suíte no commit candidato;
- fechar changelog, testar tag em ambiente limpo e publicar notas reais.

## Reduzir falsos positivos do corretor de Português

- criar corpus versionado de válidos/erros por variedade e fenómeno;
- medir precisão, revocação e falsos positivos;
- corrigir `assunto`, `comprimento`, `sala` e `medido` sem degradar os erros-alvo;
- manter sugestões consultivas enquanto a qualidade for parcial.

## Investigar limite de desempenho da multiplicação PSF

- perfilar racionalização/MDC por retirada;
- explicar `20*20` concluído versus `99*99` acima de dez segundos;
- otimizar preservando construção e rastreabilidade;
- comparar antes/depois e criar regressões.

## Ampliar validação externa

- expandir casos matemáticos independentemente;
- escolher referência linguística adequada;
- guardar versões, critérios, resultados e divergências;
- manter validadores fora do fundamento PSF.

## Reproduzir em outros sistemas e por terceiro

- repetir em outra máquina Linux, Windows e macOS;
- validar versões Python declaradas;
- obter relato independente com commit, comandos e resultado.

## Reduzir dívida de análise estática gradualmente

- bloquear primeiro sintaxe, nomes indefinidos e chaves duplicadas;
- revisar imports/exportações e variáveis sem uso por módulo;
- tornar novos alertas Bandit médios/altos bloqueantes;
- não aplicar autofix massivo sobre notação matemática histórica.

Antes de publicar, deve-se pesquisar novamente por duplicados. Depois, cada
commit correspondente deve mencionar o número real atribuído pelo GitHub.

