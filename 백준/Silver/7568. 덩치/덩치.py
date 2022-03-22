import sys

N = int(sys.stdin.readline().rstrip())

person = []
result = []

def count_high(index, person):
    count = 0
    for i in range(len(person)):
        if person[i][0] > person[index][0] and person[i][1] > person[index][1]:
            count += 1
    return count


for i in range(N):
    w, h = sys.stdin.readline().rstrip().split(" ")

    person.append([int(w), int(h)])

for i in range(N):
    print((count_high(i, person) + 1), end =" ")


