from collections import deque
from pprint import pprint


def snake(map_size, apples, rotates):
    maps = [[0] * map_size for _ in range(map_size)]
    for cord in apples:
        x = cord[0] - 1
        y = cord[1] - 1
        maps[x][y] = 1

    maps[0][0] = 2
    clock = 0
    direction = 0
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    x = 0
    y = 0
    snakes = deque([(x, y)])
    rotates = deque(rotates)
    while True:
        pprint(maps)
        clock += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        print(nx, ny)
        if 0 <= nx < map_size and 0 <= ny < map_size:
            if maps[nx][ny] == 1:
                maps[nx][ny] = 2
                x, y = nx, ny
                snakes.appendleft((x, y))
            elif maps[nx][ny] == 2:
                return clock
            else:
                x, y = nx, ny
                maps[x][y] = 2
                snakes.appendleft((x, y))
                tx, ty = snakes.pop()
                maps[tx][ty] = 0

            if len(rotates):
                rotate = rotates.popleft()
                r_rec, r_dir = rotate
                if clock == r_rec:
                    if r_dir == "L":
                        direction -= 1
                        if direction == -1:
                            direction = 3
                    else:
                        direction += 1
                        if direction == 4:
                            direction = 0
                else:
                    rotates.appendleft(rotate)

        else:
            return clock



print(snake(
    map_size=6,
    apples=[[3, 4], [2, 5], [5, 3]],
    rotates=[[3, "D"], [15, "L"], [17, 'D']],
))

print(snake(
    map_size=10,
    apples=[[1, 2], [1, 3], [1, 4], [1, 5]],
    rotates=[[8, "D"], [10, "D"], [11, "D"], [13, "L"]],
))


print(snake(
    map_size=10,
    apples=[[1, 5], [1, 3], [1, 2], [1, 6], [1, 7]],
    rotates=[[8, "D"], [10, "D"], [11, "D"], [13, "L"]],
))
