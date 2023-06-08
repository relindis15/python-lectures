def get_even_numbers(n):
    even_numbers = []
    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


print(get_even_numbers(10))

numbers = [1, 2, 3, 4, 5]
squared = []  # empty list
for num in numbers:
    # printing the square of each number or the num to power 2
    squared.append(num ** 2)  # append means to store or adds behind
print(squared)
