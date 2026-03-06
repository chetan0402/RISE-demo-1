from flask import Flask, url_for, redirect, request

app = Flask(__name__)

data: dict[str, list[str]] = {}

@app.route("/")
def home():
    return redirect(url_for("static",filename="index.html"))

@app.route("/submit",methods=["POST"])
def submit():
    print(request.form)
    name=request.form["name"]
    content=request.form["content"]
    author=request.form["author"]
    value=[content,author]
    data[name]=value
    return redirect(url_for("blog",name=name))

@app.route("/blog")
def blog():
    name=request.args["name"]
    content=data[name]
    return content
