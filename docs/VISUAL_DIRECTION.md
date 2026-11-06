# Phoenix Island — guia de direção visual

**Estado:** guia visual geral em evolução para todo o jogo. A direção serve como base consistente para futuras decisões e pode ser detalhada conforme o conteúdo for aprovado. Não é uma declaração de que a arte final já existe nem um compromisso de copiar outro jogo.

## Objetivo e escopo deste guia

Este guia define uma direção visual de longo prazo para **todo Phoenix Island**, não apenas para o mapa de teste. Deve ajudar a manter uma identidade reconhecível e coerente à medida que o jogo crescer, sem exigir que cada elemento seja decidido agora.

A direção deverá orientar, quando forem projetados e autorizados, ambientes, regiões, terrenos, vegetação, água, clima, iluminação, personagens, criaturas, objetos, recursos, ferramentas, efeitos visuais, menus e demais elementos visuais. Ainda não existem decisões detalhadas para várias dessas categorias; os princípios abaixo são uma bússola, não autorização para inventar conteúdo, lore, sistemas ou assets.

O mapa e os objetos atuais são **casos de aplicação e material de diagnóstico**, não limites da direção. O mapa de teste inteiro deve ser refinado no workflow existente; não criar uma fatia isolada nem depender de artistas ou assets externos para estabelecer o caminho.

## Direção de estilo

Explorar uma fantasia 3D estilizada, com influência de animê e referência ampla aos Zelda 3D recentes, especialmente pela leitura clara das formas e pela sensação de aventura num mundo fantástico. São referências de direção, não instruções para copiar seus modelos, cenários, paletas, interfaces ou identidade visual. A referência não significa que todo elemento futuro precise parecer com Zelda ou seguir convenções de uma franquia específica.

A intenção é um mundo que pareça **intencionalmente estilizado e dirigido por uma identidade visual clara**, não realista por acidente nem composto por primitives genéricas sem integração. Formas, silhuetas, escala relativa, materiais, cores, iluminação e composição devem parecer decisões do mesmo universo. A estilização deve permanecer legível tanto nos detalhes próximos quanto nas silhuetas distantes.

A execução atual deve funcionar no workflow existente de Three.js: geometria, materiais, iluminação, texturas procedurais e composição podem ser criados ou refinados no código e nos assets já mantidos pelo projeto. Esta restrição descreve como trabalhamos agora; ela não reduz o alcance futuro deste guia nem autoriza trocar de motor, contratar artistas ou adotar pacotes externos.

## Princípios visuais que se aplicam ao jogo inteiro

- **Coerência de mundo:** elementos diferentes podem ter materiais e silhuetas próprios, mas devem compartilhar uma lógica de forma, escala, acabamento, iluminação e nível de detalhe.
- **Silhuetas legíveis:** ambientes, personagens, criaturas, vegetação, objetos e itens importantes devem ser reconhecíveis pela forma geral antes de depender de detalhes pequenos. Elementos funcionalmente distintos não devem parecer iguais quando sua distinção importa ao jogo.
- **Estilização intencional:** evitar tanto superfícies uniformes e primitivas repetidas quanto ruído excessivo de detalhes. Variação deve reforçar forma, material, função e identidade, não apenas preencher espaço.
- **Hierarquia visual:** composição, contraste, escala e iluminação devem ajudar a perceber o que é central, o que pertence ao fundo e quais elementos fazem parte do ambiente. Não exigir que cada objeto chame atenção ao mesmo tempo.
- **Materiais compreensíveis:** madeira, pedra, solo, água, vegetação, metal, tecido e outros materiais futuros devem ter leituras visuais distintas e consistentes. A estilização é livre, mas não deve embaralhar diferenças relevantes para a interação.
- **Lore por meio do ambiente, sem inventar cânone:** a catástrofe e a resistência/renovação da ilha podem influenciar ambientes e materiais quando houver conteúdo aprovado. Não acrescentar ruínas, queimadas, símbolos, criaturas ou explicações sobrenaturais só para tornar a lore visualmente explícita.
- **Variação sem arbitrariedade:** regiões futuras podem ter identidades próprias, mas suas diferenças devem decorrer de lore e decisões de design aprovadas e continuar reconhecíveis como partes do mesmo jogo.
- **Acessibilidade visual não é o único canal de acessibilidade:** uma imagem pode comunicar visualmente forma e atmosfera, mas estados e interações essenciais precisam continuar respeitando as decisões de acessibilidade do projeto. Não remover mensagens ou apoios aprovados em nome da imersão.
- **Sem texto visual durante o jogo nesta fase:** no protótipo atual, os únicos textos visíveis em jogo são feedbacks breves das ações do jogador. Menus, HUD, tutorial e opções pertencem a etapas futuras e não devem ser projetados ou implementados agora.

## Aplicação por categoria conforme o jogo crescer

Estas perguntas ajudam a aplicar os princípios quando cada categoria entrar no escopo; não são especificações de conteúdo já aprovado.

