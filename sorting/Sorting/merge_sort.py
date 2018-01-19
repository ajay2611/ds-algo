def merge(a, start, mid, end):
    p = start
    q = mid + 1
    temp = []
    while p <= mid and q <= end:
        if a[p] < a[q]:
            temp.append(a[p])
            p += 1
        else:
            temp.append(a[q])
            q += 1

    if p <= mid:
        temp += a[p:mid + 1]
    if q <= end:
        temp += a[q:end + 1]

    counter = 0
    while start <= end:
        a[start] = temp[counter]
        start += 1
        counter += 1


def _mergesort(a, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    _mergesort(a, start, mid)
    _mergesort(a, mid + 1, end)
    merge(a, start, mid, end)


def merge_sort(a):
    start = 0
    end = len(a) - 1
    _mergesort(a, start, end)

if __name__ == "__main__":
    a = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    print('unsorted:', a)
    merge_sort(a)
    print('sorted:', a)
