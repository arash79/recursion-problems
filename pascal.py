def pascal(n, preliminary_row=None):
    if preliminary_row is None:
        preliminary_row = [[1]]
    if n == 1:
        return preliminary_row
    else:
        new_line = [1]+[sum(i) for i in zip(preliminary_row[-1], (preliminary_row[-1])[1:])]+[1]
        return pascal(n-1, preliminary_row+[new_line])


print(pascal(3))
