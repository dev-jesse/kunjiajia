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