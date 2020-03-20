def longest(string):
    count = 0
    max_count = 0
    prev_char = max_char = ''
    for character in string:
        if prev_char is character:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = character
        prev_char = character
    return max_char, max_count
