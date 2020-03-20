def first_recurring_character(string):
    counts = dict()
    for char in string:
        if char in counts:
            return char
        counts[char] = 1
    return None
