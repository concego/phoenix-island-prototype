# Phoenix Island — receitas de fabricação e resultados esperados

**Escopo:** regras de crafting aprovadas e comportamentos associados no protótipo atual. Este documento registra o que está definido; não autoriza implementação, novos itens, receitas ou efeitos.

O protótipo testa uma pequena fatia de coleta, fabricação e uso de ferramentas. Estas regras não definem um sistema completo de sobrevivência nem devem ser extrapoladas para o jogo futuro. Para decisões gerais e limites do projeto, consulte [`GDD.md`](GDD.md). O GDD é a referência para as regras vigentes; o [`DEVLOG.md`](DEVLOG.md) registra o histórico de implementação e testes. Se um registro histórico divergir da regra aprovada mais recente, prevalece o GDD e este documento atualizado.

## Receita: faca de pedra

**Ingredientes:** duas pedras no total: uma pedra equipada e outra disponível no inventário.

**Consumo:** as duas pedras são consumidas.

**Resultado esperado:** fabricação de uma faca de pedra, ferramenta de corte.

**Uso definido:** quando equipada, pode cortar galhos vivos baixos da copa por golpes sucessivos. Cada alvo de galho vivo tem resistência 6; cada golpe da faca causa dano inteiro sorteado uniformemente entre 1 e 3. Ao esgotar a resistência, o alvo entrega um galho. A faca não é necessária para recolher galhos que já caíram no chão.

**Limites:** a faca não é ferramenta de impacto. Não atribuir a ela outras funções ou efeitos sem decisão explícita.

## Receita: martelo de pedra

**Ingredientes:** uma pedra, um graveto e uma fibra vegetal. A fibra serve para afixar a pedra ao cabo.

**Consumo:** os três ingredientes são necessários à receita; a descrição aprovada não detalha uma ordem ou disposição espacial de consumo.

**Resultado esperado:** fabricação de um martelo de pedra reutilizável. Não há durabilidade definida para o protótipo atual.

**Uso definido:** o martelo permite minerar afloramentos maiores. Basta estar no inventário; não precisa estar equipado. Cada afloramento tem resistência 12, e cada golpe do martelo causa dano inteiro sorteado uniformemente entre 2 e 4. A mineração exige vários golpes e só entrega as pedras no golpe final.

**Resultado e falha de inventário:** se o golpe que esgotaria a fonte não puder guardar a recompensa, a resistência não diminui; o dano já sorteado fica pendente para aplicação posterior sem novo sorteio quando houver espaço. A recompensa não deve ser perdida.

**Limites:** o martelo não corta nem quebra galhos, não converte galho em gravetos e não tem função de construção. Não adicionar outras funções sem decisão explícita.

## Receita/ação: criar uma fogueira simples

**Ingredientes:** dez gravetos na pilha equipada.

**Condições:** estar no chão seco, fora de água e lama. A ação não é permitida durante escalada ou natação.

**Consumo e colocação:** consome exatamente dez gravetos e cria a fogueira no ponto atual do terreno. Não permite duplicar fogo aceso nem criar outra fogueira sobre uma fogueira apagada a até 2,4 m. Reacender uma fogueira apagada ainda não está disponível.

**Resultado esperado:** fogueira simples acesa, com 180 segundos (3 minutos) de combustível inicial. O valor aprovado é 180 segundos; qualquer indicação de um minuto está incorreta.

**Combustível adicional:** um material inflamável consumido por ação pode adicionar até 60 segundos, respeitando o máximo total de 300 segundos (5 minutos). Gravetos, galhos e fibras vegetais são inflamáveis. O combustível continua decrescendo enquanto o menu está fechado. Ao chegar a zero, o fogo e a luz se apagam; há um anúncio único se o jogador estiver próximo.

**Limites:** as regras são experimentais do protótipo e não constituem um sistema geral de fogo ou sobrevivência. Não há salvamento/persistência das fogueiras.

## Coleta e conversão de galho em gravetos

**Conversão:** com um galho equipado, o menu de ações oferece convertê-lo em dois gravetos somente se houver uma faca de pedra em algum espaço do inventário. A faca não precisa estar equipada.

**Resultado esperado:** consumir um galho e produzir dois gravetos. Verificar espaço no inventário antes de consumir o galho; não perder recurso se os gravetos não puderem ser guardados.

**Distinção importante:** galho caído no chão é recolhido com Enter, sem faca ou golpes. Galho vivo baixo na copa é uma fonte de extração e requer faca equipada e golpes sucessivos; ao esgotá-lo, fornece um galho. Não confundir a coleta do galho caído, o corte de um galho vivo e a conversão de galho em gravetos.

## Resultados de coleta relacionados às receitas

- Cada arbusto coletado fornece duas fibras vegetais no protótipo atual.
- Pedras soltas, arbustos, galhos caídos e cinzas são coletados com Enter quando o alvo é elegível; a coleta respeita mira, alcance e espaço no inventário.
- Afloramentos exigem um martelo no inventário e são minerados com Espaço em golpes sucessivos. As pedras só são entregues ao esgotar o afloramento.
- Se a recompensa de uma coleta não couber no inventário, não consumir nem remover o recurso do cenário.

## Princípios para avaliar outras receitas

Antes de aprovar uma receita nova, registrar os ingredientes e suas quantidades, quais itens são consumidos, as condições de execução, o resultado fabricado, onde/como o resultado pode ser usado, o que acontece quando falta requisito ou espaço e se uma tentativa falha consome recursos. Não inferir uma receita a partir de convenções de gênero, realismo ou possibilidades do código.

**Ainda não definido neste documento:** receitas futuras, custos adicionais além dos listados, ordem de seleção/consumo quando não especificada, durabilidade de ferramentas, reaparecimento de recursos, progressão, salvamento e construção de base. São decisões em aberto, não espaços para completar por suposição.

## Referências de projeto

- [`GDD.md`](GDD.md) — regras de design vigentes, interações, ferramentas e limites do protótipo.
- [`DEVLOG.md`](DEVLOG.md) — histórico de implementação, verificações e validação pendente.
