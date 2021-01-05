s = "      2345 baymax"

def myAtoi(s):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    # upper and lower bounds
    # will use max and min functions to check if they overflow
    
    i = 0
    # iterator variable
    res = 0
    # result variable
    negative = 1
    # variable to keep track of positive or negative sign
    
    while i < len(s) and s[i] == ' ':
        i += 1

    #while loop will increase the iterator to skip empty spaces
    if i < len(s) and s[i] == '-':
        i += 1
        negative = -1 
    #will check for signs and increment to skip that index
    # negative will be multiplied to final value
    elif i<len(s) and s[i] == '+':
        i += 1
    # checks for sign and increments to skip that sign
  
    checker = set('0123456789')
    #contains numbers in a set similar to a regex [0-9]
    #will check to see if the numbers are all numericle 
    while i < len(s) and s[i] in checker:
        res = res * 10 + int(s[i])
        i += 1
    #creates the final number: 123  -> 0 + 1 -> 1 * 10 + 2 -> 12 *10 + 3 = 123
    res = res * negative
    if res < 0:
        return max(res, MIN_INT)
        #if overflows to negative bound, check to see which is greater value
    return min(res, MAX_INT)
    #defaults to smaller value of positive bound

print(myAtoi(s))

# -2147483648 < ___ > 2147483647