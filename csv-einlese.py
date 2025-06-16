import csv

with open('data.csv') as csvfile:
    grint = csv.reader(csvfile, delimiter=',')
    for row in grint:
        print(grint)