# Phoenix Island — documento de design do jogo (GDD)

**Versão:** 0.3 — atualização de regras vigentes  
**Data:** 27 de outubro de 2026  
**Escopo:** direção de design para o protótipo acessível Phoenix Island  
**Estado:** documento de direção vigente; decisões aprovadas são registradas como regras, e decisões em aberto continuam pendentes

## 1. Propósito deste documento

Este GDD registra a intenção de design e os limites que devem orientar mudanças futuras em Phoenix Island. Serve para explicar o que preservar, o que evitar e como avaliar propostas novas.

O GDD descreve decisões de design vigentes. O DEVLOG continua sendo o histórico cronológico do que foi implementado, alterado e testado. O README continua sendo o manual de execução e controles atuais. Se uma frase antiga do README ou do DEVLOG contradisser uma decisão aprovada neste GDD, a decisão mais recente e explicitamente aprovada pelo responsável pelo projeto prevalece; documentação histórica não deve reativar mecânicas descartadas.

Este GDD está publicado como documento de direção do protótipo. Revisões futuras devem preservar as decisões aprovadas e não significam autorização para alterar releases, tags ou backups.

## 2. Visão e escopo

Phoenix Island é um protótipo em primeira pessoa, construído com Three.js e WebGL, para investigar movimentação, orientação, percepção do cenário, acessibilidade e uso de áudio em um ambiente tridimensional. O navegador é usado como meio de teste do protótipo, não como plataforma final do jogo: a intenção é compilar o jogo posteriormente, e o formato de distribuição ainda não foi definido.

O protótipo atual também testa uma fatia inicial de inventário, coleta de recursos, ferramentas, fabricação, escalada e natação. Essas mecânicas são experimentos funcionais do protótipo; sua presença não significa que já exista um jogo completo de sobrevivência ou um conjunto definitivo de regras.

A direção visual de trabalho está registrada em [`VISUAL_DIRECTION.md`](VISUAL_DIRECTION.md). Ela propõe uma fantasia 3D estilizada, com influências ainda exploratórias, e orienta a revisão do mapa de teste inteiro no workflow atual; não afirma que essa arte já esteja implementada nem que seja final.

### Objetivos atuais

- Testar exploração tridimensional com controle independente do olhar e da orientação corporal.
- Tornar posição, alvos, bloqueios, interações e mudanças de estado compreensíveis sem depender exclusivamente de visão.
- Experimentar pistas sonoras que complementem as informações acessíveis.
- Testar um pequeno ciclo de exploração, coleta, fabricação e uso de ferramentas.
- Preservar mecânicas já implementadas quando se adicionarem novos recursos, salvo decisão explícita em contrário.

### Fora do escopo atual

O protótipo ainda não implementa sistemas completos de RPG ou sobrevivência, narrativa de campanha, combate, fome, sede, saúde, morte, progressão, salvamento, economia, construção de base ou conteúdo completo do jogo futuro. A ausência desses sistemas no código não significa que o RPG de sobrevivência planejado os exclua. As decisões de design já tomadas estão registradas neste GDD; o que ainda não foi decidido permanece em aberto e não deve ser completado por inferência.

### Progressão, atributos e recursos — decisões de design

Phoenix Island é planejado como um RPG de sobrevivência com níveis. As regras abaixo registram fundamentos já decididos, não afirmam que esses sistemas estejam implementados no protótipo.

- O personagem usa os seis atributos clássicos do sistema d20: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.
- Atributos podem ser melhorados com pontos recebidos ao subir de nível. Atributos não aumentam automaticamente pelo uso.
- Habilidades aumentam com o uso. A progressão será própria de Phoenix Island; não serão adotados os sistemas de prática e treinamento presentes em bases de MUD.
- Como referência provisória para carga máxima, adota-se capacidade de carga = valor de Força × 15 libras. A pilha de cada item não tem limite numérico próprio; o peso total carregado limita a quantidade, enquanto os espaços do inventário limitam os tipos distintos de item.
- A sobrecarga afeta a velocidade de movimento e aumenta o consumo de estamina. Os limiares e as magnitudes exatas dessas penalidades ainda não foram definidos.
- Estamina é consumida por atividades físicas; mana é consumida por todas as atividades mágicas. Valores máximos, custos específicos, regeneração e vínculo numérico desses recursos com atributos ainda não foram definidos.

Permanecem em aberto: quantidade de pontos de atributo por nível, curva e requisitos de nível, limites de atributo, quais atributos afetam quais cálculos além da capacidade de carga provisória, catálogo de habilidades e ritmo de evolução por uso, custos de estamina/mana, regeneração e níveis de sobrecarga. Essas lacunas exigem decisões próprias e não autorizam importar automaticamente fórmulas de D&D, CoffeeMUD ou outras bases.

## 3. Princípios de design

### Função antes de possibilidade

Uma interação só deve existir se tiver utilidade clara para a experiência ou para uma mecânica aprovada do jogo. O fato de algo ser tecnicamente possível, parecer realista ou ser fácil de implementar não é motivo suficiente para adicioná-lo. Antes de propor uma interação, explicitar que problema ela resolve, que resultado oferece e como contribui para o ciclo de jogo em escopo.

