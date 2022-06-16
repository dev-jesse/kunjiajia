```python3
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        positives = len(a) - self.partition(a, 0)
        negatives = len(a) - positives
        left = 1 if negatives >= positives else 0
        right = len(a) - 2 if positives >= negatives else len(a) - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left, right = left + 2, right - 2


    def partition(self, a, k):
        left, right = 0, len(a) - 1
        while left <= right:
            while left <= right and a[left] < k:
                left += 1
            while left <= right and a[right] >= k:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left, right = left + 1, right - 1

        return left
```
