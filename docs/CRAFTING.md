# Phoenix Island — receitas de fabricação e resultados esperados

**Escopo:** receitas, conversões e ações de criação que estão de fato implementadas no protótipo, separadas das decisões de design aprovadas mas ainda não codificadas. Este documento descreve o estado do código; não autoriza novos itens, receitas ou efeitos.

O protótipo testa uma pequena fatia de coleta, fabricação e uso de ferramentas. Estas regras não definem um sistema completo de sobrevivência nem devem ser extrapoladas para o jogo futuro. Para decisões gerais e limites do projeto, consulte [`GDD.md`](GDD.md). O GDD é a referência para as regras vigentes; o [`DEVLOG.md`](DEVLOG.md) registra o histórico de implementação e testes. Se um registro histórico divergir da regra aprovada mais recente, prevalece o GDD e este documento atualizado.

## Organização por tier

Para a etapa inicial de implementação, antes de alterar o mapa, as ferramentas mais rústicas aprovadas ficam no **Tier 1**. Neste momento, Tier 1 inclui a faca de pedra, o martelo de pedra e a fogueira simples. A fogueira é uma ferramenta do tipo **estação de trabalho**: não pode ser carregada e é a estação mais básica.

A classificação descreve o escopo inicial atual; não afirma que todas as ferramentas futuras já foram definidas, nem estabelece conteúdo, materiais, receitas ou regras para tiers posteriores. Tiers futuros permanecem sem especificação até decisão explícita.

## Materiais: propriedades e usos

Esta lista separa o que já está definido ou presente no protótipo das possibilidades de uso indicadas para o design futuro. Uma possibilidade não é uma receita aprovada nem significa que o objeto ou sistema já esteja implementado.

### Gravetos

- **Propriedades:** peças pequenas em comparação com galhos; menores e mais frágeis que eles. São inflamáveis.
- **Papel definido no design:** combustível e partes para ferramentas e estruturas. São adequados a cabos e outras peças menores, mas não têm a resistência de galhos.
- **Uso concreto no protótipo:** ingrediente do martelo de pedra (1 graveto) e criação da fogueira simples (10 gravetos consumidos). Um graveto também pode abastecer uma fogueira acesa.
- **Ainda não especificado:** receitas de estruturas ou de outras ferramentas com gravetos.

### Galhos

- **Propriedades:** hastes maiores e mais resistentes que gravetos; são inflamáveis.
- **Uso atual no protótipo:** são inflamáveis e podem ser consumidos como combustível. Um galho equipado pode ser convertido em dois gravetos no chão, se uma faca de pedra estiver no inventário; ela não precisa estar equipada.
- **Uso em ferramentas/estruturas:** ainda não há receita especificada que use galhos como componente. Por serem maiores e mais resistentes que gravetos, poderão servir de base para ferramentas como lança e picareta e para estruturas. São possibilidades de design, não receitas aprovadas ou autorização de implementação.

### Fibras vegetais

- **Origem atual:** encontradas em arbustos; cada arbusto fornece duas fibras vegetais no protótipo atual.
- **Papel definido no design:** material inflamável para improvisar amarrações e conectar componentes.
- **Uso de design aprovado:** uma fibra amarra a pedra ao cabo do martelo; na receita futura de design da faca, prende a lâmina de pedra lascada ao graveto.
- **Uso concreto no protótipo:** 1 fibra vegetal é consumida na receita implementada do martelo de pedra. A faca atualmente usa duas pedras e não consome graveto nem fibra.
- **Ainda não especificado:** outras receitas de amarração ou componentes de estruturas; nenhuma foi aprovada.

### Pedras

- **Propriedades:** forma mais básica de mineral presente no projeto; são resistentes e não inflamáveis. Podem ser moldadas, mas com limitações: não têm a flexibilidade de metais.
- **Papel definido no design:** matéria-prima resistente para ferramentas e estruturas, moldável dentro de limites; não tem a flexibilidade dos metais.
- **Cadeia aprovada apenas para o design futuro:** duas pedras → uma pedra afiada; uma pedra + uma pedra afiada → uma pedra lascada; uma pedra lascada + um graveto + uma fibra → faca de pedra. A pedra afiada é um componente intermediário de design; receitas para ferramentas futuras não estão decididas.
- **Uso concreto no protótipo:** pedras são recolhidas soltas ou obtidas de afloramentos; a faca atual consome duas pedras e o martelo consome uma pedra. A cadeia de pedra afiada/lascada não está implementada.
- **Ainda não especificado:** processo e limites práticos de moldagem além desta cadeia, receitas adicionais e funções estruturais concretas. Não assumir técnicas ou propriedades além das descritas.


