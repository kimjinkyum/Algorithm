import sys

T = int(sys.stdin.readline().rstrip())


def check(N, M, tmp):
    document = []
    for i in range(int(N)):
        document.append([i, int(tmp[i])])
    count = 0
    max_important = max(t[1] for t in document)

    while True:
        print_document = document.pop(0)
        if print_document[1] != max_important:
            document.append(print_document)
        else:
            count += 1
            if print_document[0] == int(M):
                print(count)
                break
            max_important = max(t[1] for t in document)

for _ in range(T):
    N, M = sys.stdin.readline().rstrip().split(" ")

    tmp = sys.stdin.readline().rstrip().split(" ")
    check(N, M, tmp)