### Escopo sob autorização

Implementar o que foi solicitado, sem acrescentar comportamentos, variações, receitas, efeitos, itens ou sistemas não pedidos. Não ampliar o escopo por iniciativa própria. Se uma ideia adicional parecer útil, apresentá-la como proposta separada e aguardar decisão antes de incluí-la no código.

Quando algo for solicitado, não atribuir explicações ou funções extras além do que foi solicitado.

### Recursos com resultado intencional

Destruir, consumir, transformar, esgotar ou remover um recurso precisa ter um resultado coerente, previsível e intencional, ligado à ação e à utilidade do recurso. Verificar o que o jogador recebe, o que perde, se a ação pode falhar e se a falha consome algo. Não remover recursos nem criar conversões cujo propósito ou consequência não estejam definidos.

### Perguntar quando houver dúvida

Se o pedido ou uma decisão de design deixar margem para mais de uma interpretação, ou se uma funcionalidade adicional não estiver claramente autorizada, não inventar uma mecânica. Explicar a dúvida de forma concreta no chat e aguardar a decisão de Anderson antes de implementar. Não tratar silêncio, convenção de gênero, realismo ou implementação existente como autorização.

### Acessibilidade como parte da mecânica
- Informações necessárias para localizar, escolher e concluir uma ação devem estar disponíveis por meios compatíveis com leitor de tela e teclado; um efeito visual sozinho não comunica um estado essencial.
- Áudio pode complementar ou, depois de revisão, substituir uma mensagem redundante, mas não se deve remover informação útil para o leitor de tela apenas porque existe um som. Uma substituição precisa manter o significado identificável e ser aprovada antes de alterar o comportamento.
- Anúncios devem começar pela informação útil, sem prefixos genéricos repetidos.
- Movimento contínuo não deve narrar cada tecla ou passo. O fluxo normal comunica mudanças de estado e resultados necessários à ação, sem excesso de instruções.
- Controles e interações precisam ser testáveis sem exigir que o jogador interprete elementos puramente visuais.
- O protótipo está em estágio básico e ainda não tem menu. A prioridade atual é implementar as mecânicas previstas, testá-las, validá-las e aprimorá-las. A criação do menu integrado ao início do jogo e das opções de apresentação/acessibilidade fica para depois que o protótipo sair do estágio básico; não antecipar essa etapa. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais. Isso não cria menu de pausa nem dá a Esc uma função fora desses painéis; F1 permanece sem função nesta fase. Não presumir que TTS embutido ou outras propostas de assistência para pessoas cegas sejam eficazes; validar qualquer solução com Anderson antes de apresentá-la como útil.

### Tutorial, ajuda e controles visíveis
- Nesta fase não há tutorial nem menu de ajuda planejados ou implementados. Não adicionar um tutorial, manual na tela ou menu de ajuda sem uma decisão e pedido futuros.
- Os controles podem ser descritos em documentação externa do projeto, mas não devem aparecer na interface durante o jogo nesta fase. Não mostrar listas de teclas, comandos, instruções ou lembretes de controles na tela. Exibi-los só poderá ser considerado se futuramente forem explicitamente requeridos como parte de um tutorial ou de menus de ajuda aprovados.
- Mensagens normais de jogo devem ser concisas e contextuais, priorizando estados e resultados; não devem ensinar comandos ou repetir requisitos.
- Se uma ação não puder prosseguir por requisito conhecido, não executar a ação nem consumir/transformar recursos indevidamente; não substituir a ausência de tutorial por explicações repetitivas em jogo.

### Preservar antes de substituir

- Uma nova forma de coletar ou interagir não deve apagar silenciosamente uma forma já existente.
- Ao mudar altura, alcance ou geometria, verificar todas as mecânicas dependentes, como escalada, caminhada nos galhos, coleta e colisão.
- Não implementar ações para uma ferramenta apenas por analogia ou conveniência. Cada ferramenta só executa as funções aprovadas.
- Uma correção de implementação não equivale a autorização para mudar o design ou remover outras mecânicas.

### Testabilidade e honestidade sobre validação

- Distinguir sempre: decisão aprovada, implementação no código, página publicada, teste manual e avaliação qualitativa.
- Verificações estáticas ou carregamento da página não comprovam que uma interação funciona corretamente em gameplay ou com leitor de tela.
- Registrar no DEVLOG o que mudou e o que continua pendente; não declarar aprovação visual ou auditiva sem avaliação correspondente.

## 4. Mundo de teste

### Coordenadas e escala

- Coordenadas de design: X/Y no plano do chão e Z como altitude; norte é Y positivo.
- Conversão de renderização: `(X, Y, Z)` de design para `(X, Z, -Y)` em Three.js.
- Campo caminhável: X de −24 m a +24 m e Y de −18 m a +36 m (48 × 54 m).
- Altura ocular humana de referência: 1,60 m.

### Regiões presentes

