```python3
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        index = self.binary_search(a, target)
        result = []

        left, right = index - 1, index
        for _ in range(k):
            if left < 0:
                result.append(a[right])
                right += 1
            elif right == len(a):
                result.append(a[left])
                left -= 1
            else:
                if target - a[left] <= a[right] - target:
                    result.append(a[left])
                    left -= 1
                else:
                    result.append(a[right])
                    right += 1

        return result

    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)
```
