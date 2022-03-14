import sys

N = int(sys.stdin.readline())

cord = []

for _ in range(N):
    tmp = sys.stdin.readline().rstrip().split(" ")
    cord.append([int(tmp[0]), int(tmp[1])])

cord.sort()

for i in cord:
    print("{0} {1}".format(i[0], i[1]))
