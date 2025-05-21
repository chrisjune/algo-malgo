from collections import deque
from itertools import combinations


def laboratory(origin):
    zero_axis = []
    virus_axis = []
    for i in range(len(origin)):
        for j in range(len(origin[0])):
            if origin[i][j] == 0:
                zero_axis.append((i, j))
            elif origin[i][j] == 2:
                virus_axis.append((i, j))
    cand_axis = list(combinations(zero_axis, 3))
    max_count = 0
    for axis in cand_axis:
        # maps = deepcopy(origin)
        maps = [row[:] for row in origin]
        # 벽설치
        for a in axis:
            x, y = a[0], a[1]
            maps[x][y] = 1
        # bfs
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        queue = deque(virus_axis)
        while queue:
            cx, cy = queue.popleft()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 0:
                    maps[nx][ny] = 2
                    queue.append((nx, ny))
        count = 0
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 0:
                    count += 1
        max_count = max(max_count, count)
        # pprint(maps, width=30)
        # print()

    print(max_count)


laboratory(
    [
        [2, 2, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
)

laboratory(
    [
        [2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
)

laboratory([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 2]
])

laboratory(
    [
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
