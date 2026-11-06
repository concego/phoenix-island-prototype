# Guia de desenvolvimento com IA — Phoenix Island

Este documento orienta o trabalho de agentes de IA neste repositório. Não substitui decisões de Anderson, o código nem os documentos de referência.

## Antes de começar

Leia `AGENTS.md`, `GDD.md`, `LORE.md`, `VISUAL_DIRECTION.md`, o `README.md` da raiz e as partes relevantes de `DEVLOG.md`. Inspecione o código relacionado ao pedido antes de propor ou fazer mudanças. O ponto de entrada principal do protótipo é `index.html`; a página usa Three.js como módulo ES e os efeitos sonoros ficam em `assets/`.

Entenda a diferença entre:

- **Decisão aprovada:** regra de design ou narrativa registrada por Anderson.
- **Implementado:** comportamento encontrado no código.
- **Documentado:** comportamento descrito no README ou nos demais documentos.
- **Verificado:** conferido por revisão estática ou execução, informando qual delas.
- **Testado/aprovado pelo usuário:** efetivamente experimentado e relatado por Anderson. Não inferir a partir de uma revisão de código ou de uma publicação.

## Delimite o pedido

1. Identifique exatamente o comportamento pedido e os arquivos que podem ser afetados.
2. Confira regras existentes, controles, alvos, prioridades, alcance, inventário, mensagens, áudio e outras dependências próximas.
3. Não amplie o escopo com melhorias não solicitadas. Ideias adicionais devem ser apresentadas separadamente e aguardar aprovação.
4. Se houver ambiguidade ou faltar uma decisão que altere o resultado, pare antes da implementação e pergunte a Anderson no chat. Não use convenções de gênero, realismo ou facilidade técnica para preencher lacunas.
5. Recursos consumidos, transformados ou removidos precisam ter resultado intencional; falhas não devem consumir recursos inadvertidamente.

## Regras específicas do projeto

- O protótipo atual usa Three.js no navegador para testes; o jogo final será compilado e o formato/plataforma ainda não está definido. Não trate o navegador como destino final. O desenvolvimento vigente é na branch `main`; a migração para Godot foi descartada.
- Não proponha TTS embutido ou outra assistência a pessoas cegas como solução garantida: Anderson relata que as alternativas sugeridas até agora e o TTS embutido não ajudam. Não prometa solução sem validação dele.
- O protótipo ainda está no estágio básico e não tem menu. A prioridade é implementar, testar, validar e aprimorar as mecânicas. Não antecipar o menu nem as opções de apresentação/acessibilidade; depois que o protótipo sair do estágio básico, integrar o menu ao início do jogo e incluir nele essas opções. Esc pode fechar/voltar dos painéis existentes de inventário e ações contextuais, mas não mostre aviso para pressioná-lo nem inclua a tecla nos rótulos de botão. Não deve abrir menu de pausa nem receber outra função nesta fase; F1 permanece sem função.
- Não exibir controles, listas de teclas, instruções ou lembretes na interface de jogo nesta fase. Tutorial e menu de ajuda não estão em uso; controles só podem ser exibidos se futuramente forem explicitamente requeridos como conteúdo de tutorial ou ajuda aprovada. O alvo visual da cena de teste é ocupar a tela sem cabeçalho/moldura que a faça parecer um site. O único texto visível no jogo atual são mensagens breves de feedback das ações do jogador; não exibir títulos, controles, instruções, lembretes, descrições persistentes nem texto decorativo.
- O objetivo de inclusão considera pessoas com diferentes necessidades, não apenas pessoas cegas. Não presuma que um único canal sensorial ou modo de controle sirva para todas.
- A lore em `LORE.md` é planejada. Não converter os elementos ainda indefinidos em fatos canônicos nem inseri-los no protótipo sem solicitação.
- A duração de combustível aprovada para a fogueira simples é 180 segundos (3 minutos). O texto do menu que diz “1 minuto” está incorreto. Corrija a descrição quando a alteração de documentação/interface estiver autorizada; não mude os 180 segundos para coincidir com o texto errado.
- Não altere releases, tags, backups ou versão oficial sem autorização explícita.

## Direção visual e diagnósticos

Siga `VISUAL_DIRECTION.md` como direção de longo prazo para o jogo inteiro; o mapa de teste atual é apenas seu primeiro caso de aplicação. Para capturas e observações específicas, consulte os registros datados em `testes/capturas/`. Não trate as bordas, abas, barra de endereço, notificações do sistema ou janelas de downloads como parte da interface do jogo. Não infira a aparência de uma área inteira a partir de um único enquadramento.

Quando Anderson enviar prints, acrescente os arquivos à pasta de captura correspondente e anote contexto, ponto de vista fornecido por ele, observações visuais, incertezas e áreas não visíveis. Não atribua causa técnica sem verificar. Um diagnóstico não é autorização para implementar; em tarefas só de documentação/análise, não altere código.

Nesta fase, não exibir controles ou instruções visíveis; o único texto visível permitido no jogo é feedback breve das ações do jogador. Se uma tela existente violar essa regra, documente a divergência e deixe a mudança de código para a conversa de desenvolvimento/autorização explícita.

## Implementação e validação

- Faça mudanças focadas e preserve mecânicas independentes já aprovadas.
- Ao mexer em geometria, altura ou seleção de alvos, verifique efeitos sobre colisão, alcance, oclusão, coleta, escalada, locomoção e descrição acessível.
- A informação necessária à interação não pode depender exclusivamente de visão ou de um som ambíguo. Preserve a navegação por teclado e os anúncios acessíveis existentes, salvo mudança explicitamente aprovada.
- Não trate checagem estática, sintaxe válida, workflow concluído ou página carregada como prova de gameplay correto ou acessibilidade validada.
- Verifique os casos de sucesso e falha pertinentes, incluindo inventário cheio, fora de alcance, disputa entre alvos, limites do mapa e estados próximos afetados.
- Se não puder executar um teste real, diga exatamente o que foi verificado e deixe explícito o que continua pendente; não invente resultados.

## Documentação e entrega

Após implementar uma mudança autorizada:

- Atualize o `README.md` da raiz se controles, execução ou comportamento observável mudarem.
- Atualize `GDD.md` apenas quando uma decisão de design aprovada mudar ou for acrescentada.
- Atualize `LORE.md` apenas quando Anderson aprovar conteúdo narrativo novo ou revisão da premissa.
- Registre em `DEVLOG.md` a mudança, arquivos afetados, verificações executadas e pendências de teste/aprovação.
- Revise consistência entre código e documentação afetada; não transforme discrepâncias conhecidas em alegações de alinhamento.
- Ao reportar, resuma o que mudou e se foi editado, publicado para teste ou validado pelo usuário. Não faça commit, publicação, release ou backup sem autorização correspondente.
