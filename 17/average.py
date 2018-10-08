#to be decided-Michelle Tang && Britni Canale
#SoftDev1 pd 6
#K17: Average
#10/7/18

import sqlite3
import csv
import db


#========Initializing Files========

DB_FILE="database.db"
dbs = sqlite3.connect(DB_FILE)
c = dbs.cursor()                           #allows sqlite to be used on database.db


#==================Calling functions for file names used, saving changes=====================

def studentGrades(ID):
    search = "SELECT name, code, mark FROM peeps, courses WHERE peeps.id="+str(ID) + " AND courses.id=peeps.id "
   # print (grades)
    c.execute(search)
    listing = c.fetchall()
    strList= "Name : " + listing[0][0] + "\n"
    for item in listing:
    	strList += "Course: " + item[1] + " Grade: "+ str(item[2]) + "\n"
    return strList

print (studentGrades(1))


def average(grades):
	sum = 0.0
	for grade in grades:
		sum += grade
	return sum / len(grades)

def studentAverages(ID):
	search = "SELECT mark FROM peeps, courses WHERE peeps.id="+str(ID) + " AND courses.id=peeps.id "
	c.execute(search)
	grades= c.fetchall()
	sum = 0.0
	for grade in grades:
		#print(grade[0])
		sum += grade[0]
	average= sum / len(grades)
	return average

print (studentAverages(1))

def display():
	search = "SELECT name , id FROM peeps"
	c.execute(search)
	listing= c.fetchall()
	strList = ""
	for entry in listing:
		strList += ("Name: " + str(entry[0]) + " ID: " + str(entry[1]) + " Average: " + str(studentAverages(entry[1])) + "\n")

	return strList
print (display())

dbs.commit()       #save changes
dbs.close()        #close database
