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
    pivot = nums[(start + end) // 2]
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

### Example Walkthrough


### Runtime Analysis
```
Runtime: Expected O(n), since T(n) = O(n) + T(n/2) 
Space: O(1), no extra storage being used
```
See [Quicksort analysis](https://iq.opengenus.org/time-and-space-complexity-of-quick-sort/) for better understanding of the algorithm's runtime.

## Two Sum - Unique pairs
Problem link: [here](https://www.lintcode.com/problem/587/)

### Prompt
Description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example 1:
```
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47
```

Example 2:
```
Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
```
### Approach
1. Sort the array
2. Use two pointers, one at the start of the array and the other at the end of the array
3. If the sum of the numbers at the two pointers is greater than our target, the move the right pointer to the left to decrease the sum. If the sum of the two pointers is less than our target, then move our left pointer to the right to increase the sum. Otherwise, the sum of the numbers at the two pointers is equal to our target, so increment a result counter by one.

### Solution
```py
def two_sum6(nums, target):
    # Sort so we can use two pointers
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        if nums[left] + nums[right] == target:
            count += 1
            left += 1
            right -= 1

            # Skip the number if it is the same, since we only
            # want unique pairs, this way is a little more
            # complicated, and if you want you can just keep a 
            # last_pair variable instead
            while left < right and nums[left - 1] == nums[left]:
                left += 1
            while left < right and nums[right + 1] == nums[right]:
                right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return count
```

### Runtime Analysis
```
Runtime: O(n), all elements are 'touched' once by a pointer
Space: O(1), since no extra storage is being used
```