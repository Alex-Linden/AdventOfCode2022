# data = open('day15test.txt').read().split('\n')
data = open('day15.txt').read().split('\n')

# print(data)


for i in range(len(data)):
    data[i] = data[i].replace("Sensor at ", "")
    data[i] = data[i].replace(": closest beacon is at", ",")
    data[i] = data[i].replace("x=", "")
    data[i] = data[i].replace("y=", "")
    data[i] = data[i].split(", ")
    data[i] = list(map(int, data[i]))

# print(data)

beacons = set()
for b in data:
    beacons.add((b[2], b[3]))

# line = 10
line = 2000000

unav = set()

for sb in data:
    man_dist = abs(sb[0] - sb[2]) + abs(sb[1] - sb[3])
    dist = abs(sb[1] - line)
    # print(f"man_dist ={man_dist}, dist = {dist}")
    min_range = (sb[0] - (man_dist - dist))
    max_range = (sb[0] + (man_dist - dist))
    # print(f"min= {min_range}, max = {max_range}")
    if dist <= man_dist:
        # print("yes")
        for i in range((sb[0] - (man_dist - dist)), (sb[0] + (man_dist - dist) + 1)):
            # print(i)
            if (i, line) not in beacons:
                unav.add((i, line))


print("unav len =",len(unav))

x_min = float("inf")
x_max = 0
y_min = float("inf")
y_max = 0

for row in data:
    x_min = min(x_min, row[0], row[2])
    x_max = max(x_max, row[0], row[2])
    y_min = min(y_min, row[1], row[3])
    y_max = max(y_max, row[1], row[3])

# print("x min / max", x_min, x_max)
# print("y min / max", y_min, y_max)

width = abs(x_min) + abs(x_max)
height = abs(y_min) + abs(y_max)
# print(f"height = {height} and width = {width}")
row = [0,1,1,0]
# print(len(row) - sum(row))


# this works for smaller input
# however once numbers grow it takes too long.
# even just creating the grid took too long
class BeaconZone:
    def __init__(self, scan, width, height, x_adj, y_adj):
        self.grid = self.make_grid(width, height)
        self.scan = scan
        self.x_adj = x_adj
        self.y_adj = y_adj
        self.width = width
        self.height = height

    def __repr__(self):
        board = ""
        for row in self.grid:
            for x in row:
                if x == 0:
                    board += "."
                elif x == 1:
                    board += "S"
                elif x == 2:
                    board += "B"
                elif x == 3:
                    board += "#"
            board += '\n'
        return(f"{board}")

    def make_grid(self, width, height):
        grid = []

        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            grid.append(row)

        return grid

    def place_sensors_and_beacons(self):
        for sb in self.scan:
            # print(sb)
            # print(f"sensor y = {sb[1] + self.y_adj}, x = {sb[0] + self.x_adj}")
            # print(f"beacon y = {sb[3] + self.y_adj}, x = {sb[3] + self.y_adj}")
            self.grid[sb[1] + self.y_adj][sb[0] + self.x_adj] = 1
            self.grid[sb[3] + self.y_adj][sb[2] + self.x_adj] = 2

    def find_unavailable_spaces(self, row):
        for s in self.scan:
            sx, sy = s[0] + self.x_adj, s[1] + self.y_adj
            bx, by = s[2] + self.x_adj, s[3] + self.y_adj
            taxi_dist = abs(sy - by) + abs(sx - bx)

            stack = [[sy, sx]]
            seen = set()
            while stack:
                cur = stack.pop()
                y, x = cur
                if (y, x) not in seen and x in range(self.width) and y in range(self.height):
                    if (abs(sy - y) + abs(sx - x)) <= taxi_dist:
                        stack.append([y, x + 1])
                        stack.append([y, x - 1])
                        stack.append([y - 1, x])
                        stack.append([y + 1, x])
                        if self.grid[y][x] == 0:
                            self.grid[y][x] = 3
                    seen.add((y, x))


# day15 = BeaconZone(data, width + 1, height + 1, abs(x_min), abs(y_min))

# print(day15)

# day15.place_sensors_and_beacons()

# print(day15)

# day15.find_unavailable_spaces()

# print(day15)

# count = 0
# y = 10 + y_min + 1
# # y = 2000000 + y_min + 1
# for space in day15.grid[y]:
#     if space == 3:
#         count += 1

# print(count)

# row10 = "..####B######################.."
# print(len(row10))
# unav = 0
# for spc in row10:
#     if spc != ".":
#         unav += 1
# print(unav)
