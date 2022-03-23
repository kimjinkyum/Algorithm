import sys

N = int(sys.stdin.readline().rstrip())

text = sys.stdin.readline().rstrip()
M = 1234567891
r = 31

base = ord("a") -1

result = sum([(ord(text[i]) - base) * r ** i for i in range(len(text))])
print(result % M)

