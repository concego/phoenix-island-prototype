# Phoenix Island — protótipo de caminhada 3D

Protótipo web em primeira pessoa para testar movimentação, olhar e pistas sonoras num pequeno campo 3D com uma colina e uma árvore. A cena usa Three.js para renderizar com WebGL. Este ainda não é o jogo nem implementa sistemas de RPG ou sobrevivência.

## Testar

Abra a página publicada no GitHub Pages. O navegador precisa permitir WebGL e carregar o módulo Three.js hospedado no jsDelivr. O áudio é liberado depois da primeira tecla de movimento, conforme a política dos navegadores.

## Controles

- W: virar para norte e caminhar enquanto estiver pressionada.
- S: virar para sul e caminhar enquanto estiver pressionada.
- A: virar para oeste e caminhar enquanto estiver pressionada.
- D: virar para leste e caminhar enquanto estiver pressionada.
- Setas esquerda/direita: olhar lateralmente a partir da posição atual.
- Setas cima/baixo: olhar para cima/baixo sem deslocar o personagem.
- C: anunciar as coordenadas atuais X, Y e Z em unidades do cenário.

As direções de movimento são fixas nos eixos do cenário; A e D não são strafe. A descrição separa o rumo do olhar da direção selecionada para caminhar; “à esquerda” e “à direita” referem-se sempre à posição de um objeto no campo de visão, não à caminhada. As setas para cima/baixo descrevem o que está no centro da visão vertical. A descrição aparece numa região acessível para leitor de tela. Ao trocar uma tecla de movimento pela oposta, ela substitui a direção anterior; soltar a tecla ativa interrompe o deslocamento, sem retomar automaticamente uma tecla anterior.

## Pistas sonoras provisórias

- Passos durante a caminhada.
- Tom agudo ao iniciar movimento subindo a colina.
- Tom grave ao iniciar movimento descendo a colina.
- Alerta pulsante cuja altura aumenta ao se aproximar dos limites do campo.
- Sinal de dois tons descendentes ao alcançar um limite. O sinal e a descrição acessível do limite são emitidos uma vez até o personagem voltar a se mover dentro do campo.

Os WAVs de passos, inclinação e limite foram sintetizados em Python para validação. São sons provisórios, não a mixagem final do jogo.

Para regenerar os WAVs: `python3 tools/generate_sounds.py`.
