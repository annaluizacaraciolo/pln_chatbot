
import json


if __name__ == '__main__':
    with open("dialogues_018.json", 'r') as file:
        data_018 = json.load(file)

    for i in range(len(data_018)):
        current_speaker = data_018[i]
        turns_amount = len(data_018[i]['turns'])
        for j in range(turns_amount):
            utterance = current_speaker['turns'][j]['utterance']
            print(utterance)