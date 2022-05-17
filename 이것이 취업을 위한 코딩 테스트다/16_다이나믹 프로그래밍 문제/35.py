# 못생긴 수

n = int(input())

data = [0] * n

data[0] = 1

i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    data[i] = min(next2, next3, next5)

    if data[i] == next2:
        i2 += 1
        next2 = data[i2] * 2

    if data[i] == next3:
        i3 += 1
        next3 = data[i3] * 3

    if data[i] == next5:
        i5 += 1
        next5 = data[i5] * 5
    print(i2, i3, i5)
    print(next2, next3, next5)

print(data)