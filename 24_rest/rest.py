# Michelle tang
# SoftDev1 pd6
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def welcome():
    lnk = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=ggxPACCj6D8IeIEilGt5Cs0oGyx7GKeeAXYqmdPP")
    data = lnk.read()
    nasa = json.loads(data) #creates a dictionary
    pic = nasa["url"]
    return render_template("home.html", pic = pic)

if __name__ == "__main__":
    app.debug = True
    app.run()
