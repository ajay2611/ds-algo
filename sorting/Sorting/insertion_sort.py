def insertion_sort(a):
    '''
    Best O(n); Average O(n^2); Worst O(n^2)
    '''
    for i in range(1, len(a)):
        temp = a[i]
        k = i
        while (k > 0 and temp < a[k - 1]):
            a[k] = a[k - 1]
            k -= 1
        a[k] = temp


if __name__ == "__main__":
    a = [8,5,3,1,9,6,0,7,4,2,5]
    print('unsorted:', a)
    # bubble_sort(a)
    insertion_sort(a)
    print('sorted:', a)
