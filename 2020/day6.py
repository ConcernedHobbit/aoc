def part1(groups: list) -> int:
    counts = [
        len(set(''.join(group)))
        for group in groups
    ]
    return sum(counts)

# TODO: do i even need to say anything
def part2(groups: list) -> int:
    counts = []
    for group in groups:
        count = 0
        for char in 'abcdefghijklmnopqrstuvwxyz':
            times = 0
            for answer in group:
                if char in answer:
                    times += 1
            if times == len(group):
                count += 1
        counts.append(count)
    return sum(counts)


if __name__ == '__main__':
    groups = []
    group = []
    for line in open('day6.txt'):
        if len(line) == 1:
            groups.append(group)
            group = []
            continue
        group.append(line.strip())
    groups.append(group)

    print(f'Part 1: {part1(groups)}')
    print(f'Part 2: {part2(groups)}')

