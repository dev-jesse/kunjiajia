# 12 Tricks to Improve Code Quality
> "The best error message is the one that never shows up." - Thomas Fuchs

As discussed in the previous section, code quality is vital in preventing bugs. During development, when other coworkers use your code, you want them be able to understand and use you code and easily as possible. Hence, in this post I will talk about some quick changes you can make to improve coding quality.

## Coding style
- Add spaces in between mathematical operations. This will make the code much easier to read, `i = i + 1` is much better than some `i=i+1` congested mess. However, for single operators, do not add any spaces. Some example syntax for this include `i++`, `!flag`, etc.
- Add spaces between `if`, `while` and `for` statements.
- Separate code logic using new lines.
- After commas and semi-colons add spaces. This is common is for loops like, `for (int i = 0; i < CONDITION; i++`.

## Readability
- Use clear naming conventions with one or two letters for functions and variables, i.e. `isPalindrome` is a good name for a function to check if a string is a palindrome.
- Don't use over 3 indentations when writing functions.
- Use helper functions to simplify code.
- Use `continue` more than `if`, this will make the code look cleaner, for example,
```py
while ...
    if not CONDITION1:
        continue
    if not CONDITION2:
        continue

    ... lines of code ...
    ... lines of code ...
    ... lines of code ...
```

## Bug Free
- Check for empty objects, as these are often source for bugs, i.e. `if s == None: DO SOMETHING`.
- Make sure that indexing still falls within range. For programming languages such as python, make sure we are not negative indexing something that we do not intend to. This is usually checked in a loop where we index into an object, i.e. `while left >= 0 and right < len(...) and CONDITION`.
- Before attempting to access a object method or attribute, check that we are currently working on an object. For example, if we are accessing the value attribute on a node in a linked list, check that `if node and node.val` not just `if node.val`.
- Avoid the usage of global variables.