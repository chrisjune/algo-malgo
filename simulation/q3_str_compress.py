def str_compress(s: str):
    min_result_count = len(s)
    for l in range(1, len(s) // 2 + 1):
        prev = s[:l]
        count = 1
        result = ""
        for i in range(l, len(s), l):
            nxt = s[i:i + l]
            if prev == nxt:
                count += 1
            else:
                result += str(count) + prev if count > 1 else prev
                prev = nxt
                count = 1
        result += str(count) + prev if count > 1 else prev
        min_result_count = min(min_result_count, len(result))
    print(min_result_count)


str_compress("aabbaccc")
str_compress("ababcdcdababcdcd")
str_compress("abcabcdede")
str_compress("abcabcabcabcdededededede")
str_compress("xababcdcdababcdcd")
