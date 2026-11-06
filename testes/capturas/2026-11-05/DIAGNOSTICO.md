# Registro de capturas e diagnóstico visual — Phoenix Island

Este documento acompanha as imagens enviadas por Anderson para diagnóstico visual. Cada anotação registra o contexto que ele informou, o que é observável na captura, os limites de avaliação e as questões a investigar. Capturas não são, por si só, aprovação visual, prova de falha de gameplay ou autorização para mudar mecânicas.

As barras do Chrome e do sistema operacional que apareçam nas imagens são externas ao jogo. Não avaliá-las como interface de Phoenix Island. A única escrita visível permitida dentro do jogo nesta fase é feedback breve das ações do jogador.

## Capturas de 5 de novembro de 2026

### 01 — `01-interface-limpa.jpg` — 15:07

Captura após a primeira tentativa de limpar a interface. O jogo aparece em uma vista relativamente próxima, com céu e campo; partes de vegetação entram cortadas nas bordas e há uma forma escura isolada perto do horizonte. O enquadramento não mostra o mapa inteiro. Referência para o estágio inicial da limpeza da interface, não para a arte final.

### 02 — `02-cena-vista-geral.jpg` — 15:32

Captura enviada com “E agora?”. A moldura do Chrome ainda aparece. Usar a imagem como vista geral do estado daquela rodada; avaliar os elementos visíveis sem confundir navegador e jogo.

### 03 — `03-vista-ampla-mapa.jpg` — 16:09

Vista ampla enviada com a indicação de que esta era a última captura até então. O céu ocupa grande parte do enquadramento; aparecem terreno verde, tufos espaçados, arbustos distantes, lago oval e margem lamacenta regular. Foi observado também um grande disco pálido no céu; sua causa ficou em aberto e deve ser identificada no código/cena antes de qualquer alteração.

### 04 — `04-vista-panoramica.jpg` — 22:05

Vista panorâmica posterior. A composição volta a mostrar grande área de céu e terreno baixo; usar como evidência de outro enquadramento, não assumir que o círculo pálido esteja sempre visível.

### 05 — `05-vista-lago-arvore-colina.jpg` — 22:08

Vista conjunta de lago, árvore e colina. A árvore aparece estreita e simétrica, com tronco fino, volumes arredondados de copa e galhos retos expostos; a colina parece rampa regular e as pedras pequenas parecem alinhadas. A margem do lago também parece regular. Estas são impressões da imagem, não decisões de solução.

### 06 — `06-vista-complementar.jpg` — 22:09

Vista complementar enviada sem descrição adicional específica. Comparar com 05 e com as demais imagens da mesma sequência; não atribuir posição ou intenção de câmera além do que a captura permite identificar.

### 07 — `07-escalada.jpg` — 22:30

Anderson esclareceu que é um print durante a escalada. A copa e os galhos ocupam quase toda a vista. Avaliar como perspectiva normal de escalada e considerar se a folhagem/estrutura deixa leitura suficiente do movimento e do entorno; não classificar como clipping sem evidência.

### 08 — `08-patamar-superior.jpg` — 22:32

Anderson identificou como vista do topo/patamar após chegar ao alto da árvore. É perspectiva intencional elevada. Lago, margem e terreno se veem de cima; o galho/plataforma não aparece claramente no enquadramento. Não confundir com vista de chão ou erro de câmera.

### 09 — `09-ponta-galho-baixo.jpg` — 22:34

Anderson identificou como ponta da árvore olhando para baixo. Mostra a paisagem de cima e parte do galho/patamar junto à borda. Considerar essa perspectiva de gameplay para avaliar relação entre galhos e cenário.

### 10 — `10-ponta-galho-max-baixo.jpg` — 22:37

Ponta da árvore com o olhar totalmente para baixo. Permite avaliar de cima a superfície/encosta da colina, pedras, lago, lama, grama e arbustos. A face escura da colina chama atenção, mas a captura não identifica sua causa; investigar iluminação/material/geometria antes de concluir.

