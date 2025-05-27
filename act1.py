base = int(input("Enter the base number: "))
exponent = int(input("Enter the power to raise the number to: "))
result = 1
for i in range(exponent):
    result *= base
print(f"{base} to the power of {exponent} is {result}")