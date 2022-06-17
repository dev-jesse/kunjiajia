```python3
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        if not a:
            return -1

        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < a[0]:
                if a[mid] <= target <= a[end]:
                    start = mid
                else:
                    end = mid
            else:
                if a[start] <= target <= a[mid]:
                    end = mid
                else:
                    start = mid

        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1
