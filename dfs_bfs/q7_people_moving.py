from pprint import pprint


def people_moving():
    maps = [
        [50, 30],
        [20, 40]
    ]
    l = 20
    r = 50
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]

    def dfs(i, j, visited):
        visited[i][j] = True
        union = [(i, j)]
        pop_sum = maps[i][j]

        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny]:
                if l <= abs(maps[i][j] - maps[nx][ny]) <= r:
                    sub_union, sub_sum = dfs(nx, ny, visited)
                    union.extend(sub_union)
                    pop_sum += sub_sum
        return union, pop_sum

    days = 0
    while True:
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        moved = False
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if not visited[i][j]:
                    union, pop_sum = dfs(i, j, visited)
                    if len(union) > 1:
                        moved = True
                        avg = pop_sum // len(union)
                        for x, y in union:
                            maps[x][j] = avg
        if not moved:
            break
        days += 1
    print(days)
    pprint(maps, width=20)
    return days


people_moving()
