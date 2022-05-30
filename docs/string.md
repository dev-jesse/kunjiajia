# String
> "The higher we soar, the smaller we seem to those who cannot fly." - Nietzsche

A strings are a sequence of characters As one of the most commonly used data types, they will be tested in interviews through a variety of questions that make use of different algorithms.
## Valid Palindrome
Problem link: [here](https://leetcode.com/problems/valid-palindrome/)

### Prompt
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
```
Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
```

Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Approach
1. Use the two pointers technique, with pointers on opposite sides of the string.
2. Iterate left and right pointers towards the middle until valid characters are found
3. Compare the two valid characters (without case) located at the pointers, and if they are different then the string is not a palindrome, otherwise move the pointers in towards the middle using idea 2. of the approach.
4. If the left and right pointers meet or pass each other, then the string is a palindrome as we have iterated the entire string and all valid characters are paired.

### Solution
```py
def is_palindrome(string):
    if string is None:
        return False

    left, right = 0, len(string) - 1
    while left < right:
        # Notice for the while statements all must check left < right since 
        # we are moving a pointer inside the while loops
        while left < right: and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Use .lower() method to compare characters regardless of case
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True
```

### Runtime Analysis


## Valid Palindrome II
Problem link: [here](https://leetcode.com/problems/valid-palindrome-ii/)

### Prompt
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
```
Input: s = "aba"
Output: true
```

Example 2:
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

Example 3:
```
Input: s = "abc"
Output: false
```

### Approach
1. Use the two pointers technique, with pointers on opposite sides of the string.
2. Iterate left and right pointers towards the middle until the characters do not match.
3. If the pointers have met or crossed at this point, then we have a palindrome so return True. Otherwise, use a helper check if a palindrome exists if the left pointer is moved one more to the right or if the right pointer is moved one more to the left.

### Solution
```py
def valid_palindrome(string):
    if string is None:
        return False
    
    left, right = find_difference(string, 0, len(string) - 1)
    if left >= right:
        # If left and right have met or crossed paths
        # then all characters have been checked
        return True

    # Check if the deletion of any of the characters at either
    # of the pointers will result in a palindrome
    return is_palindrome(string, left + 1, right) or \
    is_palindrome(string, left, right - 1)
    
def find_difference(string, left, right):
    while left < right and string[left] == string[right]:
        # Iterate and compare characters are the same
        left += 1
        right -= 1
    return left, right

def is_palindrome(string, left, right):
    left, right = find_difference(string, left, right)
    return left >= right
```

### Runtime Analysis