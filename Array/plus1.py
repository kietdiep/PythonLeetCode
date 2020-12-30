import math

digits = [9,9,9,9,9]


def plusOne(digits):
    if len(digits) == 1 and digits[0] == 9:
        return [1,0]
    counter = len(digits)-1
    sum = 0
    for num in digits:
        sum = sum + num * 10 ** counter
        print(f'added sum is {sum}')
        if counter > 0:
            counter -= 1
    sum += 1
    print(f'sum + 1: {sum}')
    counter = len(str(sum))-1
    print(f'counter: {counter}')
    array = []
    while counter >= 0:
        temp = math.floor(sum / 10**counter)
        print(f'temp: {temp}')
        array.append(temp)
        sum = sum % (temp * 10 ** counter)
        print(sum)
        counter -= 1
    return array    


#print(plusOne(digits))


#  4 3 2 1
#  4 * 10 **3 = 4000
#  3 * 10 ** 2 = 300
#  2 * 10 ** 1 =  20
#  1 * 10 ** 0 =   1

# Attempt 1 ----------------------------------------------------------

def plus1(digits):
    dig_len = len(digits)
    for i in reversed(range(dig_len)):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        else:
            digits[i] = 0
    if digits[0] == 0:
        digits.insert(0,1)
    return digits


print(plus1(digits))

