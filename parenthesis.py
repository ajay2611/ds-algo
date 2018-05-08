# https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/


def print_all_parenthesis(n):
    """
    :param: integer number of balanced parenthesis needed
    """
    if n > 0:
        s = []

    def _print_parenthesis(n, left, right, s):
        """
        :param n: number of balanced parenthesis
        :param left: number of open brackets
        :param right: number of close brackets
        :param s: list for storing brackets
        """

        if right == n:
            print("".join(s))
            return

        if left > right:
            s.append('}')
            _print_parenthesis(n, left, right + 1, s)
            s.pop()

        if left < n:
            s.append('{')
            _print_parenthesis(n, left + 1, right, s)
            s.pop()

    return _print_parenthesis(n, 0, 0, s)

if __name__ == '__main__':
    print_all_parenthesis(3)
