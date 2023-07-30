#Create a string from the given list.

l1 = ['G', 'A', 'U', 'R', 'A', 'V']
str = ""
for i in l1:
    str += i

print(str)

#method : 2
str1 = ""

str1 = str1.join(l1)

print(str1)
