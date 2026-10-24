# Phoenix Island — protótipo acessível de caminhada e natação 3D

Protótipo web em primeira pessoa para testar movimentação, olhar e pistas sonoras num mapa 3D de 36 × 36 m, com colina, árvore e lago. A cena usa Three.js e WebGL; céu, texturas e detalhes da vegetação são gerados proceduralmente no navegador, sem arquivos de arte externos. Este ainda não é o jogo nem implementa sistemas completos de RPG ou sobrevivência.

## Mapa ampliado e lago

O campo passou de 24 × 24 m para 36 × 36 m, com X e Y entre −18 m e +18 m. A colina e a árvore mantêm suas posições no setor central; a colina tem descida posterior até o terreno baixo. O lago elíptico fica ao norte e a leste, centrado em X=5,0 m, Y=13,2 m, com dimensões de água de aproximadamente 12 × 6,4 m. Uma faixa de terreno lamacento, com cerca de 1,2 m de largura, envolve a margem.

Dentro do lago, a faixa rasa contorna todo o perímetro e permite caminhar sobre um fundo que chega a cerca de 0,55 m abaixo do terreno. Em seguida, o fundo desce para uma bacia central de até 2,7 m. A região profunda bloqueia o avanço a pé. Com as mãos vazias, o jogador pode iniciar a natação na faixa rasa ao pressionar Espaço enquanto o corpo está voltado para a região profunda. A natação funciona no lago deste protótipo.

A superfície agora muda gradualmente de tom conforme a profundidade, recebe ondas muito suaves em shader e mostra ondulações circulares de baixa densidade quando o jogador caminha na água rasa ou nada à superfície.

## Natação e saídas

A entrada exige mãos vazias, estar na faixa rasa caminhável e apontar o corpo para água profunda; então Espaço inicia a natação na superfície. W/S avançam ou recuam na direção do corpo e acompanham a inclinação do olhar: apontar para baixo conduz para baixo, apontar para cima conduz para cima e o horizonte mantém a altitude. A/D deslocam lateralmente sem mudar a altitude. A velocidade de natação é 1,5 m/s. A movimentação respeita a profundidade e mantém uma distância mínima do fundo; fora do contorno de água modelado, a margem bloqueia o avanço.

Para sair, mãos vazias, o jogador deve estar na superfície e perto da faixa rasa ou de uma saída terrestre indicada por um futuro marcador; Espaço então retorna à caminhada. A natação não termina automaticamente ao tocar a margem. Em água muito rasa, o fundo pode elevar o jogador até a superfície; essa transição é anunciada, e ainda é preciso pressionar Espaço para sair. Um conector subaquático marcado como destino de água mantém a natação e não produz beep de saída; uma saída marcada como terra permite sair apenas à superfície e com Espaço. Não há passagens subaquáticas no mapa atual.

Os beeps são marcadores, não uma bússola vertical: dois pulsos médios marcam o limite das águas profundas ao caminhar; três pulsos agudos marcam uma zona possível de saída enquanto nada; um pulso mais grave e longo marca a margem. Cada sinal toca ao entrar na respectiva zona, sem repetição periódica; ao sair e voltar, pode tocar de novo.

Mudanças de estado relevantes — entrada/saída, contato com fundo/superfície e bloqueio pela margem — são anunciadas sem fala por tecla ou por braçada. A inclinação do olhar continua informada ao ajustá-la.

## Estilo visual do protótipo

O cenário usa um céu em degradê, texturas procedurais de grama, solo e casca, folhagem em grupos de formas facetadas, raízes e pequenos tufos de grama. A colina chega a 1,8 m (não 5 m) e agora varia de tom com a altitude; as sombras da colina ficam ativas e há uma sombra de contato suave sob a árvore. A margem já tem uma faixa texturizada de lama, e a água agora desaparece mais suavemente na borda rasa antes de ganhar densidade no fundo. A árvore já tem tronco cilíndrico, raízes, galhos e oito grupos de copa; esta passagem não adiciona novas pedras ou troncos que pudessem sugerir obstáculos sem colisão e sinalização. Os detalhes continuam sendo criados em código, sem imagens ou modelos de arte baixados; são uma direção visual provisória, não arte final.

## Inventário

