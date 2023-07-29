#Given a list  L1=[34,78,-12,44,78,91,60,-34,88]
#1. Return the cube of all list elements greater than 50.
l1 = [34,78,-12,44,78,91,60,-34,88]
def cube():
    cubeList = []
    for i in l1:
        if i > 50:
            cubeList.append(i ** 3)
    return cubeList

list = cube()
print(list)
#2. Remove all negative elements from the list.
def removeNeg():
    removeList = []
    for i in l1:
        if i < 0:
            l1.remove(i)

removeNeg()
print(l1)
#3. Remove the element  at index 4 from the list
def removeInd(ind):
    l1.pop(ind)

removeInd(4)
print(l1)
#4. Pop the last element from the list.
def popLast():
    l1.pop()
    
popLast()
print(l1)