- Colina central com 1,8 m de altura, rampas e terreno contornável.
- Árvore de teste perto do setor central, com tronco, raízes, galhos baixos de coleta e um patamar mais alto para escalada.
- Lago ao norte/leste, centrado em (5,0; 13,2), com superfície aproximada de 12 × 6,4 m, faixa rasa caminhável, margem lamacenta e bacia de até 2,7 m.
- Afloramentos de pedra no topo da colina e pedras soltas coletáveis ao redor da base.
- Arbustos distribuídos pelo campo como fonte de fibra vegetal e galhos caídos como recurso distinto dos gravetos.

A distribuição, quantidades e dimensões são parâmetros do protótipo e podem mudar após decisão e teste; não devem ser tratados como números universais do jogo futuro.

## 5. Controles e exploração

- W/S: avançar/recuar em relação ao corpo; A/D: deslocamento lateral.
- Shift direito combinado ao movimento: corrida, com velocidades conforme o controle atual do README.
- Shift esquerdo+A/D: girar o corpo em 45°; Shift esquerdo+W: girar 180°; Shift esquerdo+S: recuo rápido.
- Setas: olhar em passos de 15°, com limites de ±45° na horizontal e ±30° na vertical.
- C: anunciar coordenadas.
- Espaço: interagir, usar o item em mãos ou iniciar/confirmar saída da natação conforme a situação.
- Enter: recolher pedra solta ou fibra de arbusto quando o alvo e a interação forem elegíveis; não substitui a mineração de afloramentos.
- I: abrir inventário. Alt+C com item equipado: abrir ações situacionais.

O olhar e a orientação corporal são controles distintos. A/D não giram o corpo. Não introduzir atalhos que conflitem com essas funções sem decisão explícita.

### Percepção visual do cenário — parâmetros hipotéticos de trabalho e decisões pendentes

Os valores desta seção foram aprovados por Anderson em 13 de novembro de 2026 como parâmetros hipotéticos para trabalhar num escopo mais realista. São valores de design para o jogo, não medições universais da visão humana. Eles substituem a antiga instrução de que nenhum valor-base ou faixa havia sido escolhido. Não alteram por si mesmos o código nem autorizam uma mudança de implementação.

**Estado atual encontrado no código (13 de novembro de 2026):**

- A câmera Three.js usa campo vertical de 68° e plano distante de 100 m. Esses valores descrevem a implementação atual e não substituem os parâmetros de gameplay abaixo.
- As descrições atuais consultam uma lista selecionada de alvos e prioridades codificadas; não constituem percepção global de todos os objetos.
- A linha de visão atual testa o perfil matemático do terreno entre jogador e alvo, com amostras de 0,01 m e folga de 0,01 m, e lança raio contra `lookables`. O alvo ignora suas próprias malhas cadastradas, mas uma malha cadastrada antes dele pode ocultá-lo. Geometrias que não estejam em `lookables` não participam desse teste semântico de oclusão.
- `lookables`, colisão física, malhas renderizadas e alvos de interação são conjuntos distintos. O alcance de interação não é alcance de percepção.

**Faixas de distância de referência:** perto = até 8 m; média = acima de 8 m e até 20 m; longe = acima de 20 m e até 45 m. A faixa longe não é teto de renderização. Alvos podem ser apenas detectáveis além do alcance de identificação, até os limites por tamanho definidos abaixo.

**Classe de tamanho e alcance-base em condição de referência** (ar limpo, sem oclusão, iluminação ambiente de pelo menos 100 lux; distâncias medidas do jogador ao alvo):

| Classe de tamanho aparente | Exemplos do mapa atual | Identificar o objeto até | Detectar contorno/indício até |
|---|---|---:|---:|
| Grande | colina, árvore, lago | 45 m | 60 m |
| Médio | arbusto, afloramento rochoso | 20 m | 30 m |
| Pequeno | pedra solta, galho caído, fogueira | 8 m | 12 m |

A classe é uma categoria de detecção do jogo, não uma medição física das malhas. A fogueira pertence à classe pequena para identificação pela forma; sua luminosidade é tratada separadamente. Não reclassificar as classes desta tabela nem acrescentar novos alvos a ela sem decisão de Anderson.

**Escala de porte físico dos objetos (decisão aprovada em 13 de novembro de 2026):** essa é uma escala independente das classes de detecção acima. Classificar cada objeto pela sua maior dimensão física, em metros. Usar os limites exatos abaixo; cada intervalo é aberto à esquerda e fechado à direita, exceto o primeiro e a faixa final. A escala cresce para cima e pode ganhar categorias adicionais se o jogo incluir objetos ainda maiores.

| Porte físico | Maior dimensão |
|---|---:|
| Minúsculo | até 0,25 m |
| Pequeno | acima de 0,25 m até 1 m |
| Médio | acima de 1 m até 3 m |
| Grande | acima de 3 m até 10 m |
| Enorme | acima de 10 m até 30 m |
| Colossal | acima de 30 m até 100 m |
| Monumental | acima de 100 m; sem limite superior definido |

