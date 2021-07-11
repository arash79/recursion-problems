def palindrome(string):
    if len(string) == 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
    return False


print(palindrome("racecar"))