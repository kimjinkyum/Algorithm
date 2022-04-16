import sys

n = int(input())
k = int(input())

data = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

if k >=n :
    print(0)
    sys.exit()
    
arr = []
for i in range(1, len(data)):
    arr.append(data[i] - data[i-1])


arr.sort(reverse=True)

for i in range(k-1):
    arr[i] = 0
    
print(sum(arr))


