# signal = open('day13test.txt').read().split('\n')
signal = open('day13.txt').read().split('\n')

# signal = "[[1],[2,3,4]]"
# print(signal)

def substr_to_list(sub):
    lst = []
    sub = sub.split(",")
    # print(sub)
    # if sub[-1] == "":
    #     sub.pop()
    # if sub[0] == "":
    #     sub.pop(0)
    for el in sub:
        if el != "":
            lst.append(int(el))
    # print("sub to list=", sub)
    return lst

def parse_row(row):

    stack = []
    # out = []
    for i in range(len(row)):
        # print("row[i] =",  row[i], "i =", i)
        if row[i] != "]":
            # print("if")
            stack.append(row[i])
            # print("stack=", stack)
        else:
            # print("else")
            lst = []
            tmp = ""
            # print(stack)
            cur = stack.pop()
            while cur != '[':
                # print("stack =",stack)
                # print("cur =", cur)
                # print("tmp = ", tmp)
                if isinstance(cur, list):
                    if tmp != "" and tmp != ",":
                        tmp = substr_to_list(tmp)
                        lst = tmp + lst
                        tmp = ""
                    lst.insert(0, cur)
                else:
                    tmp = cur + tmp
                cur = stack.pop()


            if tmp != "" and tmp != ",":
                tmp = substr_to_list(tmp)
                lst = tmp + lst

            stack.append(lst)



    return stack[0]

parsed_signal = []

for row in signal:
    # print(row)
    if row != "":
        parsed_signal.append(parse_row(row))
    # print(parsed_signal)


# print(len(parsed_signal))

def is_sorted(lst1, lst2):
    i = 0
    while i in range(len(lst1)) and i in range(len(lst2)):
        if isinstance(lst1[i], int) and isinstance(lst2[i], list):
            if is_sorted([lst1[i]], lst2[i]):
                return True
            elif is_sorted([lst1[i]], lst2[i]) == False:
                return False
        elif isinstance(lst1[i], list) and isinstance(lst2[i], int):
            if is_sorted(lst1[i], [lst2[i]]):
                return True
            elif is_sorted(lst1[i], [lst2[i]]) == False:
                return False
        elif isinstance(lst1[i], list) and isinstance(lst2[i], list):
            if is_sorted(lst1[i], lst2[i]):
                return True
            elif is_sorted(lst1[i], lst2[i]) == False:
                return False
        elif lst1[i] > lst2[i]:
            # print(lst1[i], ">", lst2[i])
            return False
        elif lst1[i] < lst2[i]:
            return True

        i += 1
    if len(lst1) > len(lst2):
        # print(lst1, "is longer than", lst2,)
        return False
    elif len(lst1) < len(lst2):
        # print(lst1, "is shorter than", lst2,)
        return True

    return

pair = 1
out = []
i = 0
part_2 = []
while i in range(len(parsed_signal)):
    # print(pair)
    if is_sorted(parsed_signal[i], parsed_signal[i + 1]):
        out.append(pair)
        part_2.append(parsed_signal[i])
        part_2.append(parsed_signal[i + 1])
    else:
        print("pair =", pair, "and i =", i)
        print("left =", parsed_signal[i])
        print("right =", parsed_signal[i + 1])
    pair += 1
    i += 2

# print(out)

print("part 1 =",sum(out))

#part 2 is merge sort
decoder1 = [[2]]
decoder2 = [[6]]
part_2.append(decoder1)
part_2.append(decoder2)


def merge_sort():