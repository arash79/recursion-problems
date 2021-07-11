def exponential(base, power):
    if power == 1:
        return base
    else:
        return base*exponential(base, power-1)


print(exponential(2, 3))