A maior dimensão serve para classificar o porte; não determina, sozinha, oclusão nem área encoberta. O efeito visual de um objeto sobre outro depende de geometria, posição e interseção com a linha de visão, cuja regra ainda será definida. Portanto, não inferir que um objeto grande oculta integralmente algo atrás dele, nem que objetos pequenos nunca ocultam. A escala também não define quais materiais bloqueiam.

Exemplos de porte a confirmar pelas dimensões reais dos modelos do jogo: pedra solta e galho caído provavelmente pequeno; arbusto pequeno ou médio; árvore grande ou enorme; colina enorme ou colossal; montanha colossal ou monumental. Esses exemplos não atribuem dimensões aos assets existentes. Não atribuir ao lago uma função de obstáculo com base no seu porte: bloqueio da superfície, visão através da água e visão subaquática continuam sem decisão.

**Iluminação ambiente:** usar a iluminância ambiente local em lux como banda de entrada do modelo provisório. Aplicar o multiplicador indicado aos dois alcances-base (identificação e contorno/indício); não aplicar este multiplicador à luminosidade própria da fogueira.

| Iluminância ambiente local | Multiplicador do alcance-base |
|---|---:|
| Menos de 0,01 lux | 0,25 |
| De 0,01 lux até menos de 0,1 lux | 0,35 |
| De 0,1 lux até menos de 1 lux | 0,50 |
| De 1 lux até menos de 10 lux | 0,65 |
| De 10 lux até menos de 100 lux | 0,80 |
| 100 lux ou mais | 1,00 |

Os intervalos são fechados à esquerda e abertos à direita, exceto a última banda. Não interpolar entre bandas nem criar uma curva contínua sem aprovação. Lux representa iluminância incidente, não luminância aparente; não converter diretamente entre lux e cd/m². Estes números são níveis de jogo aproximados.

**Visibilidade atmosférica:** selecionar a condição aplicável e usar seu valor como teto de alcance para identificação e contorno/indício, após aplicar o multiplicador de iluminação. Assim, alcance efetivo = menor entre (alcance-base da classe × multiplicador de iluminação) e teto atmosférico.

| Condição no jogo | Teto de alcance |
|---|---:|
| Ar limpo | 60 m |
| Névoa leve | 45 m |
| Névoa moderada | 25 m |
| Névoa/nevoeiro forte ou fumaça densa | 10 m |
| Quase sem visibilidade | 5 m |

Usar uma única condição atmosférica por avaliação; não somar tetos nem inventar pesos para misturas de condições. Os limites abaixo de 1 km são escalas de gameplay, não definições meteorológicas. Não tratar altitude como multiplicador numérico: ela pode afetar linha de visada/horizonte por geometria, mas qualquer regra de oclusão e sua aplicação permanecem sujeitas à próxima definição específica.

**Mensagens por nível de detecção:**

- Dentro do alcance de identificação calculado: identificar o objeto pelo nome, se o tipo for distinguível.
- Acima do alcance de identificação, mas até o alcance de contorno/indício: usar “a silhueta de [objeto] à distância” somente quando a forma permite reconhecer a categoria; se não for possível definir o tipo, usar “algo à distância”.
- Acima do alcance de contorno/indício: não detectar nem anunciar o alvo.
- “Perto”, “a distância” e termos equivalentes descrevem a faixa global (até 8 m; acima de 8 até 20 m; acima de 20 m). Não inventar subfaixas verbais.
- A mensagem não deve afirmar identificação quando o modelo só permite detectar um contorno ou indício.

**Fogueira — detecção da luminosidade:** a fogueira é um alvo pequeno, não um objeto grande. Em condição escura, a fonte luminosa pode permitir detectar um brilho até 25 m; isso não permite identificar a fogueira como objeto a essa distância. O reconhecimento pela forma continua sujeito à classe pequena (até 8 m em condição de referência), multiplicador de luz ambiente e teto atmosférico. Para a pista de brilho, aplicar o teto atmosférico, mas não o multiplicador de iluminância ambiente. O alcance exato do bônus conforme a iluminância ambiente acima de 1 lux, a redução gradual do bônus e os limiares de transição ainda não foram definidos: não interpolar, não criar faixas adicionais e não implementar essa parte até Anderson decidir. Quando apenas o brilho for detectável, a mensagem deve dizer “uma luz” ou “um brilho”, não “uma fogueira”.

**Oclusão e múltiplos alvos — decisão ainda pendente:** os alcances numéricos acima pressupõem que não haja obstrução. A escala de porte físico acima está aprovada, mas não é regra de oclusão e não pode ser usada como substituta dela. A próxima etapa de design definirá quais geometrias bloqueiam a linha de visão, oclusão parcial, objetos alinhados no mesmo eixo e prioridade dos anúncios. Até essa definição, não converter obstáculos em multiplicadores, não assumir que qualquer geometria opaca/renderizada bloqueia, não ignorar obstrução, não escolher quantos alvos alinhados anunciar e não criar regras específicas por objeto. Se a tarefa de implementação depender dessas decisões, parar e perguntar a Anderson no chat.

