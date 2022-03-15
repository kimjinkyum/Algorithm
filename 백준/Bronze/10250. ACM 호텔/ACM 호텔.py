import sys

N = int(input())


def find_room(H, W, index):
    x = int(index / H)
    y = int(index % H)

    if y == 0 :
        y = H
    else:
        x = x + 1
    if x < 10:
        print("{0}0{1}".format(y, x))
    else:
        print("{0}{1}".format(y, x))


for _ in range(N):
    H, W, index = sys.stdin.readline().rstrip().split(" ")
    find_room(int(H), int(W), int(index))
