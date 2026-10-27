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

Ambas apontam para o commit `ed01afd6ea3118da96119a0d371ced3617988ef4`. As alterações experimentais posteriores não atualizaram essas releases. Este diário não as altera nem redefine a versão do protótipo. A cronologia de outubro continua abaixo, com os commits posteriores à consolidação inicial registrados em entradas próprias. O estado de código corrente é indicado na entrada mais recente e no histórico do repositório.

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


## 24 de outubro de 2026 — tecla Enter no botão de abertura

### Implementado no código

- Enter enquanto o foco está no botão geral “Inventário (I)” não abre o painel. A abertura pelo teclado permanece em I; clique/toque no botão continua disponível. Enter dentro da grade mantém a função de abrir as ações do item.

### Teste e aprovação

A alteração foi publicada; validar manualmente com teclado e leitor de tela continua pendente. Não registrar como teste manual ou aprovação do usuário.


## 24 de outubro de 2026 — menu de ações situacionais e fogueira

### Implementado no código

- Com item nas mãos, Alt+C abre um diálogo modal de ações contextuais. O movimento para ao abrir; Esc fecha e devolve o foco; Tab permanece no diálogo, e setas/Home/End navegam pelas ações habilitadas. Requisitos e bloqueios são descritos junto às ações, incluindo falta de gravetos, água/lama, modo de movimento e fogueira próxima apagada.
- Graveto é atualmente o único material inflamável. Criar fogueira exige estar no chão seco e ter pelo menos 10 gravetos na pilha equipada; consome exatamente 10 e a coloca no ponto atual do terreno. Não permite duplicar fogo aceso ou construir sobre fogo apagado a até 2,4 m. Reacender ainda não está disponível.
- A fogueira acende com 60 segundos de combustível. Um material inflamável — graveto, galho ou fibra vegetal — consumido de cada vez pode adicionar até 60 segundos, limitado a 300 segundos totais. O combustível decresce no loop do jogo mesmo com o menu fechado; ao zerar, fogo e luz se apagam, com anúncio único se o jogador estiver próximo. Há geometria procedural e luz Three.js.
- Conhecimento, habilidades e magia ainda não são sistemas implementados; a seleção contextual está limitada às regras presentes no protótipo. Não há salvamento/persistência das fogueiras.

### Sons candidatos conectados à página de teste (24 de outubro)

Foram conectados para revisão quatro WAVs candidatos de passos para cada um destes terrenos: grama, colina, água rasa, lama e galhos. Os passos do chão da colina selecionam um conjunto próprio; as pistas de subida/descida continuam separadas, e os efeitos de agarrar, subir, descer, apoiar-se e soltar na escalada permanecem inalterados. Os conjuntos já existentes permanecem disponíveis como fallback.

A fogueira agora usa candidatos de ignição, loop ambiente de oito segundos e extinção. O loop espacializado é iniciado depois da transição de ignição e só enquanto a fogueira está acesa, com fade ao apagar; os eventos pontuais usam a posição da fogueira correspondente. Os contextos e sons só são ativados após desbloqueio do áudio por interação do usuário. Esta publicação apenas conecta os arquivos para que possam ser testados; não é uma avaliação nem aprovação auditiva, e o fluxo de gameplay continua pendente de validação.

### Verificações automatizadas/estáticas

A sintaxe do módulo JavaScript passou por parser estático (sem erros) e verificações de presença dos parâmetros/regras. O fluxo completo de gameplay não foi testado automaticamente nem manualmente; o menu depende de coletar e equipar gravetos e requer validação do usuário com leitor de tela.

### Publicação

Publicado em `main` no commit `b8b18c668042b973fb4f9478fe1cadbd92a5a8a8` (inclui o commit funcional `395c73b31a0f4f71fd0bfce1e1e8aa5748b6bc38` e correção de retorno do foco). O workflow GitHub Pages 40124346567 concluiu com sucesso; a página teste é https://concego.github.io/phoenix-island-prototype/. O HTML servido contém o menu de ações. Nenhuma release/backup foi alterada.

### Pendente para teste do usuário

Recolher pelo menos 10 gravetos, equipar a pilha e testar a criação em terreno seco, além das mensagens de bloqueio em água/lama e durante escalada/natação; abastecer uma fogueira, confirmar consumo de um graveto e limite de cinco minutos, fechar o menu e confirmar a contagem regressiva/extinção. Testar também teclado/leitor de tela e o menu com itens/situações sem ação. O inventário inicia vazio, portanto uma página que apenas carrega não valida essas mecânicas.


## 24 de outubro de 2026 — fogueira no sistema de olhar

### Implementado no código

- As fogueiras criadas entram no conjunto de alvos do sistema de percepção; lenha e chamas também são marcadas como objetos observáveis para bloqueio e visibilidade coerentes.
- Ao orientar o olhar com as setas, a descrição informa fogueira acesa/apagada, lado ou centro do campo de visão, distância e combustível restante quando acesa. O reconhecimento acessível funciona independentemente de destaque visual.

### Validação

