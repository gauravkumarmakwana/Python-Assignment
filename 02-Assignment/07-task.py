#Create a function rever(n) in python that returns the value of the integer argument n with its digits order reversed and sign unchanged (1719 -> 9171).
import math
n = input("Enter n : ")
n = (int)(n)
def rever(n):
    flag = False
    if n < 0:
        flag = True
        n *= -1
    digit = math.floor(math.log(n, 10)) + 1
    ans = 0
    mul = 10 ** digit
    while n != 0:
        rem = n % 10
        mul //= 10
        ans += rem*mul
        n = n//10
    if flag:
        ans *= -1
    print(ans)
    
rever(n)

