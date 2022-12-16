# grid = open('day12test.txt').read().split('\n')
grid = open('day12.txt').read().split('\n')

print(grid)

row = len(grid)
col = len(grid[0])


def find_valid_moves(start):
    y, x = start
    moves = []

    if grid[y][x] == "S":
        max_val = 1
    elif grid[y][x] == "E":
        max_val = 26
    else:
        max_val = ord(grid[y][x]) - ord("a") + 1

    if x + 1 in range(col) and ord(grid[y][x+1]) - ord("a") <= max_val:
        if grid[y][x+1] != "E":
            moves.append([y, x + 1])
        elif grid[y][x+1] == "E" and max_val >= 25:
            moves.append([y, x + 1])

    if x -  1 in range(col) and ord(grid[y][x-1]) - ord("a") <= max_val:
        if grid[y][x-1] != "E":
            moves.append([y, x - 1])
        elif grid[y][x-1] == "E" and max_val >= 25:
            moves.append([y, x - 1])

    if y + 1 in range(row) and ord(grid[y+1][x]) - ord("a") <= max_val:
        if grid[y + 1][x] != "E":
            moves.append([y + 1, x])
        if grid[y + 1][x] == "E" and max_val >= 25:
            moves.append([y + 1, x])

    if y -  1 in range(row) and ord(grid[y-1][x]) - ord("a") <= max_val:
        if grid[y - 1][x] != "E":
            moves.append([y - 1, x])
        if grid[y - 1][x] == "E" and max_val >= 25:
            moves.append([y - 1, x])

    return moves


def distance_of_shortest_path(start, end):
    y, x = start
    if grid[y][x] == end:
        return 0

    seen = set()
    to_visit_queue = [[start, 0]]
    seen.add((y, x))
    # print(to_visit_queue.pop())


    while len(to_visit_queue):
        cur, distance = to_visit_queue.pop(0)

        i, j = cur
        # print(grid[i][j], cur, distance)
        if grid[i][j] == end:
            return distance

        moves = find_valid_moves(cur)

        for move in moves:
            y, x = move
            if (y, x) not in seen:
                seen.add((y, x))
                to_visit_queue.append([move, distance + 1])

    return float("inf")



for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            print(i, j)
            print(distance_of_shortest_path([i, j], "E"))
            break


# part 2

shortest_pos = float("inf")

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S" or grid[i][j] == "a":
            # print(distance_of_shortest_path([i, j], "E"))
            shortest_pos = min(shortest_pos, distance_of_shortest_path([i, j], "E"))

print("part 2", shortest_pos)

