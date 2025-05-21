from collections import deque


def check_is_ok(word):
    q = deque([])
    for w in word:
        if w == "(":
            q.append(w)
        else:
            if not len(q):
                return False
            q.pop()
    return len(q) == 0


def bfs(word):
    if not word:
        return ""
    count = 0
    point = 0
    for idx, i in enumerate(word):
        if i == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            point = idx
            break
    u = word[:point + 1]
    v = word[point + 1:]
    if check_is_ok(u):
        return u + bfs(v)
    else:
        sub = "("
        sub += bfs(v)
        sub += ")"
        for a in u[1:-1]:
            if a == "(":
                sub += ")"
            else:
                sub += "("
        return sub


print(bfs("()))((()"))
