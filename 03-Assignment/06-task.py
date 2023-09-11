#Assignment : 03 Task : 06
#list of all distinct carriers
import pandas as pd
import collections

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

carrier = myVar["Air Carrier"]
ans = set(carrier)
print(list(ans))



    

