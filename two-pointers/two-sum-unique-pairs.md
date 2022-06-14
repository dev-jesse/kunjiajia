```python3
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            if nums[left] + nums[right] == target:
                res += 1
                left, right = left + 1, right - 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return res
```
