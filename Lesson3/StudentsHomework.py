import csv

with open("StudentsCSV.csv", "r") as studentCSV:
    reader = csv.reader(studentCSV)
    rows = list(reader)


for x, y in enumerate(rows):
    if x != 0:
        print(f"{y[0]} is {y[2]} and {y[1]} years old.")
