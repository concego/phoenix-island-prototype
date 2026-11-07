# Phoenix Island — documento de design do jogo (GDD)

**Versão:** 0.3 — atualização de regras vigentes  
**Data:** 27 de outubro de 2026  
**Escopo:** direção de design para o protótipo acessível Phoenix Island  
**Estado:** documento de direção vigente; decisões aprovadas são registradas como regras, e decisões em aberto continuam pendentes

## 1. Propósito deste documento

Este GDD registra a intenção de design e os limites que devem orientar mudanças futuras em Phoenix Island. Serve para explicar o que preservar, o que evitar e como avaliar propostas novas.

O GDD descreve decisões de design vigentes. O DEVLOG continua sendo o histórico cronológico do que foi implementado, alterado e testado. O README continua sendo o manual de execução e controles atuais. Se uma frase antiga do README ou do DEVLOG contradisser uma decisão aprovada neste GDD, a decisão mais recente e explicitamente aprovada pelo responsável pelo projeto prevalece; documentação histórica não deve reativar mecânicas descartadas.

Este GDD está publicado como documento de direção do protótipo. Revisões futuras devem preservar as decisões aprovadas e não significam autorização para alterar releases, tags ou backups.

## 2. Visão e escopo

Phoenix Island é um protótipo em primeira pessoa, construído com Three.js e WebGL, para investigar movimentação, orientação, percepção do cenário, acessibilidade e uso de áudio em um ambiente tridimensional. O navegador é usado como meio de teste do protótipo, não como plataforma final do jogo: a intenção é compilar o jogo posteriormente, e o formato de distribuição ainda não foi definido.

O protótipo atual também testa uma fatia inicial de inventário, coleta de recursos, ferramentas, fabricação, escalada e natação. Essas mecânicas são experimentos funcionais do protótipo; sua presença não significa que já exista um jogo completo de sobrevivência ou um conjunto definitivo de regras.

A direção visual de trabalho está registrada em [`VISUAL_DIRECTION.md`](VISUAL_DIRECTION.md). Ela propõe uma fantasia 3D estilizada, com influências ainda exploratórias, e orienta a revisão do mapa de teste inteiro no workflow atual; não afirma que essa arte já esteja implementada nem que seja final.

### Objetivos atuais

- Testar exploração tridimensional com controle independente do olhar e da orientação corporal.
- Tornar posição, alvos, bloqueios, interações e mudanças de estado compreensíveis sem depender exclusivamente de visão.
- Experimentar pistas sonoras que complementem as informações acessíveis.
- Testar um pequeno ciclo de exploração, coleta, fabricação e uso de ferramentas.
- Preservar mecânicas já implementadas quando se adicionarem novos recursos, salvo decisão explícita em contrário.

### Fora do escopo atual

O protótipo não implementa, e este GDD não aprova por inferência, sistemas completos de RPG ou sobrevivência, narrativa de campanha, combate, fome, sede, saúde, morte, progressão, salvamento, economia, construção de base ou conteúdo completo do jogo futuro. Qualquer uma dessas áreas precisa de uma decisão de design específica antes de ser tratada como requisito.

## 3. Princípios de design

### Função antes de possibilidade

Uma interação só deve existir se tiver utilidade clara para a experiência ou para uma mecânica aprovada do jogo. O fato de algo ser tecnicamente possível, parecer realista ou ser fácil de implementar não é motivo suficiente para adicioná-lo. Antes de propor uma interação, explicitar que problema ela resolve, que resultado oferece e como contribui para o ciclo de jogo em escopo.

### Escopo sob autorização

Implementar o que foi solicitado, sem acrescentar comportamentos, variações, receitas, efeitos, itens ou sistemas não pedidos. Não ampliar o escopo por iniciativa própria. Se uma ideia adicional parecer útil, apresentá-la como proposta separada e aguardar decisão antes de incluí-la no código.

Quando algo for solicitado, não atribuir explicações ou funções extras além do que foi solicitado.

### Recursos com resultado intencional

