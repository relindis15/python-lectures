# Exercise 1
"""
In a company the monthly salary of an employee is calculated by: the minimum wage 400$ per
 month, plus 20$ multiplied by the number of years employed, plus 30$ for each child they have.
Create a program that:
● Reads the number of years employed
● Reads the number of children the employee has
● Prints the total amount of salary the employee makes
Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"
"""
# solution


def employee_salary():
    # declaring default variables from the exercise
    minimum_wage = 400
    number_of_years = 20
    amount_per_child = 30
    # getting required inputs from the user
    number_of_years_worked = float(input("Enter number of years employed: "))
    number_of_children = int(
        input("Enter the number of children by employee:"))
    # calculate total salary
    total_salary = minimum_wage + \
        (number_of_years_worked*number_of_years) + \
        (number_of_children*amount_per_child)
    # return total_salary
    print("your total salary is = : $", total_salary)


employee_salary()
# print the total salary
#print("your total salary is = ", employee_salary(), "$")
