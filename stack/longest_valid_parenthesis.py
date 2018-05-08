def longest_valid_parenthesis(a):
    stack = []
    stack.append(-1)
    res = 0
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) > 0:
                # print(res, i - stack[-1])
                res = max(res, i - stack[-1])
            else:
                stack.append(i)

    return res

if __name__ == '__main__':
    s1 = "((()"
    print(s1)
    print(longest_valid_parenthesis(s1))
    s2 = ")()())"
    print(s2)
    print(longest_valid_parenthesis(s2))
    s3 = "))())((())"
    print(s3)
    print(longest_valid_parenthesis(s3))
