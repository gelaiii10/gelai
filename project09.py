print("numbers from 0 to 100 except ending in 0 or 5:")

for i in range(101):
    if i % 10 != 0 and i % 10 != 5:
        print(i)