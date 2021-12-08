from PIL import Image
from dataclasses import dataclass

@dataclass
class Vent:
    x: int
    y: int
    part1: int = 0
    part2: int = 0

vents = {}
width = 0
height = 0

for line in open('day5.txt'):
    coords = line.strip().split(' -> ')
    start, stop = [tuple(map(int, i)) for i in (coord.split(',') for coord in coords)]

    width = max(width, start[0] + 1, stop[0] + 1)
    height = max(height, start[1] + 1, stop[1] + 1)

    if start[0] == stop[0]:
        x = start[0]
        for y in range(min(start[1], stop[1]), max(start[1], stop[1]) + 1):
            if not (x, y) in vents:
                vents[(x, y)] = Vent(x, y)
            vent = vents[(x, y)]
            vent.part1 += 1
            vent.part2 += 1
    elif start[1] == stop[1]:
            y = start[1]
            for x in range(min(start[0], stop[0]), max(start[0], stop[0]) + 1):
                if not (x, y) in vents:
                    vents[(x, y)] = Vent(x, y)
                vent = vents[(x, y)]
                vent.part1 += 1
                vent.part2 += 1
    else:
        curr = [start[0], start[1]]
        goal = [stop[0], stop[1]]
        xd = [-1, 1][start[0] - stop[0] < 0]
        xy = [-1, 1][start[1] - stop[1] < 0]
        goal[0] += xd
        goal[1] += xy

        while curr != goal:
            if not (curr[0], curr[1]) in vents:
                vents[(curr[0], curr[1])] = Vent(curr[0], curr[1])
            vents[(curr[0], curr[1])].part2 += 1
            curr[0] = curr[0] + xd
            curr[1] = curr[1] + xy
part1 = 0
part2 = 0

image = Image.new('RGB', (width, height))
pixels = image.load()
colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

for x in range(width):
    for y in range(height):
        vent = vents.get((x, y), Vent(x, y))
        if vent.part1 > 1:
            part1 += 1
        if vent.part2 > 1:
            part2 += 1
        pixels[x, y] = colors[vent.part2]
image.save('day5.png', 'png')

print(width, height)
print(part1)
print(part2)