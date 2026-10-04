# Phoenix Island — protótipo de caminhada 3D

Protótipo web em primeira pessoa para testar movimentação, olhar e pistas sonoras num espaço 3D pequeno. A cena usa Three.js para renderizar com WebGL. Este ainda não é o jogo nem implementa sistemas de RPG ou sobrevivência.

## Testar

Abra a página publicada no GitHub Pages. O navegador precisa permitir WebGL e carregar o módulo Three.js hospedado no jsDelivr. O áudio é liberado depois da primeira tecla de movimento, conforme a política dos navegadores.

## Controles

- W: virar para norte e caminhar enquanto estiver pressionada.
- S: virar para sul e caminhar enquanto estiver pressionada.
- A: virar para oeste e caminhar enquanto estiver pressionada.
- D: virar para leste e caminhar enquanto estiver pressionada.
- Setas esquerda/direita: olhar lateralmente a partir da posição atual.
- Setas cima/baixo: olhar para cima/baixo sem deslocar o personagem.

As direções de movimento são fixas no cenário; A e D não são strafe. A descrição da direção central do olhar aparece na tela e numa região acessível para leitor de tela.

## Pistas sonoras provisórias

- Passos durante a caminhada.
- Tom agudo ao iniciar movimento subindo a encosta.
- Tom grave ao iniciar movimento descendo a encosta.
- Alerta pulsante cuja altura aumenta ao se aproximar da borda sul, onde não há descida segura.

Os WAVs de passos e de inclinação foram sintetizados em Python para validação. O alerta variável da borda é sintetizado em tempo real no navegador. São sons provisórios, não a mixagem final do jogo.

Para regenerar os WAVs: `python3 tools/generate_sounds.py`.
