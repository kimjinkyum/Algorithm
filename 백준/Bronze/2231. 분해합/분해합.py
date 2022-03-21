import sys

N = (sys.stdin.readline().rstrip())

def sum_prefix(num):
    num = str(num)

    return int(num) + sum([int(i) for i in num])

if int(N) <= 10:
    s_num = 1
    while True:
        if s_num * 2 == int(N):
            print(s_num)
            break
        if s_num > int(N):
            print(0)
            break
        s_num +=1


else:
    prefix = len(N)
    s_num = 10
    while True:
        result = sum_prefix(s_num)
        if result == int(N):
            print(s_num)

            break
        s_num += 1

        if s_num > int(N):
            print(0)
            break






