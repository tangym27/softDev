# Michelle Tang
# SoftDev1 pd6
# K26 -- Getting More REST
# 2018-11-15


from flask import Flask, render_template

import urllib.request
import json

app = Flask(__name__)


@app.route("/")
def home():

    #FDA FACTS!
    url ="https://api.fda.gov/food/enforcement.json?"
    search= "search=city:%22Newark%22&limit=1"
    total = url + search
    lnk = urllib.request.urlopen(total)
    data = lnk.read()
    fda = json.loads(data)
    # print("---------------\n")
    # print(fda)

    #CAT FACTS!
    url = "https://catfact.ninja/fact"
    lnk = urllib.request.urlopen(url)
    data = lnk.read()
    cat = json.loads(data)
    # print("---------------\n")
    # print(cat)


    # Dog FACTS!
    lnk = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    data = lnk.read()
    dog = json.loads(data)
    # print("---------------\n")
    # print(dog)

    return render_template("home.html",
                           country = fda['results'][0]['country'],
                           reason = fda['results'][0]['reason_for_recall'],
                           num = fda['results'][0]['recall_number'],
                           status = fda['results'][0]['status'],
                           cat = cat['fact'],
                           dog = dog['status'],
                           pic = dog['message']
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
