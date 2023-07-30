#In Part A, we unrealistically assumed that your salary didn't change. But clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months. Modify your program to include the following 
#   a. Have the user input a semi-annual salary raise semi_annual_raise​ (as a decimal percentage)
#   b. After the 6th month, increase your salary by that percentage. Do the same after the 12th month, the 18 month, and so on.
#Write a program to calculate how many months it will take you save up enough money for a down payment. Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
#   A. The starting annual salary (annual_salary) 
#   B. The percentage of salary to be saved (portion_saved) 
#   C. The cost of your dream home (total_cost)
#   D. The semiannual salary raise (semi_annual_raise)

print("Annual Salary :" , end = ': ')
annual_salary = input()
annual_salary = float(annual_salary)

print("Total Cost of House :" , end = ': ')
total_cost = input()
total_cost = float(total_cost)

print("Portion Saved :" , end = ': ')
portion_saved = input()
portion_saved = float(portion_saved)

print("Semi Annual Raise :" , end = ': ')
semi_annual_raise = input()
semi_annual_raise = float(semi_annual_raise)

portion_down_payment = total_cost*0.25
current_savings = 0
month = 0
r = 0.04
monthly_salary = annual_salary/12
while current_savings <= portion_down_payment :
    month += 1
    current_savings += monthly_salary*portion_saved
    current_savings += current_savings*r/12
    if month % 6 == 0 :
        monthly_salary += monthly_salary*semi_annual_raise

print(month)

