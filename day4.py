elf_groups = open('day4.txt').read().split('\n')
# elf_groups = ["2-4,6-8", "2-3,4-5",
#               "5-7,7-9",
#               "2-8,3-7",
#               "6-6,4-6",
#               "2-6,4-8"]

# print(elf_groups)

elf_groups = [group.split(",") for group in elf_groups]
# elf_groups = [elf.split("-") for group in elf_groups for elf in group.split(",")]

overlapping = 0

for group in elf_groups:
    elf_1 = [int(e) for e in group[0].split("-")]
    elf_2 = [int(e) for e in group[1].split("-")]

    if (elf_1[0] <= elf_2[0] <= elf_1[1] or
        elf_1[0] <= elf_2[1] <= elf_1[1]):
        overlapping += 1
        print(elf_1, elf_2)
    elif (elf_2[0] <= elf_1[0] <= elf_2[1] or
        elf_2[0] <= elf_1[1] <= elf_2[1]):
        overlapping += 1
        print(elf_1, elf_2)

print(overlapping)







# print(elf_groups)
