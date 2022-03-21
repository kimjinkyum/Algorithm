import sys

N = int(sys.stdin.readline().rstrip())

i = 0
s_n = 2
while True:
    if N == 1:
        print(1)
        break

    S = 5 + (6 * i)
    result = s_n + S

    if N <= result:
        print(i+2)
        break
    else:
        s_n = result +1
        i += 1