Revisão estática concluída. Validar manualmente com fogueira criada e leitor de tela continua pendente.


## 24 de outubro de 2026 — fogueira simples com duração inicial de três minutos

- O nome da fogueira nas mensagens e descrições acessíveis passa a ser “fogueira simples”.
- O combustível inicial passa de 60 para 180 segundos (3 minutos). A adição de 60 segundos por graveto e o teto total de 300 segundos não mudam.

Publicado para teste no Pages; teste manual ainda pendente. Releases e backups não foram alterados.


## 24 de outubro de 2026 — expansão ao norte e pedras da colina

### Implementado no código

- Campo caminhável ampliado para X=−24…+24 m e Y=−18…+36 m (48 × 54 m), com plano de terreno e distribuição de tufos ampliados. A colina deixa de ser o limite norte e há espaço plano para contorná-la. Lago e casa não foram movidos.
- Adicionados três afloramentos facetados no topo (3–4 pedras por afloramento, esgotamento único) e oito pedras soltas coletáveis em volta da base. Desaparecem ao esgotar/recolher, têm descrição acessível e não criam colisores invisíveis.
- Espaço com mãos vazias recolhe pedra solta. Alt+C com graveto ou pedra equipado oferece a receita de martelo (1 graveto + 1 pedra); Espaço com o martelo equipado extrai afloramentos próximos. O martelo é reutilizável sem durabilidade neste protótipo. Mensagens cobrem falta de alcance, ferramenta, espaço no inventário, requisitos e resultado.

### Verificação e validação

Revisão estática concluída; delimitadores balanceados e assertions de bounds, quantidades de objetos, craft/mining e blockers passaram. Runtime/parser JavaScript não estava disponível neste ambiente, então sintaxe ainda não foi confirmada por parser. A movimentação contínua ao redor da colina, coleta, receita, seleção de alvo e extração ainda requerem teste manual de gameplay e leitor de tela. Não foi alegado teste manual.

### Publicação

Publicado em main, commit final `8a78d53976d1b6cfe50b53176b2c57c9a206a12c`. GitHub Pages workflow 40139327659 concluiu com sucesso. Página de teste: https://concego.github.io/phoenix-island-prototype/. Releases e backups permanecem intocados.


## 24 de outubro de 2026 — Enter para coletar pedras soltas

- A tecla Enter chama a coleta de pedras soltas quando o jogador está no chão, sem foco em controle de interface, com mãos vazias e com a pedra mais próxima dentro do alinhamento e alcance existentes.
- A ação compartilha a rotina de coleta existente, remove a pedra de cena e anuncia a coleta; afloramentos continuam exigindo o martelo e a ação por Espaço. Enter no botão Inventário não abre o inventário e a ativação de controles existentes não é interceptada.

Validação manual de gameplay e leitor de tela pendente. Nenhuma release ou backup foi alterada.


## 24 de outubro de 2026 — coleta por Enter sem mãos vazias

- Retirada a exigência de estar com as mãos vazias para recolher uma pedra solta por Enter. A ferramenta ou objeto equipado permanece nas mãos; alcance, mira e espaço no inventário continuam sendo verificados.

Publicado para teste. Validação manual ainda pendente.


## 24 de outubro de 2026 — priorizar alvos da árvore sobre pedras próximas

- O uso da ação agora calcula o alvo da árvore e o alvo rochoso antes de escolher. Se tronco, galho, copa ou fruto estiver suficientemente alinhado com a mira, esse alvo tem precedência sobre pedras com alinhamento quase igual.
- A seleção do alvo da árvore desempata candidatos pelo alinhamento da mira antes da distância, reduzindo a interferência de pedras próximas ao tronco. As pedras continuam coletáveis/mineráveis quando a árvore não é o alvo efetivamente mirado.

Validar manualmente perto das pedras da base e da árvore.

## 24 de outubro de 2026 — extração dos afloramentos com martelo no inventário

### Implementado

- A extração agora exige que o martelo de pedra esteja no inventário, mas não exige que esteja equipado nas mãos. O martelo continua reutilizável e não é consumido nem desgastado. Isso permite ao jogador que já o fabricou minerar diretamente sem repetir a receita ou reorganizar as mãos.
- Entre alvos concorrentes, um afloramento alinhado e ao alcance (2,4 m) tem prioridade durante a mineração quando há martelo no inventário; uma árvore claramente mais alinhada que o afloramento continua tendo prioridade. Sem martelo, a regra existente de prioridade da árvore sobre pedras próximas permanece.
- A extração continua recusada se não houver espaço para receber pedras; nesse caso, não reduz o afloramento. Ao concluir, recebe o total restante (3–4 pedras por afloramento), o afloramento esgota uma única vez, seu bloqueador de movimento é removido e suas malhas deixam de aparecer e de ser alvos observáveis.
- O README foi corrigido para explicar que basta ter o martelo no inventário.

### Verificação e validação

Revisão estática dos fluxos de alvo, alcance, inventário, recompensa, esgotamento e limpeza de cena. A publicação e a carga pública da página serão verificadas separadamente. Uma carga de página ou análise estática não substitui o teste manual de mineração, inventário cheio e desambiguação perto da árvore; esses testes ainda precisam ser feitos no gameplay publicado.


