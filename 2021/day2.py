position = 0
depth = 0
aim = 0

for line in open('day2.txt'):
    command, amount = line.strip().split(' ')
    amount = int(amount)

    if command == 'forward':
        position += amount
        depth += amount * aim
    if command == 'down':
        aim += amount
    if command == 'up':
        aim -= amount

print(f'Part 1: {position} x {aim} = {position * aim}')
print(f'Part 2: {position} x {depth} = {position * depth}')
