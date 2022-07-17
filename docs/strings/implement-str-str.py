def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    
    for i in range(len(haystack)):
        if i + len(needle) > len(haystack):
            break
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
            
    return -1