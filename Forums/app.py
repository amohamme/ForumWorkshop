########################################
# flask demo
########################################

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
     return render_template("index.html")

@app.route('/SayHello/<username>')
def say_hello(username):
    return 'Hello %s' % username

app.run()

