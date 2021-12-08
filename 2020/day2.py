def extract(line: str) -> tuple:
    length, character, password = line.split()
    low, high = tuple(map(int, length.split('-')))
    character = character[0]
    return (low, high, character, password)

def part1(lines: list) -> int:
    valid = 0
    for line in lines:
        low, high, character, password = extract(line)
        if low <= password.count(character) <= high:
            valid += 1
    return valid

def part2(lines: list) -> int:
    valid = 0
    for line in lines:
        low, high, character, password = extract(line)

        first = password[low - 1] == character
        second = password[high - 1] == character

        if first ^ second:
            valid += 1

    return valid

if __name__ == '__main__':
    lines = [
        line.strip()
        for line in open('day2.txt').readlines()
    ]
    
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')