Pressione **I** ou o botão **Inventário (I)** para abrir o inventário. A janela pausa o movimento, recebe o foco e pode ser fechada com **I**, **Esc** ou o botão de fechar. O inventário começa vazio e tem dez espaços para tipos diferentes de item, apresentados em duas fileiras de cinco. Use as setas para navegar por todos os espaços, vazios ou ocupados; esquerda/direita percorrem a fileira sem voltar à outra ponta, cima/baixo mudam de fileira, e Home/End selecionam o primeiro/último espaço da fileira atual. A navegação não anuncia qual espaço está focado nem seu número. **Enter** abre as ações de um item ocupado e move o foco para Examinar; o botão visível **Ações (Enter)** é uma alternativa equivalente. Com o foco na lista vertical de ações, use as setas para cima/baixo para percorrê-la (as extremidades se conectam); Home/End vão à primeira/última ação. Enter ou Espaço ativa a ação focada, usando os mesmos controles; Esc retorna à grade. Em espaço vazio, Enter não executa ação nem produz anúncio. Esc fecha ações e retorna à grade; Esc na grade fecha o inventário. Itens iguais acumulam sem limite artificial de pilha; um item de tipo novo só é recusado quando todos os dez espaços estão ocupados. Graveto é o primeiro item coletável, marcado como inflamável. Examinar informa propriedades; o peso unitário está explicitamente não definido e ainda não há limite de carga. Bolsas e mochilas não estão implementadas.

Selecione um espaço e escolha **Examinar**, **Mover**, **Usar**, **Largar** ou **Atribuir atalho**. Mover para espaço vazio transfere; mover para item igual agrupa; mover para tipo diferente troca os espaços. Usar equipa ou guarda o item nas mãos; neste protótipo isso não consome o item nem implementa efeito próprio do graveto. Com item equipado, Espaço apenas informa que o efeito ainda não existe, e a natação continua exigindo mãos vazias. Atribua uma tecla numérica de 1 a 0: pressioná-la fora do inventário equipa ou guarda o item daquele espaço. Cada tecla fica associada ao tipo de item e continua funcionando se ele for movido. A mesma tecla pode ser reassociada a outro item. Um tipo pode ter mais de uma tecla. Equipar/guardar só é possível no chão, sem nadar ou estar agarrado à árvore. Números não são atalhos enquanto o foco estiver em campo de formulário.

Largar cria uma entrada recuperável na lista de itens largados; o botão **Recolher itens largados** recolhe o que couber no inventário. Este é um coletor acessível global, não uma posição física de chão, e não cria objeto 3D nem colisão invisível.

## Testar

Abra a página publicada no GitHub Pages. O navegador precisa permitir WebGL e carregar o módulo Three.js hospedado no jsDelivr. O áudio é liberado depois da primeira tecla de movimento ou Espaço, conforme a política dos navegadores.

## Controles

- W: avançar na direção do corpo; norte quando começa na orientação inicial.
- S: recuar na direção oposta ao corpo; sul na orientação inicial.
- A/D: deslocar lateralmente à esquerda/direita, sem girar o corpo.
- Shift direito + W: correr para frente a 3,6 m/s; + A/D: correr lateralmente a 3,2 m/s; + S: correr para trás a 2,4 m/s. Shift direito também pode ser pressionado depois de iniciar o movimento. Ao soltá-lo, retorna à velocidade de caminhada de 2,4 m/s. Corrida não se aplica à escalada nem aos galhos.
- Shift esquerdo+A/D: girar o corpo 45° para a esquerda/direita, sem caminhar; o sistema anuncia para qual direção o corpo ficou voltado.
- Shift esquerdo+W: girar o corpo 180°, sem caminhar; o sistema anuncia para qual direção o corpo ficou voltado (norte, nordeste, leste, sudeste, sul, sudoeste, oeste ou noroeste).
- Shift esquerdo+S: recuo rápido de cerca de 1,35 unidade, equivalente a alguns passos para trás.
- Setas esquerda/direita: desviar o olhar em passos de 15°, até ±45° em relação ao corpo. No limite, o olhar para; use Shift esquerdo+A/D ou Shift esquerdo+W para virar o corpo.
- Setas cima/baixo: inclinar o olhar em passos de 15°, até ±30°. Durante a natação, a inclinação direciona W/S para cima/baixo enquanto a tecla é mantida; em posição horizontal, a profundidade permanece estável. Alterar o olhar sem manter W/S não movimenta o personagem.
- C: anunciar X/Y no plano e Z como altitude-base, em metros com duas casas decimais. A referência humana atual usa altura ocular de 1,60 m, definida no perfil de percepção. O modelo do jogo é X/Y/Z; na renderização, o Three.js converte (X, Y, Z) para (X, Z, -Y).
- Espaço: usa o item em mãos. Com mãos vazias, na faixa rasa e voltado para águas profundas, inicia a natação. Para sair da natação, mãos vazias, esteja na superfície e perto da faixa rasa ou de uma saída terrestre e pressione Espaço; o modo não termina automaticamente ao tocar a margem. Na faixa rasa e sem estar nadando, perto da árvore, olhar para o tronco agarra; olhar para um galho ou copa ao alcance extrai um graveto e o adiciona ao inventário. Se os dez tipos distintos ocuparem todos os espaços, a coleta é recusada com anúncio. Em árvores com frutos, mire o fruto específico; se estiver fora de alcance, aproxime-se da posição dele ou suba. A árvore deste teste não tem frutos. Espaço solta enquanto estiver segurando a árvore.
- Ao segurar o tronco ou a ponta do galho, W/S produzem impulsos ritmados de subida/descida, cerca de um a cada 0,43 s enquanto a tecla estiver mantida; soltar interrompe o movimento.
- A subida termina automaticamente no cruzamento dos galhos. Sobre os galhos, W/S/A/D permitem caminhar até uma ponta; pressione Espaço para se segurar e use S para descer. Espaço também solta e retorna ao chão.

