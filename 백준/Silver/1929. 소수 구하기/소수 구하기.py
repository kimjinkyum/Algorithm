import sys

N, M = sys.stdin.readline().rstrip().split(" ")

prime = [i for i in range(2, int(M) + 1)]



for p in range(len(prime)):
    if prime[p] == 0:
        continue

    for i in range(2*prime[p], int(M)+1, prime[p]):
        prime[i-2] = 0


for p in prime:
    if p < int(N) or p ==0 :
        continue
    print(p)

