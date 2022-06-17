```python3 
class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 1
        while reader.get(end - 1) < target:
            end = end * 2

        while start + 1 < end:
            mid = (start + end) // 2
            if target > reader.get(mid):
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
