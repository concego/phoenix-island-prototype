# Phoenix Island — protótipo inclusivo de exploração em primeira pessoa

Phoenix Island é um protótipo em primeira pessoa, construído com Three.js e WebGL e executado no navegador para testes. Ele permite experimentar movimento, orientação, percepção espacial, exploração, coleta de recursos, ferramentas, inventário, escalada, natação e feedback sonoro num pequeno mapa 3D. O navegador é apenas o meio de teste atual; o jogo final deverá ser compilado, e o formato/plataforma de distribuição ainda não está definido.

O protótipo já inclui suporte de interação por teclado e estrutura de anúncios compatível com leitores de tela. Isso não significa, por si só, que o jogo seja plenamente acessível a todas as pessoas cegas, nem que já seja inclusivo para todas as deficiências e necessidades. **Inclusão é o objetivo do projeto; a versão atual é uma base em evolução e requer testes com pessoas com diferentes experiências e formas de jogar.**

Esta página descreve o que o código atual oferece, seus limites conhecidos e caminhos possíveis para evoluir. As funções experimentais e provisórias não devem ser entendidas como sistemas completos de um jogo de sobrevivência ou RPG.

## Acesso e execução

- [Abrir o protótipo publicado no GitHub Pages](https://concego.github.io/phoenix-island-prototype/).
- A versão de teste roda no navegador e requer WebGL. A cena 3D depende do módulo Three.js 0.180.0 carregado pelo jsDelivr; portanto, o acesso ao CDN também é necessário. Essa configuração descreve o protótipo de teste, não o formato final de distribuição do jogo.
- O áudio é liberado após a primeira tecla de movimento ou Espaço, conforme as políticas de reprodução automática dos navegadores.
- As instruções do jogo ficam recolhidas inicialmente no painel “Instruções e detalhes do protótipo”. O inventário tem um botão próprio. Os controles de jogo são principalmente de teclado.

## Objetivo de inclusão

O objetivo não é apenas permitir que uma pessoa cega jogue por meio de anúncios ou sons. A experiência deve oferecer diferentes formas de perceber o ambiente, compreender o que está acontecendo e interagir, sem tornar uma capacidade sensorial ou motora específica a única via para o conteúdo principal.

A implementação atual já combina informação visual da cena, descrições textuais, estrutura HTML semântica, teclado e pistas sonoras. Essas camadas ainda não equivalem a opções de acessibilidade completas. O protótipo não tem hoje, por exemplo, menus de configuração para remapear controles, ajustes de contraste ou tamanho de texto, legendas configuráveis, controles por gamepad ou um modo completo de entrada alternativa.

Melhorias futuras podem incluir opções configuráveis para necessidades visuais, auditivas, motoras e cognitivas; mais de uma forma de executar ações; informação visual equivalente às pistas sonoras; ajustes de ritmo e apresentação; e testes com pessoas com diferentes deficiências. Essas são possibilidades de trabalho, não funcionalidades prometidas ou já implementadas. As prioridades devem ser definidas e validadas com pessoas que usarão o jogo.

## Escopo atual

O mapa é um campo explorável de 48 × 54 m, com colina, árvore, lago, margem lamacenta, pedras, arbustos e galhos caídos. A câmera é em primeira pessoa. Não há ainda campanha, objetivos narrativos, combate, necessidades de sobrevivência, construção de parque, progressão de personagem, salvamento de jogo ou mundo persistente. O inventário e as ações situacionais são sistemas de teste; não formam ainda uma economia ou ciclo completo de jogo.

A cena é construída proceduralmente no navegador. Não há modelos ou imagens de arte externos no cenário atual. A direção visual em exploração busca fantasia 3D estilizada, com influência de animê e referências amplas a jogos de aventura 3D, sem copiar uma obra específica. A primeira passada trabalha variação de cores e densidade no gramado, copa e madeira, faces e formações de pedra da colina, e transição entre lama, água e terreno. A arte continua provisória e precisa de avaliação nas diferentes áreas do mapa; não é arte final.

## Mapa e ambiente

O campo caminhável mede 48 × 54 m: X vai de −24 a +24 m e Y de −18 a +36 m. A posição inicial fica ao sul do lago. A orientação corporal inicial aponta para norte; na representação Three.js, o plano lógico X/Y e altitude Z é convertido para X/Z/−Y.

A colina fica na área central. Sua largura modelada é de 4,2 m (X entre −2,1 e +2,1 m), sua altura máxima é 1,8 m, a subida frontal começa perto de Y=1,1 m, o platô vai até Y=6 m e a encosta posterior desce até o terreno baixo por volta de Y=8,8 m. É possível contorná-la pelos lados ou seguir pelo terreno plano ao norte. Há três afloramentos de pedra bruta no platô e pedras soltas ao redor da base.

O lago elíptico fica ao norte e a leste, centrado em X=5,0 m, Y=13,2 m, com cerca de 12 × 6,4 m de água. Uma margem lamacenta de aproximadamente 1,2 m contorna o lago. A faixa rasa permite caminhar sobre um fundo que chega a cerca de 0,55 m; depois o fundo desce até 2,7 m na bacia central. A água muda de transparência e cor conforme a profundidade. Ondulações sutis e círculos de água aparecem com o movimento. A área profunda bloqueia a caminhada.

A árvore fica perto do centro do campo. Tem tronco, seis raízes visíveis, galhos baixos para coleta, um cruzamento alto que funciona como patamar de escalada e oito agrupamentos de copa. Os galhos baixos podem ser alcançados do chão junto ao tronco; o patamar elevado é um elemento separado da coleta baixa.

Há dez posições predefinidas de galhos caídos e 30 arbustos silvestres distribuídos pelo mapa em posições pseudoaleatórias reproduzíveis. Os arbustos evitam áreas como lago, colina, árvore e ponto inicial. Os elementos visuais são organizados para não depender de colisores invisíveis como explicação das interações; a árvore e os afloramentos, porém, bloqueiam o deslocamento conforme as regras do cenário.

O ambiente inclui céu em degradê, neblina, texturas procedurais de grama, solo, lama e casca, vegetação facetada, sombra de contato da árvore, iluminação direcional, pedras e água. O chão recebe variação de tons, grama agrupada e áreas mais secas; a colina possui faces laterais e pedras decorativas incorporadas, e uma faixa suave une a lama ao campo. Esses detalhes visuais não adicionam recursos nem obstáculos. O protótipo não oferece ainda controles gráficos para qualidade, brilho, contraste, paleta, campo de visão ou reduzir efeitos visuais.

## Movimento, orientação e olhar

O movimento é feito mantendo uma tecla e parando ao soltá-la. No chão, W/S movem para frente e para trás em relação ao corpo; A/D deslocam lateralmente sem girar o corpo. Movimento e direção do olhar são conceitos separados.

- Caminhada: 2,4 m/s.
- Corrida com Shift direito: W a 3,6 m/s, A/D a 3,2 m/s e S a 2,4 m/s. Shift direito pode ser pressionado depois de começar a caminhar; ao soltá-lo, a velocidade volta à caminhada. Corrida não se aplica à escalada nem à caminhada nos galhos.
- Shift esquerdo+A/D gira o corpo 45°; Shift esquerdo+W gira 180°. A direção final é anunciada em um dos oito rumos principais.
- Shift esquerdo+S faz um recuo rápido de cerca de 1,35 m.
- Setas esquerda/direita desviam o olhar em passos de 15°, até 45° para cada lado em relação ao corpo. Ao chegar ao limite, o olhar para; é preciso girar o corpo para continuar naquela direção.
- Setas cima/baixo inclinam o olhar em passos de 15°, até 30°.
- C anuncia coordenadas X/Y no plano e Z como altitude-base, em metros com duas casas decimais.

A câmera e o perfil de percepção humano usam altura ocular de 1,60 m e campo vertical de 68°. A descrição de objetos considera o enquadramento, o campo vertical e oclusão aproximada pelo cenário. Quando o olhar aponta para baixo, coletáveis visíveis recebem prioridade descritiva. O rumo do olhar é informado separadamente do rumo de caminhada. “À esquerda” e “à direita” descrevem a posição do alvo no campo de visão.

Os anúncios de orientação descrevem alvos como recursos, árvore, colina, lago, fogueira e limites do campo, conforme a direção e inclinação do olhar. A informação de orientação é complementar: a maior parte das interações ainda depende de alinhar a mira e usar a tecla correspondente. A descrição acessível não é um sistema visual completo de reconhecimento de todos os objetos nem uma ferramenta universal de orientação.

## Interações com o cenário

### Coleta direta

Enter recolhe uma pedra solta, fibra vegetal de arbusto, galho caído ou cinzas de fogueira quando o alvo está na direção do olhar e dentro do alcance. A ação não requer ferramenta e pode funcionar mesmo com outro item equipado. Pedras e cinzas têm alcance de coleta de 2,0 m; arbustos e galhos caídos, até 2,2 m. O sistema seleciona o alvo mais alinhado dentro dos critérios de mira e alcance; um alvo fora de alcance não impede que outro alvo elegível seja encontrado. A árvore tem prioridade quando o seu alvo está claramente mais alinhado.

Cada arbusto fornece duas fibras vegetais e desaparece ao ser colhido. Cada pedra solta fornece uma pedra. Cada galho caído fornece um galho e não precisa ser cortado. Cada pilha de cinzas pode ser recolhida uma vez e fornece uma unidade. Se o inventário não tiver espaço para um novo tipo de item, o objeto continua no mundo e a coleta é recusada.

O contato próximo com um coletável pode anunciar seu nome uma vez ao entrar no alcance ou trocar de alvo. A tecla Enter tenta recolher o mesmo tipo de alvo segundo as regras de alcance e inventário. A fala de proximidade e as pistas sonoras não substituem a mira da interação.

### Ferramentas e recursos

O inventário inclui graveto, galho, pedra, fibra vegetal, martelo de pedra, faca de pedra e cinzas. Graveto, galho e fibra vegetal são inflamáveis. O peso por unidade não está definido e não há limite de carga ou durabilidade de ferramentas.

A faca de pedra é fabricada pelo menu contextual: equipe uma pedra e tenha uma segunda pedra no inventário; a receita consome duas pedras no total. Ela é usada para cortar galhos vivos baixos da copa. Cada golpe causa dano inteiro aleatório de 1 a 3. Cada galho vivo tem resistência 6 e se esgota quando a resistência chega a zero; a coleta bem-sucedida concede um galho. Sem a faca nas mãos, os galhos baixos podem fornecer gravetos pela ação de coleta existente.

O martelo de pedra é feito com uma pedra, um graveto e uma fibra vegetal, que serve para afixar a pedra ao cabo. Ele não se desgasta e é usado para minerar afloramentos, sem precisar estar equipado. Cada golpe causa dano inteiro aleatório de 2 a 4; cada afloramento tem resistência 12 e rende três ou quatro pedras uma única vez quando esgotado. A resistência indica quanto falta para esgotar, não a quantidade de pedras que será obtida. Golpes e extração têm sons distintos; o estado e o dano também são anunciados.

Galhos caídos podem ser convertidos em dois gravetos no menu contextual. É necessário equipar um galho e ter uma faca de pedra em qualquer espaço do inventário; não é necessário equipar a faca para essa receita. O galho é consumido, e a ação só fica disponível se houver capacidade para receber os gravetos.

### Árvore e escalada

Perto da árvore, olhe para o tronco e pressione Espaço para se agarrar. Manter W inicia impulsos ritmados de subida; manter S inicia impulsos de descida. Cada impulso desloca cerca de 0,36 m, com cadência próxima de 0,43 s. Soltar a tecla interrompe a escalada. A subida pelo tronco termina automaticamente no cruzamento alto, a 2,75 m, e anuncia a chegada ao galho.

No patamar, W/S/A/D caminham pelos braços em cruz. O espaço caminhável é estreito e limitado à geometria dos galhos. Ao chegar a uma ponta, o jogo anuncia o lado quando consegue identificar a ponta. Espaço permite agarrar-se na extremidade; S inicia a descida. Espaço também solta a árvore e retorna ao chão. Shift direito não acelera a escalada ou o deslocamento sobre os galhos.

Os galhos baixos para coleta ficam entre cerca de 2,05 e 2,35 m. Sem faca nas mãos, mirar um deles ao alcance e pressionar Espaço fornece um graveto. Com a faca equipada, Espaço golpeia o galho vivo selecionado, respeitando sua resistência individual. A árvore atual não tem frutos; o código prevê pontos de fruta para árvores futuras, mas não há frutas disponíveis neste cenário.

### Natação

Com as mãos vazias, na faixa rasa e voltado para águas profundas, Espaço inicia a natação na superfície. W/S avançam ou recuam na direção do corpo e acompanham a inclinação do olhar: olhar para baixo direciona para baixo, para cima direciona para cima, e olhar horizontal mantém a profundidade. A/D deslocam lateralmente sem alterar altitude. A velocidade é 1,5 m/s. O movimento respeita a superfície, o fundo e uma distância mínima do fundo. A margem do lago bloqueia o deslocamento para fora da água.

Para sair, é preciso estar com as mãos vazias, na superfície e perto da faixa rasa de saída; pressione Espaço. A natação não termina automaticamente ao tocar a margem. Em água muito rasa, o fundo pode elevar o personagem até a superfície, e a saída ainda exige Espaço. O mapa não tem túneis, conectores ou passagens subaquáticas; o código tem suporte futuro a marcadores de saída para terra e conexões de água, mas a lista atual está vazia.

A inclinação do olhar e a profundidade aproximada são anunciadas ao alterar o olhar durante a natação. Mudanças de estado, como entrada, contato com fundo/superfície e bloqueio pela margem, têm feedback. Não há combate ou interação subaquática.

### Fogueira simples experimental

Com gravetos equipados, o menu de ações contextuais oferece a criação de fogueira simples quando o jogador está no chão, tem dez gravetos disponíveis e está em terreno seco, fora do lago e da lama. A ação consome dez gravetos e cria uma fogueira no local. O fogo tem lenha, chama, luz pontual e áudio ambiente em loop quando os arquivos de som estão disponíveis. A luz tem alcance configurado de 5,5 m.

A fogueira começa com 180 segundos de combustível e apaga quando o combustível chega a zero. Um graveto, galho ou fibra vegetal pode abastecê-la, consumindo uma unidade e acrescentando até 60 segundos; o máximo é 300 segundos. O alcance de abastecimento é 2,4 m. Uma fogueira apagada não pode ser reacendida. Ao apagar, deixa uma pilha de cinzas recolhível uma vez com Enter; sem espaço no inventário, as cinzas permanecem no mundo. Cinzas ainda não têm uso implementado.

Ao olhar para uma fogueira, a descrição informa se está acesa ou apagada, a posição e a distância; se estiver acesa, descreve qualitativamente que as chamas estão altas ou que o fogo deve apagar em breve, sem informar o tempo exato.

**Discrepância conhecida:** a fogueira recebe 180 segundos de combustível no código, mas o texto atual do menu contextual diz que ela acende por “1 minuto”. A duração efetiva é três minutos; a redação do menu precisa ser corrigida no código. O sistema também não limita a criação de uma nova fogueira por proximidade de outra. A luz, combustível, geometria e tempos são parâmetros experimentais, não sistemas gerais de sobrevivência.

## Inventário e interface

O inventário começa vazio e tem dez espaços para tipos diferentes de item, em duas fileiras de cinco. Itens do mesmo tipo se acumulam no mesmo espaço. Um novo tipo é recusado quando os dez espaços distintos estão ocupados. O inventário pausa o movimento, recebe foco e pode ser aberto por I ou pelo botão “Inventário (I)”; pode ser fechado por I, Esc ou pelo botão de fechar.

Setas navegam pela grade: esquerda/direita percorrem cada fileira sem passar para a outra; cima/baixo mudam de fileira; Home/End vão ao primeiro/último espaço da fileira. O foco não anuncia o número ou o espaço selecionado ao navegar pela grade. Enter abre as ações de um item ocupado e move o foco para Examinar; o botão “Ações (Enter)” é alternativa. Na lista de ações, setas cima/baixo percorrem as opções e as extremidades se conectam; Home/End vão à primeira/última ação. Enter ou Espaço ativa a opção em foco. Esc volta à grade e, na grade, fecha o inventário. Espaço vazio não executa ação nem produz anúncio.

As ações disponíveis são Examinar, Mover, Usar, Largar e Atribuir atalho. Mover transfere para um espaço vazio, agrupa itens iguais ou troca itens diferentes. Usar equipa ou guarda o item nas mãos; não consome o item. Largar coloca o item numa lista acessível de itens largados, e o botão “Recolher itens largados” recupera o que couber. Esse coletor é global: itens largados não viram objetos 3D no chão.

Atalhos de 1 a 0 podem ser atribuídos a tipos de item. A tecla numérica equipa ou guarda o item associado; o atalho acompanha o tipo se o item mudar de espaço. Uma tecla pode ser reassociada, e um item pode ter mais de uma tecla. Os números não funcionam como atalhos enquanto o foco está em campos de formulário. Equipar/guardar só é permitido no chão, sem estar nadando ou agarrado à árvore.

Com um item equipado, Alt+C abre ações situacionais, como receitas, corte de galho, criação de fogueira e abastecimento. Opções incompatíveis podem aparecer desabilitadas com informação dos requisitos. O menu contextual também pode abrir com Alt+C enquanto o inventário está aberto; o inventário é fechado para exibi-lo.

A interface da página tem instruções recolhidas, botão de inventário, painel de inventário responsivo e menu contextual. A cena e o indicador visual de estado são visíveis; anúncios textuais são enviados por uma região de estado para tecnologia assistiva. A estrutura emprega HTML semântico e foco de teclado para controles e inventário. O projeto depende do comportamento do navegador e do leitor de tela, e ainda não passou por uma certificação abrangente de acessibilidade.

## Controles completos

- **W:** avançar na direção do corpo; norte na orientação inicial.
- **S:** recuar na direção oposta ao corpo; sul na orientação inicial.
- **A/D:** deslocar lateralmente à esquerda/direita, sem girar o corpo.
- **Shift direito + W:** correr para frente a 3,6 m/s; **Shift direito + A/D:** correr lateralmente a 3,2 m/s; **Shift direito + S:** correr para trás a 2,4 m/s. Shift direito pode ser pressionado depois de iniciar o movimento; ao soltá-lo, retorna à velocidade de caminhada de 2,4 m/s.
- **Shift esquerdo + A/D:** girar o corpo 45° para a esquerda/direita, sem caminhar.
- **Shift esquerdo + W:** girar o corpo 180°.
- **Shift esquerdo + S:** recuo rápido de cerca de 1,35 m.
- **Setas esquerda/direita:** desviar o olhar em passos de 15°, até ±45° em relação ao corpo.
- **Setas cima/baixo:** inclinar o olhar em passos de 15°, até ±30°.
- **C:** anunciar coordenadas X, Y e Z.
- **I:** abrir/fechar o inventário.
- **Enter:** recolher pedra solta, fibra de arbusto, galho caído ou cinzas no alcance, se alinhados com a mira. Não minera afloramentos.
- **Espaço:** usar o item equipado ou realizar ação situacional. Com as mãos vazias, pode iniciar/sair da natação onde as condições permitem, agarrar/soltar a árvore, coletar graveto baixo ou cortar galho vivo com faca equipada. Espaço não recolhe itens comuns do chão.
- **Alt+C:** abrir o menu contextual do item equipado.
- **1 a 0:** equipar/guardar o tipo associado ao atalho.
- **Esc:** fechar ou voltar de painéis de inventário e ações.

Durante a natação, W/S seguem o ângulo vertical do olhar e A/D continuam o movimento lateral. Durante a escalada, W/S fazem impulsos de subida e descida. Soltar a tecla ativa interrompe o movimento. O protótipo não oferece remapeamento de teclas, gamepad, controle por toque para movimentação nem controles alternativos de uma mão.

## Áudio e feedback

Os sons são efeitos provisórios, muitos sintetizados ou produzidos para o protótipo. O carregamento de arquivos pode falhar sem impedir a execução; alguns sons têm tons sintetizados como reserva. A reprodução começa após interação por causa das restrições do navegador.

O sistema atual inclui:

- Passos com até oito variações para grama, água rasa e lama; quatro para o chão da colina; até sete para galhos. O sistema evita repetir imediatamente a mesma variação quando há outras disponíveis.
- Passos na grama com contato, impacto e ruído vegetal; passos molhados na água rasa; passos próprios de lama; contatos de madeira nos galhos.
- Cadência de passos: 0,43 s no plano, 0,52 s subindo e 0,36 s descendo; correndo, 0,30 s, 0,37 s e 0,27 s. A direção da encosta considera o terreno nos próximos 0,75 m. O recuo rápido usa cerca de 0,23 s. A cadência sonora não determina a velocidade do movimento.
- Sons ressonantes ascendentes/descendentes sincronizados aos passos na colina.
- Natação: quatro variações de braçada na superfície, quatro submersas, sons de entrada e saída, além de ondulações visuais. Dois pulsos médios marcam o limite de águas profundas ao caminhar; três agudos marcam possível zona de saída durante natação; um pulso mais grave e longo marca a margem. Os marcadores tocam ao entrar na zona, não repetidamente enquanto permanece nela.
- Alertas de limite do mapa: um pulso direcional por passo ao caminhar em direção à borda e dois impactos curtos no contato. O alerta não usa um temporizador independente dos passos.
- Escalada: contato ao agarrar, sons ritmados distintos ao subir/descer e apoio ao chegar aos galhos ou chão.
- Coleta e ferramentas: estalo e roçar de folhas ao coletar graveto; impactos e estilhaço para mineração; confirmações curtas distintas para coleta e ações bem-sucedidas de menu.
- Fogueira: ignição, loop ambiente enquanto acesa e extinção, com espacialização no mundo quando o navegador permite.
- Pistas espaciais automáticas para recursos: um timbre para itens coletáveis e outro para fontes que exigem extração. A pista pode começar a até 6,5 m, repetir em intervalos de cerca de 1 s e permanece associada à mesma fonte durante aproximação; afasta-se o suficiente e a pista pode ser rearmada. O áudio é espacializado. Uma fonte não deve tocar se terreno ou objeto distinto mais próximo bloquear sua linha de visão.

O áudio espacial e a quantidade de informação sonora podem não ser adequados a todas as pessoas. Não há ainda controles para volume separado por categoria, mono, intensidade de panning, substituição dos beeps por formas visuais/táteis, legendas de áudio ou modo de áudio reduzido. Esses são possíveis aprimoramentos inclusivos, não opções existentes no menu atual.

## Limitações e melhorias possíveis

O estado atual é um protótipo de exploração, não um produto final. As seguintes limitações são conhecidas ou são áreas que precisam ser investigadas:

- **Validação de acessibilidade:** a estrutura HTML e os anúncios foram desenvolvidos com uso por teclado e leitor de tela em mente, mas não representam teste formal em combinação de navegadores, sistemas operacionais, leitores de tela ou dispositivos. Fala duplicada, anúncios omitidos, foco e leitura de estado devem ser validados com usuários.
- **Inclusão além da cegueira:** ainda não há opções de contraste, paletas, escala de interface/texto, legendas de som, redução de animações, ajustes de tempo, modo sem áudio, navegação simplificada ou modos configuráveis para deficiência auditiva, motora, cognitiva ou sensibilidade sensorial. O visual não pode ser tratado como única fonte de estado; os sons também não podem ser a única fonte de informação.
- **Controles:** teclado é o controle principal. Não há remapeamento, gamepad, toque para movimentação, suporte específico a switches, entrada por voz ou opções para reduzir combinações simultâneas de teclas.
- **Representação e orientação:** há descrições e pistas, mas não um mapa acessível, bússola de configuração, painel de objetivos, tutorial interativo completo ou legendas persistentes da informação espacial. O olhar usa passos discretos no teclado e tem limites definidos; não há opção de ajuste fino.
- **Conteúdo:** há um mapa pequeno e um cenário de teste. Não há campanha, salvamento, objetivos, NPCs, progressão, combate, construção ou sistemas completos de sobrevivência. A árvore não tem frutos e não há passagens subaquáticas.
- **Simulação:** pesos, carga, durabilidade, receitas adicionais, efeitos de itens, cinzas e regras sistêmicas de conhecimento/habilidades não estão implementados. Ferramentas e recursos têm valores abstratos e poucos usos.
- **Visual e desempenho:** os detalhes e modelos são procedurais e provisórios. O protótipo requer WebGL e um módulo externo. O README não afirma uma taxa de quadros nem desempenho garantido em todos os dispositivos; é necessário medir e testar em aparelhos variados.
- **Áudio:** os efeitos são provisórios e ainda precisam de avaliação auditiva. A espacialização varia conforme navegador, fones, alto-falantes e configuração do usuário. O carregamento de áudio externo depende de rede.
- **Consistência:** além da descrição da fogueira de um minuto no menu, apesar de 180 segundos de combustível efetivo, textos e comportamento devem ser comparados após cada mudança. A função de criação também não impede construir outra fogueira perto de uma já existente.
- **Testes inclusivos:** é preciso testar com pessoas cegas, com baixa visão, surdas ou com perda auditiva, com mobilidade e destreza variadas, neurodivergentes e pessoas com diferentes sensibilidades sensoriais; sem presumir que uma opção sirva para todo um grupo. Participantes devem poder configurar a experiência e relatar barreiras sem depender exclusivamente de observação visual.

Possíveis linhas de evolução incluem: opções de acessibilidade configuráveis e persistentes; informação redundante entre visual, texto, som e, quando aplicável, vibração; tutoriais acessíveis; remapeamento e alternativas a combinações de teclas; alternativas visuais para pistas sonoras; legendas e controle de mixagem; suporte a diferentes resoluções e escalas; preferências de movimento e redução de estímulos; e processo de testes remunerados/colaborativos com pessoas com diferentes deficiências. Nenhuma dessas possibilidades deve ser considerada pronta até ser implementada e validada.

## Estado e manutenção deste documento

Este README descreve o código em `main` e a página publicada consultados em 5 de novembro de 2026. Valores e opções podem mudar. Quando o comportamento divergir da descrição, verificar primeiro `index.html` e os arquivos carregados pela página, e registrar a discrepância antes de afirmar alinhamento.

O protótipo não depende de uma ferramenta de build para a página atual: `index.html` carrega Three.js como módulo ES pelo jsDelivr e os efeitos sonoros estão em `assets/`. Para regenerar a coleção existente de sons sintetizados, o repositório contém `tools/generate_sounds.py`; a geração não implica que os novos arquivos tenham sido avaliados ou aprovados auditivamente.

## Documentação do projeto

Os documentos de design, histórico e orientação para desenvolvimento ficam na pasta [`docs/`](docs/): [GDD](docs/GDD.md), [diário de desenvolvimento](docs/DEVLOG.md), [lore planejada](docs/LORE.md), [guia de direção visual](docs/VISUAL_DIRECTION.md) e [orientações para agentes de IA](docs/AGENTS.md) / [guia de desenvolvimento com IA](docs/AI_DEVELOPMENT_GUIDE.md).
