s = "aa"

def isPalindrome(s):
    if len(s) == 0:
        return True
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
    return True 
            

print(isPalindrome(s))

# from test, remove spaces because they do not matter
# only thing needed is that they are letters or numbers

# Attempt 2
# Try to iterate from both sides and skipping the index if it is not a alphanumeric
#           s = race a car
#           i :  1                     first check alphanumeric, if not then add or subtract
#           j :         8              then check equal to each other 