#Assignment : 03 Task : 01
# Longest Distance Journey in miles?
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')
miles = myVar["Miles Travelled"]


ans = 0
for i in miles:
    if i > ans:
        ans = i
print(ans)
