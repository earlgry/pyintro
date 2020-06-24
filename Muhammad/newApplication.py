from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!!!!YAY!! STOP BEING SO COMP-SCI "

@app.route("/Brit")
def Brit():
    return "Hello Dona"