```python3
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
```
