```python3
from typing import (
    List,
)

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        # write your code here
        s.sort()

        result = 0
        for i in range(len(s) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if s[left] + s[right] > s[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1

        return result
```
