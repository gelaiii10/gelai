num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lower = min(num1, num2)
upper = max(num1, num2)

print(f"numbers between {lower} and {upper}:")

for i in range(int(lower) + 1, int(upper)):
    print(i)