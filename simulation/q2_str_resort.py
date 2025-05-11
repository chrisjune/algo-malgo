def str_resort(s: str):
    str_part = []
    number_part = 0
    for i in s:
        if 65 <= ord(i) <=90:
            str_part.append(i)
        else:
            number_part+=int(i)
    str_part.sort()
    print("".join(str_part)+str(number_part))
str_resort("K1KA5CB7")
str_resort("AJKDLSI412K4JSJ9D")