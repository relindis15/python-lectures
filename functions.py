# function without parameter
# Example1
def my_name():
    print("Welcome to Compudemy Relindis")


my_name()  # calling a function
print(my_name())  # calling a parameter less function

# Example2


def my_profession():
    print("My name is Relindis i am a Devops Engineer")


my_profession()
print(my_profession())

# function with parameter


def course_func(name, age):
    print("My name is", name, "i am ", age, "years")


course_func("Relindis", 34)

# function with three parameters
# Example3


def my_credentials(name, address, date_of_birth):
    print("Hello", name, "welcome to Compudemy")
    print("I live in", address)
    print("I was born on", date_of_birth)


my_credentials("Relindis", "Elicott city MD", "May 23 1988")

# example4
# propose a function that checks if a number is odd or even


def odd_even(number):
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")


odd_even(20)

# example5
# propose a function that takes two numbers and check the divisibility


def divisibility(a, b):
    if a % b == 0:
        print(a, "is divisible by", b)
    else:
        print(b, "is not divisible by", a)


# call function
divisibility(12, 4)

# function that returns a value


def math_operation(num1, num2):
    add = num1+num2
    sub = num1-num2
    # returning a single value(add)
    return add, sub


# read return value as a single variable
rere, mimi = math_operation(10, 7)
print("the sum of the two numbers is: ", rere)
print(mimi)


def check_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


# call function

print(check_number(15))


def check_divisibility(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


# call function
print(check_divisibility(12, 3))

# Local Variables in Function
# a local variable is a variable that is declared inside a function and is not accessible
# out of that function


def akum():
    a = 12
    print('this is a local variable', a)


def emma():
    b = 10
    print("the value is", b)


# call the function
akum()
emma()

# Global Variables
y1 = 600


def acha():
    print(y1)


acha()


def blaise():
    y2 = y1+20
    print(y2-4)


blaise()

# exercise
# Write a Python function called calculate_factorial that takes a positive integer as #input and calculates its factorial using a loop.

# The factorial of a number n is the product of all positive integers from 1 to n.


def calculate_factorial(n):

    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)


print(calculate_factorial(3))