Destruir, consumir, transformar, esgotar ou remover um recurso precisa ter um resultado coerente, previsível e intencional, ligado à ação e à utilidade do recurso. Verificar o que o jogador recebe, o que perde, se a ação pode falhar e se a falha consome algo. Não remover recursos nem criar conversões cujo propósito ou consequência não estejam definidos.

### Perguntar quando houver dúvida

Se o pedido ou uma decisão de design deixar margem para mais de uma interpretação, ou se uma funcionalidade adicional não estiver claramente autorizada, não inventar uma mecânica. Explicar a dúvida de forma concreta no chat e aguardar a decisão de Anderson antes de implementar. Não tratar silêncio, convenção de gênero, realismo ou implementação existente como autorização.

### Acessibilidade como parte da mecânica
- Informações necessárias para localizar, escolher e concluir uma ação devem estar disponíveis por meios compatíveis com leitor de tela e teclado; um efeito visual sozinho não comunica um estado essencial.
- Áudio pode complementar ou, depois de revisão, substituir uma mensagem redundante, mas não se deve remover informação útil para o leitor de tela apenas porque existe um som. Uma substituição precisa manter o significado identificável e ser aprovada antes de alterar o comportamento.
- Anúncios devem começar pela informação útil, sem prefixos genéricos repetidos.
- Movimento contínuo não deve narrar cada tecla ou passo. O fluxo normal comunica mudanças de estado e resultados necessários à ação, sem excesso de instruções.
- Controles e interações precisam ser testáveis sem exigir que o jogador interprete elementos puramente visuais.
- O protótipo está em estágio básico e ainda não tem menu. A prioridade atual é implementar as mecânicas previstas, testá-las, validá-las e aprimorá-las. A criação do menu integrado ao início do jogo e das opções de apresentação/acessibilidade fica para depois que o protótipo sair do estágio básico; não antecipar essa etapa. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais. Isso não cria menu de pausa nem dá a Esc uma função fora desses painéis; F1 permanece sem função nesta fase. Não presumir que TTS embutido ou outras propostas de assistência para pessoas cegas sejam eficazes; validar qualquer solução com Anderson antes de apresentá-la como útil.

### Tutorial, ajuda e controles visíveis
- Nesta fase não há tutorial nem menu de ajuda planejados ou implementados. Não adicionar um tutorial, manual na tela ou menu de ajuda sem uma decisão e pedido futuros.
- Os controles podem ser descritos em documentação externa do projeto, mas não devem aparecer na interface durante o jogo nesta fase. Não mostrar listas de teclas, comandos, instruções ou lembretes de controles na tela. Exibi-los só poderá ser considerado se futuramente forem explicitamente requeridos como parte de um tutorial ou de menus de ajuda aprovados.
- Mensagens normais de jogo devem ser concisas e contextuais, priorizando estados e resultados; não devem ensinar comandos ou repetir requisitos.
- Se uma ação não puder prosseguir por requisito conhecido, não executar a ação nem consumir/transformar recursos indevidamente; não substituir a ausência de tutorial por explicações repetitivas em jogo.

### Preservar antes de substituir

- Uma nova forma de coletar ou interagir não deve apagar silenciosamente uma forma já existente.
- Ao mudar altura, alcance ou geometria, verificar todas as mecânicas dependentes, como escalada, caminhada nos galhos, coleta e colisão.
- Não implementar ações para uma ferramenta apenas por analogia ou conveniência. Cada ferramenta só executa as funções aprovadas.
- Uma correção de implementação não equivale a autorização para mudar o design ou remover outras mecânicas.

### Testabilidade e honestidade sobre validação

- Distinguir sempre: decisão aprovada, implementação no código, página publicada, teste manual e avaliação qualitativa.
- Verificações estáticas ou carregamento da página não comprovam que uma interação funciona corretamente em gameplay ou com leitor de tela.
- Registrar no DEVLOG o que mudou e o que continua pendente; não declarar aprovação visual ou auditiva sem avaliação correspondente.

## 4. Mundo de teste

### Coordenadas e escala

- Coordenadas de design: X/Y no plano do chão e Z como altitude; norte é Y positivo.
- Conversão de renderização: `(X, Y, Z)` de design para `(X, Z, -Y)` em Three.js.
- Campo caminhável: X de −24 m a +24 m e Y de −18 m a +36 m (48 × 54 m).
- Altura ocular humana de referência: 1,60 m.

### Regiões presentes

- Colina central com 1,8 m de altura, rampas e terreno contornável.
- Árvore de teste perto do setor central, com tronco, raízes, galhos baixos de coleta e um patamar mais alto para escalada.
- Lago ao norte/leste, centrado em (5,0; 13,2), com superfície aproximada de 12 × 6,4 m, faixa rasa caminhável, margem lamacenta e bacia de até 2,7 m.
- Afloramentos de pedra no topo da colina e pedras soltas coletáveis ao redor da base.
- Arbustos distribuídos pelo campo como fonte de fibra vegetal e galhos caídos como recurso distinto dos gravetos.

A distribuição, quantidades e dimensões são parâmetros do protótipo e podem mudar após decisão e teste; não devem ser tratados como números universais do jogo futuro.

## 5. Controles e exploração

- W/S: avançar/recuar em relação ao corpo; A/D: deslocamento lateral.
- Shift direito combinado ao movimento: corrida, com velocidades conforme o controle atual do README.
- Shift esquerdo+A/D: girar o corpo em 45°; Shift esquerdo+W: girar 180°; Shift esquerdo+S: recuo rápido.
- Setas: olhar em passos de 15°, com limites laterais e verticais descritos no README.
- C: anunciar coordenadas.
- Espaço: interagir, usar o item em mãos ou iniciar/confirmar saída da natação conforme a situação.
- Enter: recolher pedra solta ou fibra de arbusto quando o alvo e a interação forem elegíveis; não substitui a mineração de afloramentos.
- I: abrir inventário. Alt+C com item equipado: abrir ações situacionais.

O olhar e a orientação corporal são controles distintos. A/D não giram o corpo. Não introduzir atalhos que conflitem com essas funções sem decisão explícita.

## 6. Interações e ferramentas aprovadas

O registro consolidado de ingredientes, consumo, resultados esperados e condições das receitas de fabricação está em [`CRAFTING.md`](CRAFTING.md). Este documento detalha as receitas atualmente aprovadas sem ampliar o escopo do protótipo.

### Árvore: duas alturas, duas mecânicas

- A escalada deve permanecer funcional: aproximar-se e mirar o tronco, pressionar Espaço para agarrar, manter W para subir ao patamar alto, caminhar pelos galhos, segurar-se numa ponta com Espaço e descer com S.
- Galhos baixos da copa são uma interação separada, alcançável do chão perto da árvore, mirando para cima.
- Sem faca equipada, o alvo baixo de coleta da copa produz um graveto.
- Com a faca de pedra equipada, o mesmo alvo de copa pode ser golpeado; cada alvo de galho vivo tem resistência individual 6, diminui com golpes de dano sorteado entre 1 e 3 e fornece um galho ao chegar a zero.
- Os galhos baixos não substituem nem rebaixam o patamar de escalada. Alterar a copa exige preservar e testar a subida, a travessia e a descida.
- A árvore de teste atual não tem alvos de fruto; não anunciar ou pressupor frutos disponíveis.

### Galhos e gravetos

- Galhos são distintos de gravetos, maiores e mais resistentes, são material para receitas e inflamáveis.
- Galhos caídos no chão são itens recolhidos somente com Enter, sem faca ou golpes; a coleta exige alcance e espaço no inventário.
- Galhos vivos baixos da copa são fontes de extração: somente eles exigem faca equipada e golpes sucessivos para serem cortados.
- Com um galho equipado, o menu oferece a conversão em dois gravetos somente se houver uma faca de pedra em algum espaço do inventário; a faca não precisa estar equipada para esta conversão.
- A conversão consome um galho e produz dois gravetos. Conferir espaço antes de consumir o recurso.
- Galhos caídos não têm resistência e são recolhidos diretamente. Galhos vivos baixos da copa têm resistência inicial 6; a faca causa dano inteiro sorteado entre 1 e 3 por golpe até esgotá-los. O martelo não interage com galhos.