- **Ambientes e regiões:** qual é a silhueta geral do lugar? Que materiais e condições o distinguem? Como se conecta visualmente à ilha e à sua história? Como muda a leitura em vistas próximas, distantes e de alturas diferentes?
- **Terreno, água e clima:** como relevo, superfícies, margens, profundidade, luz e atmosfera se relacionam sem parecer camadas independentes? As transições são visualmente intencionais e coerentes com a navegação real?
- **Vegetação e vida natural:** escala, agrupamento, silhueta e variação devem parecer parte de um ecossistema, sem que a distribuição procedural pareça ruído ou cópia repetida.
- **Personagens e criaturas:** estabelecer silhueta, proporções, materiais, expressão e nível de detalhe que pertençam à mesma fantasia estilizada. Aparência, espécies e identidades narrativas dependem de design/lore aprovados.
- **Objetos, recursos e ferramentas:** comunicar categoria, material, escala e diferença funcional. Um recurso coletável deve ser visualmente distinguível de uma fonte de extração quando isso fizer parte do design, sem mudar regras de interação para resolver só uma questão de arte.
- **Efeitos visuais e iluminação:** reforçar ação, clima e leitura espacial sem encobrir a cena ou criar dependência visual para informações essenciais. Efeitos devem compartilhar a mesma linguagem de acabamento.
- **Interface futura:** quando a etapa de menus chegar, a interface deve pertencer à identidade do jogo e não parecer uma página de site; suas decisões, conteúdo e opções serão especificados no momento apropriado, não antecipados agora.

### Como ampliar esta direção para conteúdo futuro

Quando Anderson aprovar novas regiões, personagens, criaturas, construções, interiores, itens ou outros conteúdos, acrescentar ao guia uma ficha curta para cada categoria pertinente:

- função e relação com lore/cenário aprovado;
- impressão que deve transmitir e papel na identidade do jogo;
- silhueta, proporções e escala relativa;
- materiais e acabamento estilizado;
- relação de cor e contraste com o ambiente;
- como se lê de perto, à distância e em diferentes condições de luz;
- requisitos visuais ligados a gameplay e acessibilidade;
- limitações do workflow atual e forma de testar no jogo.

Registrar separadamente o que é princípio geral, o que é decisão aprovada para uma categoria e o que é apenas proposta. O mapa de teste não deve ser usado como molde obrigatório para todos os ambientes; novos lugares podem ter identidade própria sem perder coerência com a linguagem visual comum.


## Ideia visual ligada à lore

A ilha sofreu uma catástrofe, mas não desapareceu e parece resistir, como uma fênix. Essa premissa pode fundamentar a identidade visual de todo o jogo: ambientes, materiais, mudanças de região e elementos narrativos aprovados podem explorar a coexistência de dano e vida, perda e persistência. O jogo não deve ser reduzido a uma ilha intacta e idílica nem a um mundo inteiramente morto. A fênix é uma referência temática; não exige desenhar uma fênix literal, cobrir tudo de chamas ou explicar visualmente uma causa sobrenatural ainda não definida.

Aplicar essa ideia somente quando fizer sentido ao lugar ou elemento projetado e houver conteúdo aprovado. A premissa não determina a aparência de todas as regiões, personagens ou criaturas futuras. Não inventar ruínas, construções, destroços, queimadas, novos biomas, culturas, criaturas ou acontecimentos para “provar” a lore sem decisão específica de design.


## Diagnóstico visual da sessão de capturas de 6 de novembro de 2026

O registro completo da sessão automatizada, suas limitações e as seis imagens correspondentes está em [`../testes/capturas/2026-11-06/sessao-zapia-1650/DIAGNOSTICO.md`](../testes/capturas/2026-11-06/sessao-zapia-1650/DIAGNOSTICO.md). Essa sessão observou principalmente a vista inicial, a árvore de frente/em inclinações diferentes, a colina e o inventário. Não conseguiu deslocar o personagem de forma controlada até o lago; margem próxima, fundo, escalada e galho caído não foram avaliados nela. O registro separa essas lacunas de avaliações anteriores e não substitui testes de Anderson.

Observações novas dessa rodada:

- A árvore ainda parece montada por volumes separados: copa de massas facetadas grandes, galhos retos/radiais grossos e pontudos, raízes com silhueta semelhante aos galhos. Priorizar coerência das junções e das silhuetas; manter o estilo facetado como opção estética, sem tratá-lo automaticamente como problema.
- A colina lê como rampa trapezoidal de bordas rígidas, com superfície relativamente uniforme e pedras que parecem chapadas sobre a encosta. Melhorar a integração visual do relevo e das pedras sem alterar topografia, colisões ou mineração sem aprovação.
- A grama tem tufos triangulares esparsos e repetidos, pouco integrados à superfície. Rever escala, variação e agrupamento, sem mudar a distribuição funcional dos recursos por inferência.
- No inventário, continuam visíveis instruções (“Use as setas para percorrer as duas fileiras da grade”) e o rótulo “Ações (Enter)”. Isso conflita com a regra vigente para esta fase: não exibir controles/instruções, e permitir apenas texto de feedback das ações do jogador. A captura é evidência diagnóstica; qualquer alteração de código deve seguir a conversa de desenvolvimento, não ser presumida a partir do registro.

