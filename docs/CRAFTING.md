# Phoenix Island — receitas de fabricação e resultados esperados

**Escopo:** regras de crafting aprovadas e comportamentos associados no protótipo atual. Este documento registra o que está definido; não autoriza implementação, novos itens, receitas ou efeitos.

O protótipo testa uma pequena fatia de coleta, fabricação e uso de ferramentas. Estas regras não definem um sistema completo de sobrevivência nem devem ser extrapoladas para o jogo futuro. Para decisões gerais e limites do projeto, consulte [`GDD.md`](GDD.md). O GDD é a referência para as regras vigentes; o [`DEVLOG.md`](DEVLOG.md) registra o histórico de implementação e testes. Se um registro histórico divergir da regra aprovada mais recente, prevalece o GDD e este documento atualizado.

## Organização por tier

Para a etapa inicial de implementação, antes de alterar o mapa, as ferramentas mais rústicas aprovadas ficam no **Tier 1**. Neste momento, Tier 1 inclui a faca de pedra, o martelo de pedra e a fogueira simples. A fogueira é uma ferramenta do tipo **estação de trabalho**: não pode ser carregada e é a estação mais básica.

A classificação descreve o escopo inicial atual; não afirma que todas as ferramentas futuras já foram definidas, nem estabelece conteúdo, materiais, receitas ou regras para tiers posteriores. Tiers futuros permanecem sem especificação até decisão explícita.

## Materiais: propriedades e usos

Esta lista separa o que já está definido ou presente no protótipo das possibilidades de uso indicadas para o design futuro. Uma possibilidade não é uma receita aprovada nem significa que o objeto ou sistema já esteja implementado.

### Gravetos

- **Propriedades:** peças pequenas em comparação com galhos; menores e mais frágeis que eles. São inflamáveis.
- **Papel definido no design:** combustível e partes para ferramentas e estruturas. São adequados a cabos e outras peças menores, mas não têm a resistência de galhos.
- **Uso concreto no protótipo:** combustível da fogueira simples; ingrediente da receita do martelo de pedra, cujo cabo é feito com um graveto. Dez gravetos são consumidos para criar a fogueira simples.
- **Ainda não especificado:** receitas de estruturas ou de outras ferramentas com gravetos.

### Galhos

- **Propriedades:** hastes maiores e mais resistentes que gravetos; são inflamáveis.
- **Uso atual no protótipo:** são inflamáveis e podem ser consumidos como combustível. Um galho pode ser convertido em dois gravetos quando o jogador possui uma faca de pedra no inventário.
- **Uso em ferramentas/estruturas:** ainda não há receita especificada que use galhos como componente. Por serem maiores e mais resistentes que gravetos, poderão servir de base para ferramentas como lança e picareta e para estruturas. São possibilidades de design, não receitas aprovadas ou autorização de implementação.

### Fibras vegetais

- **Origem atual:** encontradas em arbustos; cada arbusto fornece duas fibras vegetais no protótipo atual.
- **Papel definido no design:** material inflamável para improvisar amarrações e conectar componentes.
- **Usos de design aprovados:** uma fibra amarra a pedra ao cabo do martelo; a faca de pedra também usa fibra para prender sua lâmina ao graveto.
- **Uso concreto no protótipo:** uma fibra já é ingrediente do martelo de pedra. A nova receita da faca ainda não está implementada.
- **Ainda não especificado:** outras receitas de amarração ou componentes de estruturas; nenhuma foi aprovada.

### Pedras

- **Propriedades:** forma mais básica de mineral presente no projeto; são resistentes e não inflamáveis. Podem ser moldadas, mas com limitações: não têm a flexibilidade de metais.
- **Papel definido no design:** matéria-prima resistente para ferramentas e estruturas, moldável dentro de limites; não tem a flexibilidade dos metais.
- **Cadeia de processamento aprovada para o design:** duas pedras geram uma pedra afiada; uma pedra mais uma pedra afiada geram uma pedra lascada; a pedra lascada, um graveto e uma fibra geram uma faca de pedra. A pedra afiada também fica disponível como componente intermediário para ferramentas futuras, mas as receitas dessas ferramentas não estão decididas.
- **Uso concreto no protótipo:** pedras são recolhidas soltas ou obtidas de afloramentos; a receita atualmente implementada da faca e a receita do martelo usam pedras. A cadeia de pedras afiadas/lascadas e a nova receita da faca ainda não foram implementadas.
- **Ainda não especificado:** processo e limites práticos de moldagem além desta cadeia, receitas adicionais e funções estruturais concretas. Não assumir técnicas ou propriedades além das descritas.


## Processamento de pedra — cadeia aprovada para o design

A cadeia abaixo define as entradas e resultados de design. Ela ainda não substitui a implementação atual do protótipo; a mudança de código precisa ser feita e testada separadamente.

