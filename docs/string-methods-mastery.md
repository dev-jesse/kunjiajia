# String Methods Mastery
> "Code is like humor. When you have to explain it, it’s bad." – Cory House

Strings will be commonly used throughout your programming career. In this section, I will explain 10 vital string functions/methods/tricks that everyone should master. These are commonly used and will help simplify code.

## 10 Methods to Master
For the following, let us denote `s` to be variable assigned to the string `"Kunjiajia"`, i.e. `s = "Kunjiajia"`, to provide examples by.
1. Indexing a string - `s[1]  # returns "u"`
2. Slicing a string - `s[1:6]  # returns "unjia"`
3. Getting the length of a string - `len(s)  # return 9`
4. Check if character(s) in string - `"n" in s  # return True`
5. Convert all characters into lowercase - `s.lower()  # s now assigned to "kunjiajia"`
6. Convert all characters into uppercase - `s.upper()  # s now assigned to "KUNJIAJIA"`
7. String concatenation - `s += " is sleepy"  # s now assigned to "Kunjiajia is sleepy`
8. Find first index of substring - `s.find("jia")  # returns 3`
9. Swap the case of characters - `s.swapcase()  # s now assigned to "kUNJIAJIA"`
10. Split by delimiter - `s.split(i)  # returns ["Kunj", "aj", "a"]`

## Application
Chances are, if you are still on my website for interview preparation, that you will have some basic knowledge on string method application. This is not said to discourage individuals who are learning how to program from using my website, but instead for them to read segments of my website to emphasize and reinforce the knowledge they are gaining as a supplementary source of information. With that being said, the following list contains applications on where to use each of the 10 functions/methods/tricks listed above.
1. Indexing a string - Get the first or last or specific character in a string
2. Slicing a string - Need to return a segment of a string or using a sliding window technique
3. Getting the length of a string - Iterating through a string or checking if a pointer reached the end of a string
4. Check if character(s) in string - If the characters are in the string then we know it is a substring of the string
5. Convert all characters into lowercase - Compare two strings together regardless of string case
6. Convert all characters into uppercase - Example presented in 5. can also be applied here
7. String concatenation - Have a result string in which all valid characters can be added to this resultant string
8. Find first index of substring - Use in conjunction with 4 to get where a substring begins
9. Swap the case of characters - Used to modify the case of characters, possibly used in development
10. Split by delimiter - Frequently used to get the values out in [CSVs](https://en.wikipedia.org/wiki/Comma-separated_values) in development