**Regra de implementação:** os parâmetros acima substituem “nenhum alcance-base/faixa foi decidido”, mas não autorizam por si só alteração de código. Antes de uma implementação solicitada, apresentar a fórmula acima e as pendências de oclusão/alvos alinhados. Manter separados campo angular, alcance perceptivo, visibilidade atmosférica, iluminância ambiente, detecção da luz emitida pela fogueira, linha de visão, renderização, colisão/transponibilidade e alcance/seleção de interação. Nunca usar `camera.far = 100` como alcance de design.

## 6. Interações e ferramentas aprovadas

O registro consolidado de ingredientes, consumo, resultados esperados e condições das receitas de fabricação está em [`CRAFTING.md`](CRAFTING.md). Este documento detalha as receitas atualmente aprovadas sem ampliar o escopo do protótipo.

### Árvore: duas alturas, duas mecânicas

- A escalada deve permanecer funcional: aproximar-se e mirar o tronco, pressionar Espaço para agarrar, manter W para subir ao patamar alto, caminhar pelos galhos, segurar-se numa ponta com Espaço e descer com S.
- Galhos baixos da copa são uma interação separada, alcançável do chão perto da árvore, mirando para cima.
- Sem faca equipada, o alvo baixo de coleta da copa produz um graveto.
- Com a faca de pedra equipada, o mesmo alvo de copa pode ser golpeado; cada alvo de galho vivo tem resistência individual 6, diminui com golpes de dano sorteado entre 1 e 3 e fornece um galho ao chegar a zero.
- Os galhos baixos não substituem nem rebaixam o patamar de escalada. Alterar a copa exige preservar e testar a subida, a travessia e a descida.
- A árvore de teste atual não tem alvos de fruto; não anunciar ou pressupor frutos disponíveis.

### Galhos e gravetos

- Galhos são distintos de gravetos, maiores e mais resistentes, são material para receitas e inflamáveis.
- Galhos caídos no chão são itens recolhidos somente com Enter, sem faca ou golpes; a coleta exige alcance e espaço no inventário.
- Galhos vivos baixos da copa são fontes de extração: somente eles exigem faca equipada e golpes sucessivos para serem cortados.
- Com um galho equipado, o menu oferece a conversão em dois gravetos somente se houver uma faca de pedra em algum espaço do inventário; a faca não precisa estar equipada para esta conversão.
- A conversão consome um galho e produz dois gravetos. Conferir espaço antes de consumir o recurso.
- Galhos caídos não têm resistência e são recolhidos diretamente. Galhos vivos baixos da copa têm resistência inicial 6; a faca causa dano inteiro sorteado entre 1 e 3 por golpe até esgotá-los. O martelo não interage com galhos.

### Dano e resistência

- Cada acerto sorteia um valor inteiro uniforme dentro da faixa de dano da ferramenta usada. O dano é subtraído da resistência da fonte, limitada a zero; ao chegar a zero, a fonte se esgota. A escala é abstrata e não representa medida física.
- Faca de pedra, ferramenta de corte mais básica: dano inteiro sorteado uniformemente entre 1 e 3 por golpe. Martelo de pedra, ferramenta de impacto mais básico: dano inteiro sorteado uniformemente entre 2 e 4 por golpe.
- Galho vivo: resistência 6; afloramento rochoso: resistência 12. Galhos caídos são itens recolhíveis e não têm resistência.
- Enquanto a fonte resistir, cada golpe reduz sua resistência. Ao esgotar, a fonte entrega seu rendimento atual. Se não houver espaço para a recompensa, o golpe que a esgotaria não reduz a resistência; seu dano sorteado fica pendente para ser aplicado sem novo sorteio quando houver espaço.
- Esta regra e estes valores são os aprovados para as ferramentas/fontes do protótipo; não implementar outras armas, classes ou efeitos de dano por inferência.

### Faca de pedra

- Ferramenta de corte.
- Receita implementada: equipe uma pedra lascada e tenha 1 graveto e 1 fibra vegetal; consome os três componentes e cria a faca. Exige estar no chão. A fibra amarra a lâmina ao cabo de graveto.
- A cadeia de materiais implementada é: duas pedras → uma pedra afiada; uma pedra + uma pedra afiada → uma pedra lascada; uma pedra lascada + um graveto + uma fibra vegetal → uma faca de pedra.
- Corta galhos vivos baixos da copa quando equipada. Não é necessária para recolher galhos caídos.
- A faca não deve ser descrita como ferramenta de impacto.

### Martelo de pedra

- Ferramenta de impacto.
- Receita implementada: uma pedra, um graveto e uma fibra vegetal para afixar a pedra ao cabo.
- Uso implementado no protótipo: minerar afloramentos maiores. Basta o martelo estar no inventário; não precisa ser equipado.
- A mineração exige vários golpes, anuncia progresso e só entrega as pedras no golpe final.
- O martelo não corta nem quebra galhos, não divide galho em gravetos e ainda não tem função de construção. Não inventar outras funções sem decisão explícita.

