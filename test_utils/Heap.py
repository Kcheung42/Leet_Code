class MinHeap():
    def __init__(self):
        self.heap = []
        self.currentSize = 0

    def heapPush(self, value):
        self.heap.append(value)
        self.currentSize += 1
        self.heapifyUp(self.currentSize - 1)

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def heapPop(self):
        pop = self.heap[0]
        self._swap(0, self.currentSize - 1)
        self.currentSize -= 1
        self.heapifyDown(0)
        return pop

    def heapifyUp(self, i):
        parent = (i-1) // 2
        while parent >= 0:
            if self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
            i = parent
            parent = (parent - 1) // 2

    def getSmallerChild(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if right > self.currentSize - 1:
            return left
        else:
            return left if self.heap[left] < self.heap[right] else right

    def heapifyDown(self, i):
        while 2 * i + 1 <= self.currentSize - 1:
            smaller = self.getSmallerChild(i)
            if self.heap[smaller] < self.heap[i]:
                self._swap(smaller, i)
                i = smaller
            else:
                break
