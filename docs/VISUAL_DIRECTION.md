# Phoenix Island — guia de direção visual

**Estado:** direção inicial de trabalho para orientar as melhorias visuais do protótipo. Não é uma declaração de que a arte final já existe nem um compromisso de copiar outro jogo.

## Objetivo

Dar a Phoenix Island uma identidade visual de aventura de fantasia 3D, em vez da aparência de uma página de teste com uma cena 3D genérica. O mapa de teste inteiro deve ser tratado como uma unidade visual e melhorado no workflow que já existe no projeto. Não criar uma fatia de demonstração separada nem depender de artistas ou assets externos para estabelecer o caminho.

## Direção de estilo

Explorar uma fantasia 3D estilizada, com influência de animê e referência ampla aos Zelda 3D recentes, especialmente pela leitura clara das formas e pela sensação de aventura num mundo fantástico. São referências de direção, não instruções para copiar seus modelos, cenários, paletas, interfaces ou identidade visual.

A execução deve permanecer compatível com o protótipo Three.js e com o processo atual do projeto: geometria, materiais, iluminação, texturas procedurais e composição podem ser criados ou refinados no código e nos assets já mantidos pelo projeto. Não presumir a adoção de outro motor, equipe de arte ou pacote de assets.

## Ideia visual ligada à lore

A ilha sofreu uma catástrofe, mas não desapareceu e parece resistir, como uma fênix. O ambiente deve comunicar a coexistência de dano e vida, não ser apenas uma ilha intacta e idílica nem um terreno totalmente morto. A fênix é uma referência temática; não exige desenhar uma fênix literal, chamas por toda parte ou explicar visualmente uma causa sobrenatural ainda não definida.

Essa intenção deve ser traduzida nos elementos que já existem. Não inventar ruínas, construções, destroços, queimadas, novos biomas ou acontecimentos para “provar” a lore sem uma decisão específica de design.

## Escopo visual atual: o mapa inteiro

A revisão abrange todos os elementos do mapa de teste existente: uma árvore, vários arbustos, galhos caídos, grama, uma colina pedregosa, o lago e sua margem lamacenta. Dar a esses elementos uma linguagem comum de formas, escala, materiais, cores, iluminação e nível de detalhe, preservando sua identidade funcional.

- **Grama e terreno:** evitar um plano visualmente uniforme ou uma distribuição que pareça espalhada sem intenção. Variar a leitura de densidade e escala de forma coerente; manter terreno e vegetação legíveis à distância e em primeiro plano.
- **Colina pedregosa:** reforçar a leitura de relevo e de agrupamentos de pedras como parte da mesma ilha; evitar que pareça uma coleção de objetos desconectados ou apenas uma superfície plana com pedras soltas.
- **Árvore e arbustos:** estabelecer escala, silhueta e relação com o solo consistentes. A vegetação pode sugerir vitalidade e renovação sem transformar a ilha numa floresta fechada que não existe no mapa aprovado.
- **Galhos caídos:** fazê-los pertencer visualmente ao terreno e serem reconhecíveis como madeira, preservando a distinção entre galho caído e galho vivo da árvore.
- **Lago e margem lamacenta:** fazer a água, o contorno de lama e o terreno adjacente parecerem uma transição deliberada do mesmo ambiente; manter a margem identificável, sem confundi-la com água ou grama.

## Composição e apresentação da cena

A cena de jogo deve ocupar a janela de teste sem cabeçalho, moldura ou conteúdo editorial que dê aparência de site. Os únicos textos visíveis dentro do jogo atual são mensagens breves de feedback das ações do jogador. Não acrescentar título, lista de controles, instruções, descrição persistente do cenário, rótulos decorativos ou elementos de HUD por razões estéticas. Tutorial, ajuda, menu inicial e opções continuam fora da fase atual.

Ao avaliar uma captura, distinguir sempre os elementos da página do jogo dos elementos do navegador e do sistema operacional. Abas, barra de endereço, janela de downloads e barra de tarefas são moldura externa do Chrome/Windows, não arte ou UI do jogo. Se a captura incluir essa moldura, ela não é evidência de que esses elementos estejam implementados no jogo. Capturar em modo de tela cheia do navegador pode ocultá-la, mas essa escolha de captura não altera o produto.

A composição dentro da própria cena deve evitar que o mapa pareça vazio ou acidentalmente cortado: verificar horizonte, proporção visível de céu e terreno, enquadramento da vegetação próxima, distribuição dos elementos no campo de visão e objetos isolados que pareçam desconectados. Não esconder elementos necessários às mecânicas só para melhorar uma captura.

## Diagnóstico visual das capturas de 5 de novembro de 2026

