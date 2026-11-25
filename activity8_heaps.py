import heapq
import random


# ==========================================
# ACTIVITY 1: MIN-HEAP
# ==========================================

class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def extract(self):
        if len(self.heap) == 0:
            return None

        smallest = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last
            self.heapify_down(0)

        return smallest

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def size(self):
        return len(self.heap)


# ==========================================
# ACTIVITY 2: MAX-HEAP
# ==========================================

class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def extract(self):
        if len(self.heap) == 0:
            return None

        largest = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last
            self.heapify_down(0)

        return largest

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def size(self):
        return len(self.heap)


# ==========================================
# ACTIVITY 3: HEAP SORT
# ==========================================

def heap_sort(numbers):

    heap = MaxHeap()

    for number in numbers:
        heap.insert(number)

    result = []

    while heap.size() > 0:
        result.append(heap.extract())

    result.reverse()

    return result


# ==========================================
# ACTIVITY 4: KTH LARGEST
# ==========================================

def kth_largest(numbers, k):

    if k < 1 or k > len(numbers):
        return None

    heap = MinHeap()

    for number in numbers:
        heap.insert(number)

        if heap.size() > k:
            heap.extract()

    return heap.peek()


# ==========================================
# ACTIVITY 5: MERGE K SORTED ARRAYS
# ==========================================

def merge_arrays(arrays):

    heap = []
    result = []

    for i in range(len(arrays)):
        if len(arrays[i]) > 0:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    while heap:

        value, array_index, element_index = heapq.heappop(heap)

        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heapq.heappush(
                heap,
                (next_value, array_index, next_index)
            )

    return result


# ==========================================
# ACTIVITY 6: PRIORITY SCHEDULER
# ==========================================

def priority_scheduler(jobs):

    priority_queue = []

    for order, (job, priority) in enumerate(jobs):
        heapq.heappush(
            priority_queue,
            (-priority, order, job)
        )

    release_order = []

    while priority_queue:

        priority, order, job = heapq.heappop(priority_queue)

        release_order.append(job)

        print("Released Job:", job, "| Priority:", -priority)

    return release_order


# ==========================================
# TESTING ACTIVITIES 1 AND 2
# ==========================================

def test_heaps():

    print("\nHEAP TESTING")

    test_cases = {
        "Empty": [],
        "Single Element": [10],
        "Duplicates": [5, 3, 5, 2, 3],
        "Random": [random.randint(1, 100) for i in range(15)]
    }

    for name, values in test_cases.items():

        min_heap = MinHeap()
        max_heap = MaxHeap()

        for value in values:
            min_heap.insert(value)
            max_heap.insert(value)

        min_result = []
        max_result = []

        while min_heap.size() > 0:
            min_result.append(min_heap.extract())

        while max_heap.size() > 0:
            max_result.append(max_heap.extract())

        print("\nTest:", name)
        print("Input:", values)
        print("Min-Heap:", min_result)
        print("Max-Heap:", max_result)

        print("Min-Heap Verified:", min_result == sorted(values))
        print("Max-Heap Verified:", max_result == sorted(values, reverse=True))


# ==========================================
# TESTING ACTIVITY 3
# ==========================================

def test_heap_sort():

    print("\nHEAP SORT TESTING")

    test_cases = [
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
        [],
        [10],
        [random.randint(1, 100) for i in range(15)]
    ]

    for values in test_cases:

        result = heap_sort(values)

        print("Original:", values)
        print("Sorted:", result)
        print("Verified:", result == sorted(values))
        print()


# ==========================================
# TESTING ACTIVITY 4
# ==========================================

def test_kth_largest():

    print("\nKTH LARGEST TESTING")

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([10], 1),
        ([5, 5, 3, 2], 2),
        ([], 1),
        ([random.randint(1, 100) for i in range(15)], 3)
    ]

    for numbers, k in test_cases:

        result = kth_largest(numbers, k)

        if 1 <= k <= len(numbers):
            expected = sorted(numbers, reverse=True)[k - 1]
        else:
            expected = None

        print("Numbers:", numbers)
        print("K:", k)
        print("Kth Largest:", result)
        print("Verified:", result == expected)
        print()