### Dano e resistência

- Cada acerto sorteia um valor inteiro uniforme dentro da faixa de dano da ferramenta usada. O dano é subtraído da resistência da fonte, limitada a zero; ao chegar a zero, a fonte se esgota. A escala é abstrata e não representa medida física.
- Faca de pedra, ferramenta de corte mais básica: dano inteiro sorteado uniformemente entre 1 e 3 por golpe. Martelo de pedra, ferramenta de impacto mais básico: dano inteiro sorteado uniformemente entre 2 e 4 por golpe.
- Galho vivo: resistência 6; afloramento rochoso: resistência 12. Galhos caídos são itens recolhíveis e não têm resistência.
- Enquanto a fonte resistir, cada golpe reduz sua resistência. Ao esgotar, a fonte entrega seu rendimento atual. Se não houver espaço para a recompensa, o golpe que a esgotaria não reduz a resistência; seu dano sorteado fica pendente para ser aplicado sem novo sorteio quando houver espaço.
- Esta regra e estes valores são os aprovados para as ferramentas/fontes do protótipo; não implementar outras armas, classes ou efeitos de dano por inferência.

### Faca de pedra

- Ferramenta de corte.
- Receita de design aprovada: primeiro, duas pedras geram uma pedra afiada; uma pedra e uma pedra afiada geram uma pedra lascada; uma pedra lascada, um graveto e uma fibra vegetal geram uma faca de pedra. A fibra amarra a lâmina ao cabo de graveto.
- Estado atual do protótipo: a receita implementada ainda é duas pedras no total, uma equipada e outra no inventário; ambas são consumidas. A cadeia de processamento e a nova receita ainda não foram implementadas nem testadas.
- Corta galhos vivos baixos da copa quando equipada. Não é necessária para recolher galhos caídos.
- A faca não deve ser descrita como ferramenta de impacto.

### Martelo de pedra

- Ferramenta de impacto.
- Receita aprovada: uma pedra, um graveto e uma fibra vegetal para afixar a pedra ao cabo.
- Uso implementado no protótipo: minerar afloramentos maiores. Basta o martelo estar no inventário; não precisa ser equipado.
- A mineração exige vários golpes, anuncia progresso e só entrega as pedras no golpe final.
- O martelo não corta nem quebra galhos, não divide galho em gravetos e ainda não tem função de construção. Não inventar outras funções sem decisão explícita.

### Materiais e coleta

- Pedras soltas, arbustos, galhos caídos e cinzas são coletados com Enter quando elegíveis, inclusive com outro item nas mãos. Espaço usa o item equipado; não recolhe esses itens do chão.
- Afloramentos exigem martelo no inventário e são minerados com Espaço em golpes sucessivos.
- Arbustos são coletados e fornecem duas fibras vegetais cada no protótipo atual.
- Para o design, está aprovada a cadeia de processamento de pedra: duas pedras geram uma pedra afiada; uma pedra + uma pedra afiada geram uma pedra lascada; uma pedra lascada + um graveto + uma fibra vegetal geram a faca de pedra. A fibra amarra a lâmina ao cabo. Essa cadeia ainda não está implementada no protótipo. A pedra afiada pode ser componente de ferramentas futuras como machado e picareta, mas as receitas dessas ferramentas não estão decididas.
- Gravetos são menores e mais frágeis que galhos; ambos são inflamáveis. Gravetos servem de combustível e de partes para ferramentas e estruturas; no protótipo são combustível da fogueira simples e compõem o cabo do martelo de pedra. Receitas concretas de estruturas ou outras ferramentas ainda não estão definidas. Galhos são maiores e mais resistentes que gravetos; podem servir de combustível e ser convertidos em dois gravetos com faca no inventário. Ainda não há receita especificada que use galhos como componente de ferramenta ou estrutura; lança, picareta e estruturas são possibilidades de design futuras, sem receitas aprovadas.
- Fibras vegetais vêm dos arbustos, são inflamáveis e servem para improvisar amarrações que conectam componentes; a fibra da receita do martelo prende a pedra ao cabo. Outras receitas de amarração ou de estrutura ainda não estão especificadas.
- Pedras são o mineral mais básico atualmente listado, resistente e não inflamável. Podem ser moldadas com limitações e não são tão flexíveis quanto metais; servem para ferramentas e estruturas. No protótipo são usadas na faca e no martelo de pedra. Processo de moldagem, técnicas e receitas estruturais concretas ainda não estão definidos.
- Usos possíveis para ferramentas ou estruturas não são automaticamente receitas aprovadas nem autorização de implementação. O catálogo consolidado de propriedades e usos está em [`CRAFTING.md`](CRAFTING.md).
- Coletas devem respeitar mira, alcance e espaço no inventário e não consumir o objeto se a recompensa não puder ser guardada.

