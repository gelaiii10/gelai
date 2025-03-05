numbers = [0] * 10

for i in range(10):
    numbers[i] = int(input(f"Enter number {i + 1}: "))

first_number = numbers[0]

print(f"\nResults of {first_number} minus the remianing numbers:")
for i in range (1, 10):
    result = first_number - numbers[i]
    print(f"{first_number} - {numbers[i]} = {result}")