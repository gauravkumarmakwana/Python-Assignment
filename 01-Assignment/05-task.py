#Given a list of numbers, return the list containing only squares of positive numbers from the given list.
l1 = [1, 3, -5, 45, 13, 0, -1, 12]
result =[]
for i in l1 :
    if i > 0 :
        result.append(i*i)
print(l1)
print(result)