## 24 de outubro de 2026 — mineração em vários golpes e sons de rocha

### Implementado

- A mineração deixa de entregar todas as pedras com um único Espaço. Cada afloramento exige 3 ou 4 golpes — correspondentes ao rendimento de 3 ou 4 pedras — e só concede a recompensa ao golpe final.
- Cada golpe intermediário anuncia, na região acessível, o número do golpe e o progresso percentual; as malhas do afloramento se retraem, se deslocam e giram gradualmente. As transformações visuais são derivadas sempre da posição, escala e rotação iniciais, evitando deslocamento cumulativo desordenado a cada golpe.
- Dois WAVs distintos de impacto são sorteados nos golpes intermediários; o golpe final usa o efeito separado de quebra. O áudio obedece ao desbloqueio de áudio já existente no navegador. Os três WAVs originais são PCM mono, 16 bits, 48 kHz e foram conectados ao carregamento de áudio do protótipo.
- Antes do golpe final, o inventário é verificado. Sem espaço para as pedras, a rocha não recebe dano final nem concede recompensa; se a inserção da recompensa falhar, o progresso visual do último impacto é restaurado para o estado anterior. O martelo continua sendo exigido no inventário, sem precisar equipá-lo, e o afloramento continua selecionável enquanto ainda houver golpes restantes.
- Atualizados o texto de instruções em jogo e o README para explicar a sequência e a exigência do martelo.

### Verificação e validação

Inspecionados estaticamente os fluxos de seleção, presença do martelo, golpes intermediários/final, anúncio de progresso, capacidade do inventário, limpeza ao esgotar e conexões dos efeitos sonoros. WAVs identificados como RIFF PCM mono, 16 bits, 48 kHz. Não foi feita audição dos arquivos nem teste manual de gameplay; a avaliação auditiva, a coleta real, inventário cheio e acessibilidade no jogo continuam pendentes. A carga dos arquivos e a publicação da página de teste serão verificadas após o commit.


## 26 de outubro de 2026 — arbustos, fibra vegetal e novas receitas

### Implementado no código

- Distribuídos 30 arbustos pelo terreno em posições pseudoaleatórias reproduzíveis, evitando lago, colina, árvore e área inicial. Arbustos não geram colisores; as partes visíveis são pontos observáveis e o sistema de olhar informa que fornecem fibra vegetal.
- Espaço ou Enter colhe um arbusto alcançável e fornece 2 fibras vegetais; o arbusto desaparece após a coleta. A ação checa espaço no inventário e mantém o arbusto intacto quando o item não cabe. A coleta compete com os demais alvos do cenário respeitando mira e prioridades.
- Atualizada a receita do martelo: consome 1 pedra, 1 graveto e 1 fibra vegetal, que representa a amarração da pedra ao cabo. O martelo segue reutilizável sem desgaste.
- Adicionada a faca de pedra como nova receita do menu Alt+C quando uma pedra está equipada: requer 2 pedras no total (uma nas mãos e outra no inventário) e consome ambas. O uso funcional da faca foi posteriormente implementado como corte de galhos caídos em um único movimento; ver a entrada de 26 de outubro de 2026.
- Instruções em jogo e README atualizados. Nenhuma mudança em releases ou backups.

### Verificação e validação

Revisar coleta, distribuição, mira, concorrência de ações, requisitos das receitas, consumo e falta de espaço. Teste manual de gameplay, navegação com leitor de tela e validação visual dos arbustos continuam pendentes; não alegar confirmação manual.


## 26 de outubro de 2026 — galhos caídos e função definida para as ferramentas

### Implementado no código

- Receita da faca de pedra definida em 2 pedras no total: uma equipada nas mãos e mais uma no inventário; a fabricação consome ambas. A faca é uma ferramenta de corte e corta/coleta um galho caído em uma ação.
- Adicionados dez galhos caídos visíveis e descritíveis em terreno caminhável, fora do lago, colina, árvore e área inicial. São maiores e mais resistentes que gravetos; não criam colisores nem bloqueios invisíveis.
- O martelo é ferramenta de impacto usada exclusivamente para minerar os afloramentos maiores da colina, sem exigir que esteja equipado. Não corta nem quebra galhos; nenhuma ação de galho com martelo foi incluída. Auxílio à construção é futuro e ainda não foi implementado.
- A faca é a única ferramenta de corte de galhos: corta e coleta galho caído em um movimento. Com um galho equipado, Alt+C oferece “Quebrar galho em gravetos” somente se o jogador tiver uma faca de pedra em algum espaço do inventário (não precisa equipá-la); a ação revalida a faca ao ser executada, consome um galho e produz dois gravetos. A ação acomoda a saída em uma pilha de gravetos ou em espaço liberado pelo consumo; quando a capacidade não permite a saída, preserva o galho.
- Galhos e fibras vegetais são inflamáveis. A mira/alcance da faca e a capacidade do inventário são verificados antes da coleta; árvores, alvos rochosos e arbustos mantêm suas prioridades de interação.

