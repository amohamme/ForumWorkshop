########################################
# flask demo
########################################

from flask import Flask, render_template
from Forums import models
from Forums import stores

app = Flask(__name__)

post_store = stores.PostStore()
post_store.add(models.post("Life", "Life is alawys great"))
post_store.add(models.post("Sunshine", "Sunshine is amazing"))


@app.route("/")
@app.route("/index")
def home():
     return render_template("index.html", posts = post_store.get_all())

@app.route('/SayHello/<username>')
def say_hello(username):
    return 'Hello %s' % username

app.run()

