def seat_id(str: str) -> int:
    return int(
        str.replace('F', '0')
           .replace('B', '1')
           .replace('L', '0')
           .replace('R', '1'), 
        2
    )

def part1(lines: list) -> int:
    return max(
        seat_id(line)
        for line in lines
    )

def part2(lines: list) -> int:
    seats = sorted(
        seat_id(line)
        for line in lines
    )

    for i in range(1, len(seats) - 1):
        if seats[i] + 1 != seats[i + 1]:
            return seats[i] + 1            

if __name__ == '__main__':
    lines = [
        line.strip()
        for line in open('day5.txt').readlines()
    ]
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
