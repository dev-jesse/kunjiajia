```python3
from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        start, end = 1, len(a) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < a[mid + 1]:
                start = mid
            elif a[mid] < a[mid - 1]:
                end = mid
            else:
                return mid

        if a[start] > a[end]:
            return start
        return end
