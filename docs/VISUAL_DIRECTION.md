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

## Primeira leitura da captura de 5 de novembro de 2026

A captura mostra a cena de teste limpa de cabeçalho e instruções do protótipo. A interface do Chrome, a janela de downloads e a barra do Windows nela visíveis são elementos externos ao jogo e não entram na avaliação da interface interna.

No enquadramento mostrado, o céu ocupa grande parte da imagem; o horizonte é baixo; o terreno e a grama parecem uniformes; tufos aparecem espaçados; uma forma de vegetação está cortada no primeiro plano; e um arbusto escuro isolado aparece junto ao horizonte. Esses pontos são observações daquele enquadramento, não um diagnóstico do mapa completo. A captura não mostra o suficiente da colina, da árvore, do lago ou de toda a margem para avaliar esses elementos. A próxima revisão visual deve examinar e melhorar o mapa inteiro, não apenas reproduzir ou corrigir esse enquadramento.

## Método de trabalho

1. Manter o mapa e as mecânicas atuais enquanto estabelece a linguagem visual comum.
2. Fazer alterações visuais no projeto existente, com escopo explícito, sem misturá-las a mudanças de mecânica não solicitadas.
3. Avaliar a cena em diferentes posições e orientações, incluindo a colina, árvore, arbustos, galhos, lago, lama e grama, e não apenas uma captura frontal.
4. Distinguir observação por captura, revisão de código, execução e avaliação de Anderson. Não declarar o resultado visual validado só porque a página carrega ou o código está correto.
5. Registrar no DEVLOG o que mudou, quais áreas do mapa foram observadas e quais avaliações ainda faltam.

## Linguagem honesta para apresentar o projeto

Enquanto esta direção estiver sendo explorada, pode-se dizer: “Estamos desenvolvendo uma direção de fantasia 3D estilizada, com influência de animê e referências amplas aos Zelda 3D recentes. A identidade do cenário parte da lore de uma ilha devastada que resiste e parece renascer. Estamos aplicando essa direção ao mapa de teste inteiro no workflow atual.”

Não chamar essa proposta de arte final, não afirmar que a aparência atual já a representa e não sugerir que o jogo copia Zelda.
