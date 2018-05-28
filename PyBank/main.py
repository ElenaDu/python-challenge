import csv
import os
sum_revenue=0
sum_month=0
file_name=input("Please, input the file name including extension: ")
#file_name="budget_data_2.csv"
#file_name="budget_data_1.csv"
revenue=[]
month=[]
change_revenue=[]


with open(file_name, "r", newline='') as csv_file:
     csvreader=csv.reader(csv_file, delimiter=',')
     next(csvreader, None)
     
     for row in csvreader:
#Create two lists - with revenue and month data
         revenue.append(int(row[1]))
         month.append(row[0])
         
# Find the total number of months included in the dataset
total_months=len(month)

#Find the total amount of revenue gained over the entire period
total_revenue=sum(revenue)

#Create new list with change in revenue between months
for i in range(1,total_months):
    change_revenue.append(revenue[i]-revenue[i-1])
    
#Find the average change in revenue between months over the entire period
avg_revenue_change=sum(change_revenue)/len(change_revenue)

#Find the greatest increase in revenue (date and amount) over the entire period
max_revenue_change=max(change_revenue)
#Check there was an increase
if max_revenue_change > 0:
    maxpos=change_revenue.index(max_revenue_change)
    month_max_revenue_change=month[maxpos+1]
else:
    max_revenue_change = 0
    month_max_revenue_change = 'N/A'

#Find the greatest decrease in revenue (date and amount) over the entire period
min_revenue_change=min(change_revenue)
#Check there was a decrease
if min_revenue_change < 0:
    minpos=change_revenue.index(min_revenue_change)
    month_min_revenue_change=month[minpos+1]
else:
    min_revenue_change = 0
    month_min_revenue_change = 'N/A'

#Print all the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: {total_revenue}")
print(f"Average Revenue Change: {avg_revenue_change}") 
print(f"Greatest Increase in Revenue: {month_max_revenue_change} (${max_revenue_change})")
print(f"Greatest Decrease in Revenue: {month_min_revenue_change} (${min_revenue_change})")

#Export a text file ("results.txt") with the results.
with open("results.txt","w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total Revenue: {total_revenue}\n")
    datafile.write(f"Average Revenue Change: {avg_revenue_change}\n")
    datafile.write(f"Greatest Increase in Revenue: {month_max_revenue_change} (${max_revenue_change})\n")
    datafile.write(f"Greatest Decrease in Revenue: {month_min_revenue_change} (${min_revenue_change})\n")

print("Result is stored in results.txt")
