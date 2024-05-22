class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._percolate_down(0)
        return min_val

    def _percolate_down(self, index):
        while index < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[min_index]:
                min_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[min_index]:
                min_index = right_child_index

            if min_index != index:
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
                index = min_index
            else:
                break

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

# Example usage:
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(1)

    print("Min Heap:")
    print(min_heap.heap)

    print("Extracting min value:", min_heap.extract_min())
    print("Min Heap after extraction:")
    print(min_heap.heap)

    print("Min value in the heap:", min_heap.get_min())
