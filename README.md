# Chatbot para marcação de voos

Este projeto consiste do desenvolvimento de um chatbot para busca e marcação de passagens áreas.

## Entregáveis
1. Classificadores de intenção, extratores de entidade e interface de chat utilizando deep learning encontram-se no notebook `PassagensChatbot.ipynb`
2. Projeto de chatbot no rasa encontra-se no diretório `rasa_chatbot`
3. [Apresentação no Canva](https://www.canva.com/design/DAF98MwZZo0/kUGd-pG7Y_yv0a0KCV2mjQ/edit?utm_content=DAF98MwZZo0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
4. Apresentação no formato PDF encontra-se no arquivo `PassagensChatbot.pdf`
5. [Apresentação em vídeo]()

## Dados
Os dados utilizados para treinamento do chatbot encontram-se disponíveis no [dstc8 schema guided dialogue](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue). Foi selecionado um subconjunto deste conjunto de dados para refletir apenas o domínio de viagem.

### Intenções
As intenções que serão classficadas pelo chatbot serão: </br>
1. ReserveOnewayFlight
2. SearchOnewayFlight
3. SearchRoundtripFlights
4. ReserveRoundtripFlights
5. NONE *verificar se isso é válido


## Modelos de aprendizagem
O tamanho do sobconjunto de dados definido é uma característica muito relevante para a tarefa de classificação da intenção, tendo em vista que a pequena quantidade de dados de treinamento poderá resultar em overfitting dos modelos de aprendizagem. </br>

Para a tarefa de classificação de intenções, realizamos uma análise comparativa dos resultados obtidos durante treinamento e teste dos seguintes modelos:
- LSTM
- CNN
- SVM
- Transformer (BERT)
</br>

Também foram implementados extratores de entidades para reconhecimento de entidades da sentenças baseados em transformer (BERT) e LSTM.

### Avaliação
A base de dados sob estudo foi previamente dividida em subconjuntos de treinamento e de teste, de forma que ambas amostras nunca se misturam durante os processos de treino e teste. A avaliação da performance dos modelos sob o subcojunto de teste mede a acurácia e o F1-score dos modelos treinados anteriormente.

# Referências

[1] 
Rastogi, Abhinav, Xiaoxue, Zang, Srinivas, Sunkara, Raghav, Gupta, Pranav, Khaitan. "Towards scalable multi-domain conversational agents: The schema-guided dialogue dataset." Proceedings of the AAAI Conference on Artificial Intelligence. 2020.

[2] 
Lee, Harrison, Raghav, Gupta, Abhinav, Rastogi, Yuan, Cao, Bin, Zhang, Yonghui, Wu. "SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems." Proceedings of the AAAI Conference on Artificial Intelligence. 2022.

[3] [Rasa nlu in depth](https://rasa.com/blog/rasa-nlu-in-depth-part-1-intent-classification/)

[4] [Rasa FAQs](https://rasa.com/docs/rasa/chitchat-faqs/)
