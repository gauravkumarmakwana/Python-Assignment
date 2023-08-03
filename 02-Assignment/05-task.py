#Find the natural log and log base 10 of the 5 and 75 using relevant functions from the maths module.
import math

n = input("Enter The number: ")
n = (int)(n)
ans = math.log(n)
print("Natural Log of " , end = '')
print(n, end = '')
print("=", end = '')
print(ans)

ans = math.log(n, 10)
print("log base 10 of " , end = '')
print(n, end = '')
print("=", end = '')
print(ans)
