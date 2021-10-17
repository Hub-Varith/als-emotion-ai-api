from flask import Flask
from flask.json import jsonify
from model import Model
from flask import request
import sys
import logging

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route("/")
def index():
    return "<p>Main page</p>"

@app.route("/predict", methods = ['GET', 'POST'])
def predict_emo():
    if request.method == 'POST':
        x = request.json['textdata']
        prd = model.predict(x)
        return jsonify(result = str(prd))
    return "Predict"

if __name__ == "__main__":
    model = Model()
    app.run(debug=False)