1. **Duas pedras → uma pedra afiada.** A pedra afiada é um componente intermediário utilizável em ferramentas.
2. **Uma pedra + uma pedra afiada → uma pedra lascada.**
3. **Uma pedra lascada + um graveto + uma fibra vegetal → uma faca de pedra.** A fibra amarra a pedra lascada ao graveto, que funciona como cabo.

O uso da pedra afiada em ferramentas como machado e picareta é uma possibilidade de design já mencionada, mas suas receitas e quantidades ainda não foram decididas. Esta cadeia não define ferramentas, métodos, estações, tempos ou outros resultados de processamento.

## Tier 1 — ferramentas rústicas iniciais

### Ferramentas carregáveis

### Faca de pedra

**Receita de design aprovada:** uma pedra lascada, um graveto e uma fibra vegetal. A fibra amarra a lâmina de pedra lascada ao graveto, que serve de cabo.

**Resultado esperado:** uma faca de pedra, ferramenta de corte.

**Estado da implementação:** o protótipo ainda usa a receita antiga de duas pedras (uma equipada e outra no inventário), consumindo ambas. A cadeia de pedra afiada → pedra lascada → faca e a nova receita com graveto e fibra ainda precisam ser implementadas e testadas; esta atualização é documental.

**Uso definido:** quando equipada, pode cortar galhos vivos baixos da copa por golpes sucessivos. Cada alvo de galho vivo tem resistência 6; cada golpe da faca causa dano inteiro sorteado uniformemente entre 1 e 3. Ao esgotar a resistência, o alvo entrega um galho. A faca não é necessária para recolher galhos que já caíram no chão.

**Limites:** a faca não é ferramenta de impacto. Não atribuir a ela outras funções ou efeitos sem decisão explícita.

### Martelo de pedra

**Ingredientes:** uma pedra, um graveto e uma fibra vegetal. A fibra serve para afixar a pedra ao cabo.

**Consumo:** os três ingredientes são necessários à receita; a descrição aprovada não detalha uma ordem ou disposição espacial de consumo.

**Resultado esperado:** fabricação de um martelo de pedra reutilizável. Não há durabilidade definida para o protótipo atual.

**Uso definido:** o martelo permite minerar afloramentos maiores. Basta estar no inventário; não precisa estar equipado. Cada afloramento tem resistência 12, e cada golpe do martelo causa dano inteiro sorteado uniformemente entre 2 e 4. A mineração exige vários golpes e só entrega as pedras no golpe final.

**Resultado e falha de inventário:** se o golpe que esgotaria a fonte não puder guardar a recompensa, a resistência não diminui; o dano já sorteado fica pendente para aplicação posterior sem novo sorteio quando houver espaço. A recompensa não deve ser perdida.

**Limites:** o martelo não corta nem quebra galhos, não converte galho em gravetos e não tem função de construção. Não adicionar outras funções sem decisão explícita.

### Estação de trabalho: fogueira simples

A fogueira simples é uma ferramenta fixa, não carregável, e a estação de trabalho mais básica. Ela não tem superfície, apoio ou suporte onde deixar um item em preparo. Portanto, não permite iniciar algo, afastar-se e deixá-lo sendo preparado sozinho. Se o jogador for preparar, por exemplo, carne assada nela, deverá manter a carne num espeto e segurá-lo dentro do alcance da fogueira durante o preparo. Esse exemplo registra o comportamento esperado da estação; não aprova uma receita, item, duração ou implementação de preparo de alimentos.


**Ingredientes:** dez gravetos na pilha equipada.

**Condições:** estar no chão seco, fora de água e lama. A ação não é permitida durante escalada ou natação.

**Consumo e colocação:** consome exatamente dez gravetos e cria a fogueira no ponto atual do terreno. Não permite duplicar fogo aceso nem criar outra fogueira sobre uma fogueira apagada a até 2,4 m. Reacender uma fogueira apagada ainda não está disponível.

**Resultado esperado:** fogueira simples acesa, com 180 segundos (3 minutos) de combustível inicial. O valor aprovado é 180 segundos; qualquer indicação de um minuto está incorreta.

**Combustível adicional:** um material inflamável consumido por ação pode adicionar até 60 segundos, respeitando o máximo total de 300 segundos (5 minutos). Gravetos, galhos e fibras vegetais são inflamáveis. O combustível continua decrescendo enquanto o menu está fechado. Ao chegar a zero, o fogo e a luz se apagam; há um anúncio único se o jogador estiver próximo.

**Limites:** as regras são experimentais do protótipo e não constituem um sistema geral de fogo ou sobrevivência. Não há salvamento/persistência das fogueiras. O comportamento de estação acima descreve a limitação de apoio/preparo; não define receitas ou alimentos implementados.

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