### Materiais e coleta

- Pedras soltas, arbustos, galhos caídos e cinzas são coletados com Enter quando elegíveis, inclusive com outro item nas mãos. Espaço usa o item equipado; não recolhe esses itens do chão.
- Afloramentos exigem martelo no inventário e são minerados com Espaço em golpes sucessivos.
- Arbustos são coletados e fornecem duas fibras vegetais cada no protótipo atual. A descrição ao olhar os identifica simplesmente como “um arbusto silvestre”, sem indexá-los ou antecipar seu rendimento; a ação de coleta mantém o resultado de duas fibras e o anuncia após a coleta.
- A cadeia de processamento de pedra está implementada no protótipo: duas pedras geram uma pedra afiada; uma pedra + uma pedra afiada geram uma pedra lascada; uma pedra lascada + um graveto + uma fibra vegetal geram a faca de pedra. A fibra amarra a lâmina ao cabo. A pedra afiada pode ser componente de ferramentas futuras como machado e picareta, mas as receitas dessas ferramentas não estão decididas.
- Gravetos são menores e mais frágeis que galhos; ambos são inflamáveis. Gravetos servem de combustível e de partes para ferramentas e estruturas; no protótipo são combustível da fogueira simples e compõem o cabo do martelo de pedra. Receitas concretas de estruturas ou outras ferramentas ainda não estão definidas. Galhos são maiores e mais resistentes que gravetos; podem servir de combustível e ser convertidos em dois gravetos com faca no inventário. Ainda não há receita especificada que use galhos como componente de ferramenta ou estrutura; lança, picareta e estruturas são possibilidades de design futuras, sem receitas aprovadas.
- Fibras vegetais vêm dos arbustos, são inflamáveis e servem para improvisar amarrações que conectam componentes; a fibra da receita do martelo prende a pedra ao cabo. Outras receitas de amarração ou de estrutura ainda não estão especificadas.
- Pedras são o mineral mais básico atualmente listado, resistente e não inflamável. Podem ser moldadas com limitações e não são tão flexíveis quanto metais; servem para ferramentas e estruturas. No protótipo, pedra, pedra afiada e pedra lascada são usadas na cadeia da faca, e pedra também compõe o martelo. Pedra afiada e pedra lascada são componentes intermediários, não ferramentas. Processo adicional de moldagem, técnicas e receitas estruturais concretas ainda não estão definidos.
- Usos possíveis para ferramentas ou estruturas não são automaticamente receitas aprovadas nem autorização de implementação. O catálogo consolidado de propriedades e usos está em [`CRAFTING.md`](CRAFTING.md).
- Coletas devem respeitar mira, alcance e espaço no inventário e não consumir o objeto se a recompensa não puder ser guardada.

### Fogueira simples

- A fogueira simples é uma ferramenta fixa do Tier 1, do tipo estação de trabalho; não pode ser carregada e é a estação mais básica.
- Não possui superfície ou suporte para apoiar algo em preparo, então não permite deixar um item sendo preparado enquanto o jogador se afasta. Para um preparo futuro como carne assada, o jogador deve segurar a carne num espeto dentro do alcance da fogueira durante o preparo. Isso descreve o comportamento esperado da estação; não aprova receita, alimento, duração ou mecânica de preparo ainda não definida.
- Criação atual exige dez gravetos, estar no chão seco e fora de água e lama. Não há restrição de proximidade: outra fogueira pode ser criada perto de uma já acesa ou apagada. O alcance de 2,4 m é para interação/abastecimento, não uma distância mínima entre fogueiras.
- Começa com 180 segundos de combustível; material inflamável consumido pode adicionar até 60 segundos, até o máximo total de 300 segundos.
- Gravetos, galhos e fibras vegetais estão marcados como inflamáveis.
- As regras são experimentais do protótipo; não extrapolar para um sistema geral de fogo ou sobrevivência.

### Natação

- Entrada: mãos vazias, faixa rasa e corpo voltado para água profunda; Espaço inicia.
- W/S seguem a inclinação do olhar; no horizonte mantêm profundidade. A/D deslocam lateralmente. O nado para trás (S) só é permitido até 0,55 m de profundidade. Em águas mais profundas, S é completamente bloqueado e não move o personagem em qualquer direção, independentemente da inclinação do olhar. É necessário usar W com o olhar inclinado para cima, de acordo com a regra geral de natação, e alcançar a zona rasa antes de recuar. Ao recuar na faixa permitida, a profundidade não pode ultrapassar 0,55 m.
- Na natação, o anúncio do olhar corresponde ao sinal real da inclinação desde o primeiro passo de 15°; só o ângulo horizontal é descrito como horizontal.
- Saída: mãos vazias, superfície e proximidade da faixa rasa ou saída elegível, seguida de Espaço. Não sair automaticamente ao tocar a margem.
- Não existem passagens subaquáticas no mapa atual.

## 7. Inventário e interface

