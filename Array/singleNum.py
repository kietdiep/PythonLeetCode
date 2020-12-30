def singleNum(nums):
    dic = {}

    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    
    for key, val in dic.items():
        if val == 1:
            return key

print(singleNum([1,2,2,1,3]))
                
# Basic dict answer ----------------------------------------------------

def uniqueNum(nums):
    res = 0
    for num in nums:
        res ^= num
    
    return res


print(uniqueNum([1,2,2,1,3]))

# Better solution with linear runtime complexity ----------------------------------------
# bitwise XOR operator solves it
# anything times itself is 0 but if it only occurs once it will come out as 1

import operator
from functools import reduce

def unique_element(nums):
    return reduce(operator.xor, nums)

print(unique_element([1,2,2,1,3]))

# using library this time to do same thing