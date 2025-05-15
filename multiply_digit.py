target_product = int(input("enter the target product : "))
number = 1

while True:
    n = number 
    product = 1
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n // 10

    if product == target_product:
        print(f"the first number whose digit myltiply to {target_product} is {number}")
        break
    number = number + 1