def longest_valid_parenthesis(a):
    stack = []
    # initial index
    stack.append(-1)
    res = 0
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(a) > 0:
                print(res, i - stack[-1])
                res = max(res, i - stack[-1])
            else:
                stack.append(i)

    return res

s = "(((()))"
print(s)
print(longest_valid_parenthesis(s))