Estas observações pertencem ao protótipo atual. Use-as como primeiro exercício da direção visual geral, não como decisões de como toda árvore, colina, grama ou interface futura precisa parecer.

## Caso de aplicação atual: o mapa de teste inteiro

Esta seção trata apenas do primeiro cenário existente; não limita o alcance geral do guia. A revisão abrange todos os elementos do mapa de teste: uma árvore, vários arbustos, galhos caídos, grama, uma colina pedregosa, o lago e sua margem lamacenta. Dar a esses elementos uma linguagem comum de formas, escala, materiais, cores, iluminação e nível de detalhe, preservando sua identidade funcional.

- **Grama e terreno:** evitar um plano visualmente uniforme ou uma distribuição que pareça espalhada sem intenção. Variar a leitura de densidade e escala de forma coerente; manter terreno e vegetação legíveis à distância e em primeiro plano.
- **Colina pedregosa:** reforçar a leitura de relevo e de agrupamentos de pedras como parte da mesma ilha; evitar que pareça uma coleção de objetos desconectados ou apenas uma superfície plana com pedras soltas.
- **Árvore e arbustos:** estabelecer escala, silhueta e relação com o solo consistentes. A vegetação pode sugerir vitalidade e renovação sem transformar a ilha numa floresta fechada que não existe no mapa aprovado.
- **Galhos caídos:** fazê-los pertencer visualmente ao terreno e serem reconhecíveis como madeira, preservando a distinção entre galho caído e galho vivo da árvore.
- **Lago e margem lamacenta:** fazer a água, o contorno de lama e o terreno adjacente parecerem uma transição deliberada do mesmo ambiente; manter a margem identificável, sem confundi-la com água ou grama.

## Apresentação do protótipo atual

Esta seção é específica ao estágio atual do protótipo. A cena de jogo deve ocupar a janela de teste sem cabeçalho, moldura ou conteúdo editorial que dê aparência de site. Os únicos textos visíveis dentro do jogo atual são mensagens breves de feedback das ações do jogador. Não acrescentar título, lista de controles, instruções, descrição persistente do cenário, rótulos decorativos ou elementos de HUD por razões estéticas. Tutorial, ajuda, menu inicial e opções continuam fora da fase atual.

Ao avaliar uma captura, distinguir sempre os elementos da página do jogo dos elementos do navegador e do sistema operacional. Abas, barra de endereço, janela de downloads e barra de tarefas são moldura externa do Chrome/Windows, não arte ou UI do jogo. Se a captura incluir essa moldura, ela não é evidência de que esses elementos estejam implementados no jogo. Capturar em modo de tela cheia do navegador pode ocultá-la, mas essa escolha de captura não altera o produto.

A composição dentro da própria cena deve evitar que o mapa pareça vazio ou acidentalmente cortado: verificar horizonte, proporção visível de céu e terreno, enquadramento da vegetação próxima, distribuição dos elementos no campo de visão e objetos isolados que pareçam desconectados. Não esconder elementos necessários às mecânicas só para melhorar uma captura.

## Caso de aplicação: diagnóstico visual do mapa de teste (capturas de 5 de novembro de 2026)

As capturas mostram a cena de teste sem o antigo cabeçalho/manual. Abas, barra de endereço, janela de downloads e barra do Windows são do Chrome/Windows, não da interface do jogo, e ficam fora do diagnóstico da arte.

Na captura ampla de 1440 × 852, o céu ocupa cerca de metade do enquadramento e o horizonte fica baixo. Um grande disco/círculo pálido aparece no céu, atrás da paisagem, como uma forma muito regular e visualmente dominante; sua causa não é inferida pela captura, mas precisa ser investigada no código e na cena para confirmar se é intencional ou um artefato. O terreno verde tem aparência muito uniforme; os tufos de grama são finos, espaçados e repetidos, e os arbustos parecem pequenos pontos isolados ao longe. Há galhos caídos e rochas cortados pelas bordas do enquadramento. O lago é quase uma elipse geométrica perfeita, cercada por um anel de lama escuro, largo e muito regular; a água rasa/central aparece como faixas concêntricas e uma mancha azul-esverdeada lisa. Isso faz a margem parecer um contorno desenhado e a água um disco, em vez de componentes de um ambiente coeso.

A nova captura mostra a árvore: seu tronco é fino, a copa parece formada por poucos volumes arredondados sobrepostos e vários galhos escuros retos ficam muito expostos para os lados. A silhueta fica simplificada e pode parecer mecânica; revisar a relação entre copa, galhos e tronco dentro da direção estilizada, preservando a árvore e as interações já existentes. A colina fica visível como uma forma triangular/rampa bastante regular; pedras pequenas aparecem em linha perto da crista e na base. Revisar a silhueta do relevo e a integração/agrupamento das pedras para que a colina pareça uma formação do terreno, sem mudar sua topografia de gameplay por esta recomendação visual.

