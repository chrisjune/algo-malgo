from collections import deque


def icecream(maps):
    count = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                count += 1
                color_map(maps, i, j)
    print(count)


def color_map(maps, i, j):
    queue = deque([(i, j)])
    maps[i][j] = 1
    while queue:
        current = queue.popleft()
        ci, cj = current
        if ci + 1 < len(maps) and cj < len(maps[0]) and maps[ci + 1][cj] == 0:
            queue.append((ci + 1, cj))
            maps[ci + 1][cj] = 1

        if 0 <= ci - 1 < len(maps) and cj < len(maps[0]) and maps[ci - 1][cj] == 0:
            queue.append((ci - 1, cj))
            maps[ci - 1][cj] = 1

        if ci < len(maps) and 0 <= cj - 1 < len(maps[0]) and maps[ci][cj - 1] == 0:
            queue.append((ci, cj - 1))
            maps[ci][cj - 1] = 1

        if ci < len(maps) and cj + 1 < len(maps[0]) and maps[ci][cj + 1] == 0:
            queue.append((ci, cj + 1))
            maps[ci][cj + 1] = 1
    return maps


# icecream(
#     maps=[
#         [0, 0, 1, 1, 0],
#         [0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0]
#     ])
#
icecream(
    maps=[list(map(int, (list(i)))) for i in """
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
""".split()]
)
