# scan = open('day14test.txt').read().split('\n')
scan = open('day14.txt').read().split('\n')

# print(scan)

def parse_scan(row):
    out = []
    row = row.split(" -> ")
    for coord in row:
        coord = coord.split(",")
        coord = list(map(int, coord))
        out.append(coord)

    # print(out)
    return out

parsed_scan = []
for row in scan:
    row = parse_scan(row)
    parsed_scan.append(row)

# print(parsed_scan)

min_x = float("inf")
max_x = 0
max_y = 0

for row in parsed_scan:
    for coord in row:
        max_y = max(max_y, coord[1])
        min_x = min(min_x, coord[0])
        max_x = max(max_x, coord[0])


# print(max_y)
# print(min_x)
# print(max_x)

# # row = [0] * (max_x - min_x + 2)
# # print(row)
# # grid = [row] * (max_y +1)
# # for row in grid:
# #     print(row)

# grid = []

# for i in range(max_y + 1):
#     row = []
#     for j in range(max_x - min_x + 2):
#         row.append(0)
#     grid.append(row)

# for row in grid:
#     print(row)


# for rocks in parsed_scan:
#     for i in range(len(rocks) - 1):
#         x1, y1 = rocks[i]
#         x2, y2 = rocks[i + 1]

#         if x1 == x2:
#             start = min(y1, y2)
#             end = max(y1, y2)
#             print(start, end)
#             for y in range(start, end + 1):
#                 print(y, ",", x1)
#                 grid[y][x1 - min_x] = 1
#         else:
#             start = min(x1, x2) - min_x + 1
#             end = max(x1, x2) - min_x + 1
#             for x in range(start, end + 1):
#                 print(y1, ",", x)
#                 grid[y1][x] = 1

#     # for row in grid:
#     #     print(row)

# for row in grid:
#     print(row)


# set up rocks
class RocksScan:
    def __init__(self, rocks, height, width, x_adj):
        "create empty grid fill with rocks"
        self.rocks = rocks
        self.x_adjustment = x_adj
        self.grid = self.make_grid(height, width)

    def __repr__(self) -> str:
        board = ""
        for row in self.grid:
            for x in row:
                if x == 0:
                    board += "."
                elif x == 1:
                    board += "#"
                elif x == 2:
                    board += "o"
            board += '\n'
        return(f"{board}")

    def make_grid(self, height, width):
        grid = []

        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            grid.append(row)

        return grid

    def place_rocks(self, rocks):
        for rock in rocks:

            for i in range(len(rock) - 1):
                x1, y1 = rock[i]
                x2, y2 = rock[i + 1]

                if x1 == x2:
                    start = min(y1, y2)
                    end = max(y1, y2)
                    for y in range(start, end + 1):
                        self.grid[y][x1 - self.x_adjustment] = 1
                else:
                    start = min(x1, x2) - self.x_adjustment
                    end = max(x1, x2) - self.x_adjustment
                    for x in range(start, end + 1):
                        self.grid[y1][x] = 1
                        # print(self.grid)

    def add_sand(self, x, y):
        """take a piece of sand and drop it straight down until it hits something
        if possible moves diagnol to left and then continues down if pos
        if can't move straight down or down and to left, then moves down to right
        until none of those moves are pos updates grid with new sand position
        probably dfs"""

        x = x - self.x_adjustment
        # print(len(self.grid))
        while y in range(len(self.grid) - 1) and x in range(1, len(self.grid[0]) - 1):
            if self.grid[y + 1][x] == 0:
                y += 1
            elif self.grid[y + 1][x - 1] == 0:
                y += 1
                x -= 1
            elif self.grid[y + 1][x + 1] == 0:
                y += 1
                x += 1
            else:
                break
        # print(f"{y}, {x}")
        self.grid[y][x] = 2
        return [x, y]

width = max_x - min_x + 3

rock_map = RocksScan(parsed_scan, max_y + 1, width, min_x - 1)

print(rock_map)

rock_map.place_rocks(rock_map.rocks)
print(" ")

print(rock_map)

sand = 0

while rock_map.grid[-1][0] == 0 and rock_map.grid[-1][-1] == 0:
    x, y = rock_map.add_sand(500, 0)
    if x == 0 or x == width or y == (max_y):
        break
    sand += 1

print(" ")
print("pieces of sand =", sand)
print(" ")
print(rock_map)
# part 1 = 610

# part 2

# 2_sand = 0

width2 = max_x + 4

rock_map2 = RocksScan(parsed_scan, max_y + 1, width2 * 2, min_x - (width2))


rock_map2.grid.append([0] * (width2 * 2))
rock_map2.grid.append([1] * (width2 * 2))
rock_map2.place_rocks(rock_map2.rocks)

print(rock_map2)


target = 500
sand2 = 0


while rock_map2.grid[0][target-min_x-11] == 0:
    x, y = rock_map2.add_sand(target, 0)
    # if x == 0:
    #     for i in range(len(rock_map2.grid) - 1):
    #         rock_map2.grid[i].insert(0, 0)
    #     rock_map2.grid[-1].insert(0, 1)
    #     target += 1
    #     print(rock_map2)
    # elif x == len(rock_map2.grid[0]) - 1:
    #     for i in range(len(rock_map2.grid) - 1):
    #         rock_map2.grid[i].append(0)
    #     rock_map2.grid[-1].append(1)
    #     print(rock_map2)
    sand2 += 1
    # print(f"{x}, {y} sand = {sand2}")
    # if sand2 % 20 == 0:
    #     print(rock_map2)

    if y == 0:
        break
    # if sand2 == 200:
    #     break

print("")
print(rock_map2)
print("part2 pieces of sand =", sand2)


