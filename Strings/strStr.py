#Test Cases
haystack = "hello"
needle = "ll"

#output should be 2

def strStr(haystack, needle):
    #first define when empty string
    if len(needle) == 0:
        return 0
    #iterates through each slice of needle length of haystack and checks on each character
    #len(haystack) - len(needle) + 1 basically makes it so that it doesnt iterate through everything
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1 

print(strStr(haystack,needle))