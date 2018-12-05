def sum_equals_k(a, k):
    from collections import defaultdict
    d = defaultdict(int)
    count = 0

    for i in a:
        d[i] += 1

    for i in a:
        if 2 * i == k:
            if d[i] > 1:
                count += 1
                d.pop(i)
            else:
                d.pop(i)

        elif k - i in d:
            count += 1
            d.pop(i)
            d.pop(k - i)

    return count

if __name__ == '__main__':
    k = 12
    a = [7, 6, 6, 3, 9, 3, 5, 1]
    print(sum_equals_k(a, k))
    a = [1, 3, 46, 1, 3, 9]
    print(sum_equals_k(a, k))
    a = [6, 6, 6]
    print(sum_equals_k(a, k))
