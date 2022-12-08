f = open('day1.txt').read()
f = f.strip()
f.split('\n\n')
f.split('\n')
IN = [list(map(int, x.split())) for x in f.split("\n\n")]
l = sorted(map(sum, IN))
print(l[-1])
print(sum(l[-3:]))
