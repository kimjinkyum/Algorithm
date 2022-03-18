import sys

def check(s):

    if (s[-2] =="(" and s[-1] ==")"):
        s.pop()
        s.pop()
    elif (s[-2] =="[" and s[-1] =="]"):
        s.pop()
        s.pop()

    return s


while True:
    tmp = sys.stdin.readline().rstrip()
    s = []
    if tmp ==".":
        break

    for i in tmp:
        if i == "(" or i ==")" or i =="[" or i=="]":
            s.append(i)
        if len(s) >=2:
            s = check(s)

    if len(s)==0:
        print("yes")
    else:
        print("no")
