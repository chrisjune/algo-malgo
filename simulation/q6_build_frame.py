dx = [0, 1]
dy = [1, 0]


def build_frame(frames):
    result = []
    # 0 =기둥, 1=보

    for frame in frames:
        x, y = frame[0], frame[1]
        t = frame[2]
        creating = frame[3]

        nx = x + dx[t]
        ny = y + dy[t]
        f = [frame[0], frame[1], frame[2]]

        if creating:
            if t == 0:
                if 0 <= nx <= 100 and 0 < ny <= 100 and (y == 0 or [x - 1, y, 1] in result or [x, y, 1] in result or [x, y - 1, 0] in result):
                    result.append(f)
            else:
                if 0 < nx <= 100 and 0 <= ny <= 100 and (
                        [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result)):
                    result.append(f)
        else:
            if f in result:
                prev_result_len = len(result)
                result.remove(f)
                next_result_len = len(re_install_frame(result))
                if prev_result_len != next_result_len + 1:
                    result.append(f)

    print(sorted(result))


def re_install_frame(frames):
    result = []
    for frame in frames:
        x, y = frame[0], frame[1]
        t = frame[2]

        nx = x + dx[t]
        ny = y + dy[t]
        f = [frame[0], frame[1], frame[2]]
        if t == 0:
            if 0 <= nx <= 100 and 0 < ny <= 100 and (y == 0 or [x - 1, y, 1] in frames or [x, y, 1] in frames or [x, y - 1, 0] in frames):
                result.append(f)
        else:
            if 0 < nx <= 100 and 0 <= ny <= 100 and (
                    [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames)):
                result.append(f)
    return result


# build_frame(
# [    [0, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0]]
# )

# build_frame(
#     [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# )

build_frame(
    [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
)
