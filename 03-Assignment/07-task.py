#Assignment : 03 Task : 07
#list of all distinct destinations
import pandas as pd

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

carrier = myVar["Journey Finish Point"]
ans = set(carrier)
print(list(ans))



    

