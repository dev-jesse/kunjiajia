```python3
# Solution 1 - Sift down (Faster since we remove n // 2 elements)
from typing import (
    List,
)

class Solution:
    """
    @param a: Given an integer array
    @return: nothing
    """
    def heapify(self, a: List[int]):
        for i in (range(len(a) // 2, -1, -1)):
            self.sift_down(a, i)

    def sift_down(self, a, index):
        while index < len(a):
            left, right = index * 2 + 1, index * 2 + 2
            min_index = index
            if left < len(a) and a[left] < a[min_index]:
                min_index = left
            if right < len(a) and a[right] < a[min_index]:
                min_index = right

            if min_index == index:
                break

            a[min_index], a[index] = a[index], a[min_index]
            index = min_index            
            
# Solution 2 - Sift up
from typing import (
    List,
)

class Solution:
    """
    @param a: Given an integer array
    @return: nothing
    """
    # OBSERVATION: Sift up goes from top-down, it won't work in reverse
    def heapify(self, a: List[int]):
        # Can start from the left child of root since root has no parent
        for i in range(1, len(a)):
            self.sift_up(a, i)

    def sift_up(self, a, index):
        parent = (index - 1) // 2
        while parent >= 0 and a[index] < a[parent]:
            a[index], a[parent] = a[parent], a[index]
            index = parent
            parent = (index - 1) // 2
```
