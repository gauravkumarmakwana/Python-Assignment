#Given a string, remove all vowels from the string.
string = input("Enter String : ")
ans = ""
for i in string :
    if i == 'a' or  i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or  i == 'E' or i == 'I' or i == 'O' or i == 'U' :
        continue
    else:
        ans += i

print(ans)