- Dez espaços para tipos de item, em grade de duas fileiras por cinco; começa vazio.
- Itens do mesmo tipo acumulam sem limite artificial de pilha. Não há limite de peso implementado.
- O inventário inclui pedra afiada e pedra lascada como componentes intermediários empilháveis, além dos itens já listados no README; não são ferramentas nem têm outros usos implementados fora da cadeia da faca.
- Todos os dez espaços, inclusive vazios, são navegáveis por setas; Enter abre ações para espaço ocupado. O foco e os anúncios seguem as regras de acessibilidade descritas no README.
- Ações presentes: examinar, mover, usar/equipar, soltar e atribuir atalho. Itens largados são entradas recuperáveis por controle acessível, não objetos físicos no cenário.
- Não adicionar mochila, carga, durabilidade ou efeitos de item sem decisão aprovada.

## 8. Áudio e comunicação

- A coleta com Enter seleciona o item coletável elegível mais alinhado à mira e dentro do alcance, inclusive com outro item equipado; o foco no botão Inventário não bloqueia a ação. Uma árvore claramente mais alinhada conserva sua prioridade.
- A descrição acessível deve anunciar coletáveis visíveis no campo de visão, com pontos de mira consistentes com a geometria real das suas malhas e teste de oclusão contra elementos distintos.

- Uma pista em curso mantém a identidade da fonte enquanto o jogador permanece na zona de proximidade; não alternar para fontes vizinhas a cada repetição. A descrição ao olhar deve incluir fontes coletáveis no chão quando visíveis, inclusive com olhar inclinado para baixo.
- A origem espacial e a descrição de um objeto coletável devem usar o centro calculado das malhas visíveis do objeto, não uma coordenada aproximada do solo. A checagem de visibilidade ignora a geometria própria do alvo, mas respeita qualquer outro objeto que o encubra.
- Efeitos sonoros complementam a orientação e o feedback. Sons de passos por superfície, inclinação, natação, árvore, recursos, mineração, limite e fogueira estão em estágio provisório, salvo avaliação explícita registrada.
- Efeitos de escalada previamente aprovados devem ser preservados quando não houver pedido explícito para alterá-los.
- Beeps de água indicam zonas definidas; não são bússola nem substituem informação contínua de profundidade.
- Um som de referência deve ter significado consistente, ser distinguível dos demais e não remover silenciosamente informação que o leitor de tela necessita.
- Pistas espaciais de objetos e fontes de recurso devem usar fontes posicionadas no mundo em relação ao jogador; complementam e nunca substituem a informação acessível. Para recursos, a pista toca ao se aproximar, não por varredura manual ou camada contínua.
- Usar timbres diferentes para fontes que exigem extração e itens diretamente coletáveis. A pista só toca quando o recurso seria o primeiro objeto atingido na linha de visão ao virar naquela direção, respeitando a hierarquia de elementos visíveis. Repetir a pista a cada 1 s enquanto o jogador permanece próximo e a fonte tem prioridade visível, para não depender de um único evento de entrada; uma geometria pertencente ao próprio alvo não o bloqueia, mas outros objetos mais próximos continuam bloqueando. Em 27 de outubro de 2026, Anderson informou que testou o estado publicado e o considerou confortável o bastante para atualizar os documentos e o backup. Esse marco valida o ponto atual de teste em termos gerais; não deve ser expandido para afirmar que cada fonte, som, distância ou combinação com leitor de tela foi avaliada e aprovada individualmente.
- Não fazer avaliação auditiva em nome do usuário. Registrar a avaliação que Anderson efetivamente realizou sem extrapolar seu alcance: em 27/10/2026 ele considerou o estado então publicado confortável para a atualização dos documentos e do backup.

## 9. Limites: fazer e não fazer

### Fazer

- Implementar a solicitação atual sem apagar mecânicas independentes já aprovadas.
- Conferir dependências antes de alterar geometria, altura, alcance, inventário ou prioridades de mira.
- Manter a faca como corte, o martelo como impacto e cada ação restrita às funções aprovadas.
- Usar anúncios concisos, informação diretamente útil e nomes coerentes com a ação.
- Testar bloqueios, inventário cheio, alcance, disputa entre alvos e navegação acessível.
- Atualizar o README quando controles ou comportamento observável mudarem; atualizar o DEVLOG com mudanças, validação e pendências.

### Não fazer

- Não retirar uma mecânica existente por conveniência ou presumir que um novo recurso a substitui.
- Não atribuir corte ao martelo, nem efeitos de ferramenta ou de construção não aprovados.
- Não tornar uma interação essencial dependente apenas de visão, imagem ou som ambíguo.
- Não afirmar que um teste passou apenas porque o código compila, o workflow terminou ou a página carregou.
- Não alterar releases, tags ou backups sem autorização explícita.
- Não expandir o protótipo para sistemas completos de sobrevivência/RPG por inferência.

## 10. Critérios de conclusão para mudanças

Uma mudança só deve ser considerada pronta para implementação quando:

