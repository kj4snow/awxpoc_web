from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World v1</h1>"

if __name__ == '__main__':
    app.run(port='5000',debug=True)