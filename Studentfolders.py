import csv
import os


fname = input('Enter file name: ')  #Roster from Summer Welcome. Must be CSV
basepath = "P:/UGStudentFiles/"  #Where folders will go
count = 0
try:
    with open(fname) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=",")
        for row in readcsv:
            if row[0] == "Student Number" or row[0] == "Summer Welcome Report"  : continue
            #print(row[2]+",",row[1]+"-",row[0])
            foldername = row[2]+", "+row[1]+"- "+row[0]
            newpath = basepath + foldername
            #print(newpath)
            os.makedirs(newpath, exist_ok=True)
            count = count + 1
except IOError:
    print("Invalid File Name")
print("Created ", count, "folders")
