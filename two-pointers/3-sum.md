```python3
from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        result = []

        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            left, right = i + 1, len(numbers) - 1
            self.get_triplets(numbers, -numbers[i], left, right, result)

        return result

    def get_triplets(self, numbers, target, left, right, result):
        while left < right:
            if numbers[left] + numbers[right] == target:
                result.append([-target, numbers[left], numbers[right]])
                left, right = left + 1, right - 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```