As capturas mostram a cena de teste sem o antigo cabeçalho/manual. Abas, barra de endereço, janela de downloads e barra do Windows são do Chrome/Windows, não da interface do jogo, e ficam fora do diagnóstico da arte.

Na captura ampla de 1440 × 852, o céu ocupa cerca de metade do enquadramento e o horizonte fica baixo. Um grande disco/círculo pálido aparece no céu, atrás da paisagem, como uma forma muito regular e visualmente dominante; sua causa não é inferida pela captura, mas precisa ser investigada no código e na cena para confirmar se é intencional ou um artefato. O terreno verde tem aparência muito uniforme; os tufos de grama são finos, espaçados e repetidos, e os arbustos parecem pequenos pontos isolados ao longe. Há galhos caídos e rochas cortados pelas bordas do enquadramento. O lago é quase uma elipse geométrica perfeita, cercada por um anel de lama escuro, largo e muito regular; a água rasa/central aparece como faixas concêntricas e uma mancha azul-esverdeada lisa. Isso faz a margem parecer um contorno desenhado e a água um disco, em vez de componentes de um ambiente coeso.

A nova captura mostra a árvore: seu tronco é fino, a copa parece formada por poucos volumes arredondados sobrepostos e vários galhos escuros retos ficam muito expostos para os lados. A silhueta fica simplificada e pode parecer mecânica; revisar a relação entre copa, galhos e tronco dentro da direção estilizada, preservando a árvore e as interações já existentes. A colina fica visível como uma forma triangular/rampa bastante regular; pedras pequenas aparecem em linha perto da crista e na base. Revisar a silhueta do relevo e a integração/agrupamento das pedras para que a colina pareça uma formação do terreno, sem mudar sua topografia de gameplay por esta recomendação visual.

Essas são observações de capturas e enquadramentos específicos, não um diagnóstico de todo ângulo ou detalhe do mapa. A nova captura permite avaliar a silhueta da árvore e da colina, mas não os detalhes próximos do lago e da margem; esses itens continuam precisando de vistas dedicadas durante a revisão do mapa inteiro. A captura anterior mostrava outro enquadramento, então nenhuma imagem isolada representa toda a cena.

## Prioridades de melhoria visual derivadas das capturas

Aplicar as seguintes prioridades no mapa de teste inteiro, no workflow Three.js existente. São metas de aparência; não autorizam alterar regras de caminhada, profundidade, colisão, coleta ou limites do mapa.

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

## O que fazer primeiro no mapa atual

1. Conferir no código o disco pálido do céu e identificar exatamente o objeto/material que o produz antes de mudar ou remover qualquer elemento.
2. Ajustar a composição do terreno e a variação visual da grama para que o plano não pareça uma superfície vazia com pequenos tufos repetidos.
3. Rever a superfície do lago e a faixa de lama para que não leiam como círculos concêntricos rígidos; preservar os limites de água rasa, água profunda, margem e colisão.
4. Ajustar visualmente a silhueta da colina e a relação entre as pedras, sem mudar sua altura ou topografia caminhável sem aprovação.
5. Dar unidade à árvore, à copa, aos galhos vivos, aos arbustos e aos galhos caídos, preservando as formas/locais necessários às interações.
6. Reavaliar vistas amplas e próximas de todo o mapa para confirmar que a melhoria não funciona somente num único ângulo.

Esta sequência é uma ordem de investigação/priorização, não uma autorização para executar todas as mudanças automaticamente. Cada solicitação de implementação continua limitada ao que Anderson pedir e às decisões registradas.

## Método de trabalho

1. Manter o mapa e as mecânicas atuais enquanto estabelece a linguagem visual comum.
2. Fazer alterações visuais no projeto existente, com escopo explícito, sem misturá-las a mudanças de mecânica não solicitadas.
3. Avaliar a cena em diferentes posições e orientações, incluindo a colina, árvore, arbustos, galhos, lago, lama e grama, e não apenas uma captura frontal.
4. Distinguir observação por captura, revisão de código, execução e avaliação de Anderson. Não declarar o resultado visual validado só porque a página carrega ou o código está correto.
5. Registrar no DEVLOG o que mudou, quais áreas do mapa foram observadas e quais avaliações ainda faltam.

## Linguagem honesta para apresentar o projeto

Enquanto esta direção estiver sendo explorada, pode-se dizer: “Estamos desenvolvendo uma direção de fantasia 3D estilizada, com influência de animê e referências amplas aos Zelda 3D recentes. A identidade do cenário parte da lore de uma ilha devastada que resiste e parece renascer. Estamos aplicando essa direção ao mapa de teste inteiro no workflow atual.”

Não chamar essa proposta de arte final, não afirmar que a aparência atual já a representa e não sugerir que o jogo copia Zelda.
