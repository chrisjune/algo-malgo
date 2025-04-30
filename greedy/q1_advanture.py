def adventure(n: list[int]):
    n.sort()
    # 1 2 2 2 3
    # 2 2 3 3
    # 3 3

    sub_len = 0
    groups = 0
    for i in n:
        sub_len += 1
        if sub_len >= i:
            groups += 1
            sub_len = 0
        print(i)
    print(groups)

adventure([2,3,1,2,2])