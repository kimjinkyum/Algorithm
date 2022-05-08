# 공유기 설치

def check_count(distance, gap):
    count = 1
    result = []
    for i in range(len(gap)):
        if gap[i] > distance:
            count += 1
            result.append(i)
            result.append(i + 1)
    return count, result


n, c = map(int, input().split())

data = []
gap = []
for _ in range(n):
    data.append(int(input()))
data.sort()

start = 1
end = data[n - 1] - data[0]

result = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    prev = data[0]
    for i in range(1, n):
        if data[i] - prev >= mid:
            count += 1
            prev = data[i]
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = max(result, mid)

print(result)
