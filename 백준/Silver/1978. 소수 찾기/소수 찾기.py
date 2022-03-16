import sys

N = int(sys.stdin.readline().rstrip())


def is_prime(N):
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True


tmp = (sys.stdin.readline().rstrip().split(" "))
c = 0
for num in tmp:

    if int(num) == 1:
        continue
    if is_prime(int(num)):
        c += 1

print(c)