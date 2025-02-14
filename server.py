"""
Main Flask app file which provides user an interface to the emotion detector api
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def hello():
    """
    default route handler
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    callback route for index.html calls
    """
    emotion_analysis = emotion_detector(request.args['textToAnalyze'])

    if emotion_analysis['dominant_emotion'] is None: # error
        return "Invalid text! Please try again!"

    result = "'anger': " + str(emotion_analysis['anger']) + ", "
    result = result + "'disgust': " + str(emotion_analysis['disgust']) + ", "
    result = result + "'fear': " + str(emotion_analysis['fear']) + ", "
    result = result + "'joy': " + str(emotion_analysis['joy']) + "and "
    result = result + "'sadness': " + str(emotion_analysis['sadness']) + ". "
    result = result + "The dominant emotion is <strong>" + \
                        emotion_analysis['dominant_emotion'] + "</strong>."
    return result
