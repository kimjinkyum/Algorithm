import sys
A, B, V = sys.stdin.readline().rstrip().split(" ")

tmp = (int(V) - int(B)) / (int(A)- int(B))

if int(tmp) != tmp:
    print(int(tmp) + 1)
else:
    print(int(tmp))