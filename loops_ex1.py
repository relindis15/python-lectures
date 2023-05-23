# Write a program that takes a list of numbers and returns the sum of all the even numbers #in the list.
# method1
# initiate the sum variable
sum = 0

# loop through the list of 10 numbers , add all even numbers and assign their sum to the sum variable
for i in range(1, 11):
    if i % 2 == 0:
        sum += i
print('The sum of all even number is:', sum)


# method2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# assigning sum to zero
sum = 0
for num in numbers:
    if (num % 2 == 0):
        # sum each even number to sum
        sum += num
print(sum)

# Write a program in python that takes a list of numbers and returns the maximum number in #the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# assigning maximum number in list
sum = 10
for num in numbers:
    if (num % 2 > 10):
        # sum each even number to sum
        max >= num
print(max)
