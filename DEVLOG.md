# Phoenix Island — diário de desenvolvimento

> Documento de referência histórica e técnica. Não faz parte do jogo, não é carregado pela página e não altera a execução do protótipo. Este diário foi consolidado a partir do histórico Git disponível, do README e do código existente. Datas e horários estão no fuso America/Sao_Paulo; os commits GitHub registram horários UTC, convertidos para o horário local.

## Navegação

- [Escopo e princípios](#escopo-e-princípios)
- [Linha do tempo](#linha-do-tempo)
- [Como o protótipo está organizado](#como-o-protótipo-está-organizado)
- [Estado atual: mundo e coordenadas](#estado-atual-mundo-e-coordenadas)
- [Estado atual: controles e acessibilidade](#estado-atual-controles-e-acessibilidade)
- [Estado atual: áudio e apresentação visual](#estado-atual-áudio-e-apresentação-visual)
- [Validação e limites do que foi testado](#validação-e-limites-do-que-foi-testado)
- [Lacunas conhecidas](#lacunas-conhecidas)
- [Publicação e versões de referência](#publicação-e-versões-de-referência)
- [Fontes e método de reconstrução](#fontes-e-método-de-reconstrução)

## Escopo e princípios

Phoenix Island é, neste estágio, um protótipo acessível em primeira pessoa para experimentar deslocamento, orientação, percepção de pontos de interesse e pistas sonoras num cenário 3D. Ele não é a versão concluída do jogo de sobrevivência/RPG imaginado para o futuro e ainda não contém sistemas completos de sobrevivência, narrativa, progressão ou RPG; há somente uma primeira fatia funcional de inventário, documentada no fim deste diário.

A página é feita com Three.js/WebGL. O cenário, o céu, as texturas e a vegetação são produzidos proceduralmente; não há modelos, imagens ou outros assets artísticos externos. O propósito do protótipo é investigar interação e legibilidade sensorial enquanto o ambiente permanece pequeno e controlado. Os sons também são sintetizados e provisórios.

A prioridade de acessibilidade orienta os controles: olhar e orientação corporal são variáveis separadas; movimento não gera uma narração repetitiva a cada tecla; mudanças de estado, direções de giro e informações úteis são anunciadas por uma região aria-live. O áudio ambiental e as pistas são complementares, não substitutos de uma navegação acessível.

## Linha do tempo

A história do repositório abrange de 4 a 13 de outubro de 2026. São 65 commits no histórico consultado, mas esse número não representa 65 funcionalidades distintas: há tentativas/repetições de publicação no GitHub Pages e commits quase idênticos. A cronologia abaixo agrupa o encanamento de publicação e destaca mudanças funcionais, sem atribuir a cada retry o status de recurso novo.

### 4 de outubro — primeiro percurso e interação com a árvore

O trabalho começou com uma cena pequena em primeira pessoa e deslocamento básico, seguida pela configuração e publicação inicial via GitHub Pages. A experiência foi refinada em ciclos próximos: campo de teste, geometria inicial da colina e da árvore, descrições do que está no campo de visão e ajustes na relação entre olhar, movimento e colisão.

Uma decisão importante foi separar o olhar da movimentação: o jogador pode observar lateralmente sem que o corpo gire junto. A navegação foi ajustada para informar objetos em relação ao campo visual, sem confundir isso com a direção de caminhada. Durante a experimentação, a narração de cada movimento foi removida para não transformar cada passo ou tecla em fala constante.

A interação inicial com a árvore evoluiu para agarrar o tronco/galho e subir, e depois percorrer galhos. O alvo de agarrar ficou mais tolerante para que o jogador não precisasse mirar num ponto excessivamente estreito. Foram acrescentados sons conceituais de escalada. A infraestrutura e as tentativas repetidas de Pages deste dia foram trabalho de publicação/ajuste, não funcionalidades independentes.

### 5 de outubro — orientação corporal intencional

Foram consolidadas a orientação corporal e a liberdade limitada de olhar. Atingir o limite do olhar não gira o corpo automaticamente. A/D passaram a permitir deslocamento lateral (strafe), enquanto giros explícitos usam modificadores próprios. O protótipo anuncia a direção final do corpo depois do giro, evitando mensagens intermediárias redundantes quando uma combinação de teclas produz uma única rotação.

Os detalhes e instruções também foram esclarecidos para distinguir rumo do olhar, rumo do corpo e posição relativa de um objeto. Essa distinção estabelece a base do esquema atual de exploração.

### 6 de outubro — ações de coleta dirigidas a alvos

A interação com a árvore ganhou ações de coleta dirigidas a alvos: olhar para um galho/copa alcançável e pressionar Espaço permite retirar um graveto; árvores que tenham frutos devem permitir mirar cada fruto individualmente. A árvore de teste atual não contém alvos de fruto. Portanto, a possibilidade de colher frutos descreve uma interação preparada para árvores com esses alvos, e não conteúdo disponível na árvore presente.

### 8 de outubro — terreno, áudio e referência espacial

O campo recebeu uma passagem de acabamento visual procedural, com iluminação e UVs da textura da colina. Sons de campo e de interação com a árvore foram incorporados, e a reprodução ganhou pequenas variações aleatórias para evitar repetições perceptíveis. Passos, avisos de terreno e limites foram sincronizados com os eventos de movimento; a escalada passou a ter impulsos sonoros ritmados.

Em seguida, adotou-se de forma explícita a convenção lógica de coordenadas X/Y para o plano do chão e Z para altitude. Isso evita misturar a referência espacial do jogo com a convenção Y-up do Three.js. Também foi iniciado um experimento de percepção vertical com altura ocular, campo vertical e oclusão do terreno. A implementação trata pontos de interesse que o protótipo já consulta; não é um sistema geral de descoberta do mundo.

Houve mais de uma tentativa de implantação/reimplantação do Pages durante o refinamento de áudio. Elas são agrupadas como publicação e não como conteúdo novo.

### 11 de outubro — passos de grama

As pisadas na grama receberam variações sintetizadas mais distintas, e a cadência começou a reagir à inclinação do terreno. O objetivo foi fazer o som acompanhar a direção de subida/descida sem alterar a velocidade de deslocamento por causa da cadência sonora.

### 12 de outubro — corrida, lago, água rasa e natação

Os controles de corrida foram testados em mais de uma forma: Ctrl esquerdo, depois tecla R, e por fim Shift direito. A configuração vigente é Shift direito para correr; os controles anteriores fazem parte da evolução histórica, não são opções atuais.

O mapa aumentou de 24 × 24 m para 36 × 36 m e recebeu um lago ao norte/leste. O lago foi modelado com margem de lama, faixa rasa caminhável e bacia central funda. A malha do fundo e o cálculo de profundidade foram refinados para que o leito e a transição rasa-profunda concordem melhor. Passos na água rasa ganharam sons próprios.

Foi implementada a primeira mecânica experimental de natação, incluindo movimento vertical associado ao olhar, sons sintetizados de água e beeps de zonas. Os marcadores sonoros foram documentados como indicação de zona, não como bússola vertical: dois pulsos médios assinalam a borda da água funda, três agudos uma zona potencial de saída, e um pulso longo/grave a margem. Cada padrão ocorre ao entrar na zona.

No mesmo período, anúncios para leitor de tela passaram a começar diretamente pela informação, sem o prefixo redundante “Descrição”. A documentação foi atualizada para refletir o anúncio direto.

### 13 de outubro — ajustes de natação, colisão e composição visual

Uma investigação de colisão encontrou uma barreira lateral invisível na colina. O protótipo passou a avisar sobre bloqueios do flanco durante a investigação e, depois, a parede invisível foi removida: o terreno além da geometria lateral da colina é plano e caminhável.

A natação recebeu correções de controle de profundidade e de condição de saída: estar próximo da margem, por si só, não encerra o modo. É necessário confirmar contato com a superfície e usar Espaço, além de cumprir as demais condições. A superfície da água ganhou ondas suaves animadas, tonalidade graduada pela profundidade e ondulações de baixa densidade geradas por passos rasos e natação à superfície.

A velocidade lateral e para trás durante a corrida foi ajustada separadamente da corrida para a frente. A última passagem visual trabalhou o relevo e a borda do lago, incluindo tonalização por altitude na colina, tom mais quente no topo, sombras da colina, sombra de contato sob a árvore e transição mais suave na borda rasa. O commit mais recente dessa sequência clareou a tonalidade do topo.

## Como o protótipo está organizado

A cena interativa está concentrada em `index.html`; a documentação de uso e estado técnico está em `README.md`; os arquivos de efeitos ficam em `assets/`; e `tools/generate_sounds.py` gera os WAVs sintetizados. O módulo Three.js é carregado pelo navegador (a página depende de WebGL e do módulo hospedado no jsDelivr). O áudio só pode começar depois de uma interação do usuário, conforme a política usual dos navegadores.

Este diário é um arquivo Markdown independente. Não é referenciado pelo HTML, não é parte do bundle e não muda a lógica do protótipo.

## Estado atual: mundo e coordenadas

### Coordenadas e escala

- O espaço lógico do jogo usa X/Y no chão e Z como altitude em metros; norte é Y positivo.
- A renderização converte `(X, Y, Z)` para `(X, Z, -Y)` no Three.js, cujo eixo vertical é Y.
- A posição inicial é `(0, -2.5, 0)`, voltada para o norte.
- O perfil humano de percepção usa altura ocular de 1,60 m.
- O mapa vai de −18 a +18 m nos eixos X e Y: 36 × 36 m.

### Colina, árvore e lago

A colina tem 1,8 m de altura — não 5 m — e largura modelada de X = −2,1 a +2,1 m. A rampa frontal começa em Y=1,1 m, o cume fica em Y=4,8 m, o platô termina em Y=6,0 m e a descida posterior chega ao terreno baixo em Y=8,8 m. O terreno fora dos flancos modelados permanece caminhável; não há a antiga parede invisível lateral.

A árvore de teste, em `(3.8, −0.2)`, tem tronco cilíndrico, raízes, galhos cruzados e oito grupos facetados de copa. É possível agarrar, subir, percorrer galhos e retirar gravetos de alvos ao alcance. Não há alvos de frutos nessa árvore.

O lago fica ao norte e a leste, centrado em `(5.0, 13.2)`, com dimensões de água aproximadas de 12 × 6,4 m (raios de cerca de 6 × 3,2 m). A faixa de lama ao redor tem aproximadamente 1,2 m de largura. A prateleira rasa caminhável chega a cerca de 0,55 m de profundidade; a bacia central chega a 2,7 m. Água profunda bloqueia a caminhada.

## Estado atual: controles e acessibilidade

### Deslocamento no chão

- `W` avança e `S` recua segundo a orientação corporal; no início, W aponta ao norte.
- `A` e `D` deslocam lateralmente, sem virar o corpo.
- Caminhada: 2,4 m/s.
- `Shift direito + W`: corrida para a frente a 3,6 m/s.
- `Shift direito + A/D`: corrida lateral a 3,2 m/s.
- `Shift direito + S`: corrida para trás a 2,4 m/s.
- `Shift esquerdo + A/D`: giro corporal de 45° para esquerda/direita.
- `Shift esquerdo + W`: giro corporal de 180°.
- `Shift esquerdo + S`: recuo rápido de aproximadamente 1,35 m, a cerca de 4,2 m/s. Não é uma rotação.
- A cadência das pisadas acompanha o terreno e a velocidade correspondente, sem redefinir a velocidade de deslocamento.

A corrida não se aplica à escalada ou à travessia de galhos. Soltar a tecla ativa interrompe o movimento.

### Olhar, rumo e informações faladas

As setas mudam o olhar em incrementos de 15°. O desvio lateral se limita a ±45° em relação ao corpo e a inclinação vertical a ±30°. O olhar não altera a orientação corporal. Os giros corporais anunciam a direção resultante entre norte, nordeste, leste, sudeste, sul, sudoeste, oeste e noroeste.

`C` anuncia X/Y no plano e Z como altitude-base, em metros com duas casas decimais. A percepção vertical usa campo de visão de 68°. A linha de visão até um alvo é testada contra o relevo em amostras de até 1 cm, com tolerância de oclusão de 1 cm. Esse filtro é aplicado aos pontos de interesse já consultados pelo protótipo; o alcance máximo continua indefinido.

Os anúncios para leitor de tela usam região `aria-live`, começam pelo conteúdo útil e não repetem um prefixo genérico “Descrição”. O caminhar não é narrado a cada tecla ou passo. Inclinação do olhar e mudanças de estado relevantes podem ser anunciadas; os marcadores sonoros de água não oferecem orientação vertical contínua.

### Interação com a árvore

Com as mãos vazias, perto da árvore, olhar para o tronco e pressionar Espaço permite agarrar; Espaço solta. Segurar tronco ou ponta do galho e manter W/S produz impulsos ritmados de subida/descida, aproximadamente a cada 0,43 s. A subida termina ao alcançar o cruzamento dos galhos. Nos galhos, W/S/A/D permitem deslocar-se até a ponta; Espaço permite segurar e S descer. Alvos de galho/copa podem ser usados para coletar gravetos. Esta árvore de teste não tem frutos.

### Natação

A entrada exige mãos vazias, faixa rasa caminhável e corpo voltado para água profunda. Pressionar Espaço inicia a natação. W/S seguem a direção do olhar inclinado: olhar para baixo e mover conduz para baixo, olhar para cima e mover conduz para cima, olhar no horizonte mantém a profundidade. A/D deslocam lateralmente. A velocidade é 1,5 m/s e há uma folga mínima de 0,14 m em relação ao fundo.

Para sair são necessárias mãos vazias, contato confirmado com a superfície, proximidade de uma saída rasa/terra e Espaço. A proximidade da margem sozinha não encerra a natação. Em água muito rasa, o fundo pode elevar o personagem à superfície; essa transição é anunciada, mas ainda é necessário pressionar Espaço. Não há passagens subaquáticas nem marcadores de passagem/saída terrestre no mapa atual (`SWIM_PASSAGE_MARKERS` está vazio).

## Estado atual: áudio e apresentação visual

### Áudio

Os efeitos são sintetizados em Python e permanecem provisórios. O README registra variações separadas para grama, água rasa, lama, galhos, escalada, coleta, natação, limites e declives. Os passos no plano e nas inclinações têm intervalos próprios; o deslocamento em subida/descida também pode receber pistas ressonantes sincronizadas aos passos. Os sons de limite de campo estão associados à caminhada em direção à borda e ao contato, sem temporizador independente.

A caminhada na grama tem quatro variações; água rasa e lama também têm sons próprios. Há sons de braçada, bolhas, entrada/saída da água e padrões de beep por zona. Galhos têm contatos de madeira; coleta de graveto tem estalo e roçar de folhas; a escalada diferencia agarrar/soltar, subir/descer e apoiar-se. É possível regenerar os WAVs com `python3 tools/generate_sounds.py`.

Status de avaliação: os sons conceituais de escalada foram aprovados pelo usuário. As pisadas de grama foram avaliadas como um pouco melhores, mas ainda não aprovadas em definitivo. Os demais sons recentes não tiveram avaliação completa do usuário; portanto “implementado” não significa “aprovado”.

### Visual

O cenário usa céu em degradê e texturas procedurais de grama, solo, casca e lama, além de tufos de grama, árvore volumétrica e água com ondas animadas. A água recebe tom dependente da profundidade e uma área delimitada de ondulações discretas na caminhada rasa e na natação de superfície.

As melhorias recentes incluem tonalização dos vértices da colina por altitude, topo mais quente, sombras da colina ativas, sombra de contato suave sob a árvore e transição/fade mais forte na borda rasa. A margem lamacenta continua sendo uma faixa texturizada. Estes elementos são uma direção visual procedural e provisória, não arte final. A árvore não é composta por “caixas”: sua forma atual é descrita no código e no README como tronco cilíndrico, raízes, galhos e grupos facetados de copa.

## Validação e limites do que foi testado

É importante separar quatro estados diferentes: o recurso existe no código; a página publicada carrega; alguém percorreu/testou a mecânica; e alguém avaliou subjetivamente a qualidade visual ou sonora. Eles não são equivalentes.

- O código atual foi inspecionado e as alterações mais recentes de natação e visuais passaram por verificações estáticas.
- A página do GitHub Pages foi carregada sem erros no console do navegador durante a verificação mais recente; isso confirma carregamento, não a qualidade do percurso.
- Não foi feita, por quem consolidou este diário, uma travessia manual completa recente do mapa nem validação subjetiva visual/auditiva das últimas mudanças.
- O usuário já confirmou agarrar o tronco e que W inicia a escalada. A sequência completa de subida e travessia não foi validada integralmente.
- A percepção vertical e a percepção visual da colina só têm validação parcial do usuário.
- Sons de escalada foram aprovados; a avaliação das pisadas na grama foi provisória; outros efeitos recentes ainda não receberam avaliação completa.

Assim, as frases sobre funcionamento descrevem implementação documentada, salvo quando o estado de teste é explicitamente indicado. A verificação sem erro de console não demonstra ausência de bugs de interação, acessibilidade ou desempenho.

## Lacunas conhecidas

- O protótipo não implementa o jogo completo de sobrevivência/RPG nem sistemas completos de descoberta, progressão ou narrativa.
- O alcance máximo de percepção de pontos de interesse não foi definido; a percepção de linha de visão não é um sistema global de descoberta.
- A árvore de teste não tem frutos, embora o sistema de coleta tenha suporte a alvos de fruto em árvores que os possuam.
- Não existem passagens subaquáticas ou marcadores de passagem/saída terrestre; a lista `SWIM_PASSAGE_MARKERS` está vazia.
- A natação está implementada para o lago de teste, sem comprovação de um sistema geral aplicável a corpos d’água arbitrários.
- Sons e acabamento visual são provisórios e aguardam avaliação/refinamento; implementar efeitos não equivale a validá-los.
- As mudanças mais recentes não foram submetidas a uma avaliação manual completa de percurso, imagem e som por quem preparou o diário.

## Publicação e versões de referência

O protótipo é servido em [GitHub Pages](https://concego.github.io/phoenix-island-prototype/). A página requer navegador com WebGL e acesso ao módulo Three.js hospedado no jsDelivr. O histórico contém diversos commits de publicação/retry; eles foram agrupados na cronologia para não confundir tentativas de implantação com avanço de funcionalidade.

Há duas releases de backup registradas:

- [backup-2026-10-04](https://github.com/concego/phoenix-island-prototype/releases/tag/backup-2026-10-04)
- [backup-2026-10-08](https://github.com/concego/phoenix-island-prototype/releases/tag/backup-2026-10-08)

Ambas apontam para o commit `ed01afd6ea3118da96119a0d371ced3617988ef4`. As alterações experimentais posteriores não atualizaram essas releases. Este diário não as altera nem redefine a versão do protótipo. A referência de código mais recente conhecida ao preparar o documento é `9ae38bb123a39d426ed58f4a1bc4c169e1a2fb49`.

## Fontes e método de reconstrução

Este registro foi produzido comparando o README atual, a implementação vigente e o histórico de 65 commits de 4–13 de outubro de 2026, com consulta adicional dos detalhes disponíveis para commits relevantes. Entradas repetidas ou quase idênticas de publicação foram agrupadas; nomes de commits e seus resumos serviram para estabelecer a sequência, mas não foram tratados como prova de validação do comportamento em execução.

O estado técnico presente foi descrito de acordo com os controles e os limites documentados no README e no código corrente. Em caso de divergência histórica, o texto identifica a evolução e reserva “estado atual” para o comportamento documentado vigente. Este é um retrato do histórico disponível, não uma transcrição de cada decisão conversacional nem uma alegação de que todos os experimentos intermediários foram preservados.


## 24 de outubro de 2026 — primeira fatia do inventário

### Implementado no código

- Inventário inicial vazio com dez espaços de tipos distintos, em grade de duas fileiras por cinco; pilhas idênticas se acumulam sem limite artificial. Graveto tem `flammable: true`; `weightKg` fica indefinido (`null`). Não há limite de carga nem recipientes equipáveis nesta etapa. A coleta da árvore agora adiciona gravetos ao inventário e anuncia quando falta espaço.
- Acesso por I e botão visível, pausa do movimento ao abrir, foco no inventário e fechamento por I/Esc/botão. Controles semânticos e estado de seleção são expostos aos leitores de tela.
- Examinar, mover, usar/equipar, largar e atribuir atalhos 1–0. Mover para tipo igual agrupa, mover para espaço diferente ocupado troca os itens. Os atalhos ficam associados ao tipo de item e equipam/guardam o item quando usados fora do inventário; equipar só é permitido no chão, sem nadar ou estar agarrado à árvore.
- Largar mantém o item numa lista recuperável pelo botão acessível “Recolher itens largados”; isto ainda não é um objeto colocado fisicamente no cenário. O graveto equipado não tem efeito implementado e não é consumido; nadar continua exigindo mãos vazias.

### Teste e aprovação

A mudança foi preparada para publicação e requer validação manual do usuário na página pública; não registrar esta implementação como teste manual de jogabilidade ou como aprovação do usuário. A página pública foi consultada após a publicação e o build do GitHub Pages foi conferido; não foi realizada uma travessia manual de jogabilidade. O status não representa aprovação do usuário.


## 24 de outubro de 2026 — navegação por teclado na grade do inventário

### Implementado no código

- Os dez espaços, inclusive os vazios, são botões navegáveis com uma única parada no Tab e foco móvel. Rótulos anunciam apenas o item e a quantidade (e, quando aplicável, estado equipado e atalho), ou “vazio”; não anunciam o número do espaço. Setas navegam sem contornar os limites; Home/End vão ao início/fim da fileira atual. A estrutura usa grupo e fileiras visuais sem semântica de grade/índices ARIA, para evitar anúncio automático de posição.
- Enter abre o conjunto de ações de um item ocupado e move o foco à primeira ação disponível. O botão visível “Ações (Enter)” fornece alternativa equivalente e fica desativado em espaço vazio. Enter em espaço vazio não executa ação nem acrescenta fala. Esc retorna da lista de ações/seleção de alvo à grade ou fecha o inventário.
- Mover o foco pela navegação não anuncia qual espaço está selecionado, seu número, nem instrução para pressionar Enter. No limite da fileira, a tecla mantém o foco sem anúncio.

### Teste e aprovação

A mudança foi revisada estaticamente e requer teste manual do usuário na versão experimental pública. Não registrar como validação manual do usuário nem como aprovação. A publicação e os checks do Pages serão registrados separadamente quando concluídos.


## 24 de outubro de 2026 — acabamento visual e navegação da lista de ações

### Implementado no código

- O inventário agora ativa uma camada escurecida de fundo enquanto está aberto e a remove ao fechar; o painel conserva o layout responsivo em duas áreas no desktop e empilhado em telas estreitas.
- A lista de comandos recebeu apresentação vertical consistente, destaque claro de foco/hover e contorno de foco reforçado.
- Com uma ação focada, Setas para cima/baixo percorrem a lista em ciclo, Home/End focam a primeira/última ação. Enter continua ativando os botões nativos e seus handlers existentes; a navegação por setas não produz anúncios adicionais. A navegação da grade e os fluxos de seleção de destino de mover/atalho permanecem separados.
- O painel preserva um único botão de fechar acessível, além do fechamento por I/Esc.

### Teste e aprovação

A lógica e a documentação foram revisadas estaticamente. A inspeção do código não equivale a uma validação manual da interação; teste com leitor de tela e confirmação do usuário ainda são necessários. A verificação da página publicada/build será registrada separadamente após a publicação.