Essas são observações de capturas e enquadramentos específicos, não um diagnóstico de todo ângulo ou detalhe do mapa. A nova captura permite avaliar a silhueta da árvore e da colina, mas não os detalhes próximos do lago e da margem; esses itens continuam precisando de vistas dedicadas durante a revisão do mapa inteiro. A captura anterior mostrava outro enquadramento, então nenhuma imagem isolada representa toda a cena.

## Prioridades para a próxima revisão do protótipo atual

Aplicar estas prioridades ao mapa de teste atual, dentro do workflow Three.js existente. Elas são exemplos concretos de como aplicar a direção geral ao cenário existente; não definem a aparência de todas as regiões futuras e não autorizam alterar regras de caminhada, profundidade, colisão, coleta ou limites do mapa.

1. **Investigar o grande círculo pálido no céu.** Conferir a geometria, o material, o posicionamento e a orientação do elemento que aparece como um disco enorme atrás da ilha. Determinar se a forma é parte intencional do céu; se não for, corrigir/remover o artefato. Não presumir que seja lua, sol, planeta ou outro elemento de lore sem verificar e sem aprovação.
2. **Dar mais identidade ao terreno e à grama.** Reduzir a impressão de um plano verde repetitivo. Criar variação legível de tom, agrupamento, escala e silhueta nos tufos, evitando tanto pontos uniformes distribuídos mecanicamente quanto ruído miúdo por toda a superfície. Fazer grama, solo e relevos parecerem parte de uma mesma direção estilizada.
3. **Integrar o lago ao terreno.** Quebrar visualmente a forma de “disco” causada pela elipse perfeita e pelas faixas concêntricas; dar à superfície e às transições uma leitura mais orgânica e coerente com o estilo. A borda de lama não deve parecer um anel escuro uniforme. Variar sua aparência visual e a transição para grama/água mantendo exatamente as mecânicas e limites físicos atuais. Distinguir de modo claro água rasa, água profunda e lama sem depender de texto visível.
4. **Corrigir a composição da visão normal de jogo.** Ajustar céu/horizonte e distribuição do interesse visual para que o enquadramento não seja dominado por um grande vazio acima de um campo plano. Avaliar a vista inicial e outras orientações de jogo; não corrigir só para uma screenshot nem mudar os controles de olhar ou câmera sem solicitação.
5. **Evitar cortes acidentais e objetos visualmente soltos.** Verificar a vista inicial e rotas normais: galhos ou rochas enormes cortados pelo primeiro plano, arbustos minúsculos ou isolados na linha do horizonte e tufos cuja escala pareça incompatível. Não é necessário manter todo objeto sempre dentro do enquadramento; o problema é quando a composição o faz parecer erro de posicionamento ou fragmento sem relação com o cenário.
6. **Unificar a leitura do mapa todo.** Rever a colina pedregosa, rochas, árvore única, arbustos, galhos caídos, grama, lago e margem em conjunto. Formas, escala, materiais, cores, iluminação e nível de detalhe devem pertencer ao mesmo mundo estilizado. As marcas de devastação/resistência da lore não são licença para acrescentar ruínas, fogo ou novos objetos ainda não aprovados.

### Ordem de execução sugerida

- Primeiro, investigar o círculo no céu e ajustar terreno/grama.
- Depois, rever a forma do lago e a transição de lama/água, conferindo-a em vistas próximas.
- Em seguida, conferir enquadramento/horizonte, escala e distribuição dos objetos em posições normais de jogo.
- Revisar árvore, colina, arbustos, galhos e rochas como conjunto, preservando todas as mecânicas.
- Por fim, comparar várias vistas da cena e registrar quais problemas foram resolvidos e quais permanecem. Não declarar o mapa todo validado com base numa única captura.

## Critérios para cada rodada de melhoria

Uma rodada de arte só está pronta para ser avaliada quando:

- A alteração tem um objetivo visual identificável, como remover/corrigir o disco do céu, dar variação à grama ou integrar a margem ao lago; “deixar mais bonito” sozinho não é critério verificável.
- O mapa continua sendo o cenário de teste completo, e a mudança não cria apenas uma composição isolada para screenshot.
- A forma visual melhora sem modificar inadvertidamente dimensões ou regras de gameplay, colisão, navegação, profundidade, seleção de alvos ou coleta. Se um ajuste exigir mudar uma dessas regras, separar e pedir aprovação.
- Não foram adicionados objetos, estruturas, ruínas, biomas, elementos de lore, textos de HUD ou instruções não aprovados. O texto visível em jogo permanece limitado a feedback breve das ações do jogador.
- Os elementos examinados continuam distinguíveis pela forma e pela leitura material: grama/solo, lama/água rasa/água profunda, rocha/afloramento/pedra solta, arbusto e galho caído/vivo.
- A linguagem estilizada fica coerente entre primeiro plano e horizonte, sem os objetos próximos parecerem de um estilo e a paisagem distante de outro.

Para comparar uma rodada, registrar capturas da vista inicial e de vistas que mostrem separadamente a colina pedregosa, a árvore e vegetação, o lago e a margem, além de ao menos uma vista ampla do mapa. As capturas servem para comparar aparência; o teste de mecânicas e a validação de Anderson são registros separados. Se uma área não estiver visível numa imagem, marcá-la como não avaliada, não como aprovada.

