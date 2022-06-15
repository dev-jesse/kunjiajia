```python3
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        nums.sort()

        left, right = 0, len(nums) - 1
        result = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                result += right - left
                left += 1
            else:
                right -= 1

        return result
```
