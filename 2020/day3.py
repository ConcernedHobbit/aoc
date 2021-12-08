from functools import reduce

def get_trees(lines: list, slope: tuple) -> int:
    trees = 0
    x, y = slope
    while y < len(lines):
        line = lines[y]
        if line[x % len(line)] == '#':
            trees += 1

        x += slope[0]
        y += slope[1]
    return trees

def part1(lines: list) -> int:
    return get_trees(lines, (3, 1))

def part2(lines: list) -> int:
    return reduce(
        lambda x, y: x * y, 
        [
            get_trees(lines, (1, 1)),
            get_trees(lines, (3, 1)),
            get_trees(lines, (5, 1)),
            get_trees(lines, (7, 1)),
            get_trees(lines, (1, 2))
        ]
    )

if __name__ == '__main__':
    lines = [
        line.strip()
        for line in open('day3.txt').readlines()
    ]

    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
