# Escopo de implementação — percepção visual

**Data:** 13 de novembro de 2026  
**Status:** fronteira aprovada para a próxima tarefa de implementação; nenhuma implementação é autorizada por este documento isoladamente. Uma solicitação de codificação continua necessária.  
**Referência de design:** [`GDD.md`, seção “Percepção visual do cenário”](GDD.md)

## 1. Objetivo e limite

Este documento define até onde a IA de desenvolvimento pode ir quando Anderson solicitar a codificação da etapa atual de percepção. O escopo é implementar e testar o cálculo de alcance de identificação e detecção usando os parâmetros hipotéticos já aprovados. **Não é o escopo do sistema completo de oclusão.**

A IA deve primeiro inspecionar o código atual e identificar as entradas ambientais e o ponto de referência de distância que já existem. Se uma entrada exigida abaixo não existir, não a inventar nem substituí-la por uma estimativa visual; pare no limite indicado e pergunte a Anderson. Não alterar documentos, código, publicação ou releases em resposta a um pedido apenas de análise.

## 2. O que pode ser implementado após pedido explícito de codificação

1. Criar ou ajustar um cálculo determinístico e testável que receba:
   - distância atual entre jogador e o ponto de referência do alvo já usado pelo código;
   - classe de detecção de gameplay já listada no GDD (grande, média ou pequena);
   - iluminância ambiente local em lux;
   - uma condição atmosférica pertencente às cinco categorias do GDD.
2. Calcular, separadamente para identificação e para detecção de contorno/indício:
   `alcance efetivo = min(alcance-base da classe × multiplicador da banda de lux, teto da condição atmosférica)`.
   Usar os números e os limites inclusivos/exclusivos exatamente como registrados no GDD. Não interpolar, arredondar parâmetros, acumular modificadores nem acrescentar fatores.
3. Para um alvo que o sistema atual já seleciona e considera sem oclusão segundo sua regra existente, aplicar os estados:
   - distância menor ou igual ao alcance de identificação: permitir o nome/tipo do alvo já selecionado;
   - acima do alcance de identificação e menor ou igual ao alcance de contorno: somente mensagem de silhueta quando a categoria já é conhecida; se o tipo não puder ser definido pelo estado de dados existente, usar “algo à distância”;
   - acima do alcance de contorno: não emitir a descrição perceptiva desse alvo.
4. Preservar integralmente a seleção atual de candidatos: mesma lista de alvos, prioridades, quantidade e ordem de anúncio. A implementação não pode revelar candidatos que o código atual não selecionaria nem suprimir/alterar outros anúncios por uma regra nova. Se não for possível aplicar o limiar sem modificar essa seleção ou sua prioridade, não integrar; entregar apenas o cálculo isolado com testes e relatar a dependência.
5. A fogueira permanece na classe pequena para reconhecimento pela forma. Pode-se implementar cálculo separado do brilho com alcance-base de 25 m **somente se** o jogo já fornecer um estado explícito de “condição escura” e as entradas de lux e condição atmosférica necessárias. Aplicar ao brilho o teto atmosférico, sem o multiplicador de lux, e não chamar a fonte de “fogueira” além do limite de identificação da forma. Se não houver sinal explícito de escuridão, não definir um limiar de lux nem ligar esse bônus ao gameplay; perguntar a Anderson.
6. Testes unitários ou equivalentes para valores imediatamente abaixo, exatamente nos limites e imediatamente acima de todas as bandas de lux, limites de distância, seleção de estado (identificação/contorno/não detectado), tetos atmosféricos e tratamento separado do brilho da fogueira. Testar também que a lista, a ordem e a prioridade dos anúncios existentes não mudaram.

As palavras “grande”, “média” e “pequena” neste cálculo são **classes de detecção**. Não usar a escala de porte físico (minúsculo a monumental) para atribuir ou calcular classes de detecção. Usar apenas as associações de alvos já explicitadas na tabela do GDD; não classificar novos objetos nem reavaliar dimensões de assets nesta etapa.

## 3. Parar e perguntar — entradas ausentes ou não decididas

- Se o jogo não tiver uma fonte de iluminância local em lux, não derivar lux de cor, intensidade de shader, horário, preset, exposição ou aparência de captura. O cálculo pode ser implementado como função isolada que recebe lux; integração ao jogo fica bloqueada até Anderson definir a fonte/representação.
- Se não existir um estado atmosférico explícito com uma das cinco categorias do GDD, não inferir névoa de partículas ou distância visual e não criar clima, névoa, fumaça, controles, configurações ou interface. A função pode receber a categoria como entrada isolada; a integração fica bloqueada.
- O bônus de brilho da fogueira só pode ser integrado se houver estado explícito de escuridão. Não inventar corte de lux, transição gradual, interpolação ou regra para ambientes claros.
- Se o código não tiver um ponto de referência estável do alvo que possa ser mantido sem mudança semântica, não escolher centro, origem, bounding box ou outro ponto por conta própria. Relatar o ponto existente e perguntar qual deve ser usado.
- Se integrar exigir novos alvos, nova enumeração global, mudança de prioridade/quantidade de anúncios ou alteração de textos fora das mensagens já aprovadas, parar e perguntar.

## 4. Fora do escopo — não implementar nesta etapa

- Oclusão geométrica nova ou geral; classificação de quais geometrias bloqueiam; oclusão parcial; fração do alvo encoberta; vários alvos alinhados; transparência, folhagem, água, fumaça ou materiais como categorias de bloqueio; e regra de anúncio para alvos atrás de outros. Esses tópicos aguardam decisões específicas de Anderson.
- Usar porte físico, dimensão da malha, área projetada ou distância para deduzir automaticamente que um alvo bloqueia outro. A escala de porte físico é taxonomia aprovada, não política de oclusão.
- Multiplicador numérico por altitude, relevo, obstáculos, contraste ou qualquer fator além das bandas e tetos aprovados. A oclusão existente deve permanecer inalterada nesta etapa.
- Alterar campo de visão/câmera, converter o `camera.far = 100` em regra de percepção, alterar colisões, deslocamento, alcance de interação, coleta, escalada, natação ou geometria do mapa.
- Criar ou ampliar sistemas de dia/noite, clima, neblina, fumaça, iluminação, detecção global ou classes de objetos para alimentar o cálculo.
- Tratar esta fronteira documental como autorização para codificar sem solicitação explícita.

## 5. Relato obrigatório ao terminar uma tarefa de código

Informar os arquivos alterados e separar: cálculo implementado; fontes reais de lux/atmosfera/escuridão encontradas ou ausentes; integração realizada ou deliberadamente não realizada; testes automatizados executados; teste de gameplay e validação de Anderson ainda pendentes. Não declarar oclusão, percepção geral ou acessibilidade validadas por testes unitários, revisão estática ou página carregada.
