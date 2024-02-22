def to_binary(num: int, res: str = ""):
    if num == 0:
        return res

    res = str((num % 2)) + res

    return to_binary(num // 2, res)


print(to_binary(8))
