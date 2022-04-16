# 럭키 스트레이트
import sys

data = sys.stdin.readline().rstrip()

mid = int(len(data) / 2)
result = 0

for i in range(mid):
    result += (int(data[i]) - int(data[mid + i]))

if result == 0:
    print("LUCKY")
else:
    print("READY")
