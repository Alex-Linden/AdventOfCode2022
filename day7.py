"""if a $ do an action
if a num create a key value pair
if a dir create a nested dictionary"""

commands = open('day7.txt').read().split('\n')

# print(commands)

class TreeNode:
    def __init__(self, name, val=0, parent=None):
        self.children = []
        self.name = name
        self.val = val
        self.parent = parent

file_system = TreeNode("/")


def handle_command(cmd, node):
    """takes a command and node. returns corresponding node"""

    if cmd[1] == "ls":
        return node
    elif cmd[2] == "..":
        return node.parent
    else:
        for child in node.children:
            if child.name == cmd[2]:
                return child

def make_child_node(cmd, node):
    """takes a command and node. returns new node to append to parent node"""
    if cmd[0] == 'dir':
        return TreeNode(cmd[1], 0, node)
    else:
        return TreeNode(cmd[1], int(cmd[0]), node)

i = 2 #can skip first 2 lines
curr = file_system

while i < len(commands):
    cmd = commands[i].split(" ")
    if cmd[0] == '$':
        curr = handle_command(cmd, curr)
    else:
        curr.children.append(make_child_node(cmd, curr))
    i += 1

for node in file_system.children:
    print(node.name, ":", node.val)

def get_vals_of_children(node):
    val = 0
    for child in node.children:
        if child.children:
            val += get_vals_of_children(child)
        else:
            val += child.val
    node.val = val
    return val

get_vals_of_children(file_system)


for node in file_system.children:
    print(node.name, ":", node.val)

def find_dirs_over_x(x, node):
    total = 0
    for child in node.children:
        if child.val < x and child.children:
            total += child.val
            total += find_dirs_over_x(x, child)
        elif child.children:
            total += find_dirs_over_x(x, child)

    return total


print("part 1 =",find_dirs_over_x(100001, file_system))

# part 1 = 1501149

# part 2
print(file_system.val)

def find_free_space_needed(num):
    return num - 40000000

space_needed = find_free_space_needed(file_system.val)
print(space_needed)

def find_dirs_large_enough(num, node):
    out = []
    if node.val > num:
        out.append(node.val)
    for child in node.children:
        if child.children:
            out += find_dirs_large_enough(num, child)

    return out

dirs_large_enough = find_dirs_large_enough(space_needed, file_system)
print(dirs_large_enough)

print("part2 =", min(dirs_large_enough))

# part2 = 10096985

