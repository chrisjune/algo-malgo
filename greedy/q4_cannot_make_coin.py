# 이해 아직 안됨
def cannot_make_coin(coins: list[int]):
    coins.sort()
    # 1 2 3 8
    target = 1
    for coin in coins:
        if target < coin:
            print(target)
            break
        target += coin


cannot_make_coin([1,2,3,8])
cannot_make_coin([3,2,1,1,9])