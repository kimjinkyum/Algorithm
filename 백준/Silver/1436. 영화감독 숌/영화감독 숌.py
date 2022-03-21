import sys


def make_6(prefix, s, count, N):
    index = len(s) - 1
    count_s = 0

    while index>=0:
        if s[index] != "6":
            break
        index -= 1
        count_s += 1

    for i in range(3 - count_s):
        s += "6"

    prefix = int(prefix - len(s))
    for i in range(0, 10 ** prefix):
        # print("In", s, i, prefix)
        count += 1
        if count == N:
            for _ in range(prefix - len(str(i))):
                s += "0"
            s += str(i)
            break
    return s, count


N = int(sys.stdin.readline().rstrip())
count = 1
s = 1
s_6 = 0
prefix = 4
if N==1:
    print("666")
while True:
    if N == count:
        print()
        break
    else:
        s = max(0, 10 ** (prefix - 4))
        for s in range(s, 10 ** (prefix - 3), 1):
            s = str(s)
            if s[-1] == "6":
                num, count = make_6(prefix, s, count, N)

            else:
                num = s + "666"
                count += 1

            if N == count:
                print(int(num))
                break

        prefix += 1
