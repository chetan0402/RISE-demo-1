from flask import Flask, url_for, redirect, request

app = Flask(__name__)

data: dict[str, list[str]] = {}

@app.route("/")
def home():
    return redirect(url_for("static",filename="index.html"))

@app.route("/submit")
def submit():
    print(request.args)
    name=request.args["name"]
    content=request.args["content"]
    author=request.args["author"]
    value=[content,author]
    data[name]=value
    return "Submitted"

@app.route("/blog")
def blog():
    name=request.args["name"]
    content=data[name]
    return content
