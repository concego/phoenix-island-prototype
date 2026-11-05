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

Na captura ampla de 1440 × 852, o céu ocupa cerca de metade do enquadramento e o horizonte fica baixo. O terreno verde tem aparência muito uniforme; os tufos de grama são finos, espaçados e repetidos, e os arbustos parecem pequenos pontos isolados ao longe. Há galhos caídos e rochas cortados pelas bordas do enquadramento. O lago é quase uma elipse geométrica perfeita, cercada por um anel de lama escuro, largo e muito regular; a água rasa/central aparece como faixas concêntricas e uma mancha azul-esverdeada lisa. Isso faz a margem parecer um contorno desenhado e a água um disco, em vez de componentes de um ambiente coeso.

Essas são observações desse ângulo, não um diagnóstico completo do mapa. A captura não permite avaliar adequadamente a árvore nem toda a colina; elas continuam incluídas na revisão do mapa inteiro. A captura anterior também mostrava um enquadramento mais fechado, então não tratar uma única posição da câmera como representação suficiente da cena.

## Prioridades de melhoria visual derivadas das capturas

Aplicar as seguintes prioridades no mapa de teste inteiro, no workflow Three.js existente. São metas de aparência; não autorizam alterar regras de caminhada, profundidade, colisão, coleta ou limites do mapa.

1. **Dar mais identidade ao terreno e à grama.** Reduzir a impressão de um plano verde repetitivo. Criar variação legível de tom, agrupamento, escala e silhueta nos tufos, evitando tanto pontos uniformes distribuídos mecanicamente quanto ruído miúdo por toda a superfície. Fazer grama, solo e relevos parecerem parte de uma mesma direção estilizada.
2. **Integrar o lago ao terreno.** Quebrar visualmente a forma de “disco” causada pela elipse perfeita e pelas faixas concêntricas; dar à superfície e às transições uma leitura mais orgânica e coerente com o estilo. A borda de lama não deve parecer um anel escuro uniforme. Variar sua aparência visual e a transição para grama/água mantendo exatamente as mecânicas e limites físicos atuais. Distinguir de modo claro água rasa, água profunda e lama sem depender de texto visível.
3. **Corrigir a composição da visão normal de jogo.** Ajustar céu/horizonte e distribuição do interesse visual para que o enquadramento não seja dominado por um grande vazio acima de um campo plano. Avaliar a vista inicial e outras orientações de jogo; não corrigir só para uma screenshot nem mudar os controles de olhar ou câmera sem solicitação.
4. **Evitar cortes acidentais e objetos visualmente soltos.** Verificar a vista inicial e rotas normais: galhos ou rochas enormes cortados pelo primeiro plano, arbustos minúsculos ou isolados na linha do horizonte e tufos cuja escala pareça incompatível. Não é necessário manter todo objeto sempre dentro do enquadramento; o problema é quando a composição o faz parecer erro de posicionamento ou fragmento sem relação com o cenário.
5. **Unificar a leitura do mapa todo.** Rever a colina pedregosa, rochas, árvore única, arbustos, galhos caídos, grama, lago e margem em conjunto. Formas, escala, materiais, cores, iluminação e nível de detalhe devem pertencer ao mesmo mundo estilizado. As marcas de devastação/resistência da lore não são licença para acrescentar ruínas, fogo ou novos objetos ainda não aprovados.

### Ordem de execução sugerida

- Primeiro, ajustar terreno/grama e a aparência da margem/água, os elementos mais dominantes na captura.
- Depois, conferir enquadramento/horizonte e escala/distribuição dos objetos em posições normais de jogo.
- Em seguida, revisar colina, árvore, arbustos, galhos e rochas como conjunto, preservando todas as mecânicas.
- Por fim, comparar várias vistas da cena e registrar quais problemas foram resolvidos e quais permanecem. Não declarar o mapa todo validado com base numa única captura.

## Método de trabalho

1. Manter o mapa e as mecânicas atuais enquanto estabelece a linguagem visual comum.
2. Fazer alterações visuais no projeto existente, com escopo explícito, sem misturá-las a mudanças de mecânica não solicitadas.
3. Avaliar a cena em diferentes posições e orientações, incluindo a colina, árvore, arbustos, galhos, lago, lama e grama, e não apenas uma captura frontal.
4. Distinguir observação por captura, revisão de código, execução e avaliação de Anderson. Não declarar o resultado visual validado só porque a página carrega ou o código está correto.
5. Registrar no DEVLOG o que mudou, quais áreas do mapa foram observadas e quais avaliações ainda faltam.

## Linguagem honesta para apresentar o projeto

Enquanto esta direção estiver sendo explorada, pode-se dizer: “Estamos desenvolvendo uma direção de fantasia 3D estilizada, com influência de animê e referências amplas aos Zelda 3D recentes. A identidade do cenário parte da lore de uma ilha devastada que resiste e parece renascer. Estamos aplicando essa direção ao mapa de teste inteiro no workflow atual.”

Não chamar essa proposta de arte final, não afirmar que a aparência atual já a representa e não sugerir que o jogo copia Zelda.
