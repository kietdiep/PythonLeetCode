nums = [-3,4,3,90]
target = 0
#Attempt 1 ------------------------------------------------------
def twoSum(nums, target):
    i = 0
    j = len(nums)-1
    while j > 0:
        if nums[i] > target:
            i += 1
        elif nums[j] > target:
            j -= 1
        else:
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                i += 1

# declare an index for beginning and end
# check if values @index of i and j are greater than target
# if greater, move inward until both are smaller than target

#Notes: Doesnt work, only occasionally, will improve on if new things in future

#Attempt 2 -------------------------------------------------------
def twoSums(nums,target):
    
    complementMap = dict()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            return [complementMap[num], i]
        else:
            complementMap[complement] = i
        
print(twoSums(nums, target))

# Instead of keeping track of front and end
# create a map of complements and just iterate through until i find a complement
# Original method I was thinking of could only work if I sort the list first