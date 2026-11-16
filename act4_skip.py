#Sorwelos Nataniel G.
#BAET 2101

total = 0

for number in range(1, 51):
    if number % 3 == 0:
        continue

    print(number, end=" ")
    total += number

    print("\nSum:", total)