## Ordem sugerida de investigação do mapa atual

1. Conferir no código o disco pálido do céu e identificar exatamente o objeto/material que o produz antes de mudar ou remover qualquer elemento.
2. Ajustar a composição do terreno e a variação visual da grama para que o plano não pareça uma superfície vazia com pequenos tufos repetidos.
3. Rever a superfície do lago e a faixa de lama para que não leiam como círculos concêntricos rígidos; preservar os limites de água rasa, água profunda, margem e colisão.
4. Ajustar visualmente a silhueta da colina e a relação entre as pedras, sem mudar sua altura ou topografia caminhável sem aprovação.
5. Dar unidade à árvore, à copa, aos galhos vivos, aos arbustos e aos galhos caídos, preservando as formas/locais necessários às interações.
6. Reavaliar vistas amplas e próximas de todo o mapa para confirmar que a melhoria não funciona somente num único ângulo.

Esta sequência é uma ordem de investigação/priorização, não uma autorização para executar todas as mudanças automaticamente. Cada solicitação de implementação continua limitada ao que Anderson pedir e às decisões registradas.

## Roteiro de capturas para avaliar o protótipo atual

As capturas devem permitir comparar a versão anterior e a nova sem exigir uma inspeção de todo o mapa numa única imagem. Repetir, quando possível, os mesmos pontos e ângulos entre as rodadas. A captura ampla já fornecida funciona como referência geral; as próximas podem priorizar os detalhes abaixo.

- **Vista geral:** enquadrar o máximo possível do mapa a partir do ponto de início, em orientação aproximadamente igual à captura ampla existente. Deve mostrar a relação geral entre terreno, lago, colina e vegetação. Informar se a câmera está na posição inicial ou se foi movida.
- **Lago e margem:** aproximar-se da borda e olhar de lado, incluindo no mesmo enquadramento grama/solo, lama e água. Se a margem for longa, fazer uma segunda vista de outro trecho. Evitar imagem tão próxima que esconda a transição entre as três superfícies.
- **Árvore:** ficar a uma distância em que a árvore inteira caiba na imagem, incluindo base, tronco, copa e galhos principais. Fazer uma segunda captura em ângulo lateral/oblíquo para revelar profundidade e relação entre copa e galhos. Separadamente, registrar a vista do jogador no patamar superior olhando para a paisagem e, se possível, outra ao longo dos galhos; não confundir perspectiva do topo com uma captura da árvore inteira. Inclua também uma captura da ponta de um galho olhando para baixo, deixando visível o galho no canto inferior e a paisagem abaixo; se a área refinada for terreno, colina, pedras, lago ou lama, faça outra com o olhar no limite máximo para baixo.
- **Colina:** fazer uma vista da base em diagonal que inclua a encosta e as pedras; se possível, outra de lado que mostre a silhueta e o topo. Para avaliar uma pedra específica, enquadrá-la inteira junto ao terreno ao redor, com margem até as bordas; informar se é afloramento ou pedra solta. Para a pedra solta, manter enquadramento que mostre o objeto inteiro junto ao terreno e, se possível, contexto distante suficiente para distinguir sua localização de gameplay. Não sacrificar a comparação da inclinação por um ângulo meramente decorativo.
- **Detalhe do solo:** aproximar-se de grama, arbustos e galhos caídos e enquadrá-los junto ao chão, com uma pequena porção do terreno ao redor para avaliar escala, agrupamento e integração. Se não couberem bem juntos, separar detalhe de vegetação e detalhe de galhos. Para galho caído, enquadrar um exemplar próximo com a grama ao redor para confirmar que a silhueta de madeira é distinguível dos tufos.

Ao enviar cada captura, indicar em poucas palavras o ponto de referência ou as coordenadas anunciadas pelo jogo e a direção aproximada do olhar, se souber. Não é necessário criar legendas dentro da imagem. Se não souber a posição ou direção, basta dizer qual elemento pretendia mostrar. Para alterações de água/natação, acrescentar uma vista subaquática no fundo e outra rasa ou na superfície, identificando o estado do jogador; essas vistas são complementares às capturas de lago e margem em terra. F11 pode ocultar temporariamente a moldura do Chrome para a captura; abas, barra do navegador e barra do sistema não são parte do jogo e não precisam orientar o refinamento.

Não é obrigatório produzir todas as vistas em cada rodada. Escolher as que correspondem às áreas alteradas e, no mínimo, incluir uma vista geral mais uma vista próxima de cada área refinada. Uma captura mostra somente o que está enquadrado: registrar como “não avaliado” qualquer elemento oculto ou pequeno demais para examinar.

### Captura adicional — vista conjunta do lago, árvore e colina (5 de novembro de 2026, 22:08)

Esta vista permite avaliar simultaneamente os três elementos que faltavam nas capturas anteriores, além de uma faixa do terreno. A moldura superior é do Chrome e não pertence ao jogo.

