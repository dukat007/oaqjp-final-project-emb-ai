import requests

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
        return response.text
    else:
        return "Something went wrong. Status Code: " + str(response.status_code)