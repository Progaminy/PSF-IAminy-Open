// PSF-IAminy — chat, vanilla JS, sem framework nem CDN.
(() => {
  "use strict";

  const elMensagens = document.getElementById("mensagens");
  const elBoasVindas = document.getElementById("boas-vindas");
  const elListaConversas = document.getElementById("lista-conversas");
  const elFormEntrada = document.getElementById("form-entrada");
  const elCampoTexto = document.getElementById("campo-texto");
  const elBtnEnviar = document.getElementById("btn-enviar");
  const elBtnAnexar = document.getElementById("btn-anexar");
  const elInputArquivo = document.getElementById("input-arquivo");
  const elBtnLateral = document.getElementById("btn-lateral");
  const elLateral = document.getElementById("lateral");
  const elBtnNovaConversa = document.getElementById("btn-nova-conversa");
  const elBtnCopiarConversa = document.getElementById("btn-copiar-conversa");
  const elAtalhosChat = document.getElementById("atalhos-chat");

  let idConversaAtual = null;

  // ------------------------------------------------------------------
  // Utilidades
  // ------------------------------------------------------------------

  async function pedirJSON(caminho, opcoes) {
    const resposta = await fetch(caminho, opcoes);
    const corpo = await resposta.json().catch(() => ({}));
    if (!resposta.ok) {
      throw new Error(corpo.erro || `pedido falhou (${resposta.status})`);
    }
    return corpo;
  }

  function arquivoParaBase64(arquivo) {
    return new Promise((resolve, reject) => {
      const leitor = new FileReader();
      leitor.onload = () => {
        const resultado = leitor.result;
        const base64 = resultado.substring(resultado.indexOf(",") + 1);
        resolve(base64);
      };
      leitor.onerror = () => reject(leitor.error);
      leitor.readAsDataURL(arquivo);
    });
  }

  function textoPublico(texto) {
    return String(texto)
      .replace(/\b(?:ETAPA|Etapa|etapa)[_\-\s]*\d+[A-Za-z0-9_\-\s/]*/g, "registro interno")
      .replace(/\b[Ee]tapas\b/g, "registros internos")
      .replace(/\b[Ee]tapa\b/g, "registro interno");
  }

  async function copiarTexto(texto, botao) {
    try {
      await navigator.clipboard.writeText(texto);
    } catch (erro) {
      // sem permissão/API de clipboard (ex.: contexto não seguro) --
      // fallback silencioso: seleciona um textarea temporário.
      const area = document.createElement("textarea");
      area.value = texto;
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      document.body.removeChild(area);
    }
    if (botao) {
      const original = botao.innerHTML;
      botao.textContent = "✓";
      setTimeout(() => { botao.innerHTML = original; }, 1200);
    }
  }

  // ------------------------------------------------------------------
  // Renderização
  // ------------------------------------------------------------------

  function iconeCopiar() {
    return (
      '<svg viewBox="0 0 24 24" width="14" height="14">' +
      '<rect x="8" y="8" width="12" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>' +
      '<path d="M4 16V5a1 1 0 0 1 1-1h11" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>' +
      "</svg>"
    );
  }

  function iconeRenomear() {
    return (
      '<svg viewBox="0 0 24 24" width="13" height="13">' +
      '<path d="M12 20h9" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>' +
      '<path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/>' +
      "</svg>"
    );
  }

  function iconeApagar() {
    return (
      '<svg viewBox="0 0 24 24" width="13" height="13">' +
      '<path d="M4 7h16M9 7V4h6v3M6 7l1 13a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-13" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' +
      "</svg>"
    );
  }

  function renderizarMensagem(mensagem) {
    const linha = document.createElement("div");
    linha.className = "mensagem " + (mensagem.papel === "assistente" ? "assistente" : "aluno");

    const interior = document.createElement("div");
    interior.className = "mensagem-interior";

    const cabecalho = document.createElement("div");
    cabecalho.className = "mensagem-cabecalho";

    const papel = document.createElement("span");
    papel.className = "papel";
    papel.textContent = mensagem.papel === "assistente" ? "PSF-IAminy" : "Tu";

    const botaoCopiar = document.createElement("button");
    botaoCopiar.className = "icone-botao copiar-mensagem";
    botaoCopiar.innerHTML = iconeCopiar();
    botaoCopiar.title = "Copiar esta mensagem";
    botaoCopiar.type = "button";
    botaoCopiar.addEventListener("click", () => copiarTexto(textoPublico(mensagem.texto), botaoCopiar));

    cabecalho.appendChild(papel);
    cabecalho.appendChild(botaoCopiar);

    const corpo = document.createElement("div");
    corpo.className = "mensagem-corpo";
    corpo.textContent = mensagem.papel === "assistente" ? textoPublico(mensagem.texto) : mensagem.texto;

    interior.appendChild(cabecalho);
    interior.appendChild(corpo);
    linha.appendChild(interior);
    return linha;
  }

  function renderizarConversa(conversa) {
    elMensagens.innerHTML = "";
    if (!conversa.mensagens.length) {
      elMensagens.appendChild(elBoasVindas);
      return;
    }
    for (const mensagem of conversa.mensagens) {
      elMensagens.appendChild(renderizarMensagem(mensagem));
    }
    elMensagens.scrollTop = elMensagens.scrollHeight;
  }

  function adicionarMensagemNaTela(mensagem) {
    if (elMensagens.contains(elBoasVindas)) {
      elMensagens.innerHTML = "";
    }
    elMensagens.appendChild(renderizarMensagem(mensagem));
    elMensagens.scrollTop = elMensagens.scrollHeight;
  }

  async function renderizarListaConversas() {
    const { conversas } = await pedirJSON("/api/conversas");
    elListaConversas.innerHTML = "";
    for (const conversa of conversas) {
      const linha = document.createElement("div");
      linha.className = "item-conversa-linha" + (conversa.id === idConversaAtual ? " ativa" : "");

      const botao = document.createElement("button");
      botao.type = "button";
      botao.className = "item-conversa";
      botao.textContent = conversa.titulo;
      botao.title = conversa.titulo;
      botao.addEventListener("click", () => abrirConversa(conversa.id));

      const botaoRenomear = document.createElement("button");
      botaoRenomear.type = "button";
      botaoRenomear.className = "item-conversa-acao";
      botaoRenomear.innerHTML = iconeRenomear();
      botaoRenomear.title = "Renomear conversa";
      botaoRenomear.setAttribute("aria-label", "Renomear conversa: " + conversa.titulo);
      botaoRenomear.addEventListener("click", (evento) => {
        evento.stopPropagation();
        renomearConversa(conversa.id, conversa.titulo);
      });

      const botaoApagar = document.createElement("button");
      botaoApagar.type = "button";
      botaoApagar.className = "item-conversa-acao";
      botaoApagar.innerHTML = iconeApagar();
      botaoApagar.title = "Apagar conversa";
      botaoApagar.setAttribute("aria-label", "Apagar conversa: " + conversa.titulo);
      botaoApagar.addEventListener("click", (evento) => {
        evento.stopPropagation();
        apagarConversa(conversa.id, conversa.titulo);
      });

      const acoes = document.createElement("div");
      acoes.className = "item-conversa-acoes";
      acoes.appendChild(botaoRenomear);
      acoes.appendChild(botaoApagar);

      linha.appendChild(botao);
      linha.appendChild(acoes);
      elListaConversas.appendChild(linha);
    }
  }

  // ------------------------------------------------------------------
  // Ações
  // ------------------------------------------------------------------

  async function criarNovaConversa() {
    const conversa = await pedirJSON("/api/conversas", { method: "POST" });
    idConversaAtual = conversa.id;
    renderizarConversa(conversa);
    await renderizarListaConversas();
    elCampoTexto.focus();
  }

  async function abrirConversa(id) {
    const conversa = await pedirJSON(`/api/conversas/${id}`);
    idConversaAtual = conversa.id;
    renderizarConversa(conversa);
    await renderizarListaConversas();
  }

  async function renomearConversa(id, tituloAtual) {
    const novoTitulo = window.prompt("Novo título da conversa:", tituloAtual);
    if (novoTitulo === null) return;
    const limpo = novoTitulo.trim();
    if (!limpo || limpo === tituloAtual) return;
    await pedirJSON(`/api/conversas/${id}/titulo`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo: limpo }),
    });
    await renderizarListaConversas();
  }

  async function apagarConversa(id, titulo) {
    // "de verdade": chama o DELETE real (apaga o ficheiro no disco, ver
    // interface/conversas.py::remover) -- não é só esconder da lista.
    const confirmado = window.confirm(`Apagar "${titulo}"? Isto é permanente e não pode ser desfeito.`);
    if (!confirmado) return;
    await pedirJSON(`/api/conversas/${id}`, { method: "DELETE" });
    if (id === idConversaAtual) {
      idConversaAtual = null;
      renderizarConversa({ mensagens: [] });
    }
    await renderizarListaConversas();
  }

  async function garantirConversa() {
    if (!idConversaAtual) {
      const conversa = await pedirJSON("/api/conversas", { method: "POST" });
      idConversaAtual = conversa.id;
    }
    return idConversaAtual;
  }

  async function enviarTextoDireto(texto) {
    const id = await garantirConversa();
    adicionarMensagemNaTela({ papel: "aluno", texto });
    const pendente = { papel: "assistente", texto: "…" };
    adicionarMensagemNaTela(pendente);
    try {
      const conversa = await pedirJSON(`/api/conversas/${id}/mensagens`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto }),
      });
      renderizarConversa(conversa);
    } catch (erro) {
      renderizarErro(erro);
    }
    await renderizarListaConversas();
  }

  function renderizarErro(erro) {
    adicionarMensagemNaTela({ papel: "assistente", texto: `Ocorreu um erro: ${erro.message}` });
  }

  async function enviarMensagemDoFormulario(evento) {
    evento.preventDefault();
    const texto = elCampoTexto.value.trim();
    if (!texto) return;
    elCampoTexto.value = "";
    ajustarAlturaTextarea();
    elBtnEnviar.disabled = true;
    try {
      await enviarTextoDireto(texto);
    } finally {
      elBtnEnviar.disabled = false;
      elCampoTexto.focus();
    }
  }

  async function anexarArquivo(arquivo) {
    const id = await garantirConversa();
    adicionarMensagemNaTela({ papel: "aluno", texto: `[anexo: ${arquivo.name}]` });
    adicionarMensagemNaTela({ papel: "assistente", texto: "A ler o anexo…" });
    try {
      const conteudoBase64 = await arquivoParaBase64(arquivo);
      const conversa = await pedirJSON(`/api/conversas/${id}/anexos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome: arquivo.name, conteudo_base64: conteudoBase64 }),
      });
      renderizarConversa(conversa);
    } catch (erro) {
      renderizarErro(erro);
    }
    await renderizarListaConversas();
  }

  function ajustarAlturaTextarea() {
    elCampoTexto.style.height = "auto";
    elCampoTexto.style.height = Math.min(elCampoTexto.scrollHeight, 160) + "px";
  }

  async function copiarConversaInteira() {
    if (!idConversaAtual) return;
    const conversa = await pedirJSON(`/api/conversas/${idConversaAtual}`);
    const texto = conversa.mensagens
      .map((m) => `${m.papel === "assistente" ? "PSF-IAminy" : "Tu"}: ${m.papel === "assistente" ? textoPublico(m.texto) : m.texto}`)
      .join("\n\n");
    await copiarTexto(texto, elBtnCopiarConversa);
  }

  // ------------------------------------------------------------------
  // Ligações de eventos
  // ------------------------------------------------------------------

  elFormEntrada.addEventListener("submit", enviarMensagemDoFormulario);
  elCampoTexto.addEventListener("input", ajustarAlturaTextarea);
  elCampoTexto.addEventListener("keydown", (evento) => {
    if (evento.key === "Enter" && !evento.shiftKey) {
      evento.preventDefault();
      elFormEntrada.requestSubmit();
    }
  });

  elBtnAnexar.addEventListener("click", () => elInputArquivo.click());
  elInputArquivo.addEventListener("change", () => {
    const arquivo = elInputArquivo.files[0];
    elInputArquivo.value = "";
    if (arquivo) anexarArquivo(arquivo);
  });

  elBtnLateral.addEventListener("click", () => elLateral.classList.toggle("recolhida"));
  elBtnNovaConversa.addEventListener("click", criarNovaConversa);
  elBtnCopiarConversa.addEventListener("click", copiarConversaInteira);
  elAtalhosChat.querySelectorAll("button[data-text]").forEach((botao) => {
    botao.addEventListener("click", () => enviarTextoDireto(botao.dataset.text));
  });

  // ------------------------------------------------------------------
  // Arranque
  // ------------------------------------------------------------------

  renderizarListaConversas();
})();
