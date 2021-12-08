numbers = [int(n) for n in open('day1.txt')]
part_one = 0
part_two = 0

for i in range(len(numbers)):
    if i > 0 and numbers[i] > numbers[i - 1]:
        part_one += 1

    if i > 2 and sum(numbers[i - 3 : i]) > sum(numbers[i - 4 : i - 1]):
        part_two += 1


print(f'Part 1: {part_one}')
print(f'Part 2: {part_two}')
