# 가사 검색
from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def first(data, target, s, e):
    if s > e:
        return None
    mid = (s + e) // 2

    if (mid == 0 or target > data[mid - 1][0]) and data[mid][0] == target:
        return mid

    elif data[mid][0] >= target:
        return first(data, target, s, mid - 1)

    else:
        return first(data, target, mid + 1, e)


def last(data, target, s, e):
    if s > e:
        return None
    mid = (s + e) // 2

    if (mid == len(data) - 1 or target < data[mid + 1][0]) and data[mid][0] == target:
        return mid

    elif data[mid][0] > target:
        return last(data, target, s, mid - 1)

    else:
        return last(data, target, mid + 1, e)


def check(data, query):
    # print(data, query)
    count = 0
    data.sort(key=lambda x: x[1])
    index = 0
    candi = []
    qu = []
    for q in query:
        if q == "?":
            index += 1
        else:
            candi.append(index)
            index += 1
            qu.append(q)
    for d in data:
        tmp = [d[1][i] for i in candi]
        if tmp == qu:
            count += 1
    return count


def solution(words, queries):
    result = []
    answer = []
    for w in words:
        result.append((len(w), w))
    result.sort()
    for q in queries:
        left = first(result, len(q), 0, len(result) - 1)
        right = last(result, len(q), 0, len(result) - 1)
        if left is None:
            answer.append(0)
            continue
        answer.append(check(result[left:right + 1], q))

    return answer


print(solution(words, queries))