- **Composição:** o céu continua dominando grande parte da janela; a linha do horizonte e os principais elementos do mapa ficam concentrados numa faixa baixa e estreita. A árvore e a colina estão visíveis, mas ainda parecem pequenas em relação ao espaço vazio acima delas. Rever enquadramento/composição da vista de jogo sem alterar câmera ou controles por inferência.
- **Árvore:** a silhueta é estreita e muito simétrica: tronco fino, poucos volumes arredondados de copa, folhas pequenas soltas no contorno e vários galhos retos que atravessam a copa horizontalmente. No conjunto, a árvore lembra um objeto montado por peças separadas ou um topiário, não uma árvore integrada ao cenário. Rever silhueta, distribuição/escala da copa e integração dos galhos no estilo estilizado. Preservar os pontos e geometrias necessários para coleta e escalada; mudanças nesses elementos exigem verificar as mecânicas dependentes.
- **Colina:** aparece como um bloco/rampa trapezoidal muito regular, com uma face escura extensa e bordas retas; as pedras parecem pequenos objetos pousados em fileiras ou faixas sobre a superfície e junto à crista. Rever a integração visual entre relevo e pedras para reduzir a aparência de rampa artificial e pedras alinhadas decorativamente. Não alterar altura, limites, perfil caminhável ou colisões sem decisão de gameplay aprovada.
- **Lago e margem:** a borda visível forma um arco limpo e estreito entre a água e a grama; água e margem têm superfícies visualmente lisas e uma transição bastante uniforme. Essa vista confirma que água, lama e terreno precisam ser considerados juntos, mas não mostra toda a forma do lago nem detalhes próximos suficientes para avaliar suas faixas de profundidade.
- **Terreno e vegetação distante:** a grama continua com aparência de tufos pequenos e espalhados por um plano muito regular; arbustos distantes aparecem como pequenos volumes isolados no horizonte. Rever escala, agrupamento, variação e integração visual, mantendo as posições e funções de gameplay salvo aprovação explícita.

A captura revela problemas de leitura visual neste enquadramento, não define sozinha uma solução artística. Usá-la em conjunto com vistas próximas da árvore, colina e margem e com a captura ampla; registrar separadamente o que foi inspecionado em cada imagem.

### Captura da ponta da árvore olhando para baixo — 5 de novembro de 2026, 22:35

Anderson identificou esta imagem como uma vista da ponta de um galho, olhando para baixo. É uma perspectiva intencional da escalada, não uma vista do chão nem um erro de câmera.

O enquadramento mostra o lago quase inteiro, a margem lamacenta como um anel contínuo, a área de grama ao redor, arbustos e galhos caídos espalhados pelo terreno, além da colina e de suas pedras no primeiro plano. A ponta/galho em que o jogador está aparece na parte inferior esquerda, com a superfície superior do galho e a lateral escura visíveis. O céu ocupa a metade superior da imagem.

Usar esta captura para avaliar a leitura do mapa a partir da altura da árvore, a integração entre colina, lago e terreno e a forma como a posição elevada expõe a distribuição dos elementos. Ela reforça os problemas já registrados: terreno e vegetação distantes parecem esparsos e regulares; o lago e a lama formam uma geometria muito limpa; a colina tem uma face rígida e as pedras parecem agrupadas em linhas. A vista também permite avaliar se o galho/patamar parece uma estrutura integrada à árvore ou uma plataforma geométrica isolada.

Não interpretar a presença do galho no canto como defeito de composição: o jogador está deliberadamente na ponta e olhando para baixo. Não alterar a altura do patamar, a navegação pelos galhos, a câmera ou a geometria de colisão apenas para reproduzir uma composição diferente. Qualquer ajuste visual deve preservar escalada, apoio na ponta e retorno ao chão.

## Método de trabalho

1. Manter o mapa e as mecânicas atuais enquanto estabelece a linguagem visual comum.
2. Fazer alterações visuais no projeto existente, com escopo explícito, sem misturá-las a mudanças de mecânica não solicitadas.
3. Avaliar a cena em diferentes posições e orientações, incluindo a colina, árvore, arbustos, galhos, lago, lama e grama, e não apenas uma captura frontal.
4. Distinguir observação por captura, revisão de código, execução e avaliação de Anderson. Não declarar o resultado visual validado só porque a página carrega ou o código está correto.
5. Registrar no DEVLOG o que mudou, quais áreas do mapa foram observadas e quais avaliações ainda faltam.

## Como descrever a direção geral sem prometer arte ainda não implementada

Enquanto esta direção estiver sendo explorada, pode-se dizer: “Estamos desenvolvendo uma direção de fantasia 3D estilizada, com influência de animê e referências amplas aos Zelda 3D recentes. A identidade do cenário parte da lore de uma ilha devastada que resiste e parece renascer. Estamos aplicando essa direção ao mapa de teste inteiro no workflow atual.”

Não chamar essa proposta de arte final, não afirmar que a aparência atual já a representa e não sugerir que o jogo copia Zelda.


### Captura do patamar superior da árvore — 5 de novembro de 2026, 22:32

