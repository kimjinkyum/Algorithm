# 문자열 뒤집기
import sys


data = sys.stdin.readline().rstrip()

count0 = 0
count1 = 0
change0 = False
change1 = False

for i in range(len(data)):
    if data[i] != "0":
        change0 = True
        i += 1

    else:
        if change0:
            count0 += 1
            change0 = False
        i += 1

for i in range(len(data)):
    if data[i] != "1":
        change1 = True
        i += 1

    else:
        if change1:
            count1 += 1
            change1 = False
        i += 1

if change0:
    count0 += 1

if change1:
    count1 += 1


print(min(count0, count1))