### Verificação e validação

- Revisão estática de sintaxe JavaScript, receita, consumo, espaço de inventário, mira, alcance, posições dos dez galhos e prioridades. A mineração existente com martelo foi preservada.
- Teste manual de gameplay, TalkBack/leitor de tela, inspeção visual e audição dos sons não foram realizados. Publicar ou analisar o código não equivale a validação manual.


## 26 de outubro de 2026 — galhos baixos da copa cortáveis com faca

### Implementado no código

- A copa agora oferece dois resultados contextuais: sem faca equipada, os galhos continuam fornecendo gravetos como antes; com a faca de pedra nas mãos, olhar para cima e pressionar Espaço corta e coleta um galho da copa. O item recebido é `branch`, inflamável e compatível com as ações já existentes de inventário.
- A coleta checa alcance e espaço antes de adicionar o item; se o inventário não puder receber um tipo novo, o galho permanece intacto. O corte toca o efeito de colheita de graveto já disponível como feedback provisório. Galhos caídos mantêm seus dez pontos de coleta separados, e sua coleta com faca e a divisão de um galho em dois gravetos continuam sem alteração.
- A estrutura da árvore foi abaixada: cruzamento/galhos perto de 2,05 m e copa baixa por volta de 2,45–2,63 m, com topo em torno de 3,5 m. Alvos de coleta ficam em torno dos galhos baixos, ao alcance de uma pessoa no chão junto ao tronco ao inclinar o olhar para cima. A árvore continua escalável.
- Instruções do jogo e README distinguem o galho vivo da copa dos galhos caídos e explicam as duas ações condicionais. Regras de ferramentas permanecem: faca corta galhos; martelo somente minera afloramentos; a faca continua custando duas pedras no total.

### Verificação e validação

Revisar sintaxe JavaScript e estaticamente confirmar a seleção contextual, entrega de `branch`, bloqueio por inventário cheio, preservação da coleta de gravetos sem faca, das dez fontes de galhos caídos e da mineração exclusiva por martelo. Gameplay, altura real de alcance, leitor de tela e áudio ainda precisam de teste manual; o efeito de corte usa o WAV de colheita já existente, ainda não avaliado auditivamente nesta alteração. Nenhuma release, tag ou backup foi alterado.


## 26 de outubro de 2026 — preservar escalada ao baixar galhos de coleta

### Implementado no código

- Separadas as alturas dos recursos baixos da copa (2,05 e 2,35 m) da altura do patamar de escalada (2,75 m). A pessoa pode continuar coletando gravetos do chão sem faca ou cortar um galho vivo com faca equipada, mirando para cima perto do tronco.
- Reconstruído o cruzamento alto de galhos como patamar distinto; o tronco ainda agarra, W sobe até o patamar, o movimento pelos galhos e a ação de segurar nas pontas para descer com S permanecem. A silhueta da copa continua incluindo galhos altos.
- Instruções dentro do jogo e README atualizados para explicar as duas rotas: coleta do chão e escalada até o patamar alto.

### Verificação e validação

A sintaxe, a altura alcançável, o patamar de escalada e os ramos de interação serão verificados estaticamente. É necessário ainda testar manualmente agarre, subida completa, movimentação nas pontas, descida, coleta baixa com/sem faca e leitor de tela. Não tratar revisão estática como playtest.


## 26 de outubro de 2026 — cinzas de fogueiras apagadas

### Direção aprovada

- Fogueiras apagadas não podem ser reacendidas. Cada fogueira que se extingue deixa cinzas no local como recurso destinado a ajudar no futuro sistema de plantio.
- Anderson confirmou que as cinzas são um item do inventário e que cada pilha rende uma unidade.
- Não foi aprovado nenhum uso atual, receita ou plantio com cinzas; não adicionar funcionalidade além da coleta.

### Implementado no código

- Ao extinguir-se, cada fogueira cria uma única pilha visual e descritível de cinzas no local.
- A pilha é recolhida com Enter quando o jogador mira e está a até 2 m; a ação adiciona uma cinza ao inventário e remove a pilha do cenário. Se o inventário não tiver espaço, a pilha permanece.
- Cinzas foram adicionadas como tipo de item não inflamável, sem peso definido e sem ação de uso. O anúncio identifica o alvo, informa alcance ou inventário cheio quando necessário e confirma a coleta.
- Mensagens de criação e de descrição da fogueira apagada agora deixam claro que ela não pode ser reacendida e que suas cinzas podem ser recolhidas. A descrição de olhar também identifica cinzas próximas.
- Atualizado o README para registrar regras e limite de uso atual.

### Verificação e validação

- Revisão estática confirma criação uma vez por fogueira, inclusão no inventário, coleta única, preservação da pilha em caso de inventário cheio, suporte à descrição e integração da interação por Enter.
- Sintaxe e comportamento em gameplay, leitor de tela, prioridade da mira quando há alvos concorrentes e apresentação visual/auditiva ainda exigem teste manual; não foram avaliados. Nenhuma release, tag ou backup foi alterado.


