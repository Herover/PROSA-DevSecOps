import os

from flask import Flask

app = Flask(__name__)

secret = "/j'Asv]4(bky*u2o[E|o]7pji=pQ$/I+v!Di?%$)lK;*464llLoQ}&FO\]8YVyU&"

@app.route('/')
def home():
    return "<h1>Welcome to the DevSecOps Secure App</h1>"+secret

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=os.environ['HOME'] == "a")
