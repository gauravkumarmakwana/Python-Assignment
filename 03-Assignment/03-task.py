#Assignment : 03 Task : 03
#Longest single journey in miles?
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

ans = 0
for ind in myVar.index:
    if myVar["Ticket Single or Return"][ind] == "Single":
        ans = max(ans, myVar["Miles Travelled"][ind])
print(ans)