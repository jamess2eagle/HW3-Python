import os
import csv
from statistics import mean

#join file path
csvpath = os.path.join("budget_data.csv")

#create empty lists
month = []
profit = []
changeProfit = []

#open and read the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))
    csvheader = next(csvreader)
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
    
NoMonth = len(month)
SumProfit = sum(profit)

#set the initial change in profit to 0
changeProfit.append(0)

#calculate and appen the change in profit
for i in range (1, NoMonth):
    changeProfit.append(profit[i]-profit[i-1])

#calculate max, min and avg of the changes in profit
MaxProfit = max(changeProfit)
MinProfit = min(changeProfit)
#need to subtract 1 from No Month, because first month does not contain change in profit
AvgProfit = "%.2f" %(sum(changeProfit)/(NoMonth-1))

#add two columns together
combined = list(zip(month, changeProfit))

#find the max and min profit
for row in combined:
    if row[1] == MaxProfit:
        MaxMonth = row[0]
    if row[1] == MinProfit:
        MinMonth = row[0]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {NoMonth}")
print(f"Total: ${SumProfit}")
print(f"Average Change: ${AvgProfit}")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxProfit})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MinProfit})")

#write file
with open("output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {NoMonth}\n")
    file.write(f"Total: ${SumProfit}\n")
    file.write(f"Average Change: ${AvgProfit}\n")
    file.write(f"Greatest Increase in Profits: {MaxMonth} (${MaxProfit})\n")
    file.write(f"Greatest Decrease in Profits: {MinMonth} (${MinProfit})\n")