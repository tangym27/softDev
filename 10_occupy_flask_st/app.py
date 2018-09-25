'''
Aaron-gu-tang: Xiaojie(Aaron) Li & Michelle Tang
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-23
'''

# import flask
from flask import Flask, render_template
# import our functions
from util import randoccup

# instantiate instance of Flask class
app = Flask(__name__)

# route 1: homepage
@app.route("/")
def welcome():
    return render_template('home.html')


# route 2: occupations page
@app.route("/occupations")
def occupations():
    return render_template('occupations.html',
                               name = "Occupations Data",
                               occu = randoccup.weight(randoccup.list),
                               occuList = randoccup.keys,
                               dict = randoccup.dict
                               )

if __name__ == "__main__":
    app.debug = True
    app.run()
