#Michelle Tang
#SoftDev1 pd6
#K08: Fill Yer Flask
#2018-09-19

from flask import Flask, render_template, request

app = Flask (__name__) #create instance of class FLask

@app.route("/") #assign fxn to route
def hello_world():
    return render_template('home.html')

@app.route("/intro")
def intro():
    return("Hi. My name is Michelle. wooo. <a href=\"/\"> Hi </a>" )

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template('user.html',
                           user = request.args['username'],
                           method = request.method)
    

if __name__ == "__main__": #will only run if it recognizes this a main (not outside source)   
    app.debug = True
    app.run()

