from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)

cors = CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, Dog!</p>"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=8080)