def min_max_finder(sequence):
    if len(sequence) == 1 or len(sequence) == 2:
        return max(sequence), min(sequence)
    else:
        maximum = max(sequence[0], min_max_finder(sequence[1:])[0])
        minimum = min(sequence[0], min_max_finder(sequence[1:])[1])
        return maximum, minimum


print(min_max_finder([5, 3, 10, 1, 4]))