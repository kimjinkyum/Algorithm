#  괄호 변환

p = "()))((()"


def split_two(p):
    count = 0
    index = 0
    for i in range(len(p)):
        tmp = p[i]
        if tmp == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            index = i
            break

    return p[0:index + 1], p[index + 1:]


def is_right(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
        return True


def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    u, v = split_two(p)
    if is_right(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer

