from collections import deque
from pprint import pprint


def infection(maps, sec, final_x, final_y):
    virus_axis = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 0:
                virus_axis.append([maps[i][j], 0, i, j])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # sort
    virus_axis.sort(key=lambda x: x[0])
    queue = deque(virus_axis)

    while queue:
        q = queue.popleft()
        val, s, x, y = q
        if s >= sec:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 0:
                maps[nx][ny] = val
                queue.append([val, s + 1, nx, ny])

    print(maps[final_x - 1][final_y - 1])
    pprint(maps, width=30)


infection(
    [
        [1, 0, 2],
        [0, 0, 0],
        [3, 0, 0]
    ],
    2, 3, 2
)

infection(
    [
        [1, 0, 2],
        [0, 0, 0],
        [3, 0, 0]
    ],
    1, 2, 2
)
