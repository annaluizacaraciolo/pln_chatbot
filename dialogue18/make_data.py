import json

if __name__ == '__main__':
    with open("dialogue18/dialogues_018.json", 'r') as file:
        data_018 = json.load(file)

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
        