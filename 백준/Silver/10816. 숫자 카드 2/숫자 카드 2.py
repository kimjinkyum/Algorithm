import sys
from bisect import bisect_left, bisect_right
N = int(input())

card = input().split(" ")

card = list(map(int, card))

card.sort()
M = int(input())
num = []
candi = input().split(" ")
candi = list(map(int, candi))

s = 0
e = N - 1


for c in candi:
    left_index = bisect_left(card, c)
    right_index = bisect_right(card, c)

    print(right_index-left_index, end=" ")