1. A solicitação e a utilidade clara da interação estiverem definidas; possibilidade técnica, realismo ou convenção de gênero não bastam.
2. O comportamento pedido estiver delimitado, sem conteúdo ou sistemas adicionais não autorizados.
3. Recurso consumido, transformado, esgotado ou removido tiver resultado e consequência intencionais, inclusive em caso de falha.
4. Dúvidas que mudem o comportamento tiverem sido levadas ao chat e respondidas por Anderson antes da implementação.

Uma mudança implementada só deve ser considerada concluída quando:

5. Alcance, mira, ferramenta, consumo e capacidade do inventário tiverem sido verificados.
6. A interação continuar compreensível com leitor de tela e teclado.
7. As mecânicas próximas que poderiam ser afetadas tiverem sido preservadas e verificadas.
8. A publicação de teste for distinta de uma release oficial ou backup.
9. O DEVLOG registrar o que foi alterado e separar verificação estática de teste manual e avaliação do usuário.

## 11. Decisões ainda não aprovadas

A premissa narrativa planejada está em [`LORE.md`](LORE.md): um conselho de magos, com base na suspeita de um mal antigo, tenta destruir a ilha e sacrifica seus habitantes; a ilha é devastada, mas não desaparece, e a personagem do jogador, jovem e inexperiente, começa tentando sobreviver antes de buscar compreender o ocorrido. A premissa é direção narrativa planejada, não conteúdo implementado no protótipo.

Este GDD não define a história completa, a estrutura da campanha, nomes, detalhes do mundo ou personagens além da premissa geral, regras completas de combate, fome, sede, saúde, morte, salvamento, persistência, respawn de recursos, construção, durabilidade de ferramentas, receitas futuras nem os valores e fórmulas numéricas de progressão que ainda não foram aprovados. As decisões fundamentais de níveis, atributos, habilidades e recursos estão registradas na seção 2; as lacunas restantes continuam sem decisão e não são autorização para inventar uma solução. Quando forem necessárias para uma implementação, apresentar a decisão no chat antes de codificar.


### Seleção de objetos

A tolerância angular comum para mirar objetos interativos é de 65° em relação à direção da câmera, para reduzir a precisão exigida ao coletar ou interagir. A ampliação não altera alcances físicos, prioridade de alvos ou regras de oclusão.


### Pistas de recursos da árvore

A árvore emite a pista grave de recurso coletável quando há gravetos ou galhos disponíveis nela, pois ambos podem ser recolhidos pelo jogador.


### Confirmação sonora de coleta e ações


- A coleta bem-sucedida de itens emite um som curto próprio de confirmação.
- Cada ação concluída com sucesso pelo menu contextual do item equipado emite outro som curto, distinto da coleta. Falhas, requisitos não atendidos ou inventário cheio não emitem esses sons.


### Feedback de proximidade e anúncios

- Ao entrar na área física de contato/interação de um elemento, anunciar o nome do alvo mais próximo; não repetir continuamente enquanto o jogador permanecer junto a ele. Incluir itens de coleta, recursos, árvore e fogueira, sem ultrapassar os alcances definidos por cada mecânica.
- Manter o texto visual da cena separado da região viva para leitor de tela. Reanunciar a mesma informação após pausa breve, sem depender da inserção de espaços invisíveis no texto, sobretudo nas coordenadas e descrições do campo de visão.


A fala ao entrar na área de contato deve conter somente o nome do objeto, sem prefixo ou explicação adicional.


### Coerência entre contato e coleta

- O anúncio de um item coletável como alvo ao alcance deve usar exatamente o mesmo seletor do Enter: mesma geometria de referência, mira angular, alcance individual e prioridade entre objetos. Assim, o alvo nomeado é o que Enter tentará recolher.


### Apresentação da cena de teste

- Na fase atual, a cena 3D deve ocupar a tela inteira, sem cabeçalho ou moldura com aparência de página de site.
- O único texto visível durante o jogo são mensagens de feedback das ações do jogador. Elas devem ser breves e contextuais, comunicando resultado ou estado da ação. Não exibir título, controles, lista de teclas, instruções, lembretes, descrições persistentes do cenário ou outros textos de interface durante o jogo.
- A inspeção visual de 6 de novembro de 2026 registrou que a tela de inventário ainda exibe “Use as setas para percorrer as duas fileiras da grade” e “Ações (Enter)”. Esses textos são uma divergência em relação à regra vigente, não uma exceção aprovada. Registrar a observação para a conversa de desenvolvimento; não corrigir código durante uma tarefa apenas documental.
- Não há tutorial nem menu de ajuda nesta fase. Os controles continuam funcionando, mas não são exibidos nem anunciados em rótulos ou mensagens. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais, sem aviso visível.
- Não antecipar menu inicial, menu de pausa ou opções: entram numa etapa posterior, depois que o protótipo sair do estado básico. Esc pode fechar ou voltar dos painéis existentes de inventário e ações contextuais, mas a interface não deve instruir o jogador a pressioná-lo nem incluir “Esc” nos rótulos dos botões. A tecla não abre menu de pausa nem recebe outra função nesta fase. F1 permanece sem função.
