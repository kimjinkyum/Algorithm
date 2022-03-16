import sys


def merge_sort(arr):

    
    if len(arr) <= 1:
        
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left, right):

    l = 0
    r = 0
    merge_result = []
    while l < len(left) and r < len(right):
        if (left[l]) < right[r]:
            merge_result.append(left[l])
            l += 1
        else:
            merge_result.append(right[r])
            r += 1

    while l < len(left):
        merge_result.append(left[l])
        l += 1

    while r < len(right):
        merge_result.append(right[r])
        r += 1
    
    
    return merge_result


N = int(input())

result = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# (result).sort()
result = merge_sort(result)

for i in result:
    print(i)
