def element_uniqueness(sequence):
    if len(sequence) == 1:
        return True
    else:
        if sequence[0] not in sequence[1:] and element_uniqueness(sequence[1:]) is True:
            return True
        return False


print(element_uniqueness([1, 3, 2, 1]))
