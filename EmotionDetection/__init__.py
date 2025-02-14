import json
import requests

def emotion_detector(text_to_analyze):
    """Given a string text_to_analyze, will return string analysis."""
    if (text_to_analyze == ""):
        print("Error: no input provided to emotion_detector()")
        return {'dominant_emotion': None,
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0
            }
    # set up library call...
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    api_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    api_data_out = { "raw_document": { "text": text_to_analyze } }
    # fetch transfored data...
    response = requests.post(api_url, json=api_data_out, headers=api_headers)
    if response.status_code == 200:
        output = response.json()
    else:
        output = "Error: API failed to return a response"
        print("Error: API returned " + str(response.status_code) + ":" + response.reason)
        return {'dominant_emotion': None,
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0
            }
    
    # extract emotion scores with dominant emotion name...
    emotion_anger_score = output['emotionPredictions'][0]['emotion']['anger']
    emotion_disgust_score = output['emotionPredictions'][0]['emotion']['disgust']
    emotion_fear_score = output['emotionPredictions'][0]['emotion']['fear']
    emotion_joy_score = output['emotionPredictions'][0]['emotion']['joy']
    emotion_sadness_score = output['emotionPredictions'][0]['emotion']['sadness']
    emotion = output['emotionPredictions'][0]['emotion']

    scores = list(emotion.values())
    high_score_index = scores.index(max(scores))
    emotions = list(emotion.keys())
    emotion_dominant = emotions[high_score_index]


    return {'dominant_emotion': emotion_dominant,
            'anger': emotion_anger_score,
            'disgust': emotion_disgust_score,
            'fear': emotion_fear_score,
            'joy': emotion_joy_score,
            'sadness': emotion_sadness_score
            }
