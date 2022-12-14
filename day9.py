moves = open('day9.txt').read().split('\n')
# moves = ['R 5', 'U 8']

# print(moves)

head_x, head_y = 0, 0

tail_x, tail_y = 0, 0

visited = set()

visited.add((tail_y, tail_x))

for move in moves:
    move = move.split(" ")
    # right moves
    if move[0] == 'R':
        for i in range(int(move[1])):
            head_x += 1
            if [head_y - tail_y, head_x - tail_x] == [0, 2]:
                tail_x += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [1, 2]:
                tail_y += 1
                tail_x += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [-1, 2]:
                tail_y -= 1
                tail_x += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))

            # print("head =", [head_y, head_x])
            # print("tail =", [tail_y, tail_x])
    # left moves
    elif move[0] == 'L':
        for i in range(int(move[1])):
            head_x -= 1
            if [head_y - tail_y, head_x - tail_x] == [0, -2]:
                tail_x -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [1, -2]:
                tail_y += 1
                tail_x -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [-1, -2]:
                tail_y -= 1
                tail_x -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
    # up moves
    elif move[0] == 'U':
        for i in range(int(move[1])):
            head_y += 1
            if [head_y - tail_y, head_x - tail_x] == [2, 0]:
                tail_y += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [2, -1]:
                tail_y += 1
                tail_x -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [2, 1]:
                tail_y += 1
                tail_x += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
    # down moves
    elif move[0] == 'D':
        for i in range(int(move[1])):
            head_y -= 1
            if [head_y - tail_y, head_x - tail_x] == [-2, 0]:
                tail_y -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [-2, -1]:
                tail_y -= 1
                tail_x -= 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))
            elif [head_y - tail_y, head_x - tail_x] == [-2, 1]:
                tail_y -= 1
                tail_x += 1
                if (tail_y, tail_x) not in visited:
                    visited.add((tail_y, tail_x))


print("Answer is", len(visited))


# part 2
rope = [
    [0, 0], # H
    [0, 0], # 1
    [0, 0], # 2
    [0, 0], # 3
    [0, 0], # 4
    [0, 0], # 5
    [0, 0], # 6
    [0, 0], # 7
    [0, 0], # 8
    [0, 0], # 9
]
visited_part2 = set()

for move in moves:
    move = move.split(" ")
    for i in range(int(move[1])):
        head = rope[0]
        print(head)
        if move[0] == 'R':
            head[1] += 1
        elif move[0] == 'L':
            head[1] -= 1
        elif move[0] == 'U':
            head[0] += 1
        elif move[0] == 'D':
            head[0] -= 1

        for i in range(1, len(rope)):
            tail = rope[i]
            print(tail, head)
            # right moves
            if [head[0] - tail[0], head[1] - tail[1]] == [0, 2]:
                tail[1] += 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [1, 2]:
                tail[0] += 1
                tail[1] += 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [-1, 2]:
                tail[0] -= 1
                tail[1] += 1

            # left moves
            elif [head[0] - tail[0], head[1] - tail[1]] == [0, -2]:
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [1, -2]:
                tail[0] += 1
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [-1, -2]:
                tail[0] -= 1
                tail[1] -= 1

            # up moves
            elif [head[0] - tail[0], head[1] - tail[1]] == [2, 0]:
                tail[0] += 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [2, -1]:
                tail[0] += 1
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [2, 1]:
                tail[0] += 1
                tail[1] += 1

            # down moves
            elif [head[0] - tail[0], head[1] - tail[1]] == [-2, 0]:
                tail[0] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [-2, -1]:
                tail[0] -= 1
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [-2, 1]:
                tail[0] -= 1
                tail[1] += 1

            #diagonals
            elif [head[0] - tail[0], head[1] - tail[1]] == [-2, -2]:
                tail[0] -= 1
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [2, -2]:
                tail[0] += 1
                tail[1] -= 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [-2, 2]:
                tail[0] -= 1
                tail[1] += 1
            elif [head[0] - tail[0], head[1] - tail[1]] == [2, 2]:
                tail[0] += 1
                tail[1] += 1



            head = tail
        print(rope)
        end = rope[-1]
        # print(end)
        if (end[0], end[1]) not in visited_part2:
            visited_part2.add((end[0], end[1]))

print(rope)
print(visited_part2)
print("part 2 answer is", len(visited_part2))


# def move_head(move, x, y):
#     move = move.split(" ")
#     if move[0] == 'R':
#         x += int(move[1])
#     elif move[0] == 'L':
#         x -= int(move[1])
#     elif move[0] == 'U':
#         y += int(move[1])
#     else:
#         y -= int(move[1])

#     return [y, x]

# def move_tail(move, head, tail):
#     global visited
#     h_y, h_x = head
#     t_y, t_x = tail
#     x_diff = h_x - t_x
#     y_diff = h_y - t_y
#     if abs(x_diff) <= 1 and abs(y_diff) <= 1:
#         return tail
#     elif move[1] == "R":

# for move in moves:
#     coordinate = move_head(move, head_x, head_y)
#     head_y, head_x = coordinate
#     print(head_y, head_x)
