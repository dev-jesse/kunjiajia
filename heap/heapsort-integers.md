```python3
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
    # Step to implement heapsort:
    # 1. First heapify the list, so that you have a built heap
    # 2. Swap the first and last element of the list, then sift down with
    # all but the last element
    # 3. Repeat this process and the back of the list will always be the
    # sorted areas

    # Example:
    # [2, 3, 5] -- heapify --> [5, 2, 3] -- swap --> [3, 2, 5]
    # -- sift down 3 --> [3, 2, 5] -- swap with n - 1 -- > [2, 3, 5]

        self.heapify(a)
        n = len(a)
        # Just need n - 1 elements since the n-th (last) element will not do
        # anything (i.e. swap with itself)
        for i in range(n - 1):
            a[0], a[n - i - 1] = a[n - i - 1], a[0]
            self.sift_down(a, 0, n - i - 1)

    def heapify(self, a):
        for i in range(len(a) // 2, -1, -1):
            self.sift_down(a, i, len(a))

    def sift_down(self, a, index, end):
        while index < end:
            left, right = index * 2 + 1, index * 2 + 2
            max_index = index
            if left < end and a[left] > a[max_index]:
                max_index = left
            if right < end and a[right] > a[max_index]:
                max_index = right
            
            if max_index == index:
                break

            a[index], a[max_index] = a[max_index], a[index]
            index = max_index
```
