from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexMF.html")

@app.route("/<string:name>")
def hello(names):
    return "Hello, {names}!"

