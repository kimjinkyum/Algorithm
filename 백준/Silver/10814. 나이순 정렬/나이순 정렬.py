import sys

N = int(input())

enroll = []
for i in range(N):
    tmp = sys.stdin.readline().rstrip().split(" ")
    enroll.append([int(tmp[0]), i, tmp[1]])



enroll.sort()


for i in range(N):
    print("{0} {1}".format(enroll[i][0], enroll[i][2]))
