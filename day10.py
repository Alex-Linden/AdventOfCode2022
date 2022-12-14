cmds = open('day10.txt').read().split('\n')

print(cmds)
x = 1
queue = [0]
for cmd in cmds:
    queue.append(0)
    cmd = cmd.split(" ")
    if cmd[0] == "addx":
        queue.append(int(cmd[1]))

total = 0
image = ''
for i in range(len(queue)):
    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
        print("i =", i, "x =", x)
        print(x * i)
        total += (x * i)
        print("total =",  total)
    # if i > 215:
    #     print("i =", i, "x =", x)

    if x <= (i % 40) <= x + 2:
        image += '#'
    else:
        image += "."

    x += queue.pop(0)

image_out = [image[i:i + 40] for i in range(0, len(image), 40)]

for line in image_out:
    print(line)