```python3
# Solution 1 - O(nlg n) w/ O(1) space
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        
        return res
        
# Solution 2 - O(n) w/ O(n) space
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums: List[int]) -> int:
        duplicates, result = {}, 0
        for num in nums:
            if num not in duplicates:
                duplicates[num] = True
                nums[result] = num
                result += 1

        return result
```
