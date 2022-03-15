import sys

N = int(input())


def is_vps(a, b):
    if a == "(" and b == ")":
        return True
    return False


def check(tmp):
    stack = []
    # stack = [tmp[0]]
    for i in range(len(tmp)):
        stack.append(tmp[i])
        if len(stack) > 1:
            if is_vps(stack[-2], stack[-1]):
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    check(tmp)
