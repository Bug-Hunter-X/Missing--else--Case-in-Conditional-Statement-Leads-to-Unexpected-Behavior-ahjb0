def function_with_uncommon_bug_solution(data):
    result = []
    for item in data:
        if item > 5:
            result.append(item * 2)
        elif item == 5:
            result.append(item + 5)
        else:
            result.append(item) # Handle cases where item < 5
    return result