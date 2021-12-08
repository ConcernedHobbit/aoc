lanternfish = []
for line in open('day6.txt'):
    lanternfish = [int(n) for n in line.strip().split(',')]
original = lanternfish[:]

days = 80
for day in range(days):
    new_lanternfish = []
    for fish in lanternfish:
        if fish == 0:
            new_lanternfish.append(6)
            new_lanternfish.append(8)
        else:
            new_lanternfish.append(fish - 1)

    lanternfish = new_lanternfish
print(f'Part 1: {len(lanternfish)}')

in_state = [original.count(i) for i in range(9)]
days = 256
for day in range(days):
    hatching = in_state.pop(0)
    in_state[6] += hatching
    in_state.append(hatching)
print(f'Part 2: {sum(in_state)}')
    