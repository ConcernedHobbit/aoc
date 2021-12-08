lanternfish = []
for line in open('day6.txt'):
    lanternfish = [int(n) for n in line.strip().split(',')]
in_state = [lanternfish.count(i) for i in range(9)]

for day in range(256):
    if day == 80:
        print(f'Part 1: {sum(in_state)}')

    hatching = in_state.pop(0)
    in_state[6] += hatching
    in_state.append(hatching)

print(f'Part 2: {sum(in_state)}')
