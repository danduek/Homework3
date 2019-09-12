import os
import csv

pybank_csv = os.path.join("budget_data_1.csv")

with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # con csvreader podemos hacer cosas
    encabezado = next(csvreader)
    totalMeses=0
    total=0
    for row in csvreader:
        totalMeses += 1
        total += int(row[1])
    print(f'''
        \n El total de meses es : {totalMeses}
        \n El total : {total}
    ''')

#file_output = "raw_data/results.txt"

#total_months = 

