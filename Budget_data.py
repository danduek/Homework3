import os
import csv

pybankCSV = os.path.join("budget_data_1.csv")
with open(pybankCSV, "r",encoding="UTF-8", newline="\n") as data:
    csvreader = csv.reader(data, delimiter=",")
    csv_header = next(csvreader)

    months= 0
    total= 0
    changes= []
    average_change= 0.0
    greatest_increase= 0.0
    greatest_increase_date = ''
    greatest_decrease = 0.0
    greatest_decrease_date = ''
    current_value = 0
    

    last_value = 0


    for row in csvreader:
        total_months = int(row[1])
        months += 1
        total += total_months
        change = total_months - last_value
        changes.append(change)


        if (average_change > greatest_increase):
           greatest_increase = average_change
           greatest_increase_date = row[0]
  
        if (average_change > average_change):
           greatest_decrease = average_change
           greatest_increase_date = row[0]

        #if (change < greatest_decrease):
            #greatest_decrease = change
            #greatest_decrease= row[0]
        avgerage_change = round (sum(changes) / len(changes))


    print (f'''
        Financial Analysis
        _______________________________
        \n The total of months is : {months}
        \n The total is : ${total}
        \n The total average change is : ${avgerage_change}
        \n The greatest increase in profits : {str(greatest_increase_date)} ${str(greatest_increase)}
        \n The greatest decrease in profits : {greatest_decrease_date} (${greatest_decrease})
     ''')
#file1 = open("pybank_csv", "W")
#file1.write(report)
#file1.close()

#print(report)


#file_output = "raw_data/results.txt"

#total_months = 
#rev_change = int(row["Revenue"])- prev_revenue
        #prev_revenue = int(row["Revenue"])
        #revenue_change_list = revenue_change_list + [rev_change]
        #month_of_change = month_of_change + [row["Date"]]

    #  ${avgerage_change} ${round( sum(changes) / len(changes), 2)}