#I've Had Ahnaf, I'm Tangry: Michelle Tang, Ahnaf Kazi
#SoftDev1 pd6
#K#14 -- Do I Know You?    
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect
import os
app = Flask (__name__) #create instance of class FLask
app.secret_key = os.urandom(32) 

USER = "ultimate"
PASS = "frisbee"

#root route!
@app.route("/", methods = ["POST", "GET"])
def intro():
    # if user has already been logged in, automatically go to user page
    if("username" in session and session.get('username') == USER):
      print("still here")
      return render_template("user.html", username = USER)
    # else bring person to login page
    return render_template("home.html")

    
#login page    
@app.route("/login", methods=["POST", "GET"])
def login():
  #checks if username and password are correct 
  if request.form['username'] == USER and request.form['password'] == PASS:
    # if it is, establish session & go to user page
    session['username'] = request.form['username'] 
    print("YOU SHOULD ONLY SEE THIS IS USER AND PASS IS CORRECT")
    return render_template("user.html", username = USER)
  # if it is not, return appropriate error
  elif request.form['username'] != USER:
    return render_template('error.html',error = "username")
  else:
    return render_template('error.html',error = "password")

# logout page
@app.route("/logout", methods=["POST"])
def logout():
    #if button is pressed to logout...
    if(request.form["logout"] == "logout"):
        #remove session and go back to login page
        session.pop("username", None) 
        return render_template("home.html")


if __name__ == "__main__": #will only run if it recognizes this a main (not outside source)   
  app.debug = True
  app.run()