Anderson identificou esta imagem como a vista do topo/patamar da árvore, após concluir a escalada. Portanto, deve ser analisada como uma vista intencional da posição elevada de jogo, não como uma câmera no chão, um erro de clipping ou uma imagem de aproximação à copa.

O enquadramento mostra uma visão ampla do terreno a partir de cima: o lago oval e a margem aparecem ao centro; pedras e parte da colina ocupam o primeiro plano à esquerda; há uma grande área verde relativamente plana, com tufos de grama, arbustos e galhos espalhados até o horizonte. O céu continua ocupando grande parte da imagem. O patamar/galhos não aparecem no enquadramento, embora a mensagem de estado confirme que o personagem concluiu a subida.

Usar esta captura como referência específica para avaliar a composição vista de cima e se a paisagem distante mantém identidade visual a partir da árvore. A distribuição dos elementos parece esparsa e regular nesta vista; revisar agrupamento/escala de grama, arbustos e galhos e integração do lago com o terreno, sem acrescentar objetos ou alterar sua distribuição funcional por inferência. Não concluir que o topo deve ser redesenhado nem que há clipping: a imagem é da perspectiva do jogador no patamar, conforme informação de Anderson.

No roteiro de captura, incluir uma vista a partir do patamar superior olhando para o lago/terreno e, se possível, outra olhando ao longo dos galhos para registrar o contexto da própria árvore. Distinguir claramente estas duas vistas: paisagem observada do alto e detalhes visuais dos galhos/plataforma.

### Captura da ponta da árvore com olhar totalmente para baixo — 5 de novembro de 2026, 22:37

Anderson identificou esta imagem como a posição na ponta da árvore com o olhar no limite máximo para baixo. É uma vista de gameplay intencional e não deve ser confundida com a câmera ao nível do chão.

O enquadramento permite observar de cima a colina pedregosa no primeiro plano à esquerda, incluindo uma face inclinada muito escura e abrupta, o topo plano/gramado com pedras facetadas agrupadas, além de pedras soltas ao redor da base. O lago aparece quase ao centro, com uma forma oval regular, superfície azul-escura lisa e um anel largo de lama. No terreno ao redor há grama em tufos repetidos e esparsos, arbustos arredondados e galhos caídos separados entre si. O horizonte é curvo/arqueado nos extremos do mapa; grande parte da metade superior é céu claro. A moldura do Chrome não pertence ao jogo.

Esta vista confirma que é necessário avaliar a superfície da colina e a transição para suas encostas, não apenas a silhueta lateral. A mudança brusca de iluminação/escurecimento na face da colina chama atenção e deve ser investigada como problema visual no contexto de luz e sombra, sem concluir pela imagem que seja uma falha específica. Rever se topo, encosta, rochas e terreno se leem como uma formação contínua; manter altura, inclinação caminhável, colisão, locais e disponibilidade das pedras inalterados sem aprovação.

O ângulo oferece referência complementar para forma do lago e da lama vistos de cima. A forma elíptica, a água lisa e o anel marrom homogêneo reforçam a prioridade de integrar visualmente água, margem e terreno, preservando as faixas físicas e as regras de profundidade. A grama e os objetos distribuídos no terreno também devem ser avaliados pela escala e agrupamento nesta perspectiva elevada.

Adicionar ao roteiro de comparação uma vista de cima do patamar com o olhar no limite inferior, sempre que a alteração visual afetar colina, pedras, lago, lama ou distribuição do terreno. Comparar com a vista da ponta olhando para baixo em inclinação menos extrema para distinguir a composição normal da visão totalmente descendente.

### Captura subaquática — chegada ao fundo do lago (5 de novembro de 2026, 22:38)

A captura inclui a mensagem de feedback “Você chegou ao fundo do lago.”; as barras do Chrome permanecem externas à interface do jogo. A vista deve ser interpretada como uma perspectiva subaquática durante o teste de natação, não como uma imagem do terreno seco.

Quase toda a cena está preenchida por duas grandes áreas de cor azul-escura e verde muito escura, divididas por uma borda diagonal abrupta que atravessa o enquadramento. Há poucos detalhes visíveis; alguns tufos aparecem apenas no alto à esquerda. A água e o fundo não ficam visualmente distinguíveis com clareza, e o enquadramento não mostra uma leitura evidente da superfície do lago, da margem ou da profundidade.

Registrar como prioridade de investigação visual da natação: verificar como água, fundo e iluminação/fog subaquáticos se combinam quando o jogador chega à profundidade máxima. Identificar no código a origem das duas áreas e da linha diagonal antes de alterar materiais, névoa, geometria ou câmera. A captura isolada não permite afirmar se a diagonal é a borda do lago, um limite de malha, uma sombra ou outro efeito; não inventar uma causa. A revisão deve buscar uma leitura estilizada e intencional de água/fundo e manter legível a relação espacial do jogador com o lago, sem alterar profundidade, colisão, movimento, saída ou regras de natação sem aprovação.

