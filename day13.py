signal = open('day13test.txt').read().split('\n')
# signal = "[[1],[2,3,4]]"
print(signal)

def substr_to_list(sub):
    sub = sub.split(",")
    # print(sub)
    if sub[-1] == "":
        sub.pop()
    if sub[0] == "":
        sub.pop(0)
    # print("sub to list=", sub)
    return list(map(int, sub))

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


print(parsed_signal)
