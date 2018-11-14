# Michelle Tang
# SoftDev1 pd6
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def welcome():
    lnk = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=Qyrxovb3AXTeMsth93T4hVnmzDcSGQDZnHxsr77i")
    data = lnk.read()
    nasa = json.loads(data) #creates a dictionary
    pic = nasa["url"]
    return render_template("home.html", pic = pic)

if __name__ == "__main__":
    app.debug = True
    app.run()
