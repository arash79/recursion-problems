def convert_string(string):
    if len(string) == 1:
        return int(string)
    else:
        return (int(string[0]) * pow(10, len(string)-1))+convert_string(string[1:])


print(convert_string("1203"))
