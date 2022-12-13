tree_grid = open('day8.txt').read().split('\n')

# print(tree_grid)

visible_trees = (len(tree_grid) * 2) + ((len(tree_grid[0]) - 2) * 2 )
print(visible_trees)

seen = set()

print("top")
# handles trees visible from the top
for j in range(1, len(tree_grid[0]) - 1):
    maxH = int(tree_grid[0][j])
    # print("maxH =", maxH)
    for i in range(1, len(tree_grid) - 1):
        if int(tree_grid[i][j]) > maxH:
            maxH = int(tree_grid[i][j])
            if (i, j) not in seen:
                seen.add((i, j))
                visible_trees += 1
# print(seen)
# print(visible_trees)


print("left")
# handles trees visible from the left
for i in range(1, len(tree_grid) - 1):
    maxH = int(tree_grid[i][0])
    # print("maxH =", maxH)
    for j in range(1, len(tree_grid[0]) - 2):
        if int(tree_grid[i][j]) > maxH:
            maxH = int(tree_grid[i][j])
            if (i, j) not in seen:
                seen.add((i, j))
                visible_trees += 1
# print(seen)
# print(visible_trees)

bottom = len(tree_grid) - 1
print("bottom", bottom)
# handles trees visible from the bottom
for j in range(1, len(tree_grid[0]) - 1):
    maxH = int(tree_grid[bottom][j])
    # print("maxH =", maxH)
    for i in range(bottom - 1, 1, -1):
        if int(tree_grid[i][j]) > maxH:
            maxH = int(tree_grid[i][j])
            if (i, j) not in seen:
                seen.add((i, j))
                visible_trees += 1
# print(seen)
# print(visible_trees)


right = len(tree_grid[0]) - 1
print("right", right)
# handles trees visible from the right
for i in range(1, len(tree_grid) - 1):
    maxH = int(tree_grid[i][right])
    # print("maxH =", maxH)
    for j in range(right - 1, 0, -1):
        if int(tree_grid[i][j]) > maxH:
            maxH = int(tree_grid[i][j])
            if (i, j) not in seen:
                seen.add((i, j))
                visible_trees += 1

# print(len(seen))
# print(seen)
print(visible_trees)

def dfs_top(x, y):
    tree = int(tree_grid[x][y])
    distance_score = 0
    while x > 0:
        distance_score += 1
        x -= 1
        if tree <= int(tree_grid[x][y]):
            break
    return distance_score

def dfs_left(x, y):
    tree = int(tree_grid[x][y])
    distance_score = 0
    while y > 0:
        distance_score += 1
        y -= 1
        if tree <= int(tree_grid[x][y]):
            break
    return distance_score

def dfs_bottom(x, y):
    tree = int(tree_grid[x][y])
    distance_score = 0
    while x < len(tree_grid) - 1:
        distance_score += 1
        x += 1
        if tree <= int(tree_grid[x][y]):
            break
    return distance_score

def dfs_right(x, y):
    tree = int(tree_grid[x][y])
    distance_score = 0
    while y < len(tree_grid[0]) - 1:
        distance_score += 1
        y += 1
        if tree <= int(tree_grid[x][y]):
            break
    return distance_score

# print("t", dfs_top(3, 2))
# print("l",dfs_left(3, 2))
# print("b",dfs_bottom(3, 2))
# print("r", dfs_right(3, 2))
max_score = 0

for tree in seen:
    t = dfs_top(tree[0], tree[1])
    l = dfs_left(tree[0], tree[1])
    b = dfs_bottom(tree[0], tree[1])
    r = dfs_right(tree[0], tree[1])

    tree_score = t * l * b * r

    max_score = max(tree_score, max_score)

print(max_score)