No chão, W/S seguem a frente e a parte de trás do corpo; A/D são deslocamentos laterais. As teclas de movimento só giram o corpo quando usadas com Shift esquerdo conforme a lista acima. O rumo do olhar é informado separadamente do rumo da caminhada; “à esquerda” e “à direita” referem-se sempre à posição de um objeto no campo de visão, não à caminhada. Os anúncios são expostos numa região acessível para leitor de tela e começam diretamente com a informação, sem repetir um rótulo genérico; caminhar não narra cada tecla ou passo. Soltar a tecla ativa interrompe o deslocamento.

O tronco bloqueia a caminhada: não é possível subir simplesmente caminhando contra ele. A colina tem largura modelada entre X = −2,1 m e X = +2,1 m; o terreno para além das laterais é plano e caminhável, permitindo contorná-la. Não há paredes invisíveis nas laterais. Outros bloqueios não identificados recebem um aviso geral, em vez de interromper o movimento silenciosamente.

## Percepção vertical — teste inicial

Cada ator usa um perfil de percepção com altura ocular própria e campo vertical. O perfil humano atual usa olhos a 1,60 m da base e campo vertical de 68°. Para um ponto-alvo, o protótipo calcula o ângulo de elevação com `atan2(Z_alvo - Z_olhos, distância_horizontal)` e o compara com a inclinação atual do olhar.

A linha entre os olhos e o alvo é verificada contra a função numérica de altitude do terreno, em amostras de até 1 cm. O alvo é bloqueado se o relevo ultrapassar a linha de visão por mais de 1 cm. Assim, o limite angular e a oclusão pelo relevo são testes separados; o alcance máximo continua independente. Nesta etapa, o filtro é aplicado aos pontos de interesse que o sistema acessível já examina, não a um sistema completo de descoberta do mundo.

## Pistas sonoras provisórias

- Caminhada na grama: quatro variações curtas e mais distinguíveis, com diferenças de impacto, contato da ponta e ruído vegetal; os níveis médios foram mantidos próximos e a seleção evita repetição imediata.
- Caminhada na água rasa: quatro variações sintetizadas de impacto molhado, respingo e pequena ondulação; usadas somente na faixa caminhável do lago, sem repetição imediata.
- Margem lamacenta: quatro variações próprias de passos, separadas dos passos de grama e água rasa.
- Natação: quatro variações de braçada à superfície, quatro de bolhas submersas e efeitos de entrada e saída. Os bipes marcam somente a borda da água profunda, a zona possível de saída e a margem; cada um toca ao entrar na respectiva zona, sem repetição periódica nem instrução vertical.
- Caminhada sobre os galhos: três variações de contato de madeira, separadas das pisadas no chão.
- Cadência no terreno: caminhando, intervalo de 0,43 s no plano, 0,52 s subindo e 0,36 s descendo; correndo, 0,30 s, 0,37 s e 0,27 s, respectivamente. A direção é calculada pela diferença de altitude nos próximos 0,75 m, com limiar de 0,035 m; o recuo rápido mantém 0,23 s. A cadência ajusta apenas os sons; Shift direito altera a velocidade de deslocamento para 3,6 m/s.
- Subida e descida da colina: pistas ressonantes ascendentes ou descendentes, sincronizadas aos passos no terreno inclinado.
- Limite do campo: alerta pulsante uma vez por passo ao caminhar na direção da borda; ao tocá-la, dois impactos curtos confirmam o contato. No máximo um aviso direcional é tocado por passo, e os alertas não usam temporizador independente.
- Coleta de graveto: estalo seco seguido de um roçar breve de folhas.
- Escalada: agarrar e soltar com fricção abafada; subir e descer com contatos ritmados diferentes; apoiar-se no galho ou no chão com rangido leve. Esses efeitos foram preservados sem alteração.

Os efeitos são sintetizados em Python e continuam provisórios; ainda precisam de avaliação auditiva e refinamento. Para regenerar os WAVs: `python3 tools/generate_sounds.py`.
