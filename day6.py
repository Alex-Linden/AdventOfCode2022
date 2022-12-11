signal = open('day6.txt').read()

signal1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' #7 - 19
signal2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz' #6 - 23
signal3 = 'nppdvjthqldpwncqszvftbrmjlhg' #5 - 23
signal4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #10 - 29
signal5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' #11 - 26
        #  '01234567890123'

def find_marker(str):
    l, r = 0, 0

    char_indx = {}

    while (r - l) < 4:
        if str[r] in char_indx:
            idx = char_indx[str[r]] + 1
            l = idx if idx > l else l

        char_indx[str[r]] = r
        r += 1
        # print("l=", l, "r=", r)
        # print(char_indx)

    print(r)

find_marker(signal)
find_marker(signal1)
find_marker(signal2)
find_marker(signal3)
find_marker(signal4)
find_marker(signal5)

def find_marker2(str):
    l, r = 0, 0

    char_indx = {}

    while (r - l) < 14:
        if str[r] in char_indx:
            idx = char_indx[str[r]] + 1
            l = idx if idx > l else l

        char_indx[str[r]] = r
        r += 1
        # print("l=", l, "r=", r)
        # print(char_indx)

    print(r)

find_marker2(signal)
find_marker2(signal1)
find_marker2(signal2)
find_marker2(signal3)
find_marker2(signal4)
find_marker2(signal5)