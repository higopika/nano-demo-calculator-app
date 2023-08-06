from flask import Flask
from flask import request
import json
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    result = {}
    result['result'] = "hello world!"
    return result['result']

@app.route("/calculator/add", methods=['POST'])
def add():
    result={}
    numbers = request.get_json()
    res = int(numbers['first']) + int(numbers['second'])
    return json.dumps({'result':res})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    result = {}
    numbers = request.get_json()
    result['result'] = int(numbers['first']) + int(numbers['second'])
    return str(result['result'])

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
