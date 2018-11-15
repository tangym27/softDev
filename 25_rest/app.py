# Michelle Tang
# SoftDev1 pd6
# K25 -- Getting More Rest
# 2018-11-14

from flask import Flask, render_template
from yelpapi import YelpAPI


import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def welcome():
    lnk = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=Qyrxovb3AXTeMsth93T4hVnmzDcSGQDZnHxsr77i")
    data = lnk.read()
    nasa = json.loads(data) #creates a dictionary
    pic = nasa["url"]
    return render_template("home.html", pic = pic)

@app.route('/api', methods=['GET'])
def api():
    yelp_api = YelpAPI("92b7FDwkewHE9-5Ii9ig1hrlYWRtuzGWzaCTSRialTUvjhx7IpvJvRI2KP2T71WiWxlc8eu4ASfYfdiQbPXAkKQvaQyIypoI9j9DXeqecgrgw78PM2CXiJe_JKrsW3Yx")
    # args="?"
    # search_results = yelp_api.search_query(args)
    #print("10")
    response = yelp_api.phone_search_query(phone='+17189966288')
    #
    # print(response)
    # print("\n\n\n\n\n\n")
    # print (response['businesses'][0]['name'])

    return render_template('api.html', business = response)

if __name__ == "__main__":
    app.debug = True
    app.run()
