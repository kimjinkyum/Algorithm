import sys

N = int(sys.stdin.readline().rstrip())

coord = []
for i in range(N):
    x, y = sys.stdin.readline().rstrip().split(" ")

    coord.append([int(y), int(x)])


coord.sort()

for i in range(N):
    print(coord[i][1], coord[i][0])