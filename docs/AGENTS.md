# Instruções para agentes de IA — Phoenix Island

Leia `AI_DEVELOPMENT_GUIDE.md`, `GDD.md`, `LORE.md`, o `README.md` da raiz e as partes relevantes de `DEVLOG.md` antes de trabalhar. O ponto de entrada principal do protótipo é `index.html`; a página usa Three.js como módulo ES e os sons ficam em `assets/`.

O código atual é a referência para o que está implementado. O GDD e `LORE.md` registram decisões aprovadas; o README descreve comportamento, controles e execução; o DEVLOG é histórico, não autorização para reintroduzir regras antigas. Se houver conflito entre código e documentos, investigue e relate a divergência; não escolha silenciosamente qual lado mudar.

Implemente apenas o escopo solicitado. Não invente mecânicas, história, personagens, objetivos ou requisitos para preencher lacunas. Se uma decisão necessária não estiver aprovada ou o pedido permitir interpretações diferentes, pare antes de codificar e pergunte a Anderson no chat, com alternativas concretas quando possível.

Preserve as mecânicas existentes que não fazem parte da mudança. O desenvolvimento vigente é no protótipo web Three.js na branch `main`; não migre o projeto para Godot nem substitua a implementação Three.js. Não altere tags, releases, backups ou a versão oficial sem autorização explícita.

A duração aprovada do combustível da fogueira simples é 180 segundos (3 minutos). Se o texto do menu disser “1 minuto”, corrija a descrição quando autorizado; não mude a duração correta de 180 segundos.

Depois de uma mudança autorizada, atualize os documentos afetados e registre em `DEVLOG.md` o que foi feito, o que foi verificado e o que ainda não foi validado. Diferencie revisão estática, execução, publicação e teste/avaliação de Anderson; nunca declare validação que não ocorreu.
