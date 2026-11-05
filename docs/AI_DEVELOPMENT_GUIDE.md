# Guia de desenvolvimento com IA — Phoenix Island

Este documento orienta o trabalho de agentes de IA neste repositório. Não substitui decisões de Anderson, o código nem os documentos de referência.

## Antes de começar

Leia `AGENTS.md`, `GDD.md`, `LORE.md`, o `README.md` da raiz e as partes relevantes de `DEVLOG.md`. Inspecione o código relacionado ao pedido antes de propor ou fazer mudanças. O ponto de entrada principal do protótipo é `index.html`; a página usa Three.js como módulo ES e os efeitos sonoros ficam em `assets/`.

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

- O desenvolvimento vigente é no protótipo web Three.js na branch `main`; a migração para Godot foi descartada. Não recrie nem sugira a migração como direção vigente.
- O objetivo de inclusão considera pessoas com diferentes necessidades, não apenas pessoas cegas. Não presuma que um único canal sensorial ou modo de controle sirva para todas.
- A lore em `LORE.md` é planejada. Não converter os elementos ainda indefinidos em fatos canônicos nem inseri-los no protótipo sem solicitação.
- A duração de combustível aprovada para a fogueira simples é 180 segundos (3 minutos). O texto do menu que diz “1 minuto” está incorreto. Corrija a descrição quando a alteração de documentação/interface estiver autorizada; não mude os 180 segundos para coincidir com o texto errado.
- Não altere releases, tags, backups ou versão oficial sem autorização explícita.

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
