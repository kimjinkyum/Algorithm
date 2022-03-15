import sys
import itertools
N, M = input().split(" ")

card = input().split(" ")

card = list(map(int, card))

card.sort()


card_3 = list(itertools.combinations(card, 3))
m = 1
for i in card_3:
    tmp = sum(i)
    if tmp < int(M):
        m = max(tmp, m)
        
    if tmp == int(M):
        m = int(M)
        break

print(m)
