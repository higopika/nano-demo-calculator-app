from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    result = {}
    result['result'] = "Greetings"
    return result

@app.route("/calculator/add", methods=['POST'])
def add():
    result={}
    numbers = request.get_json()
    result['result'] = int(numbers['first']) + int(numbers['second'])
    return result

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    result = {}
    numbers = request.get_json()
    result['result'] = int(numbers['first']) + int(numbers['second'])
    return result

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
