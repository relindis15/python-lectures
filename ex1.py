# Create two variables x and y, and initially set them each to a different number. Write a python script that swaps both values.

# Example: x = 10, y = 20
# Output: x = 20, y = 10

# solution without swapping function

# method 1
# initial function
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of x: "))
print("the value of x and y before swapping is :", x, y)
swap = x
x = y
y = swap
print("the value of x is :", x)
print("the value of y is :", y)


# method2
x = int(input("enter the value of x for method 2 :"))
y = int(input("enter the value of y for method 2:"))
print("the values of x and y before swapping is:", x, y)

x = y = y, x
print("the value of x is :", x)
print("the value of y is :", y)

# method 3
# swap


def swap_value(x, y):
    swap = x
    x = y
    y = swap
    return x, y


numbers = swap_value(
    int(input("enter the value of x for method 3 :")),
    int(input("enter the value of y for method 3 :")),
)

print(numbers)

# or you can print line 40 in this manner
print(swap_value(
    int(input("enter the value of x for method 3 :")),
    int(input("enter the value of y for method 3 :")),
))
