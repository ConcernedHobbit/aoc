from statistics import mode

bits_list = []
bytes = []

for line in open('day3.txt'):
    line = line.strip()
    bytes.append(line)

    if not bits_list:
        bits_list = [0 for i in range(len(line))]

    for n, bit in enumerate(line):
        if bit == '1':
            bits_list[n] += 1
        else:
            bits_list[n] -= 1

most_common = []
least_common = []

for balance in bits_list:
    most_common.append(['0', '1'][balance >= 0])
    least_common.append(['1', '0'][balance >= 0])

gamma = int(''.join(most_common), 2)
epsilon = int(''.join(least_common), 2)
print(f'Part 1: {gamma * epsilon}')

generator = bytes[:]
scrubber = bytes[:]
for i in range(len(most_common)):
    if len(generator) < 2 and len(scrubber) < 2:
        break

    if len(generator) > 1:
        bits_list = [0 for i in range(len(generator[0]))]
        for byte in generator:
            for n, bit in enumerate(byte):
                if bit == '1':
                    bits_list[n] += 1
                else:
                    bits_list[n] -= 1
        most_common = []
        for balance in bits_list:
            most_common.append(['0', '1'][balance >= 0])
        generator = [x for x in generator if x[i] == most_common[i]]
    
    if len(scrubber) > 1:
        bits_list = [0 for i in range(len(scrubber[0]))]
        for byte in scrubber:
            for n, bit in enumerate(byte):
                if bit == '1':
                    bits_list[n] += 1
                else:
                    bits_list[n] -= 1
        least_common = []
        for balance in bits_list:
            least_common.append(['1', '0'][balance >= 0])
        scrubber = [x for x in scrubber if x[i] == least_common[i]]

    
generator = int(generator[0], 2)
scrubber = int(scrubber[0], 2)
print(f'Part 2: {generator * scrubber}')

