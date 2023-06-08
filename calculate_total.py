from calculate_total_cost import calculate_total
product_cost = float(input("what is the product cost: "))
location = input("Enter your location (US,EUROPE,CANADA, OTHERS): ")
total_cost = calculate_total(location, product_cost)
print("You have to pay $", total_cost)
