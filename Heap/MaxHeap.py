

class maxHeap:

    def __init__(self) -> None:
        self.items = []

        self.get_left_child_idx = lambda idx: 2 * idx + 1
        self.get_right_child_idx = lambda idx: 2 * idx + 2
        self.get_parent_idx = lambda idx:(idx - 1) // 2

        self.has_left_child = lambda idx: self.get_left_child_idx(idx) < len(self.items)
        self.has_right_child = lambda idx: self.get_right_child_idx(idx) < len(self.items)
        self.has_parent = lambda idx: self.get_parent_idx(idx) >= 0

        self.left_child = lambda idx: self.items[self.get_left_child_idx(idx)]
        self.right_child = lambda idx: self.items[self.get_right_child_idx(idx)]
        self.parent = lambda idx: self.items[self.get_parent_idx(idx)]

    def peek(self) -> int:
        if not self.items:
            raise ValueError('the heap is empty')
        return self.items[0]

    def poll(self) -> int:
        if not self.items:
            raise ValueError('the heap is empty')
        if len(self.items) <= 1:
            return self.items.pop()

        item = self.items[0]
        self.items[0] = self.items.pop()
        self.heapify_down()
        return item

    def swap(self, idx1, idx2) -> None:
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]

    def add(self, item) -> None:
        self.items.append(item)
        self.heapify_up()

    def heapify_up(self) -> None:
        idx = len(self.items)-1
        while self.has_parent(idx) and self.items[idx] > self.parent(idx):
            self.swap(idx, self.get_parent_idx(idx))
            idx = self.get_parent_idx(idx)

    def heapify_down(self) -> None:
        idx = 0
        while self.has_left_child(idx):
            larger_child = self.get_left_child_idx(idx)
            if self.has_right_child(idx) and self.left_child(idx) < self.right_child(idx):
                larger_child = self.get_right_child_idx(idx)

            if self.items[idx] > self.items[larger_child]:
                break
            else:
                self.swap(idx, larger_child)

            idx = larger_child




heap = maxHeap()
heap.add(14)
heap.add(1)
heap.add(20)
heap.add(5)
print(heap.items)
heap.poll()
print(heap.items)
heap.add(100)
heap.add(50)
heap.add(3)
print(heap.items)




