#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db" #it will create this

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#INSERT YOUR POPULATE CODE IN THIS ZONE
# with statement means less errors(automatically closes file)
with open("data/occupations.csv","r") as csvF:
    csvR = csv.DictReader(csvF) # reads the csv file
    # iterate through the csv file
    for line in csvR:
        print( line['Job Class'], line['Percentage'])
#==========================================================



command = "CREATE TABLE discobandit (JobClass TEXT, Percentage REAL);"
command1= "INSERT INTO discobandit VALUES(\"teacher\", 5);" #build SQL stmt, save as string
c.execute(command)
c.execute(command1)#run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


