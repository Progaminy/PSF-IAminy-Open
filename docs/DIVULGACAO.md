# Divulgação técnica honesta

Estado: **texto reutilizável; nenhuma publicação externa é alegada aqui**.

## Descrição curta

> PSF-IAminy é uma investigação open source e local sobre construção
> rastreável de conhecimento em Matemática e Português. Resultados mostram
> dependências e limites; hipóteses e lacunas permanecem marcadas. O projeto é
> experimental, tem validação inicial e procura reprodução e crítica externa.

## Descrição técnica

O projeto implementa motores separados de Matemática e Português apoiados por
serviços comuns de memória, dependências, auditoria e rastreabilidade. A regra
central é não usar bibliotecas ou modelos externos como fundamento escondido:
eles podem comparar e medir, mas não decidir conhecimento puro.

Há instalação local, demonstrações executáveis, testes, cobertura, auditoria
de segurança, primeira comparação com SymPy e uma avaliação linguística que
expõe falsos positivos em vez de os ocultar. A CI pública ainda não ficou
verde, a release é candidata e não há reprodução independente documentada.

## Pedidos concretos à comunidade

- reproduzir instalação, integridade, demonstração e suíte num ambiente limpo;
- enviar um caso mínimo quando um resultado ou justificativa estiver errado;
- revisar a separação entre conhecimento, hipótese e validação externa;
- testar Português de diferentes variedades sem tratar uma amostra como norma
  universal;
- contribuir com documentação, regressões ou comparação externa isolada.

## Onde partilhar quando houver autorização humana

Comunidades Python, matemática computacional, linguística computacional,
educação, sistemas simbólicos, explicabilidade, código aberto e tecnologia
africana são públicos relevantes. Cada publicação deve ligar o commit ou a
release exata, indicar o estado experimental e evitar títulos que impliquem
IA geral, prova de completude ou validação por terceiros inexistente.

Respostas e feedback recebidos fora do repositório só devem ser registados
com consentimento e sem dados pessoais. Issues e discussões públicas devem
seguir `CODE_OF_CONDUCT.md` e `SECURITY.md`.
