```python3
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return left + 1, right + 1 
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
```
