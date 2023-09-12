#Assignment : 03 Task : 08
#Mean price of all single route ticket prices?
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')
sum = 0
n = 0
for i in myVar.index:
    if myVar["Ticket Single or Return"][i] == "Single":
        sum += myVar["Total Cost ex VAT"][i]
        n += 1

print(sum/n)

    

