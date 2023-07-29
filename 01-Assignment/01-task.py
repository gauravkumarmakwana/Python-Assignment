##Ruchita is looking for her dream job, but has some choices and restrictions. She loves Bangalore and would take a job there if paid over 15,00,000 per year. She hates Hyderabad and demands at least 20,00,000 per year. Any other place she is content to work for 17,00,000 a year, unless she can work in space in which case she would work for free.  Write code for the same.
city = input("Enter city\n")
sal = input("Enter Salary\n")
sal = int(sal)

if city.upper() == "HYDRABAD" :
    if sal >= 2000000 :
        print("interested")
    else:
        print("Not interested")
elif city.upper() == "BANGLORE" :
    if sal >= 1500000 :
        print("interested")
    else:
        print("Not interested")
elif sal >= 1700000 :
    print("interested at", city)
else:
    print("I am interested in space")
