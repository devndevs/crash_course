odd_numbers = range(1, 21, 2)

for odd in odd_numbers:
    print(odd)
print()
by_three = range(3, 31, 3)

for three in by_three:
    print(three)
print()
squares = []
for value in range(1, 11):
    squares.append(value ** 3)
print(squares)
print()

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)