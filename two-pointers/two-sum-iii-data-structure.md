```python3
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.nums = {}

    def add(self, number):
        self.nums[number] = self.nums.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.nums:
            difference = value - num
            num_cnt = 2 if difference == num else 1
            if difference in self.nums and self.nums[difference] >= num_cnt:
                return True

        return False
```
