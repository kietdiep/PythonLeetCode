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




#                   [4,1,2,1,2]
# sorted            [1,1,2,2,4]
# start ------------>  *
# end -------------------->*