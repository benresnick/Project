from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def opensite():
    my_name = "Ben Resnick"
    return render_template("firstsite.html", name=my_name)

@app.route('/<name>')
def invalidroutes(name):
    return "Sorry, but '" + name + "' is not a valid route"

app.run()