### Fogueira simples

- A fogueira simples é uma ferramenta fixa do Tier 1, do tipo estação de trabalho; não pode ser carregada e é a estação mais básica.
- Não possui superfície ou suporte para apoiar algo em preparo, então não permite deixar um item sendo preparado enquanto o jogador se afasta. Para um preparo futuro como carne assada, o jogador deve segurar a carne num espeto dentro do alcance da fogueira durante o preparo. Isso descreve o comportamento esperado da estação; não aprova receita, alimento, duração ou mecânica de preparo ainda não definida.
- Criação atual exige dez gravetos, estar no chão seco e fora de água e lama.
- Começa com 180 segundos de combustível; material inflamável consumido pode adicionar até 60 segundos, até o máximo total de 300 segundos.
- Gravetos, galhos e fibras vegetais estão marcados como inflamáveis.
- As regras são experimentais do protótipo; não extrapolar para um sistema geral de fogo ou sobrevivência.

### Natação

- Entrada: mãos vazias, faixa rasa e corpo voltado para água profunda; Espaço inicia.
- W/S seguem a inclinação do olhar; no horizonte mantêm profundidade. A/D deslocam lateralmente.
- Saída: mãos vazias, superfície e proximidade da faixa rasa ou saída elegível, seguida de Espaço. Não sair automaticamente ao tocar a margem.
- Não existem passagens subaquáticas no mapa atual.

## 7. Inventário e interface

- Dez espaços para tipos de item, em grade de duas fileiras por cinco; começa vazio.
- Itens do mesmo tipo acumulam sem limite artificial de pilha. Não há limite de peso implementado.
- Todos os dez espaços, inclusive vazios, são navegáveis por setas; Enter abre ações para espaço ocupado. O foco e os anúncios seguem as regras de acessibilidade descritas no README.
- Ações presentes: examinar, mover, usar/equipar, soltar e atribuir atalho. Itens largados são entradas recuperáveis por controle acessível, não objetos físicos no cenário.
- Não adicionar mochila, carga, durabilidade ou efeitos de item sem decisão aprovada.

## 8. Áudio e comunicação

- A coleta com Enter seleciona o item coletável elegível mais alinhado à mira e dentro do alcance, inclusive com outro item equipado; o foco no botão Inventário não bloqueia a ação. Uma árvore claramente mais alinhada conserva sua prioridade.
- A descrição acessível deve anunciar coletáveis visíveis no campo de visão, com pontos de mira consistentes com a geometria real das suas malhas e teste de oclusão contra elementos distintos.

