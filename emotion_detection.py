"""Emotion detection"""

import json
import requests

# pylint: disable=line-too-long
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"


def get_dominant_emotion(emotions):
    """Return dominant emotion."""
    first_emotion = list(emotions.keys())[0]
    max_score = emotions[first_emotion]
    dominant_emotion = first_emotion
    for emotion, score in emotions.items():
        if score > max_score:
            dominant_emotion = emotion
            max_score = score

    return dominant_emotion


def emotion_detector(text_to_analyze):
    """This function performs emotion detection."""
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_to_send = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=json_to_send, headers=headers, timeout=30)
    if response.status_code == 200:
        result = json.loads(response.text)
        emotions = result["emotionPredictions"][0]["emotion"]
        output = emotions
        output["dominant_emotion"] = get_dominant_emotion(emotions)
        return output

    return None
