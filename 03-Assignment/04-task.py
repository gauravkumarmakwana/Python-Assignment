#Assignment : 03 Task : 04
#Carrier whom we paid the most?
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

ans = 0
for ind in myVar.index:
    if myVar["Ticket Price ex VAT"][ind] > ans:
        customerInd = ind
        ans = myVar["Ticket Price ex VAT"][ind]
print(customerInd)
