import os
import csv

#locate the source data file
budgetdata = os.path.join("Resources", 'budget_data.csv')

#Variables to store totals

GtTotal= 0
month_count=0
total_monthly_change=0
lowest_monthly_change=0
highest_monthly_change=0
monthly_change=0.000000000
current_month_total=0.000000000

# Use encoding for Windows
with open(budgetdata, newline='', encoding='utf-8') as csvfile:
    #
    #Loop through every row of data skipping the first line which is the header. save it 
    #
    header= next (csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #Count the months as we go along
        if month_count==0:
         #store the first month's total to enable calculation of average monthly change
          current_month_total=int(row[1])
        else:
            #print (debug : current_month_total)
          monthly_change = int(row[1]) - current_month_total
          total_monthly_change = monthly_change + total_monthly_change
          current_month_total= int(row[1])
          if monthly_change > highest_monthly_change:
              highest_monthly_change = monthly_change 
              highest_month=row[0]
          if monthly_change < lowest_monthly_change:
              lowest_monthly_change = monthly_change 
              lowest_month=row[0]

        month_count=month_count+1
        #Keep a running total from each month
        GtTotal= GtTotal + int(row[1])
        #print (f"Month change {monthly_change}")
   
    AvgMonthlyChange = round(total_monthly_change/(month_count-1),2)
    #output the  results to he screen
    print ("  Financial Analysis")
    print ("---------------------------------------------------------------------")
    print ("")
    print (f"Total Months: {month_count}")    
    print (f"Total: ${GtTotal}")
    print (" ")
    print (f"Average Monthly Change: ${AvgMonthlyChange}")
    print (f"Greatest Monthly Increase in Profits: {highest_month} ${highest_monthly_change}")
    print (f"Greatest Monthly Decrease in Profits: {lowest_month} ${lowest_monthly_change}")
    print ("---------------------------------------------------------------------")  

# Set variable for output file
output_file = os.path.join("analysis","FinancialAnalysisResults.txt")

#  Open the output file and write the same results to a file
newline="\n"
with open(output_file, "w") as datafile:
    # Write the header row
    (datafile)
    datafile.write ("  Financial Analysis"+newline)
    datafile.write ("---------------------------------------------------------------------"+newline)
    datafile.write ("")
    datafile.write (f"Total Months: {month_count}"+newline)    
    datafile.write (f"Total: ${GtTotal}"+newline)
    datafile.write ("")
    datafile.write (f"Average Monthly Change: ${AvgMonthlyChange}"+newline)
    datafile.write (f"Greatest Increase in Profits: {highest_month} ${highest_monthly_change}"+newline)
    datafile.write (f"Greatest Decrease in Profits: {lowest_month} ${lowest_monthly_change}"+newline)
    datafile.write("---------------------------------------------------------------------"+newline)
