#Michelle Tang
#SoftDev1 pd6
#K08: Fill Yer Flask
#2018-09-19

from flask import Flask

app = Flask (__name__) #create instance of class FLask

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __naame__ ...") # print out whenever you refresh
    print(__name__) #where will this go? #this will print out main
    return("no hablo queso! check out my other routes (/intro, /puns, /animal)")

@app.route("/intro")
def intro():
    return("Hi. My name is Michelle. wooo. ")

@app.route("/puns")
def puns(): #testing out lists
    line= "here are some great fantastic puns"
    zero = "<ol start=0> <li> What has four wheels and flies? A garbage truck. </li> "
    one = " <li> This is my step ladder. I never knew my real ladder. </li>"
    two = " <li> What's E.T. short for? Because he's got little legs. </li>"
    three= "<li> Why couldn't the pony sing? Because it was a little hoarse. </li>"
    four = " <li> Why does Norway put bar codes on all of its ships? So they can Scandinavian. </li>"
    five = "<li> Have you ever tried eating a clock? It's really time consuming. </li> </ol> "
    return line + zero + one + two + three + four + five

@app.route("/animal")
def animal(): #testing out images
    return("This is a picture of a cute kitten! <br> <br><img height =\"600\" width = \"800\" src=\"http://tabify.io/wp-content/uploads/2016/08/image27-1170x757.jpg\"> ")

if __name__ == " __main__": #will only run if it recognizes this a main (not outside source)   
    app.debug = True
    app.run()
