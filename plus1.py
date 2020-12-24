import math

digits = [4,3,2,1]


def plusOne(digits):
    counter = len(digits)-1
    sum = 0
    for num in digits:
        sum = sum + num * 10 ** counter
        if counter > 0:
            counter -= 1
    sum += 1
    counter = len(digits)-1
    array = []
    while counter >= 0:
        temp = math.floor(sum / 10**counter)
        array.append(temp)
        sum = sum % (temp * 10 ** counter)
        counter -= 1
    return array    


print(plusOne(digits))


#  4 3 2 1
#  4 * 10 **3 = 4000
#  3 * 10 ** 2 = 300
#  2 * 10 ** 1 =  20
#  1 * 10 ** 0 =   1