Incluir no roteiro de capturas uma vista subaquática no fundo do lago apenas quando a rodada mexer na água, natação, iluminação subaquática ou materiais do fundo. Registrar também uma vista rasa/na superfície para comparar a transição; não usar apenas a captura do fundo para avaliar a aparência completa do lago.

#### Rodada subaquática posterior — 6 de novembro de 2026

Anderson compartilhou o relato da outra conversa referente ao commit `0a93b6bedf242f95cc9c1fdd97c1e07b78507ced`: variações de cor foram adicionadas ao leito raso/profundo e a névoa passou a ter transição gradual. Segundo o relato, a geometria do fundo e as regras de profundidade e natação foram preservadas, e a página carregou sem erros no console. O DEVLOG registra a mudança.

**Estado de validação:** a vista no fundo ainda não foi comparada; portanto, não há confirmação de que a diagonal desapareceu ou de que a leitura melhorou. Também faltam testes de natação, saída e leitor de tela. A imagem de 5 de novembro continua sendo referência anterior para comparar, não prova do estado atual. A página indicada para teste é [o protótipo publicado](https://concego.github.io/phoenix-island-prototype/?v=0a93b6b); o parâmetro ajuda a contornar cache, mas não fixa uma versão histórica.

### Captura de galho caído com olhar para baixo — 5 de novembro de 2026, 22:43

Anderson identificou a imagem como uma vista de um galho caído no chão com o olhar inclinado para baixo. A captura foi feita no campo aberto, com grama ocupando quase todo o primeiro plano; a colina, a árvore e uma parte do lago aparecem longe, junto ao horizonte. A grama forma tufos angulares verdes e amarelados, pequenos e espaçados, distribuídos sobre uma textura de solo verde bastante uniforme.

O galho-alvo não fica claramente distinguível nesta imagem: no primeiro plano, os tufos angulares têm silhuetas estreitas que podem se confundir com fragmentos/galhos, mas não é possível confirmar qual forma corresponde ao objeto. Registrar como problema de legibilidade visual do galho caído entre a vegetação, não afirmar que o objeto está ausente ou que a mecânica de coleta falhou. A vista mostra também a escala reduzida dos arbustos distantes e a grande extensão de terreno relativamente vazio.

Para refinar a representação de galhos caídos, verificar no código a geometria, escala, orientação, cor/material e contraste contra solo e grama. O galho deve ser visualmente reconhecível como madeira deitada no chão e diferenciável de tufos de grama, sem virar um objeto enorme ou chamativo que domine o mapa. Preservar os pontos de coleta, alcance, colisão, distribuição e comportamento da mecânica sem alteração não aprovada. Em nova captura, aproximar o galho o bastante para mostrar sua forma junto a uma pequena porção de grama e solo; incluir um galho sozinho e outro em meio à vegetação, se isso for possível sem mover ou alterar recursos no jogo.

### Captura da pedra no topo da colina — 5 de novembro de 2026, 22:48

Anderson identificou esta imagem como uma captura da pedra no topo da colina. O enquadramento mostra principalmente o lago oval e a margem lamacenta; no limite inferior central aparece apenas a parte superior de uma pedra clara e facetada, cortada pela borda da imagem. Portanto, o contexto do lago/terreno é visível, mas não há área suficiente da pedra para avaliar sua silhueta completa, material, escala ou relação com o topo da colina.

Registrar como referência incompleta da pedra, não como prova de que ela esteja ausente ou de um defeito específico. Para a próxima captura dessa pedra, enquadrar o objeto inteiro e uma porção suficiente do chão ao redor, deixando margem de espaço até as bordas da imagem. Indicar se a pedra está no afloramento ou se é pedra solta/coletável, pois são objetos de gameplay diferentes. Preservar sua localização, colisão, disponibilidade e comportamento; esta anotação é apenas sobre a legibilidade da captura.

### Captura da pedra solta — 5 de novembro de 2026, 22:49

Anderson identificou esta imagem como uma pedra solta recolhível, diferente dos afloramentos rochosos maiores da colina. A captura mostra a pedra inteira, pequena e clara, no terreno gramado entre a colina e a margem do lago. Outros elementos também estão visíveis: a água tem uma forma oval muito regular, cercada por um anel largo de lama; tufos de grama aparecem como pequenos pontos ou lâminas repetidos; arbustos arredondados e alguns galhos estão espalhados pelo terreno. A encosta da colina e os afloramentos ocupam muito do primeiro plano inferior.

A pedra solta é legível como um objeto individual devido ao tom claro e ao contraste com o terreno, mas parece uma forma poliédrica quase esférica e isolada, sem integração visual evidente com o solo. Considerar no refinamento se a silhueta e o material podem sugerir melhor uma pedra natural assentada no terreno, mantendo-a distinguível e encontrável. A captura já mostra a pedra inteira com contexto suficiente; não inferir que sua escala ou localização de gameplay devam mudar.

Manter explícita a distinção visual e funcional entre esta pedra solta recolhível com Enter e as pedras maiores/afloramentos da colina, que são fontes de mineração com martelo. Não alterar o seletor, alcance, colisão, quantidade de recursos ou posição dos objetos com base nesta avaliação de aparência.
