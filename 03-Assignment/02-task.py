#Assignment : 03 Task : 02
#Longest return journey in miles?
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

ans = 0
for ind in myVar.index:
    if myVar["Ticket Single or Return"][ind] == "Return":
        ans = max(ans, myVar["Miles Travelled"][ind])
print(ans)