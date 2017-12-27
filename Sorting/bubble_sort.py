def bubble_sort(a):
    '''
    Complexity O(n^2) in all cases
    '''
    n = len(a) - 1
    for i in range(n):
        for j in range(0, n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == "__main__":
    a = [8,5,3,1,9,6,0,7,4,2,5]
    print('unsorted:', a)
    bubble_sort(a)
    print('sorted:', a)
