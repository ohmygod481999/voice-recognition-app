from flask import Flask, render_template, request, jsonify
import librosa
import os
import wave
import test
from flask_cors import CORS
from random import seed
from random import random
from db.database import *

app = Flask(__name__)
seed(1)

cors = CORS(app)

nchannels = 2
sampwidth = 2
framerate = 27000
nframes = 2

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/api/check-attendance', methods = ['POST'])
def api():
    try:
        blob = request.files['file']
        name = request.form['name']
        name_map = {
            "Nguyễn Nhật Minh": "nhat_minh",
            "Vương Bảo Long": "bao_long",
            "Nguyễn Huy Linh": "huy_linh",
            "Nguyễn Duy Chương": "duy_chuong",
            "Lê Văn Lợi": "le_loi",
            "Đinh Khánh Linh": "khanh_linh"
        }
        # data = blob.read()
        # print(data) 
        blob.save('blob.wav')
        best_score = test.best_score("blob.wav")
        print(best_score)
        if (name_map[name] == best_score[0]):
            return {
                'status': "success",
            }
        else:
            return {
                'status': "fail",
            }
    except Exception:
        return {
                'status': "fail",
        }


@app.route('/api/get-classes', methods = ['GET'])
def gClasses():
    conn = openConnection()
    classes = getClasses(conn)
    print(classes)
    return jsonify(classes)

@app.route('/api/get-students', methods = ['GET'])
def gStudents():
    classId = request.args['classId']
    conn = openConnection()
    students = getStudents(conn, classId)
    print(students)
    return jsonify(students)

@app.route('/api/get-class-transaction', methods = ['GET'])
def gClassTrans():
    classId = request.args['classId']
    conn = openConnection()
    transaction = getClassTransaction(conn, classId)
    print(transaction)
    return jsonify(transaction)

@app.route('/api/add-class-transaction', methods = ['POST'])
def aClassTrans():
    req = request.get_json()
    conn = openConnection()
    result = addClassTransaction(conn, req['classId'], req['detail'], req['date'])
    if result:
        return "success"
    return "fail"

if __name__ == "__main__":
    app.debug = True
    app.run()