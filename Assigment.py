import os
import csv

pybank_csv = os.path.join("budget_data_1.csv")

with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # con csvreader podemos hacer cosas
    encabezado = next(csvreader)
    total_months=0
    total_revenue=0
    prev_revenue = 0
    months_of_change=[]
    revenue_change_list = []
    biggest_decr= 0.0
    biggest_incr = 0.0
    biggest_decr_date = ''
    biggest_incr_date = ''
    changes = []
    average_change = 0.0

    last_value = 0

    

    for row in csvreader:
        total_months += 1
        total_revenue += total_months

        revenue_change_list = total_months - last_value
        revenue_change_list.apend(revenue_change_list)

        if (change > biggest_incr):
            biggest_incr = change
            biggest_incr_date = row[0]

        if (change < biggest_decr):
            biggest_decr = change
            biggest_decr_date= row[0]
        

    print(f'''
        Financial Analysis
        _______________________________
        \n The total of months is : {total_months}
        \n The total is : {total_revenue}
        \n The total average change is : ${avg_change}
        \n The greatest increase in profits : {biggest_incr_date}(${biggest_incr})
        \n The greatest decrease in profits : {biggest_decr_date} (${biggest_decr})
    ''')

file1 = open("pybank_csv", "W")
file1.write(report)
file1.close()

#file_output = "raw_data/results.txt"

#total_months = 
#rev_change = int(row["Revenue"])- prev_revenue
        #prev_revenue = int(row["Revenue"])
        #revenue_change_list = revenue_change_list + [rev_change]
        #month_of_change = month_of_change + [row["Date"]]

