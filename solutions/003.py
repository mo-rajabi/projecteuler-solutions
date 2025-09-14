# projecteuler.net - problem 003
factor = 2
number = 600851475143

while (factor ** 2 <= number):
    if number % factor == 0:
        number = number / factor
    else:
        factor = factor + 1

print (int(number))