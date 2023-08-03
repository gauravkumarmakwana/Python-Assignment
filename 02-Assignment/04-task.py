#Check the maths library version you are using and use the gcd function to find the gcd for given numbers 200,444,66, 28,48. Also find the lcm of given numbers using the relevant function.

import math
#l1 = [200, 444, 66, 28, 48]
l1 = [100, 50]
result = l1[0]

for i in l1:
    result = math.gcd(result, i)

print(result)
