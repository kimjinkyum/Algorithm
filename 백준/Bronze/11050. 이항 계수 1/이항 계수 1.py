import sys

N, K = sys.stdin.readline().rstrip().split(" ")

def fact(N):
    result = 1
    for i in range(2, N+1):
        result *= i
    return result


result = fact(int(N)) / (fact(int(K)) * fact(int(N) - int(K)))
print(int(result))