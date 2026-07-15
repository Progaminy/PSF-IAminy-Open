# PSF-IAminy — Marcador histórico 1061: equivalência entre leis geradoras

## Construção pura

Liga `lei geradora aproximação real` (ETAPA 1035), que deixou expresso
que "equivalência entre leis diferentes, operações preservadas entre
leis, ordem entre leis e a prova de completude continuam pendentes" —
este é o primeiro desses quatro. Duas leis geradoras (regras
computáveis passo→intervalo, possivelmente algoritmos completamente
diferentes) representam o mesmo número real quando, para qualquer erro
racional positivo, seus intervalos refinados ficam arbitrariamente
próximos.

```text
lei geradora aproximação real (ETAPA 1035)
→ dado epsilon > 0: refina lei1 e lei2 até largura <= epsilon/2 cada
→ se os dois intervalos resultantes se sobrepõem: consistente até epsilon
→ se não se sobrepõem: prova definitiva de que NÃO são a mesma lei
```

A assimetria é deliberada e honesta: provar igualdade para **todo**
epsilon exigiria verificar um número infinito de valores, o que nenhum
PSF finito faz — por isso o resultado `True` é rotulado como evidência
"até esse epsilon", nunca como prova de igualdade absoluta. Já o
resultado `False` é definitivo e finito: se os dois intervalos
refinados não se tocam, nenhum valor real cabe nos dois ao mesmo tempo,
então as leis não podem gerar o mesmo número — essa metade da pergunta
tem prova completa, a outra não.

Para testar a construção contra algo genuíno (não só a lei comparada
consigo mesma, caso trivial), este módulo constrói uma segunda lei
geradora da mesma raiz quadrada por **bisseção**: convergência linear
(largura cai pela metade a cada passo), estruturalmente diferente do
Newton quadrático da ETAPA 1035, mas convergindo para o mesmo valor —
prova de que a equivalência é detectada mesmo entre algoritmos
diferentes, não só entre uma lei e ela mesma.

## Dependências permitidas

- lei geradora aproximação real

## Implementação

```text
nucleo/equivalencia_leis_geradoras.py
```

## Validação

```text
testes/test_equivalencia_leis_geradoras.py
```

## Estado

Equivalência entre leis geradoras construída e testada: uma lei
consistente consigo mesma (caso trivial), Newton e bisseção convergindo
para a mesma raiz de 2 (algoritmos diferentes, mesmo valor — o caso não
trivial), e raiz de 2 versus raiz de 3 definitivamente distinguidas
(prova de não-equivalência, não evidência). Operações preservadas entre
leis, ordem entre leis e a prova de completude (propriedade do supremo)
continuam como próximo alvo dentro do mesmo item do plano.
