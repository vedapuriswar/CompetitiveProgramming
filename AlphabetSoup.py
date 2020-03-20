def swap(string):
    l = list(string)
    li = sorted(list(string.lower()))
    caps = []
    new_string = ''
    for char in l:
        if char.isupper():
            caps.append(char)
    for char in li:
        if caps.count(char.upper()) is not 0:
            new_string += str(char.upper)
            caps.pop(caps.index(char.upper()))
        else:
            new_string += char
    return new_string