- Uma pista em curso mantém a identidade da fonte enquanto o jogador permanece na zona de proximidade; não alternar para fontes vizinhas a cada repetição. A descrição ao olhar deve incluir fontes coletáveis no chão quando visíveis, inclusive com olhar inclinado para baixo.
- A origem espacial e a descrição de um objeto coletável devem usar o centro calculado das malhas visíveis do objeto, não uma coordenada aproximada do solo. A checagem de visibilidade ignora a geometria própria do alvo, mas respeita qualquer outro objeto que o encubra.
- Efeitos sonoros complementam a orientação e o feedback. Sons de passos por superfície, inclinação, natação, árvore, recursos, mineração, limite e fogueira estão em estágio provisório, salvo avaliação explícita registrada.
- Efeitos de escalada previamente aprovados devem ser preservados quando não houver pedido explícito para alterá-los.
- Beeps de água indicam zonas definidas; não são bússola nem substituem informação contínua de profundidade.
- Um som de referência deve ter significado consistente, ser distinguível dos demais e não remover silenciosamente informação que o leitor de tela necessita.
- Pistas espaciais de objetos e fontes de recurso devem usar fontes posicionadas no mundo em relação ao jogador; complementam e nunca substituem a informação acessível. Para recursos, a pista toca ao se aproximar, não por varredura manual ou camada contínua.
- Usar timbres diferentes para fontes que exigem extração e itens diretamente coletáveis. A pista só toca quando o recurso seria o primeiro objeto atingido na linha de visão ao virar naquela direção, respeitando a hierarquia de elementos visíveis. Repetir a pista a cada 1 s enquanto o jogador permanece próximo e a fonte tem prioridade visível, para não depender de um único evento de entrada; uma geometria pertencente ao próprio alvo não o bloqueia, mas outros objetos mais próximos continuam bloqueando. Em 27 de outubro de 2026, Anderson informou que testou o estado publicado e o considerou confortável o bastante para atualizar os documentos e o backup. Esse marco valida o ponto atual de teste em termos gerais; não deve ser expandido para afirmar que cada fonte, som, distância ou combinação com leitor de tela foi avaliada e aprovada individualmente.
- Não fazer avaliação auditiva em nome do usuário. Registrar a avaliação que Anderson efetivamente realizou sem extrapolar seu alcance: em 27/10/2026 ele considerou o estado então publicado confortável para a atualização dos documentos e do backup.

## 9. Limites: fazer e não fazer

### Fazer

- Implementar a solicitação atual sem apagar mecânicas independentes já aprovadas.
- Conferir dependências antes de alterar geometria, altura, alcance, inventário ou prioridades de mira.
- Manter a faca como corte, o martelo como impacto e cada ação restrita às funções aprovadas.
- Usar anúncios concisos, informação diretamente útil e nomes coerentes com a ação.
- Testar bloqueios, inventário cheio, alcance, disputa entre alvos e navegação acessível.
- Atualizar o README quando controles ou comportamento observável mudarem; atualizar o DEVLOG com mudanças, validação e pendências.

### Não fazer

- Não retirar uma mecânica existente por conveniência ou presumir que um novo recurso a substitui.
- Não atribuir corte ao martelo, nem efeitos de ferramenta ou de construção não aprovados.
- Não tornar uma interação essencial dependente apenas de visão, imagem ou som ambíguo.
- Não afirmar que um teste passou apenas porque o código compila, o workflow terminou ou a página carregou.
- Não alterar releases, tags ou backups sem autorização explícita.
- Não expandir o protótipo para sistemas completos de sobrevivência/RPG por inferência.

## 10. Critérios de conclusão para mudanças

Uma mudança só deve ser considerada pronta para implementação quando:

1. A solicitação e a utilidade clara da interação estiverem definidas; possibilidade técnica, realismo ou convenção de gênero não bastam.
2. O comportamento pedido estiver delimitado, sem conteúdo ou sistemas adicionais não autorizados.
3. Recurso consumido, transformado, esgotado ou removido tiver resultado e consequência intencionais, inclusive em caso de falha.
4. Dúvidas que mudem o comportamento tiverem sido levadas ao chat e respondidas por Anderson antes da implementação.

Uma mudança implementada só deve ser considerada concluída quando:

5. Alcance, mira, ferramenta, consumo e capacidade do inventário tiverem sido verificados.
6. A interação continuar compreensível com leitor de tela e teclado.
7. As mecânicas próximas que poderiam ser afetadas tiverem sido preservadas e verificadas.
8. A publicação de teste for distinta de uma release oficial ou backup.
9. O DEVLOG registrar o que foi alterado e separar verificação estática de teste manual e avaliação do usuário.

