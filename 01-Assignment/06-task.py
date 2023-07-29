#What is the error in this below code ?
n = 10
i = 10
while i > 0 :
    print(i)
    if i % 2 == 0:
        i = i/2
    else:
        i = i+1
#While loop goes to in Infinite loop. Because, i is continuous move from 1 to 2
#So, Change the condition of while loop instead i > 0 to i > 1
