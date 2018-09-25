'''
Aaron-gu-tang: Xiaojie(Aaron) Li & Michelle Tang
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-23
'''

# import uniform from random to generate random floats
from random import uniform
# to access csv.reader() to read csv files
import csv

csvDict = {} # dictionary with percentages as keys
dict = {} # REAL dictionary with occupation as keys
keys = [] # stores REAL dictionary keys
list = [] # list to store percentages(this is for the weighted random function)
rows = 0 # how many rows of csv files


# with statement means less errors(automatically closes file)
with open("data/occupations.csv","r") as csvF:
    csvR = csv.reader(csvF) # reads the csv file
    # iterate through the csv file
    for line in csvR:
        # add the percentages to the dictionary as a key
        if line[0] != "Job Class" and line[0] != "Total":
            key = line[0]
            rows += 1
            dict.setdefault(key, [])
            dict[key].extend([line[1], line[2]])
            keys.append(key)
            csvDict[float(line[1])] = line[0]
            list.append(float(line[1])) # also add the percentage to the list

# sort list in ascending order
list = sorted(list)

# weighted random function takes in a list(of the percentages used earlier) as input
def weight(list):
    total = 0.0 # this will represent the total percentage(99.8)
    for i in list: # this adds the actual percentages
        total += i
    # generate a random percentage
    rand = uniform(0, total)
    index = 0
    temp = 0.0
    # iterate through the list, add the percentage at index i to a temp float,
    # and if that temp float is >= the randomly generated percentage, return the key
    # value of that percentage(occupation)
    for i in list:
        temp += i
        if temp >= rand:
            return(csvDict[list[index]])
        else: # otherwise increase the index to the next-to-smallest percentage
            index += 1

weight(list)
