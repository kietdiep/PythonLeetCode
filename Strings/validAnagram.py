s = "anagram"
t = "nagaram"

def isAnagram(s, t):
    anaDict = dict()
    if len(s) == len(t):
        for char in s:
            if char not in anaDict:
                anaDict[char] = 1
            else: 
                anaDict[char] += 1
        for char in t:
            if char not in anaDict:
                anaDict[char] = 1
            else:
                anaDict[char] -= 1
        for key in anaDict:
            if anaDict[key] != 0:
                return False
        return True
    else:
        return False   

print(isAnagram(s,t))


