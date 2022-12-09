packs = open('day3.txt').read().split('\n')
# packs = ['vJrwpWtwJgWrhcsFMMfFFhFp',
#     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#     'PmmdzqPrVvPwwTWBwg',
#     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#     'ttgJtRGJQctTZtZT',
#     'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]
"""Part 1"""
score = 0

for pack in packs:
    half = int(len(pack) // 2)
    # print(half)
    first_half = pack[:half]
    second_half = pack[half:]
    # print(pack)
    # print(first_half)
    # print(second_half)
    for item in first_half:
        if item in second_half:
            if item.islower():
                score += ord(item) - ord('a') + 1
                # print(ord(item) - ord('a') + 1)
                break
            else:
                score += ord(item) - ord('A') + 27
                # print(ord(item) - ord('A') + 27)
                break


print("Part 1", score)

"""Part 2"""

l = 0
badge_score = 0

while l < len(packs):
    pack = packs[l:l + 3]
    for item in pack[0]:
        if item in pack[1] and item in pack[2]:
            if item.islower():
                badge_score += ord(item) - ord('a') + 1
                break
            else:
                badge_score += ord(item) - ord('A') + 27
                break
    l += 3

print(badge_score)
