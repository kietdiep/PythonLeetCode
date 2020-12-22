
tempArray = [1,2,3,4,5,6,7]
steps = 3


def rotate(tempArray, steps):
    steps %= len(tempArray)
    tempArray[:] = tempArray[-steps:] + tempArray[:-steps]

rotate(tempArray,steps)
print(tempArray)


# splicing
# takes the mod of the length of the array s.t. rotations > size do not matter
# moves the back end to front and front end to back 


