import sys

N = int(sys.stdin.readline().rstrip())

num = []

for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    num.append(tmp)

num.sort()

mean = int(round(sum(num) / N, 0))

if mean == -0:
    print(0)
else:
    print(mean)

counts = {i: 0 for i in num}
for n in num:
    counts[n] += 1


print(num[N // 2])


l = max(counts.values())
count_flag = 0
max_fre = 4001
for n in num:
    if counts[n] == l and count_flag<2:
        if max_fre != n:
            count_flag += 1
        max_fre = n
    if count_flag == 2:
        break
print(max_fre)

print(int(num[-1] - num[0]))

