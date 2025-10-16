import requests
import json

def emotion_detector(text_to_analyze):
    '''This function takes a text as an input and lets Watson NLP Library 
    Function 'Emotion Predict' analyse the text. The Output is in text format. '''
    
    #url to library
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #define header for request
    HEADERS =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #define input json file
    INPUT_JSON = { "raw_document" : { "text" : text_to_analyze}}
    #send a get request to application and store response
    response = requests.post(URL, headers = HEADERS, json = INPUT_JSON)
    #check if request was succesful
    if response.status_code == 200:
        #if request succesful convert response.text in json file
        formatted_response = json.loads(response.text)
        #Retrieve emotions with respective scores in dictionary
        res_dict = {}
        res_dict['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        res_dict['disgust'] =  formatted_response['emotionPredictions'][0]['emotion']['disgust']
        res_dict['fear'] =  formatted_response['emotionPredictions'][0]['emotion']['fear']
        res_dict['joy'] =  formatted_response['emotionPredictions'][0]['emotion']['joy']
        res_dict['sadness'] =  formatted_response['emotionPredictions'][0]['emotion']['sadness']
        ### find dominant emotion ###
        #convert scores to list and get the highest score and index
        score_list = list(res_dict.values())
        dominant_score = max(score_list)
        dominant_index = score_list.index(dominant_score)
        #having the index we can extract now the corresponding dominant_key
        key_list = list(res_dict.keys())
        dominant_key = key_list[dominant_index]
        # add dominant emotion to dict
        res_dict['dominant_emotion'] = dominant_key 
        ### output ###
        print('{')
        #iterate through the dictionary and print items for reqired output format
        for key, value in res_dict.items():
            print(f"'{key}': {value}")
        print('}')
        return res_dict
    elif response.status_code == 400:
        res_dict = {}
        res_dict['anger'] = None
        res_dict['disgust'] =  None
        res_dict['fear'] =  None
        res_dict['joy'] =  None
        res_dict['sadness'] =  None
        res_dict['dominant_emotion'] = None
        return res_dict
    else:
        return "Something went wrong. Status Code: " + str(response.status_code)