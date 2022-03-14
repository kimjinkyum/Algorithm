import sys

N, K = sys.stdin.readline().rstrip().split(" ")

def fact_dp(N, K):

    cache = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(0, N+1):
        cache[i][0] = 1
    for i in range(0, K+1):
        cache[i][i] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
            
    
    return cache[N][K]

print(fact_dp(int(N),  int(K)))
