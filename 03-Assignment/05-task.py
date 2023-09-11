#Assignment : 03 Task : 05
#Carries whom we flew the most number of times?
import pandas as pd
import collections

myVar = pd.read_csv('Met_Office_2011_Air_Data.csv')

list = myVar["Air Carrier"]
#frequency = {}
frequency = collections.Counter(list)

#for i in list:
 #   if i in frequency:
  #      frequency[i] += 1
   # else:
    #    frequency[i] = 1
ansCount = 0
ans = ""
for i in frequency:
    if frequency[i] > ansCount:
        ansCount = frequency[i]
        ans = i

print(ans)
print(ansCount)



    

