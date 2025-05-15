num = 1

while num <= 1000:
    temp = num
    sum_of_cubes = 0

    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10

    if sum_of_cubes == num:
        print(num)

    num += 1
