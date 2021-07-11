def greatest_common_divisor(a, b):
    if max(a, b) % min(a, b) == 0:
        return b
    return greatest_common_divisor(min(a, b), (max(a, b) % min(a, b)))


print(greatest_common_divisor(8, 12))