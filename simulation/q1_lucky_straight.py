def lucky(s: str):
    left = sum([int(i) for i in s[:len(s)//2]])
    right = sum([int(i) for i in s[len(s)//2:]])
    print("LUCKY" if left == right else "READY")

lucky("123402")
lucky("7755")

