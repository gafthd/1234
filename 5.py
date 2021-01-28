import re
import csv
import os

with open('csv/1000 Basic Electrical Engineering MCQs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader: 
        print(r[-2])
        break