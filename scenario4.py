# Exercise 2
"""
An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user
pays 5$. Find if someone is a member or not and calculate the price based on how many hours
the user spend. If the user is a member the tax is 10% else the tax is 20%.
Create a program that:
● Reads how many hours the user spend
● Check if is a member
● Add the proper tax fee
● Print the total amount the user has to pay
Output: "The user is a member stayed 2 hours for 2$/hour plus the 10% the total amount
is 4.4$"
"""
# Solution

member_fee_per_hour = 2
non_member_fee_per_hour = 5
membership_tax = 0.1
non_membership_tax = 0.2
hours_spent = int(input("Enter hours spent:"))
check_membership = str(input("Are you a member:"))
if check_membership == "yes":
    total_hours = (hours_spent*member_fee_per_hour)
    tax_fee = total_hours*membership_tax
    membership_status = "the user is a member stayed "
    membership_rate = member_fee_per_hour
    tax = membership_tax
else:
    total_hours = (hours_spent*non_member_fee_per_hour)
    tax_fee = total_hours*membership_tax
    membership_status = "the user is not a member stayed"
    membership_rate = non_member_fee_per_hour
    tax = non_membership_tax
total_amount = total_hours+tax_fee
print(membership_status, hours_spent, "hours for", membership_rate,
      "$/hour", "plus", tax, "the total amount is", total_amount)
