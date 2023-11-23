# Chatbot para marcação de transporte de viagens

Este projeto consiste do desenvolvimento de um chatbot para marcação de passagens áreas ou de ônibus.

## Dados
Os dados utilizados para treinamento do chatbot encontram-se disponíveis no [dstc8 schema guided dialogue](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue). Foi selecionado um subconjunto deste conjunto de dados para refletir apenas o domínio de viagem.

### Intenções
As intenções que serão classficadas pelo chatbot serão: </br>
1.  ReserveOnewayFlight
2. SearchOnewayFlight
3. SearchRoundtripFlights
4. ReserveRoundtripFlights
5. NONE *verificar se isso é válido
6. FindBus
7. BuyBusTicket


## Modelos de aprendizagem
O tamanho do sobconjunto de dados definido é uma característica muito relevante para a tarefa de classificação da intenção, tendo em vista que a pequena quantidade de dados de treinamento poderá resultar em overfitting dos modelos de aprendizagem. </br>

Desta forma, foram escolhidas 3 redes neurais ... 

# Referências

[1] 
Rastogi, Abhinav, Xiaoxue, Zang, Srinivas, Sunkara, Raghav, Gupta, Pranav, Khaitan. "Towards scalable multi-domain conversational agents: The schema-guided dialogue dataset." Proceedings of the AAAI Conference on Artificial Intelligence. 2020.

[2] 
Lee, Harrison, Raghav, Gupta, Abhinav, Rastogi, Yuan, Cao, Bin, Zhang, Yonghui, Wu. "SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems." Proceedings of the AAAI Conference on Artificial Intelligence. 2022.


