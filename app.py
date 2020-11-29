import json
from flask import Flask, render_template
import requests 

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

'''
@app.route('/parks')
def parksPage():
    return render_template("parks.html", parks = parks)
'''

@app.route('/parks')
def nationalParksPage():
    base_url = 'https://developer.nps.gov/api/v1/parks?api_key=oqa2UTZlkEAwogH10IBj7Rt687267NUWoSqoNQLC&limit=10'

    r = requests.get(base_url)

    parks = r.json()['data']

    return render_template("parks.html", parks = parks)

if __name__ == "__main__":
    app.run()

