import sys

result_a = 0
result_b = 0
S = input()
count = 0
index = -1
for i in range(1, len(S)):
    if S[i] != S[0] and S[i - 1] == S[0]:
        count += 1
        if index == -1:
            index = i
count_b = 0
for i in range(1, len(S)):
    if S[i]!= S[0] and S[i-1] == S[0]:
        count_b += 1

print(min(count+1, count_b))