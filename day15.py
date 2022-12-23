data = open('day15test.txt').read().split('\n')
# data = open('day15.txt').read().split('\n')

print(data)


for i in range(len(data)):
    data[i] = data[i].replace("Sensor at ", "")
    data[i] = data[i].replace(": closest beacon is at", ",")
    data[i] = data[i].replace("x=", "")
    data[i] = data[i].replace("y=", "")
    data[i] = data[i].split(", ")
    data[i] = list(map(int, data[i]))

print(data)

x_min = float("inf")
x_max = 0
y_min = float("inf")
y_max = 0

for row in data:
    x_min = min(x_min, row[0], row[2])
    x_max = max(x_max, row[0], row[2])
    y_min = min(y_min, row[1], row[3])
    y_max = max(y_max, row[1], row[3])

print("x min / max", x_min, x_max)
print("y min / max", y_min, y_max)

width = abs(x_min) + abs(x_max)
height = abs(y_min) + abs(y_max)

row = [0,1,1,0]
print(len(row) - sum(row))

class BeaconZone:
    def __init__(self, scan, width, height, x_adj, y_adj):
        self.grid = self.make_grid(width, height)
        self.scan = scan
        self.x_adj = x_adj
        self.y_adj = y_adj

    def __repr__(self):
        return f"{self.grid}"

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
            self.grid[sb[1]][sb[0]] = 1
            self.grid[sb[3]][sb[2]] = 2

    def find_unavailable_spaces(self):





# row10 = "..####B######################.."
# print(len(row10))
# unav = 0
# for spc in row10:
#     if spc != ".":
#         unav += 1
# print(unav)