# ==========================================
# TESTING ACTIVITY 5
# ==========================================

def test_merge_arrays():

    print("\nMERGE K SORTED ARRAYS TESTING")

    test_cases = [
        [[1, 4, 7], [2, 5, 8, 10], [3, 6, 9]],
        [[], [], []],
        [[5], [], []],
        [[1, 2, 2], [2, 3], [3, 4]],
        [
            sorted([random.randint(1, 50) for i in range(5)]),
            sorted([random.randint(1, 50) for i in range(7)]),
            sorted([random.randint(1, 50) for i in range(4)])
        ]
    ]

    for arrays in test_cases:

        result = merge_arrays(arrays)
        expected = sorted(sum(arrays, []))

        print("Arrays:", arrays)
        print("Merged:", result)
        print("Verified:", result == expected)
        print()


# ==========================================
# TESTING ACTIVITY 6
# ==========================================

def test_priority_scheduler():

    print("\nPRIORITY SCHEDULER TESTING")

    test_cases = [
        [],
        [("Job A", 5)],
        [("Job A", 3), ("Job B", 3), ("Job C", 1)],
        [
            ("Job A", 2),
            ("Job B", 5),
            ("Job C", 1),
            ("Job D", 4),
            ("Job E", 3)
        ],
        [
            (f"Job {i}", random.randint(1, 10))
            for i in range(15)
        ]
    ]

    for jobs in test_cases:

        print("\nJobs:", jobs)

        result = priority_scheduler(jobs)

        expected = [
            job for job, priority in
            sorted(jobs, key=lambda x: -x[1])
        ]

        print("Release Order:", result)
        print("Verified:", result == expected)


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("ACTIVITY 8: HEAPS AND PRIORITY QUEUES")

    # Activity 1
    print("\nACTIVITY 1: MIN-HEAP")

    values = [5, 9, 11, 14, 19, 17, 18, 13]

    min_heap = MinHeap()

    for value in values:
        min_heap.insert(value)

    print("Inserted:", values)
    print("Heap:", min_heap.heap)
    print("Peek:", min_heap.peek())
    print("Size:", min_heap.size())

    extracted = []

    while min_heap.size() > 0:
        extracted.append(min_heap.extract())

    print("Extracted:", extracted)

    # Activity 2
    print("\nACTIVITY 2: MAX-HEAP")

    max_heap = MaxHeap()

    for value in values:
        max_heap.insert(value)

    print("Inserted:", values)
    print("Heap:", max_heap.heap)
    print("Peek:", max_heap.peek())
    print("Size:", max_heap.size())

    extracted = []

    while max_heap.size() > 0:
        extracted.append(max_heap.extract())

    print("Extracted:", extracted)

    # Activity 3
    print("\nACTIVITY 3: HEAP SORT")

    numbers = [4, 10, 3, 5, 1]

    print("Original:", numbers)
    print("Sorted:", heap_sort(numbers))

    # Activity 4
    print("\nACTIVITY 4: KTH LARGEST")

    numbers = [3, 2, 1, 5, 6, 4]
    k = 2

    result = kth_largest(numbers, k)

    print("Numbers:", numbers)
    print("K:", k)
    print("Kth Largest:", result)
    print("Verified:", result == sorted(numbers, reverse=True)[k - 1])

    # Activity 5
    print("\nACTIVITY 5: MERGE K SORTED ARRAYS")

    arrays = [
        [1, 4, 7],
        [2, 5, 8, 10],
        [3, 6, 9]
    ]

    print("Original Arrays:", arrays)
    print("Merged Array:", merge_arrays(arrays))

    # Activity 6
    print("\nACTIVITY 6: PRIORITY SCHEDULER")

    jobs = [
        ("Job A", 2),
        ("Job B", 5),
        ("Job C", 1),
        ("Job D", 4),
        ("Job E", 3)
    ]

    print("Jobs:", jobs)

    release_order = priority_scheduler(jobs)

    print("Release Order:", release_order)

    # Additional Testing
    test_heaps()
    test_heap_sort()
    test_kth_largest()
    test_merge_arrays()
    test_priority_scheduler()

    print("\nALL ACTIVITIES AND TESTS COMPLETED!")
