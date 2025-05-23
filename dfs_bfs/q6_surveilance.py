from itertools import combinations


def hide(x, y, maps, direction):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    nx, ny = x + dx[direction], y + dy[direction]

    while 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
        if maps[nx][ny] in ['s', 'o']:
            break
        if maps[nx][ny] == 't':
            return False
        nx, ny = nx + dx[direction], ny + dy[direction]

    return True


def surveillance(maps):
    choice = 3
    maps = [[i for i in m] for m in maps]
    s_axis = []
    emp_axis = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 's':
                s_axis.append((i, j))
            if maps[i][j] == 'x':
                emp_axis.append((i, j))

    emp_candidates = combinations(emp_axis, choice)
    for cand in emp_candidates:
        for c in cand:
            x, y = c
            maps[x][y] = 'o'

        hidden = True
        for q in s_axis:
            x, y = q
            if not hide(x, y, maps, 0) or not hide(x, y, maps, 1) or not hide(x, y, maps, 2) or not hide(x, y, maps, 3):
                hidden = False

        if hidden:
            return hidden

        for c in cand:
            x, y = c
            maps[x][y] = 'x'

    return False


surveillance(
    maps=[
        'xsxxt', 'txsxx', 'xxxxx', 'xtxxx', 'xxtxx'
    ])
surveillance(
    maps=[
        'ssst', 'xxxx', 'xxxx', 'tttx'
    ])
