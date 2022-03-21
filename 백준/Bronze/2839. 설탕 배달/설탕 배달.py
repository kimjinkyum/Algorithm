import sys

N = int(sys.stdin.readline().rstrip())
count = int(N / 5)
while True:
    w = N - (5*count)

    if count < 0:
        print(-1)
        break

    if w % 3 != 0:
        count -= 1
    else:
        print(count + int(w/3))
        break
