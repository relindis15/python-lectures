# create a function and assign a parameter num and check if the number is a prime
# number or not


# method2
def is_prime(num):
    if num < 2:
        return False
    for a in range(2, num):

        if num % a == 0:
            return False
    return True


print(is_prime(5))
