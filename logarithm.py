def integer_part(argument, base):
    if argument < base:
        return 0
    else:
        return 1+integer_part((argument/base), base)


print(integer_part(30, 2))
