from flask import Flask, render_template, request, jsonify, send_from_directory
import librosa
import os
import wave
import test
from flask_cors import CORS, cross_origin
from random import seed
from random import random
from db.database import *
from export_excel import *

app = Flask(__name__, static_folder='static', static_url_path='/')
seed(1)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["CLIENT_CSV"] = "csv_file"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/check-attendance', methods = ['POST'])
@cross_origin()
def api():
    try:
        blob = request.files['file']
        noiseBlob = request.files['noise']

        name = request.form['name']
        name_map = {
            "Nguyễn Nhật Minh": "nhat_minh",
            "Vương Bảo Long": "bao_long",
            "Nguyễn Huy Linh": "huy_linh",
            "Nguyễn Duy Chương": "duy_chuong",
            "Lê Văn Lợi": "le_loi",
            "Đinh Khánh Linh": "khanh_linh"
        } 
        blob.save('blob.wav')
        noiseBlob.save('noise_blob.wav')
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
@cross_origin()
def gClasses():
    conn = openConnection()
    classes = getClasses(conn)
    print(classes)
    return jsonify(classes)

@app.route('/api/get-students', methods = ['GET'])
@cross_origin()
def gStudents():
    classId = request.args['classId']
    conn = openConnection()
    students = getStudents(conn, classId)
    print(students)
    return jsonify(students)

@app.route('/api/get-class-transaction', methods = ['GET'])
@cross_origin()
def gClassTrans():
    classId = request.args['classId']
    conn = openConnection()
    transaction = getClassTransaction(conn, classId)
    print(transaction)
    return jsonify(transaction)

@app.route('/api/add-class-transaction', methods = ['POST'])
@cross_origin()
def aClassTrans():
    req = request.get_json()
    conn = openConnection()
    result = addClassTransaction(conn, req['classId'], req['detail'], req['date'])
    if result:
        return "success"
    return "fail"


@app.route("/attendant-csv/<id>")
def get_file(id):
    """Download a file."""
    # req = request.get_json()
    conn = openConnection()
    transaction = getTransaction(conn, id)
    date = transaction[1]
    classId = transaction[2] 
    detail_json = transaction[3]
    detail = json.loads(detail_json)
    print(detail)
    print(type(detail))
    ids = []
    names = []
    attendances = []
    for student in detail:
        ids.append(student['id'])
        names.append(student['name'])
        attendances.append(student['attendant'])
    exportData = {
        'MSSV': ids,
        'Họ và Tên': names,
        'Có mặt': attendances
    }
    filename = "attendant-" + classId + "-" + date + ".csv"
    saveFileCsv(filename, exportData, ['MSSV', 'Họ và Tên', 'Có mặt'])
    return send_from_directory(app.config["CLIENT_CSV"], filename, as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()