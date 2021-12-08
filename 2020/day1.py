def part1(nums: list) -> int:
    for i in nums:
        for j in nums:
            if i + j == 2020:
                return i * j

def part2(nums: list) -> int:
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == '__main__':
    nums = [
        int(n) 
        for n in open('day1.txt').readlines()
    ]
    print(f'Part 1: {part1(nums)}')
    print(f'Part 2: {part2(nums)}')
