def split(string, delimiter):
    """
    Desc: Python's split function implementation
    :param string: a string
    :return: a list after breaking string on delimiter match
    """
    result_list = []
    if not delimiter:
        raise ValueError("Empty Separator")

    if not string:
        return [string]
    start = 0
    for index, char in enumerate(string):
        if char == delimiter:
            result_list.append(string[start:index])
            start = index + 1
    if start == 0:
        return [string]
    result_list.append(string[start:index + 1])
    
    return result_list

if __name__ == '__main__':
    print(split("abc def xyz", " "))
    print(split("abc", " "))