## Estado do crafting no protótipo

No código consultado, há quatro ações implementadas de criação/conversão relacionadas a itens:

1. **Faca de pedra:** equipa uma pedra e mantenha outra pedra no inventário; a ação consome duas pedras no total e produz uma faca. Estar no chão é obrigatório. Não requer graveto nem fibra. É a receita atual do protótipo, embora seja diferente da receita de design futuro abaixo.
2. **Martelo de pedra:** consome 1 pedra, 1 graveto e 1 fibra vegetal, e produz um martelo reutilizável. Estar no chão é obrigatório. A fibra representa a amarração da pedra ao cabo.
3. **Galho → gravetos:** equipe 1 galho e tenha uma faca de pedra em qualquer espaço do inventário. No chão, a ação consome o galho e produz 2 gravetos; a faca não é consumida nem precisa estar equipada. É preciso haver espaço para receber gravetos, a menos que já exista uma pilha de gravetos.
4. **Fogueira simples:** equipe uma pilha com pelo menos 10 gravetos e esteja no chão, em terreno seco, fora da água e da lama. Consome exatamente 10 gravetos e coloca uma fogueira no ponto atual do jogador, com 180 segundos (3 minutos) de combustível inicial.

As ferramentas e a fogueira são resultados distintos: o martelo e a faca permanecem no inventário como ferramentas, enquanto a fogueira é criada no cenário. As descrições de menu/contexto, requisitos e condições podem restringir quando cada ação aparece ou pode ser executada; não se deve inferir receitas adicionais a partir dos materiais disponíveis.

### Processamento de pedra — design futuro aprovado, ainda não implementado

A cadeia abaixo continua sendo uma decisão de design, não a receita que o protótipo executa hoje:

1. Duas pedras → uma pedra afiada.
2. Uma pedra + uma pedra afiada → uma pedra lascada.
3. Uma pedra lascada + um graveto + uma fibra vegetal → uma faca de pedra; a fibra amarra a lâmina ao cabo.

O código atual ainda fabrica a faca diretamente com duas pedras. Pedra afiada, pedra lascada e as duas primeiras etapas de processamento não estão implementadas. Ferramentas futuras como machado e picareta não têm receitas definidas. Esta distinção evita tratar o plano aprovado como funcionalidade existente.

## Tier 1 — ferramentas rústicas iniciais

### Ferramentas carregáveis

### Faca de pedra

**Receita atualmente implementada:** equipe uma pedra e mantenha pelo menos uma pedra adicional no inventário. A ação consome duas pedras no total e produz uma faca de pedra. Exige estar no chão. Não requer graveto nem fibra vegetal.

**Receita de design futuro aprovada, não implementada:** uma pedra lascada, um graveto e uma fibra vegetal; a fibra amarra a lâmina de pedra lascada ao graveto, que serve de cabo. A cadeia de processamento de pedra necessária para obter a pedra lascada também não está implementada.

**Uso definido:** quando equipada, pode cortar galhos vivos baixos da copa por golpes sucessivos. Cada alvo de galho vivo tem resistência 6; cada golpe da faca causa dano inteiro sorteado uniformemente entre 1 e 3. Ao esgotar a resistência, o alvo entrega um galho. A faca não é necessária para recolher galhos que já caíram no chão.

**Limites:** a faca não é ferramenta de impacto. Não atribuir a ela outras funções ou efeitos sem decisão explícita.

### Martelo de pedra

**Receita implementada:** consome 1 pedra, 1 graveto e 1 fibra vegetal; a fibra serve para afixar a pedra ao cabo. Exige estar no chão.

**Resultado:** um martelo de pedra reutilizável. Não há durabilidade definida para o protótipo atual.

**Uso definido:** o martelo permite minerar afloramentos maiores. Basta estar no inventário; não precisa estar equipado. Cada afloramento tem resistência 12, e cada golpe do martelo causa dano inteiro sorteado uniformemente entre 2 e 4. A mineração exige vários golpes e só entrega as pedras no golpe final.

**Resultado e falha de inventário:** se o golpe que esgotaria a fonte não puder guardar a recompensa, a resistência não diminui; o dano já sorteado fica pendente para aplicação posterior sem novo sorteio quando houver espaço. A recompensa não deve ser perdida.

