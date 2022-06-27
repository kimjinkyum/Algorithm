import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


T = int(input())


def lcm(a, b):
    gcd_value = gcd(a, b)
    if gcd_value == 0:
        return 0
    return int((a * b) / gcd_value)


for _ in range(T):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())

    end_year = lcm(m, n)

    while True:

        if x < y:
            x = x + m
        elif x > y:
            y = y + n
        else:
            print(x)
            break
        if end_year <= x or end_year <= y:
            print(-1)
            break

