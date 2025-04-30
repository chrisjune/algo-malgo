def mul_add(string: str):
    result = int(string[0])
    for s in string[1:]:
        s = int(s)
        if result in [0,1] or s in [0,1]:
            result += s
        else:
            result *= s
    print(result)

mul_add("02984")
mul_add("567")
mul_add("210")
mul_add("3")
