#Given a list L1=[“Test”,”Find”,”Try”,”Search”,”Think”,”Innovate”]
#Output = [‘e’,’k’,’h’,’y’,’d’,’t’] 
#Reverse the list and take only last character of each string in the list

l1 = ['Test','Find','Try','Search','Think','Innovate']
ans = []
l1.reverse()

# print(l1)
for i in l1 :
    ans.append(i[-1])
    
print(ans)
