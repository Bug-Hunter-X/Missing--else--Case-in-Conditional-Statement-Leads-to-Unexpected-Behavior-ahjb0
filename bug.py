def function_with_uncommon_bug(data):
    result = []
    for item in data:
        if item > 5:
            result.append(item * 2)
        elif item == 5:
            result.append(item + 5)
        # Missing 'else' case, this will be problem for item < 5
    return result