## 26 de outubro de 2026 — anúncios concisos da fogueira

### Direção aprovada

- A confirmação de criação anuncia somente “Fogueira simples acesa.”
- Ao olhar para a fogueira, a estimativa do combustível é qualitativa, sem quantidade exata de segundos.

### Implementado no código

- A confirmação de criação foi encurtada à frase aprovada.
- As descrições ao olhar para a fogueira, olhando para baixo ou horizontalmente, com o alvo central ou fora do centro, não anunciam segundos exatos. A descrição compara o combustível restante ao limite máximo: acima de um terço, “acesa; as chamas estão altas”; com um terço ou menos, “acesa; o fogo deve apagar em breve”. Fogueira apagada continua descrita como apagada.
- README atualizado para registrar a informação qualitativa e a confirmação concisa.

### Verificação e validação

- Revisão estática confirma que todas as variações de olhar usam a mesma estimativa qualitativa e que a confirmação e estado apagado permanecem distintos.
- Playtest e validação com leitor de tela ainda não foram feitos.


## 26 de outubro de 2026 — criar fogueira perto de outra

### Direção aprovada

- O jogador pode escolher criar outra fogueira mesmo se já houver uma acesa ou apagada por perto. A presença de uma fogueira não bloqueia a criação.
- Criar outra fogueira continua exigindo os requisitos já existentes, incluindo gravetos suficientes e terreno seco. Fogueiras apagadas continuam sem poder ser reacendidas.

### Implementado no código

- Removida a restrição de proximidade tanto da execução quanto da disponibilidade da ação no menu. “Criar fogueira simples” permanece como ação separada de “Abastecer fogueira simples”; se ambas forem possíveis, o jogador pode escolher.
- README atualizado para esclarecer que o alcance de 2,4 m vale para abastecer e não impede construir outra fogueira em terreno seco.

### Verificação e validação

- Revisão estática confirma que criar fogueira já não consulta ou bloqueia por fogueiras próximas e que a ação de abastecer continua usando a fogueira acesa mais próxima dentro do alcance.
- Gameplay, leitor de tela e caso de múltiplas fogueiras próximas ainda precisam de teste manual.


## 26 de outubro de 2026 — dano e resistência de ferramentas e recursos

### Direção aprovada

- Cada acerto sorteia dano inteiro dentro da faixa da ferramenta e reduz a resistência da fonte; resistência nunca fica abaixo de zero e a fonte se esgota quando chega a zero. Os valores são abstratos, não medidas físicas.
- Faca de pedra, ferramenta de corte mais básica: dano 1–3. Martelo de pedra, ferramenta de impacto mais básica: dano 2–4. Galho caído: resistência 3; galho vivo: 6; afloramento rochoso: 12.
- Um galho caído de resistência 3 pode se esgotar num único golpe apenas quando o dano sorteado for 3; isso não é garantido.
- Mantidos rendimentos existentes: um galho por galho esgotado e 3 ou 4 pedras por afloramento, conforme definido para cada fonte.

### Implementado no código

- Incluídos sorteio uniforme de dano inteiro nas faixas aprovadas e resistência individual para galhos caídos, cada alvo baixo de galho vivo e afloramentos.
- Cada golpe reduz a resistência e anuncia dano e resistência restante. A fonte só é removida e entrega seu recurso ao chegar a zero; afloramentos mantêm deformação nos impactos e removem o bloqueio ao esgotar.
- Se não houver espaço para receber o rendimento, o golpe que esgotaria a fonte não é aplicado e a resistência fica preservada.
- Atualizados detalhes da faca e do martelo, descrições de afloramento e instruções antigas que afirmavam corte instantâneo ou quantidade fixa de golpes. README atualizado.

### Verificação e validação

- Revisão estática confirma faixas 1–3 e 2–4 inclusivas, limite inferior zero, dano sorteado por impacto, persistência da resistência entre golpes e preservação do recurso em caso de inventário cheio.
- Não houve playtest, teste com leitor de tela ou avaliação auditiva. Ainda precisam de validação a persistência dos alvos da copa, resultados variáveis, mineração, disputa de mira e inventário sem espaço.


### 27 de outubro de 2026 — correção do golpe final sem espaço

A revisão confirmou que o commit anterior não havia publicado o código do sistema de dano. O sistema aprovado e as atualizações de instrução foram integrados no `index.html` em commit próprio. Também corrigido o caso de inventário sem espaço: o dano é sorteado uma vez; se zeraria a resistência e não houver espaço, ele fica pendente, não reduz a resistência nem remove a fonte. Após liberar espaço, o mesmo resultado pendente é aplicado sem novo sorteio. As demais mudanças publicadas de coleta não foram substituídas. A implementação e as instruções estão publicadas; faltam playtest, validação com leitor de tela e avaliação sonora.


## 26 de outubro de 2026 — swoosh de golpe no ar ao falhar alvo de galho caído

### Mudança implementada

