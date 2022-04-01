# 곱하기 혹은 더하기
import sys

data = sys.stdin.readline().rstrip()
result = 0

for i in data:
    i = int(i)
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
