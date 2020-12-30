#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        if len(nums) == 0: return j
        for i in range(1,len(nums)):
            if nums[j] < nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1


#         [0,1,2,3,4,2,2,3,3,4]
#       j: ^ 
#       i: ^ 