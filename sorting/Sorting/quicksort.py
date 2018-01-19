def partition(a, start, end):
    pivot = a[start]
    smaller_index = start
    for i in range(start + 1, end + 1):
        if a[i] < pivot:
            smaller_index += 1
            a[i], a[smaller_index] = a[smaller_index], a[i]

    a[start], a[smaller_index] = a[smaller_index], pivot
    return smaller_index


def _quicksort(a, start, end):
    if start < end:
        pivot = partition(a, start, end)
        _quicksort(a, start, pivot - 1)
        _quicksort(a, pivot + 1, end)


def quicksort(a):
    '''
    Best = Average = O(nlog(n)); Worst = O(n^2).
        '''
    _quicksort(a, 0, len(a) - 1)


if __name__ == "__main__":
    a = [8,5,3,1,9,6,0,7,4,2]
    print('unsorted:', a)
    quicksort(a)
    print('sorted:', a)
