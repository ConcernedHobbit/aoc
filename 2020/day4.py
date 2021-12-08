import re

def extract(filename: str) -> list:
    passports = []
    passport = dict()
    for line in open(filename):
        if len(line) == 1:
            passports.append(passport)
            passport = dict()
            continue

        for part in line.split():
            key, value = part.split(':')
            passport[key] = value
    passports.append(passport)
        
    return passports


def is_valid_format(passport: dict) -> bool:
    return set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']).issubset(passport.keys())

def part1(passports: list) -> int:
    return len(list(filter(is_valid_format, passports)))

def is_number_between(str: str, min: int, max: int) -> bool:
    try:
        return min <= int(str) <= max
    except ValueError:
        return False

def is_height(str: str) -> bool:
    unit = str[-2:]
    height = str[:-2]

    if unit == 'cm':
        return is_number_between(height, 150, 193)
    elif unit == 'in':
        return is_number_between(height, 59, 76)
    else:
        return False

def is_hexstr(str: str) -> bool:
    return re.match(r'^#[0-9a-f]{6}$', str)

def is_valid_pid(str: str) -> bool:
    return re.match(r'^\d{9}$', str)

def part2(passports: list) -> int:
    passports = list(filter(is_valid_format, passports))
    return sum([
        1 for passport in passports if 
        all([
                is_number_between(passport['byr'], 1920, 2002),
                is_number_between(passport['iyr'], 2010, 2020),
                is_number_between(passport['eyr'], 2020, 2030),
                is_height(passport['hgt']),
                is_hexstr(passport['hcl']),
                passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                is_valid_pid(passport['pid'])
        ])
    ])

if __name__ == '__main__':
    passports = extract('day4.txt')
    print(f'Part 1: {part1(passports)}')
    print(f'Part 2: {part2(passports)}')