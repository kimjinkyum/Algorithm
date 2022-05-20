# 연산자 끼워 넣기

import sys
from itertools import product, permutations


def cal(s, data):
    result = data[0]
    for i in range(1, len(data)):
        if s[i - 1] == "+":
            result += data[i]
        elif s[i - 1] == "-":
            result -= data[i]
        elif s[i - 1] == "*":
            result *= data[i]
        else:
            result = int(result / data[i])
    return result


n = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))

add, sub, mul, div = map(int, sys.stdin.readline().rstrip().split())

sign = []

sign.extend(['+'] * add)
sign.extend(['-'] * sub)
sign.extend(['*'] * mul)
sign.extend(['/'] * div)

candi = (list(permutations(sign, n - 1)))

min_value = 1e9
max_value = -1e9

for c in candi:
    result = cal(c, data)
    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)
