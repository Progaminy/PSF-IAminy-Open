# Classificação e qualidade dos testes

## Inventário reproduzível

Em 17 de julho de 2026, `pytest --collect-only -q` recolheu 1106 casos em 110
ficheiros. `python3 ferramentas/classificar_testes.py` reproduz a classificação
abaixo a partir da coleta real:

| Categoria | Testes | Ficheiros |
| --- | ---: | ---: |
| Ensino e exercícios | 319 | 4 |
| Integridade e auditoria | 32 | 7 |
| Integração e motores | 66 | 8 |
| Interface | 55 | 6 |
| Matemática e estruturas finitas | 310 | 55 |
| Português | 289 | 27 |
| Segurança | 35 | 3 |
| **Total** | **1106** | **110** |

A unidade de classificação é o ficheiro, seguindo regras explícitas no script.
Um ficheiro pode exercitar mais de uma camada; portanto, as categorias indicam
finalidade dominante, não uma taxonomia científica perfeita. O ficheiro de
recursos de instalação é classificado em Matemática pela heurística de nomes;
seu conteúdo real é de empacotamento/integração, exemplo de limite conhecido da
classificação automática.

## Tipos de evidência

- **Unitária:** função ou estrutura isolada, sobretudo nos ficheiros de
  Matemática e Português.
- **Integração:** comunicação entre motores, correção integrada, empacotamento
  e validação auxiliar.
- **Interface:** rotas HTTP, páginas, navegação, mapas e contraste.
- **Segurança/regressão:** travessia de caminhos, limite de corpo HTTP,
  anexos hostis e comportamentos que não podem regressar.
- **Integridade estrutural:** pontes, pureza, coerência documental e cobertura
  declarada.
- **Científica finita:** exemplos, bordas e busca exaustiva dentro do domínio
  construído; não equivale a prova universal fora dele.

## Concentração e profundidade

O total bruto superestima diversidade quando parametrização gera muitos casos.
`testes/test_exercicio_real.py` sozinho contém 291 casos coletados (26,3% da
suíte), gerados sobre conceitos e sementes. Isso é útil para amplitude de
exercícios, mas não vale como 291 comportamentos arquiteturalmente distintos.

Passar 1106 casos também não prova:

- ausência de duplicação semântica entre asserções;
- qualidade de cada oráculo esperado;
- cobertura dos módulos sem testes;
- correção fora dos domínios finitos declarados;
- reprodução em outro sistema ou por outra pessoa.

## Auditoria sintática de profundidade mínima

`python3 ferramentas/auditar_testes.py` inspeciona a AST dos 110 ficheiros,
sem executar o código. Resultado de 17 de julho de 2026:

```text
778 funções test_*
1544 instruções assert
80 usos de pytest.raises
0 funções sem assert/pytest.raises explícito
0 grupos de corpos AST exatamente duplicados
0 ficheiros com erro de sintaxe
```

Os 778 corpos geram 1106 casos coletados porque parametrizações expandem uma
função em várias entradas. O resultado exclui a forma mais superficial de
teste (só importar/chamar sem evidência explícita) e duplicação textual exata.
Ele não detecta asserções semanticamente equivalentes escritas de outra forma,
oráculos fracos, duplicação de dados parametrizados nem código de produção que
contenha a verdadeira verificação fora da função de teste.

## Execução integral atual

```text
Python 3.13.5
1106 passed in 182.28s (0:03:02)
```

A medição anterior de 1103 testes em Python 3.14.4 foi mais rápida; versão do
interpretador, carga, cache e testes adicionados impedem atribuir a diferença a
uma regressão sem uma comparação controlada.

## Próxima auditoria

1. medir duplicação semântica por conjunto de entradas e oráculos;
2. revisar força das asserções, mesmo quando existem explicitamente;
3. ligar cada capacidade pública a pelo menos um teste de resultado e borda;
4. marcar regressões com o erro real que motivou o caso;
5. priorizar módulos críticos com baixa cobertura, conforme `docs/COBERTURA.md`.

Essa auditoria deve reduzir números enganosos, não apagar testes apenas para
obter uma distribuição mais bonita.