- A tentativa pela ação contextual de golpear um galho caído que não pode prosseguir por alvo/mira/alcance ou faca não anuncia mais a explicação longa. Ela toca um breve swoosh conceitual de golpe no ar.
- O swoosh é sintetizado com ruído filtrado e envelope curto no Web Audio, sem depender de arquivo ou serviço externo; a alteração não muda requisitos, consumo ou resultado de outros golpes.

### Validação

- Revisão estática confirma que a mensagem anterior foi removida desse ramo e o som é chamado apenas pela falha dessa ação contextual. Teste auditivo e validação com leitor de tela continuam pendentes.


## 26 de outubro de 2026 — pistas espaciais de fontes de recurso

### Implementado

- O gerador Python `tools/generate_sounds.py --resource-locators-only` cria cinco WAVs mono curtos e distintos: pedra, planta/arbusto, galho, cinzas e fogueira, sem regravar os outros efeitos.
- V ou o botão acessível “Localizar fontes próximas” inicia uma varredura pontual das fontes ativas em até 22 m; as pistas tocam uma por vez, da mais próxima, com limite de 12 por varredura.
- Web Audio usa HRTF e posicionamento tridimensional, com o listener acompanhado pela posição e orientação do jogador. Fontes coletadas/esgotadas e cinzas antes da extinção não geram pista. A busca não toca continuamente.
- README e GDD foram complementados com controles e princípios de áudio espacial acessível.

### Verificação e validação

- Gerador Python executado: cinco WAVs mono, 24 kHz, 0,24 s cada. Revisão estática confirma que a varredura usa fontes posicionadas e estado ativo.
- Ainda falta o teste auditivo e validação espacial pelo usuário, inclusive compatibilidade prática com leitor de tela. Não considerei a revisão estática como aprovação qualitativa.


## 27 de outubro de 2026 — pistas de recurso ao se aproximar

- A varredura manual (V/botão) foi removida por não ser útil.
- Pistas de pedra, arbusto, galho vivo/caído, cinzas e fogueira acesa agora disparam automaticamente ao entrar num raio de 6,5 m; cada fonte só rearma depois de afastamento a 8 m e nova aproximação. Intervalo global mínimo de 850 ms entre pistas.
- Antes de tocar, uma raycast do jogador à fonte verifica se ela é visível como primeira interseção; objetos mais próximos prevalecem, seguindo a prioridade de elementos visíveis. Pista usa HRTF no ponto real da fonte, auxiliando a localizar e virar na direção correta.
- Verificação estática confirma remoção do botão/tecla de varredura e uso do sistema de prioridade/visibilidade. Falta teste de gameplay, percepção auditiva/direção/distância e leitor de tela pelo Anderson.


## 27 de outubro de 2026 — repetição de pistas e dois timbres de recurso

- Corrigida a sinalização que dependia apenas da primeira aproximação: a pista volta a tocar a cada 3,8 segundos enquanto a fonte estiver próxima e visível segundo a prioridade, com intervalo global para evitar sobreposição.
- Separados dois timbres: som mais claro/agudo para item diretamente coletável; som grave/áspero para fonte que exige extração/ferramenta. Pedras soltas, arbustos e cinzas são coletáveis; galhos caídos/vivos e afloramentos são fontes de extração.
- Atualizado `tools/generate_sounds.py --resource-locators-only`, que gera somente `locate-collectible.wav` e `locate-extractable.wav`, sem regravar outros sons.
- Não houve avaliação auditiva do usuário; diferença perceptiva entre os timbres e espaçamento das repetições continuam aguardando validação.


## 27 de outubro de 2026 — frequência das pistas e visibilidade do alvo

- Ajustado o intervalo global e por fonte das pistas espaciais para 1 segundo, mantendo o alcance de 6,5 m e a prioridade entre recursos próximos.
- A descrição acessível agora associa os alvos de coleta às suas próprias malhas; a verificação de obstrução ignora somente as malhas pertencentes ao alvo descrito. Objetos distintos mais próximos continuam bloqueando a descrição e as pistas, sem tornar toda uma categoria transparente.
- Para os galhos vivos, a associação usa a geometria de galho baixo mais próxima, sem dispensar a oclusão por outros elementos da árvore.
- Validação realizada: revisão estática das alterações, comparação da base remota e verificação de sintaxe pendente. Não foram feitos testes manuais de gameplay, leitor de tela nem avaliação auditiva; esses testes permanecem para o usuário.


## 27 de outubro de 2026 — alinhamento entre som espacial e alvo visível

- Pistas de pedras, arbustos, galhos, cinzas e afloramentos passaram a usar o centro do volume delimitador das malhas 3D do próprio recurso. O mesmo ponto é usado pela descrição ao olhar, mantendo direção sonora e alvo anunciado alinhados.
- A checagem de oclusão continua ignorando somente as malhas que constituem o alvo selecionado; outros elementos mais próximos ainda o ocultam e preservam a hierarquia. Alvos dos galhos baixos da árvore usam o mesh específico do galho de coleta, não a árvore inteira.
- Pistas repetem a cada segundo conforme a publicação anterior. A validação geral do estado pelo Anderson foi registrada na entrada de 27 de outubro sobre atualização dos documentos e backup; não se atribui aprovação individual a cada som ou cenário.


