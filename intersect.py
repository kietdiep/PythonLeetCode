nums1 =  [1,2,1]
nums2 = [2,2]

def intersect(nums1, nums2):
    array = []

    if len(nums1) > len(nums2):
        for nums in nums2:
            if nums in nums1:
                array.append(nums)
    else:
        for nums in nums1:
            if nums in nums2:
                array.append(nums)
    return array
    
    
print(intersect(nums1,nums2))
# initial attempt somewhat works but fails to work when the smaller array has multiple intersections


