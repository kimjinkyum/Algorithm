t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    for j in range(1, n+1):
        if j == 1:
            dp[1] = 1
            continue
        elif j == 2:
            dp[2] = 2
            continue
        elif j == 3:
            dp[3] = 4
            continue
        for i in range(1, 4):
            tmp = j-i
            if tmp <= 0:
                continue
            dp[j] += dp[tmp]

    print(dp[n])