## 27 de outubro de 2026 — manter a origem da pista e descrever coletáveis no chão

- A pista atual fica vinculada à fonte que a acionou; fontes vizinhas não roubam os beeps seguintes enquanto o jogador continuar perto da fonte inicial. Isso evita que panning/volume aparente recuar ou saltar quando o jogador está caminhando para ela. O vínculo é liberado ao afastar-se a 8 m ou quando a fonte deixa de existir.
- A descrição de olhar para baixo agora verifica e anuncia pedras soltas, arbustos, galhos e cinzas visíveis, antes de retornar apenas o nome do chão/terreno. Assim, ao virar na direção do som, itens pequenos no solo são considerados pelo canal acessível.
- O intervalo sonoro continua em 1 s. É necessário testar no jogo real se o panning fica coerente ao avançar e se cada item é de fato anunciado na mira, além de validar com leitor de tela.


## 27 de outubro de 2026 — atualizar os documentos e criar backup de teste

### Estado documentado

- README, GDD e DEVLOG atualizados para refletir os comportamentos publicados de pistas espaciais, continuidade da origem, descrição de coletáveis ao olhar para baixo, regra de criação de fogueiras próximas e estado de validação. Corrigido no README um trecho que continha separadores de parágrafo literais em vez de quebras de linha.
- Anderson informou que testou o estado publicado e considerou que chegou a um ponto confortável para atualizar documentos e backup. O registro não presume resultados mais específicos do que essa confirmação geral.
- Criado backup datado deste snapshot após a atualização dos documentos. Os backups anteriores permanecem preservados e sem alteração. Nenhuma release estável foi declarada.


## 27 de outubro de 2026 — confirmação do teste e atualização do backup

- Anderson informou que havia testado o estado publicado e que chegamos a um ponto confortável para atualizar os documentos e o backup.
- Esta confirmação corrige o registro anterior, que havia tratado a validação manual como pendente por não ter inferido o teste a partir do pedido de atualização. O estado testado é o publicado com pistas automáticas a cada segundo, origem espacial estável durante a aproximação e descrição ampliada dos coletáveis no olhar para baixo.
- O registro não inventa resultados por item ou uma aprovação universal de todos os sons; registra somente que Anderson testou a versão e a considerou suficientemente confortável para atualizar.
- README, GDD e este DEVLOG passam a refletir essa confirmação. O backup de 27 de outubro será atualizado para apontar para este estado documental corrigido; os backups anteriores continuam intactos.


## 27 de outubro de 2026 — mensagem curta para galho sem espaço no inventário

- Nas tentativas de golpe que esgotariam um galho caído ou vivo sem espaço para guardá-lo, o anúncio passa a ser apenas “Sem espaço no inventário.”
- A regra de preservar a resistência e o dano pendente do golpe permanece inalterada; nenhuma mensagem de falta de espaço de outras ações foi modificada.
- A mudança foi publicada no Pages. Não altera release, tag ou backup.


## 27 de outubro de 2026 — galhos caídos são itens recolhíveis

- Corrigida a distinção de design: galho caído no chão é um item recolhível, não uma fonte que deve ser golpeada. Pode ser recolhido com Espaço ou Enter, sem faca; a coleta exige alcance de 2,2 m e espaço no inventário.
- Removidos o estado de resistência dos galhos caídos, a ação contextual de golpear com faca e a classificação deles como fontes de extração. Pistas sonoras passam a identificá-los como coletáveis.
- A rotina de coleta remove o galho do cenário somente depois de guardar o item; sem espaço, o galho permanece no chão.
- Somente os galhos vivos que ainda estão na árvore precisam ser cortados com a faca equipada, com resistência 6 e dano por golpe de 1–3. A conversão de um galho recolhido em dois gravetos com faca no inventário continua sendo ação distinta.
- README, GDD e instruções acessíveis do jogo atualizados. Entradas históricas que descrevem os galhos caídos como golpeáveis registram o comportamento antigo, substituído por esta decisão.
- Publicado para teste no Pages; nenhuma release, tag ou backup foi alterado.


## 27 de outubro de 2026 — galho caído coleta-se somente com Enter

- Corrigida a interação: recolher itens do cenário é função de Enter; Espaço executa a ação correspondente ao item equipado. Galho caído permanece recolhível, mas sai da ação de Espaço e é coletado somente por Enter.
- Galhos vivos que ainda estão na árvore continuam sendo cortados pela ação de Espaço com a faca equipada.
- README e instruções do jogo atualizados para manter essa separação de controles.


## 27 de outubro de 2026 — Enter coleta; Espaço usa o item equipado

- Anderson esclareceu a regra dos controles: itens do cenário são coletados com Enter; Espaço realiza a ação do item equipado.
- Ajustado o fluxo de Espaço para não recolher galhos caídos, arbustos ou pedras soltas. Os galhos caídos são recolhidos somente com Enter, inclusive com outro item equipado; galhos vivos da árvore ainda podem ser cortados com a faca equipada e Espaço. A mineração de afloramentos com martelo também permanece uma ação de Espaço.
- README e GDD alinhados a essa separação de controles.


