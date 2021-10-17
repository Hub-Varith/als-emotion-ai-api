from flask import Flask
from flask.json import jsonify
from model import Model
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Main page</p>"

@app.route("/predict", methods = ['POST'])
def predict_emo():
    if request.method == 'POST':
        x = request.json['textdata']
        prd = model.predict(x)
        return jsonify(result = str(prd))

if __name__ == "__main__":
    model = Model()
    app.run(host='0.0.0.0', port=8080)



