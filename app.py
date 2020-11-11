import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def helloName(name=None):
    return render_template("hello.html", name=name)


#Read parks.json file and store it as parks
with open('parks.json', 'r') as f:
    parks = json.load(f)

@app.route('/parks')
def parksList():
    return render_template("parksDisplay.html", parks = parks)

if __name__ == "__main__":
    app.run()

