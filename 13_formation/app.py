#Michelle Tang
#SoftDev1 pd6
#K13: Echo Echo Echo . . .
#2018-09-27

from flask import Flask, render_template, request, session, url_for, redirect

app = Flask (__name__) #create instance of class FLask

session["username"]= "ultimate"
session["password"]= "frisbee"


@app.route("/auth", methods=['POST'])
def auth():
    print url_for('disp_loginpage')
    print url_for("auth")
    return redirect(url_for("disp_login")

@app.route("/intro")
def intro():
    return("Hi. My name is Michelle. wooo. <a href=\"/\"> Hi </a>" )

@app.route("/auth" ,methods=["GET"])
def authenticate():
    user = request.form['username']
   
    print(request)
    print(request.args['username'])
    print(request.args['password'])
    if ((request.args['username'] == session["username"]) and (request.args['password'] == session["password"])):
        return render_template('user.html',
                           user = request.args['username'],
                           method = request.method)
    else:
        return render_template('occupations.html')
    

if __name__ == "__main__": #will only run if it recognizes this a main (not outside source)   
    app.debug = True
    app.run()

@app.route('/')    
def index():
   if ('username' in session):
    return redirect(url_for('authenticate'))
    else: redirect(url_for('login'))
       username = session['username']
       return 'Logged in as ' + username + '<br>' + \

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
  
