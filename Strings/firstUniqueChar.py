s = "loveleetcode"

def firstUniqChar(s):
    characters = dict()
    for char in s:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    for char in characters:
        if characters[char] == 1:
            return s.find(char)
    return -1
print(firstUniqChar(s))

# runtime 108 ms
# memory usage 14.2 MB

# runtimes beats 62.50% of python3 submissions
# memory usage beats 92.84% of python3 submissions