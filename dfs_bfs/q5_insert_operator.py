from itertools import permutations


def insert_operator(numbers, operator):
    operators = []
    for i in range(operator[0]):
        operators.append("+")
    for i in range(operator[1]):
        operators.append("-")
    for i in range(operator[2]):
        operators.append("*")
    for i in range(operator[3]):
        operators.append("/")
    perms = list(permutations(operators))
    min_result = 1e9
    max_result = -1e9
    for perm in perms:
        num = numbers[0]
        for i in range(1, len(numbers)):
            op = perm[i - 1]
            cur = numbers[i]
            if op == "+":
                num += cur
            elif op == "-":
                num -= cur
            elif op == "*":
                num *= cur
            else:
                if num < 0:
                    num = - (abs(num) // cur)
                else:
                    num = num // cur
        min_result = min(min_result, num)
        max_result = max(max_result, num)

    print(min_result, max_result)


def insert_operation_dfs(numbers, operator):
    n = len(numbers)
    add, sub, mul, div = tuple(operator)

    max_val = -1e9
    min_val = 1e9

    def dfs(cur, val):
        nonlocal max_val, min_val, add, sub, mul, div
        if cur == n:
            max_val = max(max_val, val)
            min_val = min(min_val, val)
        else:
            if add > 0:
                add -= 1
                dfs(cur + 1, val + numbers[cur])
                add += 1
            if sub > 0:
                sub -= 1
                dfs(cur + 1, val - numbers[cur])
                sub += 1
            if mul > 0:
                mul -= 1
                dfs(cur + 1, val * numbers[cur])
                mul += 1
            if div > 0:
                div -= 1
                dfs(cur + 1, -(abs(val) // numbers[cur]) if val < 0 else val // numbers[cur])
                div += 1

    dfs(1, numbers[0])
    print(max_val, min_val)


insert_operator(
    numbers=[5, 6],
    operator=[0, 0, 1, 0]
)

insert_operator(
    numbers=[3, 4, 5],
    operator=[1, 0, 1, 0]
)

insert_operator(
    numbers=[1, 2, 3, 4, 5, 6],
    operator=[2, 1, 1, 1]
)

insert_operation_dfs(
    numbers=[5, 6],
    operator=[0, 0, 1, 0]
)
