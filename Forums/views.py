from flask import render_template, request, Flask, redirect, url_for
from Forums import models
from Forums.app import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())

@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")
