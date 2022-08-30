

class MinIntHeap:

    def __init__(self) -> None:

        self.items = []

        self.getLeftChildIndex = lambda parentIdx: 2 * parentIdx + 1
        self.getRightChildIndex = lambda parentIdx: 2 * parentIdx + 2
        self.getParentIndex = lambda childIdx: (childIdx - 1) // 2

        self.hasLeftChild = lambda idx: self.getLeftChildIndex(idx) < len(self.items)
        self.hasRightChild = lambda idx: self.getRightChildIndex(idx) < len(self.items)
        self.hasParent = lambda idx: self.getParentIndex(idx) >= 0

        self.leftChild = lambda idx: self.items[self.getLeftChildIndex(idx)]
        self.rightChild = lambda idx: self.items[self.getRightChildIndex(idx)]
        self.parent = lambda idx: self.items[self.getParentIndex(idx)]

    def swap(self, idx1, idx2) -> None:
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]
    
    def peek(self) -> int:
        if not self.items: raise ValueError('this just won\'t do')
        return self.items[0]

    def poll(self) -> int:
        if not self.items: raise ValueError('items is empty')
        item = self.items[0]
        self.items[0] = self.items.pop()
        self.heapifyDown()
        return item

    def add(self, item) -> None:
        self.items.append(item)
        self.heapifyUp()

    def heapifyUp(self) -> None:
        idx = len(self.items) - 1

        while self.hasParent(idx) and self.parent(idx) > self.items[idx]:
            self.swap(self.getParentIndex(idx), idx)
            idx = self.getParentIndex(idx)

    def heapifyDown(self) -> None:
        idx = 0

        while self.hasLeftChild(idx):
            smaller_child = self.getLeftChildIndex(idx)
            if self.hasRightChild(idx) and self.rightChild(idx) < self.leftChild(idx):
                smaller_child = self.getRightChildIndex(idx)

            if self.items[idx] < self.items[smaller_child]:
                break
            else:
                self.swap(idx, smaller_child)

            idx = smaller_child


heap = MinIntHeap()
heap.add(10)
heap.add(1)
heap.add(2)
heap.add(4)
heap.add(40)
print(heap.items)
heap.poll()
heap.add(35)
print(heap.items)