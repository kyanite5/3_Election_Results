import os
import csv

csvpath = "budget_data.csv"
# Method 2: Improved Reading using CSV module

with open(csvpath, encoding="utf8", newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
   csvhand = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvfile)
   # headers = csv_header.split(',')
   # headers = csv_header.strip()
   # print(headers)

# Declarations for total months, month index, and average profit/loss
   count_months = int()
   count_months = 0
   totalpl = int()
   totalpl = 0
   profit_loss = []
   months = []
   amt = int()

# Find total months and average profit/loss
   for row in csvhand:
      count_months = count_months + 1
      totalpl = int(row[1]) + totalpl
      mon = row[0]
      amt = int(row[1])
      months.append(mon)
      profit_loss.append(amt)

# Declarations for min, max and average change of profit/loss
   minch = int()
   maxch = int()
   avgch = float()

# Determine min, max and average change of profit/loss
   change_list = []
   i = 0
   change_list = [profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]

   minch = min(change_list)
   maxch = max(change_list)
   avgch = sum(change_list)/(len(profit_loss)-1)

   minindex = change_list.index(minch) + 1
   maxindex = change_list.index(maxch) + 1

# Print results
   print("Financial Analysis")
   print("--------------------------")
   print("Total Months: ", count_months)
   print("Total: $", totalpl)
   print("Average Change: $", (round(avgch,2)))
   print("Greatest Increase in Profits:", months[maxindex], "($", maxch,")")
   print("Greatest Decrease in Profits:", months[minindex], "($", minch, ")")

# print to text file
import sys

sys.stdout = open('output_budget.txt','w')
print("Financial Analysis")
print("--------------------------")
print("Total Months: ", count_months)
print("Total: $", totalpl)
print("Average Change: $", (round(avgch,2)))
print("Greatest Increase in Profits:", months[maxindex], "($", maxch,")")
print("Greatest Decrease in Profits:", months[minindex], "($", minch, ")")
