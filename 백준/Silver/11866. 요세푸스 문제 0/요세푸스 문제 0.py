N, k = input().split()

N = int(N)
k = int(k)

people = [0 for _ in range(N)]

result = []

index = 0
for i in range(N):
    count = 1
    while True:
        if index >= N:
            index -= N

        if people[index] == 0:
            if count == k:
                result.append(index+1)
                people[index] = 1
                break
            index += 1
            count += 1
        else:
            index += 1


print("<", end="")
for i in range(N-1):
    print(result[i], end=", ")

print(result[-1], end=">")
