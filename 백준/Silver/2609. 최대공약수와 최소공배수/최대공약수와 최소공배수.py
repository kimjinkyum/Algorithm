import sys


def GCD(A, B):
    tmp = A % B

    if tmp == 0:
        return B
    else:
        return GCD(B, A % B)


def LCM(A, B, gcd):
    return int((A * B) / gcd)


N = sys.stdin.readline().rstrip().split(" ")

gcd = GCD(int(N[0]), int(N[1]))
print(gcd)
print(LCM(int(N[0]), int(N[1]), gcd))
