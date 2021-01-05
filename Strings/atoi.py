s = "      2345 baymax"

def myAtoi(s):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    
    
    i = 0
    res = 0
    negative = 1
    while i < len(s) and s[i] == ' ':
        i += 1

    if i < len(s) and s[i] == '-':
        i += 1
        negative = -1
    elif i<len(s) and s[i] == '+':
        i += 1
    #check number 0-9
    checker = set('0123456789')
    while i < len(s) and s[i] in checker:
        res = res * 10 + int(s[i])
        i += 1
    
    res = res * negative
    if res < 0:
        return max(res, MIN_INT)
    return min(res, MAX_INT)

print(myAtoi(s))

# -2147483648 < ___ > 2147483647