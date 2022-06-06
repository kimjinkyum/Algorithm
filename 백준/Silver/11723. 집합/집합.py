import sys

n = int(input())
s = [0] * 21
for _ in range(n):
    data = sys.stdin.readline().rstrip().split()
    cmd = data[0]
    if cmd == "add":
        s[int(data[1])] = 1
    if cmd == "remove":
        s[int(data[1])] = 0
    if cmd == "check":
        print(s[int(data[1])])
    if cmd == "toggle":
        if s[int(data[1])] == 0:
            s[int(data[1])] = 1
        else:
            s[int(data[1])] = 0
    if cmd == "all":
        s = [1] * 21

    if cmd == "empty":
        s = [0] * 21


