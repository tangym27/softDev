#Michelle Tang
#SoftDev1 pd6
#K08: Fill Yer Flask
#2018-09-19

from flask import Flask, render_template, request

app = Flask (__name__) #create instance of class FLask

@app.route("/") #assign fxn to route
def hello_world():
    #print("about to print __naame__ ...") # print out whenever you refresh
    #print(__name__) #where will this go? #this will print out main
    print(app)
    return render_template('home.html')

@app.route("/intro")
def intro():
    return("Hi. My name is Michelle. wooo. ")

@app.route("/auth")
def autheicate():
    print(app)
    print(request)
    print(request.args)
    return render_template('home.html',
                           title = "hi",)


if __name__ == "__main__": #will only run if it recognizes this a main (not outside source)   
    app.debug = True
    app.run()

#print request.args['username']
