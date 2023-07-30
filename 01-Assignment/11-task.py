#You have graduated from MSU and now have a great job! You move to the Bangalore and decide that you want to start saving to buy house. As housing prices are very high in the Bangalore,you realise you are going to have to save for several years before you can afford to make the down payment on a house. In Part A, we are going to determine how long it will take you to save enough money to make the down payment  given the following assumptions:
#a. Call the cost of your dream home total_cost.
#b. Call the portion of the cost needed for a down payment portion_down_payment For simplicity, assume that portion_down_payment = 0.25 (25%). 
#c. Call the amount that you have saved thus far current_savings. You start with a current savings of $0.
#d. Assume that you invest your current savings wisely, with an annual return of r (in other words, at the end of each month, you receive an additional current_savings*r/12 funds to put into your savings – the 12 is because r is an annual rate).
#e. Assume that your investment earn a  return of r = 0.04 (4%).
#f. Assume your annual salary is annual_salary.
#g. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1 for 10%). 
#h. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary/12). Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. Your program should ask the user to enter the following variables:
#    i. The starting annual salary (annual_salary)
#   ii. The portion of salary to be saved (portion_saved) 
#   iii.  The cost of your dream home (total_cost)
print("Annual Salary :" , end = ': ')
annual_salary = input()
annual_salary = float(annual_salary)

print("Total Cost of House :" , end = ': ')
total_cost = input()
total_cost = float(total_cost)

print("Portion Saved :" , end = ': ')
portion_saved = input()
portion_saved = float(portion_saved)

portion_down_payment = total_cost*0.25
current_savings = 0
month = 0
r = 0.04
monthly_salary = annual_salary/12
while current_savings <= portion_down_payment :
    month += 1
    current_savings += monthly_salary*portion_saved
    current_savings += current_savings*r/12

print(month)
