def select_bowling(balls: list[int]):
    balls.sort()
    weights = [0] * 11
    for ball in balls:
        weights[ball] += 1
    # 1 3 2 3 2
    # 1 2 2 3 3
    result = 0
    length = len(balls)

    # 0 1 2 2
    # 1 2 2
    for w in weights:
        if w:
            result += w * (length - w)
            length = length - w
    print(result)


select_bowling([1, 3, 2, 3, 2])
select_bowling([1, 5, 4, 3, 2, 4, 5, 2])
