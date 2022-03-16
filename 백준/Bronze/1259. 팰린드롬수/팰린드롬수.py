import sys
from collections import deque

def search(t):
    q = deque(t)

    while len(q) > 1:
        if q.popleft() != q.pop():
            return "no"
    return "yes"

while True:
    text = sys.stdin.readline().rstrip()

    if text == "0":
        break
    print(search(text))