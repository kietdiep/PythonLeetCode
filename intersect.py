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

def intersect2(nums1,nums2):
    i = 0
    j = 0
    result = []
    nums1.sort()
    nums2.sort()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result


print(intersect2(nums1,nums2))
