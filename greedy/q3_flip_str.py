def flip_str(string: str):
    first = string[0]
    count0, count1 = 0, 0
    for second in string[1:]:
        if first != second:
            if second == "0":
                count1 += 1
            else:
                count0 += 1
            first = second
    if first == "0":
        count0 += 1
    else:
        count1 += 1

    print(min(count0, count1))


flip_str("0001100")
flip_str("0101")
flip_str("1010")
flip_str("10101")
flip_str("01010")
