# Array
> “They tried to bury us. They didn’t know we were seeds.” — Mexican Proverb

Arrays are a data structure used to store multiple items in a single variable. They are mutable and can be used for various implementations of other data structures. With such a versatile data structure, comes many questions that can be asked during interviews.

## Two Sum II - Input Array Is Sorted
Problem link: [here](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

### Prompt
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

### Approach
1. Start with two pointers of opposite ends of the array
2. If the sum of values directed by the two pointers are greater than the target, then move the right pointer to the left, if it is less, then move the left pointer to the right. Otherwise, we have found the indexes of the two numbers that add up to the target.

### Solution
```py
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return left, right  # leetcode wants left + 1, right + 1
                                # indexing (i.e. non-zero indexing)
```

### Runtime Analysis
```
Runtime: O(n) the two pointers travel a total of n elements (n = len(numbers))
Space: O(1) no extra storage is being used up with data structures
```

## Kth Largest Element
Problem link: [here](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### Prompt
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

### Approach
1. To find the k-th largest element is the same as finding the len(nums) - k-th smallest element. This is the simple complement rule from statistics.
2. Use the [Quickselect](https://www.geeksforgeeks.org/quickselect-algorithm/) algorithm, derived from Quicksort. 


### Solution
```py
def kth_largest_element(k, nums):
    if not nums or k < 1 or k > len(A):
        return None

    # Finding the k-th largest element is the same as finding the
    # len(nums) - k-th smallest element
    k = len(nums) - k
    return quickselect(k, nums, 0, len(nums) - 1)

def quickselect(k, nums, start, end):
    # K must fall between start and end because of the error checking in the
    # first line of code in kth_largest_element()
    if start == end:
        return nums[k]

    left, right = start, end
    pivot = nums[0]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
    
    # IMPORTANT, SEE VIDEO BELOW FOR EXPLANATION
    if k <= right:
        return quickselect(k, nums, start, right)
    if k >= left:
        return quickselect(k, nums, left, end)
    return nums[k]
```

### Video Walkthrough
<video width="100%" controls>
    <source src="tutorials/kth-largest.mp4" type="video/mp4">
</video>

### Runtime Analysis
```
Runtime: Expected O(n), since T(n) = O(n) + T(n/2) 
Space: O(1), no extra storage being used
```
See [Quicksort analysis](https://iq.opengenus.org/time-and-space-complexity-of-quick-sort/) for better understanding of the algorithm's runtime.