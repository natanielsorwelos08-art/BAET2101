#Sorwelos Nataniel G.
#BAET 2101

while True:
    n = int(input("Size: "))

    if 1 <= n <= 10:
        break

    print("Invalid input! Enter a number from 1 to 10.")

for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(f"{row * col:4}", end="")
        print()
