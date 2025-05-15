n = int(input("n="))

while n >=10:
    sum_of_digits = 0
    while n > 0:
        digit = n % 10
        sum_of_digits = sum_of_digits + digit
        n = n // 10
    n = sum_of_digits
print(f" single digit sum is {n}")