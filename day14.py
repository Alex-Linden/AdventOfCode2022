scan = open('day14test.txt').read().split('\n')
# scan = open('day14.txt').read().split('\n')

print(scan)

def parse_scan(row):
    out = []
    row = row.split(" -> ")
    for coord in row:
        coord = coord.split(",")
        coord = list(map(int, coord))
        out.append(coord)

    print(out)
    return out

parsed_scan = []
for row in scan:
    row = parse_scan(row)
    parsed_scan.append(row)

print(parsed_scan)

min_x = float("inf")
max_x = 0
max_y = 0

for row in parsed_scan:
    for coord in row:
        max_y = max(max_y, coord[1])
        min_x = min(min_x, coord[0])
        max_x = max(max_x, coord[0])


print(max_y)
print(min_x)
print(max_x)

row = [0] * (max_x - min_x + 2)
print(row)
grid = [row] * max_y
for row in grid:
    print(row)

# set up rocks
class RocksScan:
    def __init__(self):
        "create empty grid fill with rocks"