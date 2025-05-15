n = 1234
reversed = 0
while n > 0:
    digit = n % 10         # Get the last digit because 
    print(digit, end = "")
    reversed = reversed * 10 + digit
    n = n // 10      
print("\n")
total = reversed + 101
print(total) 