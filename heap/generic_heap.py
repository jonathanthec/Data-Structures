class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        self.storage.append(-1)
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        value = self.storage[1]
        self.swap(1, len(self.storage) - 1)
        self.storage.pop()
        self._sift_down(1)
        return value

    def get_priority(self):
        return self.storage[1]

    def get_size(self):
        return len(self.storage) - 1

    def _bubble_up(self, index):
        if not self.comparator:
            while int(index/2) > 0 and self.storage[index] >= self.storage[int(index/2)]:
                self.swap(index, int(index/2))
                index = int(index/2)
        elif self.comparator(0, 1):
            while int(index/2) > 0 and self.storage[index] <= self.storage[int(index/2)]:
                self.swap(index, int(index/2))
                index = int(index/2)

    def _sift_down(self, index):
        if not self.comparator:
            while 2*index+1 < len(self.storage) or 2*index < len(self.storage):
                if 2*index+1 < len(self.storage) and self.storage[2*index+1] >= self.storage[2*index]:
                    index_max = 2*index+1
                else:
                    index_max = 2*index
                self.swap(index, index_max)
                index = index_max
        elif self.comparator(0, 1):
            while 2*index < len(self.storage) or 2*index+1 < len(self.storage):
                if 2*index+1 < len(self.storage) and self.storage[2*index] >= self.storage[2*index+1]:
                    index_min = 2*index+1
                else:
                    index_min = 2*index
                self.swap(index, index_min)
                index = index_min

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp


def main():
    my_heap = Heap()
    my_heap.insert(6)
    my_heap.insert(8)
    my_heap.insert(10)
    my_heap.insert(9)
    my_heap.insert(1)
    my_heap.insert(9)
    my_heap.insert(9)
    my_heap.insert(5)
    my_heap.delete()
    my_heap.delete()
    my_heap.delete()
    my_heap.delete()
    print(my_heap.storage[1:])


if __name__ == '__main__':
    main()
