def isPal(word):
    if word[:] == word[::-1]:
        return 1
    else:
        return 0

def largestPal(s):
    for size in range(len(s), 1, -1):
        for offset in range(len(s) - size + 1):
            if isPal(s[offset:offset+size]):
                return size
    return 1

s = input()
print(largestPal(s))




