```python3
class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        partition_index = self.partition(a, 0)
        left = 1 if partition_index >= (len(a) / 2) else 0
        right = len(a) - 2 if partition_index <= (len(a) / 2) else len(a) - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left, right = left + 2, right - 2
        return a

    def partition(self, a, pivot):
        left, right = 0, len(a) - 1
        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] >= pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left, right = left + 1, right - 1
        return left
```
