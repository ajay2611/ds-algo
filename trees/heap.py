class Heap():

    def __init__(self, data_list=[]):
        n = len(data_list)
        self.a = [0] + data_list
        for i in range(n // 2, 0, -1):
            self._max_heapify(i, n)

    def __repr__(self):
        return str(self.a[1:])

    def _max_heapify(self, index, n):
        left = index * 2
        right = left + 1
        larger = index
        if left <= n and self.a[left] > self.a[index]:
            larger = left
        else:
            larger = index
        if right <= n and self.a[right] > self.a[larger]:
            larger = right

        if index != larger:
            self.a[larger], self.a[index] = self.a[index], self.a[larger]
            self._max_heapify(larger, n)

    def insert(self, data):
        self.a.append(data)
        n = len(self.a) - 1
        while(n // 2 and self.a[n // 2] < self.a[n]):
            self.a[n // 2], self.a[n] = self.a[n], self.a[n // 2]
            n = n // 2

    def pop(self):
        maximum = self.a[1]
        self.a[1] = self.a.pop(-1)
        self._max_heapify(1, len(a))
        return maximum

    def heapsort(self):
        '''
        Complexity O(nLog(n)) in all cases
        '''
        n = len(self.a) - 1
        for i in range(n, 1, -1):
            self.a[1], self.a[i] = self.a[i], self.a[1]
            n -= 1
            self._max_heapify(1, n)


if __name__ == "__main__":
    l = [4, 3, 7, 1, 8, 5]
    h = Heap(l)
    print(h)
    print('now sorting...')
    h.heapsort()
    print(h)
