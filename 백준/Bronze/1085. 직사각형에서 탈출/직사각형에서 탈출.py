import sys

x,y,W,H = sys.stdin.readline().rstrip().split(" ")


move_x = min(int(x), int(W)-int(x))
move_y = min(int(y), int(H)-int(y))

print(min(move_x, move_y))
