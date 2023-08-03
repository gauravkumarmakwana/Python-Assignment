#Write a recursive python function that takes a parameter list and  returns the maximum number stored in the list.
l1 = [1, 2, 32, 12, 32, 14, 6, 7]
min = l1[-1]
n = len(l1)
def fun(l1, n, min):
    if n == -1:
        return min
    if l1[n] < min:
        min = l1[n]
    return fun(l1, n-1, min)
    
print(fun(l1, n-1, min))
