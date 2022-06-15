```python3
from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k: int, nums: List[int]) -> int:
        return self.quickselect(k - 1, nums, 0, len(nums) - 1)

    def quickselect(self, k, nums, start, end):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        if k <= right:
            return self.quickselect(k, nums, start, right)
        if k >= left:
            return self.quickselect(k, nums, left, end)
        return nums[k]
```
