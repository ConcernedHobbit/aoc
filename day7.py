pos = [int(n) for n in open('day7.txt').readline().strip().split(',')]
part1 = []
part2 = []
for i in range(max(pos)):
    diffs = list(map(lambda x: abs(i - x), pos))
    part1.append(sum(diffs))
    part2.append(sum(sum(range(x + 1)) for x in diffs))

print(f'Part 1: {min(part1)}')
print(f'Part 2: {min(part2)}')
