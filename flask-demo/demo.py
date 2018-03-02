########################################
# flask demo
########################################

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
     return "Hi there"

@app.route('/SayHello/<username>')
def say_hello(username):
    return 'Hello %s' % username

app.run()

