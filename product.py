def product(m, n):
    if n == 1:
        return m
    else:
        return m+product(m, n-1)


print(product(3, 4))