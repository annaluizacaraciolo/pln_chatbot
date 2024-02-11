import json
import yaml
import ruamel.yaml
import sys

def literal(*args):
    # convert args to a multiline string that looks like block sequence
    # convert to string in case non-strings were passed in
    return ruamel.yaml.scalarstring.LiteralScalarString('- ' + '\n- '.join([str(x) for x in args]) + '\n')   

if __name__ == '__main__':
    with open("dialogue18/dialogues_018.json", 'r') as file:
        data_018 = json.load(file)

    NONE_list = []
    SearchOnewayFlight_list = []
    ReserveOnewayFlight_list = []
    SearchRoundtripFlights_list = []
    ReserveRoundtripFlights_list = []

    for i in range(len(data_018)):
        frames_amount = len(data_018[i]['turns'])
        for j in range(frames_amount):
            current_frame = data_018[i]['turns'][j]
            speaker = current_frame['speaker']
            if speaker == 'USER':
                intent = current_frame['frames'][0]['state']['active_intent']
                utterance = current_frame['utterance']
                
                file_path = "c:\\Users\\Anna Luiza\\Documents\pln_chatbot\\dialogue18\\" + intent + "\\" + str(i) + "_" + str(j) + ".txt"
                
                f = open(file_path, "w+")
                f.write(utterance)
                f.close()

                # adaptando conjunto de dados para o RASA
                if intent == 'SearchOnewayFlight':
                    SearchOnewayFlight_list.append(utterance)
                elif intent == 'ReserveOnewayFlight':
                    ReserveOnewayFlight_list.append(utterance)
                elif intent == 'SearchRoundtripFlights':
                    SearchRoundtripFlights_list.append(utterance)
                elif intent == 'ReserveRoundtripFlights':
                    ReserveRoundtripFlights_list.append(utterance)
                elif intent == 'NONE':
                    NONE_list.append(utterance)
    
    
    data = {'version': '3.1',
    'nlu': [{'intent': 'SearchOnewayFlight', 'examples': literal(*SearchOnewayFlight_list)},
    {'intent': 'ReserveOnewayFlight', 'examples': literal(*ReserveOnewayFlight_list)},
    {'intent': 'SearchRoundtripFlights', 'examples': literal(*SearchRoundtripFlights_list)},
    {'intent': 'ReserveRoundtripFlights', 'examples': literal(*ReserveRoundtripFlights_list)},
    {'intent': 'NONE', 'examples': literal(*NONE_list)}]}
        
    yaml = ruamel.yaml.YAML()
    #yaml.dump(data, sys.stdout)

    # File path
    file_path = 'output.yml'

    # Open the file in write mode and use yaml.dump
    with open(file_path, 'w') as file:
        yaml.dump(data, file)
        