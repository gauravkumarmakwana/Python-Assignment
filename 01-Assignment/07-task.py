#Check  and return the palindromes in a string and list both.
#str = "ABCDCBA"
str = ['A', 'B', 'C', 'D', 'C', 'B', 'A']

i = 0
j = len(str)-1

while i > j:
    if str[i] != str[j] :
        print(str, end=" ")
        print("is not Palindrome")
print(str, end=" ")
print("is Palindrome")
