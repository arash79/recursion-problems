def subset(sequence):
    if len(sequence) == 0:
        return [[]]
    else:
        return subset(sequence[1:])+[[sequence[0]]+items for items in subset(sequence[1:])]


print(subset([1, 2, 3]))
