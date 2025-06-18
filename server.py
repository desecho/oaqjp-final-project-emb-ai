"""Flask app"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector()
    function.
    """
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result is None:
        return "Invalid input! Try again."
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    message = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return message


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


# This executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
