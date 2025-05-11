from pprint import pprint


def rotate(k):
    # 00 01 02
    # 20 10 00
    key_size = len(k)
    new_k = [[0] * key_size for _ in range(key_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_k[key_size - j - 1][i] = k[i][j]
    pprint(new_k, width=30)
    return new_k


def transpose(k):
    # 00 01 02
    # 22 12 02

    key_size = len(k)
    new_k = [[0] * key_size for _ in range(key_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_k[key_size - j - 1][key_size - i - 1] = k[i][j]

    pprint(new_k, width=30)


def check(l, lock_size):
    for i in range(lock_size, lock_size * 2, 1):
        for j in range(lock_size, lock_size * 2, 1):
            if l[i][j] != 1:
                return False
    return True


def lock_key(k: list, l: list):
    lock_size = len(l)
    key_size = len(k)

    # lock expand
    l3 = [[0] * lock_size * 3 for _ in range(lock_size * 3)]
    for i in range(lock_size):
        for j in range(lock_size):
            l3[lock_size + i][lock_size + j] = l[i][j]
    l = l3

    for _ in range(4):
        for i in range(lock_size, lock_size * 2, 1):
            for j in range(lock_size, lock_size * 2, 1):
                for m in range(key_size):
                    for n in range(key_size):
                        l[i + m][j + n] += k[m][n]
                pprint(l)
                if check(l, lock_size): return True

                # 자물쇠 빼기
                for m in range(key_size):
                    for n in range(key_size):
                        l[i + m][j + n] -= k[m][n]
        k = rotate(k)
    return False


print(lock_key([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