### 11 — `11-fundo-lago.jpg` — 22:38

Captura subaquática com o feedback “Você chegou ao fundo do lago.” A cena está quase toda coberta por grandes áreas azul e verde-escuras divididas por uma diagonal abrupta; a origem dessa forma não pode ser determinada só pela imagem. Investigar materiais, geometria, iluminação e névoa; preservar profundidade, colisão e regras de natação.

### 12 — `12-galho-caido.jpg` — 22:43

Anderson identificou como vista de galho caído no chão, olhando para baixo. O objeto não é distinguível com segurança entre tufos de grama nesta imagem. Diagnóstico: verificar se silhueta, escala, orientação e material do galho o separam visualmente da vegetação. Não presumir que esteja ausente nem que a coleta falhou.

### 13 — `13-pedra-topo.jpg` — 22:47

Anderson identificou como pedra no topo da colina. A pedra aparece apenas parcialmente, cortada pelo limite inferior; não é possível avaliar sua forma completa ou material. Para nova referência, enquadrar a pedra inteira com o terreno ao redor e distinguir se é afloramento ou pedra solta.

### 14 — `14-pedra-solta.jpg` — 22:49

Anderson identificou como pedra solta recolhível, diferente dos afloramentos. Aparece inteira, clara, sobre terreno gramado; destaca-se do solo, mas parece quase esférica/facetada e isolada. Considerar como torná-la reconhecível como pedra assentada no terreno, preservando a distinção funcional e sem alterar posição, coleta, colisão ou quantidade.

## Como usar este registro nas próximas rodadas

- Anderson pode enviar capturas no chat; adicioná-las em uma subpasta datada de `testes/capturas/` e acrescentar aqui uma entrada com nome do arquivo, hora/contexto, vista, observações e incertezas.
- Preservar o texto fornecido por Anderson sobre onde estava e para onde olhava; não reinterpretar uma perspectiva intencional como erro de câmera.
- Distinguir observação visual de hipótese técnica. Quando a imagem não determinar a causa, marcar para investigar no código, sem inventá-la.
- Para comparar refinamentos, registrar capturas em pontos e ângulos semelhantes; indicar o que mudou e quais vistas ainda faltam.
- Remover imagens somente quando já não forem necessárias para comparação/diagnóstico, conforme autorização de Anderson; manter a nota histórica se ainda for útil, ou removê-la junto da imagem se ele pedir limpeza completa.

## Atualização da outra conversa — refinamento subaquático (6 de novembro de 2026)

Anderson compartilhou o relato da outra conversa sobre a rodada no commit `0a93b6bedf242f95cc9c1fdd97c1e07b78507ced`: foram introduzidas variações de cor no leito entre as áreas rasa e profunda e uma transição gradual de névoa. Segundo o relato, a geometria do fundo e as regras de profundidade e natação foram preservadas no código. O DEVLOG registra a mudança.

O relato informa que a página carregou sem erros no console, mas que a vista no fundo ainda não foi comparada. Portanto, **não há confirmação de que a faixa diagonal da captura 11 desapareceu ou de que a leitura visual melhorou**. Também permanecem pendentes os testes de natação, saída e leitor de tela. A ausência de erro no console não substitui esses testes.

A versão informada para teste é https://concego.github.io/phoenix-island-prototype/?v=0a93b6b. A página abriu nesta conversa; a captura do fundo e a validação dos comportamentos ainda não foram realizadas aqui. O parâmetro de URL serve para atualização de cache e, por si só, não fixa uma versão histórica quando `main` avançar; para confirmar o código testado, conferir também o commit e o conteúdo publicado.

A captura `11-fundo-lago.jpg` é referência anterior para comparação, não comprovação do estado atual. Não foram alterados releases nem backups segundo o relato. Esta entrada é documentação da informação recebida, não validação do resultado.