**Limites:** o martelo não corta nem quebra galhos, não converte galho em gravetos e não tem função de construção. Não adicionar outras funções sem decisão explícita.

### Estação de trabalho: fogueira simples

A fogueira simples é uma ferramenta fixa, não carregável, e a estação de trabalho mais básica. Ela não tem superfície, apoio ou suporte onde deixar um item em preparo. Portanto, não permite iniciar algo, afastar-se e deixá-lo sendo preparado sozinho. Se o jogador for preparar, por exemplo, carne assada nela, deverá manter a carne num espeto e segurá-lo dentro do alcance da fogueira durante o preparo. Esse exemplo registra o comportamento esperado da estação; não aprova uma receita, item, duração ou implementação de preparo de alimentos.


**Ingredientes:** dez gravetos na pilha equipada.

**Condições:** estar no chão seco, fora de água e lama. A ação não é permitida durante escalada ou natação.

**Consumo e colocação no código atual:** consome exatamente dez gravetos e cria a fogueira na posição atual do jogador, desde que esteja no chão e fora de água e lama. A implementação consultada não verifica proximidade de fogueiras já existentes; portanto, a regra de impedir outra fogueira dentro de 2,4 m não está implementada. Reacender uma fogueira apagada também não está disponível.

**Resultado no código atual:** fogueira simples acesa, com 180 segundos (3 minutos) de combustível inicial. O valor aprovado e implementado é 180 segundos; qualquer indicação de um minuto está incorreta. O texto do menu contextual ainda contém essa indicação incorreta.

**Combustível adicional:** um material inflamável consumido por ação pode adicionar até 60 segundos, respeitando o máximo total de 300 segundos (5 minutos). Gravetos, galhos e fibras vegetais são inflamáveis. O combustível continua decrescendo enquanto o menu está fechado. Ao chegar a zero, o fogo e a luz se apagam; há um anúncio único se o jogador estiver próximo.

**Limites:** as regras são experimentais do protótipo e não constituem um sistema geral de fogo ou sobrevivência. Não há salvamento/persistência das fogueiras. O comportamento de estação acima descreve a limitação de apoio/preparo; não define receitas ou alimentos implementados.

## Coleta e conversão de galho em gravetos

**Conversão implementada:** no chão, com um galho equipado e uma faca de pedra em algum espaço do inventário (não precisa estar equipada), a ação consome 1 galho e produz 2 gravetos. A faca não é consumida. Se não houver pilha de gravetos nem espaço para criar uma, a ação não consome o galho.

**Distinção importante:** galho caído no chão é recolhido com Enter, sem faca ou golpes. Galho vivo baixo na copa é uma fonte de extração e requer faca equipada e golpes sucessivos; ao esgotá-lo, fornece um galho. Não confundir a coleta do galho caído, o corte de um galho vivo e a conversão de galho em gravetos.

## Resultados de coleta relacionados às receitas

- Cada arbusto coletado fornece duas fibras vegetais no protótipo atual.
- Pedras soltas, arbustos, galhos caídos e cinzas são coletados com Enter quando o alvo é elegível; a coleta respeita mira, alcance e espaço no inventário.
- Afloramentos exigem um martelo no inventário e são minerados com Espaço em golpes sucessivos. As pedras só são entregues ao esgotar o afloramento.
- Se a recompensa de uma coleta não couber no inventário, não consumir nem remover o recurso do cenário.

## Princípios para avaliar outras receitas

Antes de aprovar uma receita nova, registrar os ingredientes e suas quantidades, quais itens são consumidos, as condições de execução, o resultado fabricado, onde/como o resultado pode ser usado, o que acontece quando falta requisito ou espaço e se uma tentativa falha consome recursos. Não inferir uma receita a partir de convenções de gênero, realismo ou possibilidades do código.

**Ainda não definido neste documento:** além da cadeia futura de pedra já aprovada, receitas futuras, custos adicionais, durabilidade de ferramentas, reaparecimento de recursos, progressão, salvamento e construção de base. São decisões em aberto, não espaços para completar por suposição.

## Referências de projeto

- [`GDD.md`](GDD.md) — regras de design vigentes, interações, ferramentas e limites do protótipo.
- [`DEVLOG.md`](DEVLOG.md) — histórico de implementação, verificações e validação pendente.
