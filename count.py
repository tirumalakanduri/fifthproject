n = int(input("n="))

target_digit = 3
count = 0
while n > 0:
    last_digit = n % 10
    if last_digit == target_digit:
        break
    count = count + 1 
    n = n // 10

if n == 0:
    print(f"Digit {target_digit} not found.")
else:
    print(f"It took {count} divisions to reach digit {target_digit}.")