## 11. Decisões ainda não aprovadas

A premissa narrativa planejada está em [`LORE.md`](LORE.md): um conselho de magos, com base na suspeita de um mal antigo, tenta destruir a ilha e sacrifica seus habitantes; a ilha é devastada, mas não desaparece, e a personagem do jogador, jovem e inexperiente, começa tentando sobreviver antes de buscar compreender o ocorrido. A premissa é direção narrativa planejada, não conteúdo implementado no protótipo.

Este GDD não define a história completa, a estrutura da campanha, nomes, detalhes do mundo ou personagens além da premissa geral, combate, fome, sede, saúde, morte, salvamento, persistência, respawn de recursos, construção, durabilidade de ferramentas, receitas futuras ou progressão. As lacunas listadas em `LORE.md` também permanecem sem decisão. Essas lacunas não são autorização para inventar uma solução. Quando forem necessárias para uma implementação, apresentar a decisão no chat antes de codificar.


### Seleção de objetos

A tolerância angular comum para mirar objetos interativos é de 65° em relação à direção da câmera, para reduzir a precisão exigida ao coletar ou interagir. A ampliação não altera alcances físicos, prioridade de alvos ou regras de oclusão.


### Pistas de recursos da árvore

A árvore emite a pista grave de recurso coletável quando há gravetos ou galhos disponíveis nela, pois ambos podem ser recolhidos pelo jogador.


### Confirmação sonora de coleta e ações


- A coleta bem-sucedida de itens emite um som curto próprio de confirmação.
- Cada ação concluída com sucesso pelo menu contextual do item equipado emite outro som curto, distinto da coleta. Falhas, requisitos não atendidos ou inventário cheio não emitem esses sons.


### Feedback de proximidade e anúncios

- Ao entrar na área física de contato/interação de um elemento, anunciar o nome do alvo mais próximo; não repetir continuamente enquanto o jogador permanecer junto a ele. Incluir itens de coleta, recursos, árvore e fogueira, sem ultrapassar os alcances definidos por cada mecânica.
- Manter o texto visual da cena separado da região viva para leitor de tela. Reanunciar a mesma informação após pausa breve, sem depender da inserção de espaços invisíveis no texto, sobretudo nas coordenadas e descrições do campo de visão.


A fala ao entrar na área de contato deve conter somente o nome do objeto, sem prefixo ou explicação adicional.


### Coerência entre contato e coleta

- O anúncio de um item coletável como alvo ao alcance deve usar exatamente o mesmo seletor do Enter: mesma geometria de referência, mira angular, alcance individual e prioridade entre objetos. Assim, o alvo nomeado é o que Enter tentará recolher.


### Apresentação da cena de teste

- Na fase atual, a cena 3D deve ocupar a tela inteira, sem cabeçalho ou moldura com aparência de página de site.
- O único texto visível durante o jogo são mensagens de feedback das ações do jogador. Elas devem ser breves e contextuais, comunicando resultado ou estado da ação. Não exibir título, controles, lista de teclas, instruções, lembretes, descrições persistentes do cenário ou outros textos de interface durante o jogo.
- A inspeção visual de 6 de novembro de 2026 registrou que a tela de inventário ainda exibe “Use as setas para percorrer as duas fileiras da grade” e “Ações (Enter)”. Esses textos são uma divergência em relação à regra vigente, não uma exceção aprovada. Registrar a observação para a conversa de desenvolvimento; não corrigir código durante uma tarefa apenas documental.
- Não há tutorial nem menu de ajuda nesta fase. Os controles continuam funcionando, mas não são exibidos nem anunciados em rótulos ou mensagens. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais, sem aviso visível.
- Não antecipar menu inicial, menu de pausa ou opções: entram numa etapa posterior, depois que o protótipo sair do estado básico. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais, mas a interface não deve instruir o jogador a pressioná-lo nem incluir “Esc” nos rótulos dos botões. A tecla não abre menu de pausa nem recebe outra função nesta fase. F1 permanece sem função.
