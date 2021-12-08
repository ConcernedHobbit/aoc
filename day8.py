from itertools import permutations

p1 = 0
for line in open('day8.txt'):
    a = line.strip().split(' | ')
    b = a[1].split(' ')
  
    for n in b:
        # unique lengths: 1 2, 7 3, 4 4, 8 7
        if 2 <= len(n) <= 4 or len(n) == 7:
            p1 += 1
print(f'Part 1: {p1}')

lookup = {'abcdefg': 8, 'bcdef': 5, 'acdfg': 2, 'abcdf': 3, 'abd': 7, 'abcdef': 9, 'bcdefg': 6, 'abef': 4, 'abcdeg': 0, 'ab': 1}

p2 = 0
for line in open('day8.txt'):
    a = line.strip().split(' | ')

    b = a[0].split(' ') # wire data
    c = a[1].split(' ') # segment output

    # go through all permutations of abcdefg (5040)
    for p in permutations('abcdefg'):
        # dirty lookup
        d = {}
        for f, g in zip(p, 'abcdefg'):
            d[f] = g

        # unwrap
        an = [''.join(d[c] for c in k) for k in b]
        bn = [''.join(d[c] for c in k) for k in c]
        #print(an, bn)

        if all(''.join(sorted(e)) in lookup for e in an):
            # we have a winning combo!!
            # quick unwrap
            bn = [''.join(sorted(x)) for x in bn]
            # add to total
            p2 += int(''.join(str(lookup[x]) for x in bn))
            break
print(f'Part 2: {p2}')