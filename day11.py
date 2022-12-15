rounds = open('day11.txt').read().split('\n\n')

"""
monkeys will be a dict {
    (monkey num) : [x, y, z ...] item represented by int indicating worry level
}
variable keeping track of worry level
need to figure out how to parse instructions into one instruction
"""

class Monkey:
    def __init__(self, name, items, operation, divis, true, false):
        self.name = name
        self.items = items
        self.operation = operation
        self.divis = divis
        self.true = true
        self.false = false
        self.business = 0

    def inspect_item(self, item):
        """increases worry level by operation amount either + or *"""
        self.business += 1
        if self.operation[0] == "+":
            out = item + int(self.operation[1])
            # print(out, '=', item, "+", self.operation[1])
            return out
        elif self.operation[1] == "old":
            out = item * item
            # print(out, '=', item, "* old")
            return out
        else:
            out = item * int(self.operation[1])
            # print(out, '=', item, "*", self.operation[1])
            return out

    def find_next_monkey(self, item):
        """tests item to find next monkey the item goes to"""
        if item % self.divis == 0:
            # print(item, "is divisible by", self.divis, "sent to", self.true)
            return self.true
        else:
            # print(item, "is not divisible by", self.divis, "sent to", self.false)
            return self.false

    def monkey_business(self):
        return f"{self.name} inspected items {self.business} times"

    def __str__(self):
        return f"{self.name} : {self.items}"

monkeys = []

"create monkeys"
for rnd in rounds:
    rnd = rnd.split("\n")
    # print(rnd)
    name = rnd[0][-2]
    # print(name)
    items = rnd[1].replace('  Starting items: ', "").split(", ")
    items = list(map(int, items))
    # print(items)
    ops = rnd[2].split(" ")
    ops = ops[-2:]
    # print(ops)
    divis = int(rnd[3].split(" ")[-1])
    # print(divis)
    true = rnd[4][-1]
    false = rnd[-1][-1]
    # print(f"true: {true} -- false: {false}")
    monkey = Monkey(name, items, ops, divis, true, false)
    monkeys.append(monkey)

"turn true/false from string to monkey"
for monkey in monkeys:
    true = monkey.true
    monkey2 = [monkey for monkey in monkeys if monkey.name == true]
    monkey.true = monkey2[0]

    false = monkey.false
    monkey_f = [monkey for monkey in monkeys if monkey.name == false]
    monkey.false = monkey_f[0]

# tmp = monkeys[0]
# print(tmp)
# print(tmp.operation)
# print(tmp.divis)
# print(tmp.true)
# print(tmp.false)

"do rounds"
for i in range(1, 21):
    # print("==== Round ", i, "====" )
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item = monkey.inspect_item(item)
            item = item // 3
            next_monkey = monkey.find_next_monkey(item)
            next_monkey.items.append(item)

for monkey in monkeys:
    print(monkey)

m_business = []
for monkey in monkeys:
    m_business.append(monkey.business)
    print(monkey.monkey_business())

m_business.sort()
print(m_business[-1] * m_business[-2])


"""Part 2 """

monkeys_pt2 = []

"create monkeys_pt2"
for rnd in rounds:
    rnd = rnd.split("\n")

    name = rnd[0][-2]

    items = rnd[1].replace('  Starting items: ', "").split(", ")
    items = list(map(int, items))

    ops = rnd[2].split(" ")
    ops = ops[-2:]

    divis = int(rnd[3].split(" ")[-1])

    true = rnd[4][-1]
    false = rnd[-1][-1]

    monkey = Monkey(name, items, ops, divis, true, false)
    monkeys_pt2.append(monkey)

"turn true/false from string to monkey"
for monkey in monkeys_pt2:
    true = monkey.true
    monkey2 = [monkey for monkey in monkeys_pt2 if monkey.name == true]
    monkey.true = monkey2[0]

    false = monkey.false
    monkey_f = [monkey for monkey in monkeys_pt2 if monkey.name == false]
    monkey.false = monkey_f[0]

manage_worry = [monkey.divis for monkey in monkeys_pt2]
worry_factor = 1
for num in manage_worry:
    worry_factor = worry_factor * num

"do rounds"
for i in range(1, 10001):
    # print("==== Round ", i, "====" )
    for monkey in monkeys_pt2:
        while monkey.items:
            item = monkey.items.pop(0)
            item = monkey.inspect_item(item)
            item = item % worry_factor
            # item = item % monkey.divis

            next_monkey = monkey.find_next_monkey(item)
            next_monkey.items.append(item)

    if i == 1 or i == 20 or i % 1000 == 0:
        print(f"== After round {i} ==")
        for monkey in monkeys_pt2:
            print(monkey.monkey_business())

for monkey in monkeys_pt2:
    print(monkey)

m_business_pt2 = []
for monkey in monkeys_pt2:
    m_business_pt2.append(monkey.business)
    print(monkey.monkey_business())

m_business_pt2.sort()
print(m_business_pt2[-1] * m_business_pt2[-2])

# m1_bz = [5204, 10419, 15638, 20858, 26075, 31294, 36508]
# for i in range(len(m1_bz) - 1):
#     print(m1_bz[i + 1] - m1_bz[i])