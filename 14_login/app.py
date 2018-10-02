#Michelle Tang
#SoftDev1 pd6
#K13: Echo Echo Echo . . .
#2018-09-27

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask (__name__) #create instance of class FLask
app.secret_key = os.urandom(32)

USER = "ultimate"
PASS = "frisbee"

@app.route("/", methods = ["POST", "GET"])
def intro():
    if("username" in session and session.get('username') == USER):
      print("still here")
      return render_template("user.html", username = USER)
    return render_template("home.html")

    
    
@app.route("/login", methods=["POST", "GET"])
def login():
  if request.form['username'] == USER and request.form['password'] == PASS:
    session['username'] = request.form['username'] 
    return render_template("user.html", username = USER)
  else:
    return render_template('occupations.html')

@app.route("/logout", methods=["POST"])
def logout():
    if(request.form["logout"] == "logout"):
        session.pop("username", None) #removes username from session, logging out
        return render_template("home.html")#returns to login page

#if __name__ == "__main__": #will only run if it recognizes this a main (not outside source)   
app.debug = True
app.run()
