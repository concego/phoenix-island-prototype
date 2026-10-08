# Phoenix Island — protótipo de caminhada 3D

Protótipo web em primeira pessoa para testar movimentação, olhar e pistas sonoras num pequeno campo 3D com uma colina e uma árvore. A cena usa Three.js e WebGL; céu, texturas e detalhes da vegetação são gerados proceduralmente no navegador, sem arquivos de arte externos. Este ainda não é o jogo nem implementa sistemas completos de RPG ou sobrevivência.

## Estilo visual do protótipo

O cenário usa um céu em degradê, texturas procedurais de grama, solo e casca, folhagem em grupos de formas facetadas, raízes e pequenos tufos de grama. Esses detalhes são criados em código, sem imagens ou modelos de arte baixados; continuam sendo uma direção visual provisória, não arte final.

## Testar

Abra a página publicada no GitHub Pages. O navegador precisa permitir WebGL e carregar o módulo Three.js hospedado no jsDelivr. O áudio é liberado depois da primeira tecla de movimento, conforme a política dos navegadores.

## Controles

- W: avançar na direção do corpo; norte quando começa na orientação inicial.
- S: recuar na direção oposta ao corpo; sul na orientação inicial.
- A/D: deslocar lateralmente à esquerda/direita, sem girar o corpo.
- Shift+A/D: girar o corpo 45° para a esquerda/direita, sem caminhar; a descrição acessível anuncia para qual direção o corpo ficou voltado.
- Shift+W: girar o corpo 180°, sem caminhar; a descrição acessível anuncia para qual direção o corpo ficou voltado (norte, nordeste, leste, sudeste, sul, sudoeste, oeste ou noroeste).
- Shift+S: recuo rápido de cerca de 1,35 unidade, equivalente a alguns passos para trás.
- Setas esquerda/direita: desviar o olhar em passos de 15°, até ±45° em relação ao corpo. No limite, o olhar para; use Shift+A/D ou Shift+W para virar o corpo.
- Setas cima/baixo: inclinar o olhar em passos de 15°, até ±30°. Para observar além desse limite, mude de posição.
- C: anunciar X/Y no plano e Z como altitude-base, em metros com duas casas decimais. A referência humana atual usa altura ocular de 1,60 m, definida no perfil de percepção. O modelo do jogo é X/Y/Z; na renderização, o Three.js converte (X, Y, Z) para (X, Z, -Y).
- Espaço: usa o item em mãos. Com mãos livres, perto da árvore, olhar para o tronco agarra; olhar para um galho ou copa ao alcance extrai um graveto e informa o total coletado. Em árvores com frutos, mire o fruto específico; se estiver fora de alcance, aproxime-se da posição dele ou suba. A árvore deste teste não tem frutos. Espaço solta enquanto estiver segurando a árvore.
- Ao segurar o tronco ou a ponta do galho, W/S produzem impulsos ritmados de subida/descida, cerca de um a cada 0,43 s enquanto a tecla estiver mantida; soltar interrompe o movimento.
- A subida termina automaticamente no cruzamento dos galhos. Sobre os galhos, W/S/A/D permitem caminhar até uma ponta; pressione Espaço para se segurar e use S para descer. Espaço também solta e retorna ao chão.

No chão, W/S seguem a frente e a parte de trás do corpo; A/D são deslocamentos laterais. As teclas de movimento só giram o corpo quando usadas com Shift conforme a lista acima. A descrição separa o rumo do olhar do rumo de caminhada; “à esquerda” e “à direita” referem-se sempre à posição de um objeto no campo de visão, não à caminhada. A descrição aparece numa região acessível para leitor de tela, mas caminhar não narra cada tecla ou passo. Soltar a tecla ativa interrompe o deslocamento.

O tronco também bloqueia a caminhada: não é possível subir simplesmente caminhando contra ele.

## Percepção vertical — teste inicial

Cada ator usa um perfil de percepção com altura ocular própria e campo vertical. O perfil humano atual usa olhos a 1,60 m da base e campo vertical de 68°. Para um ponto-alvo, o protótipo calcula o ângulo de elevação com `atan2(Z_alvo - Z_olhos, distância_horizontal)` e o compara com a inclinação atual do olhar.

A linha entre os olhos e o alvo é verificada contra a função numérica de altitude do terreno, em amostras de até 1 cm. O alvo é bloqueado se o relevo ultrapassar a linha de visão por mais de 1 cm. Assim, o limite angular e a oclusão pelo relevo são testes separados; o alcance máximo continua independente. Nesta etapa, o filtro é aplicado aos pontos de interesse que a descrição acessível já examina, não a um sistema completo de descoberta do mundo.

## Pistas sonoras provisórias

- Caminhada na grama: quatro variações curtas de impacto macio e ruído vegetal; a escolha varia para reduzir a repetição.
- Caminhada sobre os galhos: três variações de contato de madeira, separadas das pisadas no chão.
- Subida e descida da colina: pistas ressonantes ascendentes ou descendentes, sincronizadas aos passos no terreno inclinado.
- Limite do campo: alerta pulsante uma vez por passo ao caminhar na direção da borda; ao tocá-la, dois impactos curtos confirmam o contato. No máximo um aviso direcional é tocado por passo, e os alertas não usam temporizador independente.
- Coleta de graveto: estalo seco seguido de um roçar breve de folhas.
- Escalada: agarrar e soltar com fricção abafada; subir e descer com contatos ritmados diferentes; apoiar-se no galho ou no chão com rangido leve. Esses efeitos foram preservados sem alteração.

Os efeitos são sintetizados em Python e continuam provisórios; ainda precisam de avaliação auditiva e refinamento. Para regenerar os WAVs: `python3 tools/generate_sounds.py`.
