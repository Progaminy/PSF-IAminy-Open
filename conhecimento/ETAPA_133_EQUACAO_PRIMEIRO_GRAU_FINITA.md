# PSF-IAminy — Etapa 133: Equação de primeiro grau finita

## Posição no fluxo natural

Esta etapa começa o bloco de expressões simbólicas, construído sobre corpo finito (etapa 94).

## Construção pura

Resolve ax+b=c de duas formas independentes: fórmula fechada x=(c-b)·a⁻¹ (usa o inverso multiplicativo do corpo, etapa 94) e busca exaustiva sobre a expressão (generaliza para qualquer expressão desta gramática, correta porque o domínio é finito e pequeno). As duas concordam sempre — testado, não assumido. Bónus: a busca exaustiva aplicada a x²+1=0 sobre Z/5Z reproduz exatamente as raízes {2,3} já achadas na etapa 103 — dois caminhos independentes, mesma resposta.

## Onde este bloco parava, de propósito

O próximo passo óbvio, entendido como fórmula real de segundo grau, precisava de raiz quadrada geral, e `reais.py` já documenta, com testes, que não cobre isso em tempo prático. Construir a fórmula real em cima disso continuaria prometendo mais do que o núcleo entrega.

A continuação correta ficou registrada depois: a etapa 135 resolve **equação quadrática finita por busca exaustiva**, sem fórmula real, discriminante real ou raiz quadrada geral.

## Dependências permitidas

- distinção; igualdade; domínio finito explícito; corpo (etapas 91-94);
- avaliação expressão;
- corpo finito.

## Dependências proibidas nesta etapa

- múltiplas variáveis; equações de grau >= 2; raízes gerais;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/expressoes_simbolicas_finitas.py` e validado em `testes/test_expressoes_simbolicas_finitas.py`.
