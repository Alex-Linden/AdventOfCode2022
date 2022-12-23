data = open('day15test.txt').read().split('\n')
# data = open('day15.txt').read().split('\n')

print(data)


for i in range(len(data)):
    data[i] = data[i].replace("Sensor at ", "")
    data[i] = data[i].replace(": closest beacon is at", ",")

print(data)



class BeaconZone:
    def __init__(self, scan) -> None:
        self.grid = self.make_grid()
        self.scan = scan