nums = [0,1,0,3,12]

#Attempt 1
counter = 0
#counting zeros
# use first loop to count how many zeros there are
#insert loop below -----
for num in nums:
    if num == 0:
        counter += 1
# after counting zeroes, use the counter to delete the zeros and append them to end
# append will only delete the first instance so as long as I append as many as I delete it shouuld be fine
# check output after to make sure it works
while counter != 0 :
    nums.remove(0)
    nums.append(0)
    counter -= 1

# print(nums)


#Attempt 2

i = 0
j = 1
while j < len(nums):
    if nums[i] != 0:
        i += 1
        j += 1
    else:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            j += 1


# nums:  [1,0,0,3,12]
#    i:     1
#    j:         2








