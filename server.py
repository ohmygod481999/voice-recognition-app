from flask import Flask, render_template, request
import librosa
import os
import wave
import google_regconition

app = Flask(__name__)

nchannels = 2
sampwidth = 2
framerate = 27000
nframes = 2

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/api', methods = ['POST'])
def api():
    blob = request.files['file']
    # print(blob.read()) 
    blob.save('blob.wav')
    # y, sr = librosa.load('blob.wav')
    text = google_regconition.recognizeAudio('blob.wav')
    return text

if __name__ == "__main__":
    app.run()