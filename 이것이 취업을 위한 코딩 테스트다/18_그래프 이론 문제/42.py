G = int(input())
p = int(input())

x = [False] * (G + 1)
for i in range(p):
    Flag = False
    g = int(input())

    while g > 0:
        if not x[g]:
            x[g] = True
            Flag = True
            break
        else:
            g -= 1
    if not Flag:
        break

if not Flag:
    print(i)
else:
    print(i + 1)

