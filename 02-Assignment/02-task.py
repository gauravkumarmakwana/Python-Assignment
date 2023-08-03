#Remove all the occurrences of a specific item from the list.
l1 = ["Gaurav", "Makwana", "BE-IV", "TNP", "Gaurav"]
iteam = input("That you want to delete: ")
count = 0
for i in l1:
    if i == iteam:
        count = count + 1

print(iteam, end = "");
print("--> ", end = "")
print(count)

flag = input("You want to delete or Not ? (Y/N)")
if flag == 'Y':
    while iteam in l1:
        l1.remove(iteam)
else:
    print("Thank You")

print("------- Your Updated List is ---------")
print(l1)