## 27 de outubro de 2026 — remover aviso de alcance do galho da copa

- Removido apenas o anúncio “O galho da copa está fora de alcance; aproxime-se da árvore e olhe para cima.” Se o alvo da copa estiver além do alcance, a ação de Espaço não prossegue e não anuncia esse aviso.
- O requisito de alcance permanece; golpes em galhos vivos dentro de alcance mantêm o comportamento existente.


## 27 de outubro de 2026 — fluxo normal sem instruções de comandos

- Removidas do fluxo normal as falas que ensinavam combinações de teclas, mira, alcance, receitas ou requisitos para executar uma ação. Condições não atendidas deixam de narrar instruções; os guards e os requisitos mecânicos permanecem.
- Mantidos descrições de olhar, estados do ambiente, resultados de ações, danos/progresso, falta de espaço e confirmações concisas. Não foi criado um tutorial nem uma nova tela de ajuda.
- Removidos do menu contextual os parágrafos explicativos de requisito; a lista ainda apresenta os nomes das ações e seu estado disponível/indisponível.
- Atualizado o texto inicial de estado para não apresentar comandos.
- Publicado para teste; sem alterar release, tag ou backup.


## 27 de outubro de 2026 — corrigir Enter e ampliar a prioridade de descrição dos coletáveis

- Corrigido o filtro do Enter: o foco no botão Inventário já não impede a tentativa de recolher item no cenário. O alvo é escolhido entre itens coletáveis dentro de 2,2 m pelo alinhamento mais forte da mira; a árvore claramente mais alinhada continua com prioridade.
- O cálculo usa o centro dos meshes para pedras, cinzas, arbustos e galhos caídos, mantendo mira, descrição e posição física consistentes.
- A descrição para baixo abrange a maior parte do enquadramento e informa primeiro o coletável visível. A descrição horizontal também verifica recursos antes de devolver descrições genéricas do terreno. Elementos distintos continuam sujeitos à oclusão.
- Revisão estática confirmou a presença dos alvos e a remoção do bloqueio do botão Inventário. O código foi publicado; confirmação em gameplay do Anderson ainda é necessária.


## 27 de outubro de 2026 — refinar alcance e foco da coleta com Enter

- A seleção com Enter agora usa a origem geométrica efetiva de cada coletável e filtra cada alvo pelo alcance próprio antes de escolher; um item fora de alcance não encobre outro elegível.
- O foco no botão Inventário permanece compatível com a coleta; o Enter não abre o painel pelo botão, mas tenta coletar um item alinhado no cenário.
- Revisada a descrição do olhar para baixo e horizontal para priorizar recursos visíveis numa região maior do enquadramento; a checagem de oclusão continua ativa.
- Páginas/documentos publicados; teste manual de gameplay ainda necessário para confirmar a experiência percebida.


## 27 de outubro de 2026 — ampliar levemente a tolerância de mira

- A tolerância angular comum para interações com objetos passou de 60° para 65° em relação à câmera.
- Alcance físico, prioridades de seleção, oclusão, controles e movimentação permanecem inalterados.


## 27 de outubro de 2026 — pista grave junto à árvore

- Recursos disponíveis na árvore agora usam o beep grave de fonte coletável, pois a árvore fornece gravetos e galhos. As demais fontes de extração mantêm seu timbre próprio.


### 27 de outubro de 2026 — confirmar coleta e ações por áudio


- Adicionados padrões sonoros diferentes: duas notas ascendentes para coleta bem-sucedida e outra dupla para ação bem-sucedida do menu contextual.
- Aplicados aos coletáveis do cenário e às receitas, criação/abastecimento de fogueira; resultados bloqueados e inventário cheio não recebem confirmação falsa.
- O som só é disparado após iniciar o contexto de áudio por gesto do usuário, incluindo Enter e a ativação de ação no menu.


## 27 de outubro de 2026 — revisar mensagem ao entrar na água rasa

- Substituída a mensagem “O fundo permite caminhar”, que confundia a condição do fundo com a ação do jogador, por “Você entrou na água rasa do lago.” A caminhada rasa continua explicada na descrição do mapa/tutorial, sem atribuir a ação ao fundo.


## 27 de outubro de 2026 — avisos de contato e robustez do leitor de tela

- Adicionada fala pontual ao entrar no alcance real de um objeto interativo, anunciando seu nome; mudanças de alvo geram novo anúncio, ficar parado não repete.
- Separado o texto visual da região aria-live. Para repetir a mesma mensagem, a região viva é limpa e atualizada após 75 ms, em vez de anexar um espaço à frase; isso melhora as atualizações repetidas de coordenadas e campo de visão.
- Mantidas as mensagens visíveis, regras de interação e distâncias de alcance existentes.


## 27 de outubro de 2026 — anúncio de contato apenas com o nome

- O anúncio ao entrar no alcance de interação agora fala somente o nome do objeto, sem explicações ou frases adicionais.
