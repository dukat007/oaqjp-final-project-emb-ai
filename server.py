from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection_fun():
    ''' This functions retrieves the parameter from website and calls emotion_detection function
    The output is formatted in text form.
    '''
    text_to_analyze = request.args.get('textToAnalyze') #retrieve parameter text
    res = emotion_detector(text_to_analyze) # apply function
    ## error handling ##
    if res['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    ## output format ##
    out_str = ("For the given statement, the system response is 'anger': " + str(res['anger']) 
    + ", 'disgust': "  + str(res['disgust']) + ", 'fear': " + str(res['fear']) 
    + ", 'joy': " + str(res['joy']) + " and 'sadness': " + str(res['sadness']) 
    + ". The dominant emotion is " + str(res['dominant_emotion']) + ".")
    return out_str

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)