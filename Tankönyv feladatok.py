def pattern_count(text: object, pattern: object) -> object:
    count = 0
    for elem in range(len(text) - len(pattern)):
        if text[elem:elem + len(pattern)] == pattern:
            count = count + 1
    return count