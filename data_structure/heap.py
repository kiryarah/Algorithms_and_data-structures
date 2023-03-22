class HeapMin:

    def __init__(self, value=None):
        self.__heap = []

        if value != None:
            self.push(value)

    def __repr__(self):
        return f'{self.__heap}'

    def push(self, value):
        self.__heap.append(value)
        self._sift_up(len(self.__heap) - 1)

    def pop(self):
        if not self.__heap:
            return None

        min_val = self.__heap[0]
        last_val = self.__heap.pop()

        if self.__heap:
            self.__heap[0] = last_val
            self._sift_down(0)

        return min_val

    def _sift_up(self, index):
        parent = (index - 1) // 2

        if parent >= 0 and self.__heap[parent] > self.__heap[index]:
            self.__heap[parent], self.__heap[index] = self.__heap[index], self.__heap[parent]
            self._sift_up(parent)

    def _sift_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.__heap) and self.__heap[left_child] < self.__heap[smallest]:
            smallest = left_child

        if right_child < len(self.__heap) and self.__heap[right_child] < self.__heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.__heap[smallest], self.__heap[index] = self.__heap[index], self.__heap[smallest]
            self._sift_down(smallest)
