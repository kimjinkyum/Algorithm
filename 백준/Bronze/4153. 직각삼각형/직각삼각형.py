import sys

def is_triangle(tmp):
    tmp.sort()

    result = tmp[0] * tmp[0] + tmp[1]*tmp[1]

    if result == tmp[2] * tmp[2]:
        print("right")
    else:
        print("wrong")


while True:
    tmp = input().split(" ")
    tmp = list(map(int, tmp))

    if tmp[0] == 0  and tmp[1] == 0 and tmp[2]==0:
        break
    is_triangle(tmp)