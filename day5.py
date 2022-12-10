crates = open('day5.txt').read().split('\n')
# crates = [
#     '    [D]    ',
#     '[N] [C]    ',
#     '[Z] [M] [P]',
#     ' 1   2   3 ',
#     "",
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2',
# ]

crates, moves = crates[:8], crates[10:]
crates_dict = {stack: [] for stack in range(1, 10)}

# crates, moves = crates[:4], crates[5:]
# crates_dict = {stack: [] for stack in range(1, 4)}

for row in reversed(crates):
    for i in range(len(row)):
        if row[i].isalpha():
            x = (i + 3) / 4
            crates_dict[x].append(row[i])

# print(crates_dict)
for key in crates_dict:
    print(key, crates_dict[key])
print(moves[0])
print(moves[-1])

crates_dict_part_2 = crates_dict
# for move in moves:
#     move = move.split(" ")
#     # print(move)
#     num_to_move = int(move[1])
#     from_col = int(move[3])
#     to_col = int(move[-1])
#     for i in range(num_to_move):
#         if crates_dict[from_col]:
#             crate = crates_dict[from_col].pop()
#             crates_dict[to_col].append(crate)


# print("=====final crates_dict====")
# for key in crates_dict:
#     print(key, crates_dict[key])
# print("final top crate =========")
# out_code = ""
# for value in crates_dict.values():
#     out_code += value[-1]
#     print(value[-1])

# print(out_code)


################## part 2 ########################
"""need to fix this logic"""
print('========= Part 2 ===============')
for key in crates_dict_part_2:
    print(key, crates_dict_part_2[key])
for move in moves:
    move = move.split(" ")
    # print(move)
    num_to_move = int(move[1])
    from_col = int(move[3])
    to_col = int(move[-1])
    crates_moving = []
    for i in range(num_to_move):
        if crates_dict_part_2[from_col]:
            crate = crates_dict_part_2[from_col].pop()
            crates_moving.append(crate)
    print(crates_moving[::-1])
    crates_dict_part_2[to_col] += crates_moving[::-1]


print("=====final crates_dict_part_2====")
for key in crates_dict_part_2:
    print(key, crates_dict_part_2[key])
print("final top crate =========")
out_part_2 = ""
for value in crates_dict_part_2.values():
    out_part_2 += value[-1]
    print(value[-1])

print(out_part_2)
