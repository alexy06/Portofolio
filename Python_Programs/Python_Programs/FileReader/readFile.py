#!/usr/bin/python

finalString = ""
path = input("$Path: ")

try:
	file = open(path , 'r')
	line = file.readline().strip()
	finalString += line

	while line:
		line = file.readline().strip()
		finalString += " " + line

	file.close()

	print(finalString)

except:
	print("Can't find the file, check if the path is correct and include its extension")	

