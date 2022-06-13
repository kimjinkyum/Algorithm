n, r, c = map(int, input().split())

ans = 0

while n != 0:
    n -= 1

    # 1사분면
    if r < 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 0
    elif r < 2 ** n <= c:
        ans += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    elif r >= 2 ** n > c:
        ans += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    else:
        ans += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)


def sol(n, r, c):
    if n == 0:
        return 0
    else:
        return 2 * (r % 2) + (c % 2) + 4 * sol(n-1, int(r/2), int(c/2))


print(ans)
