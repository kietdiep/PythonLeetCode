x = 320
# output will be 023
# have to get rid of 0
def reverseInt(x):
    def divide(number, divider):
        return int(number * 1.0 / divider)
    def mod (number, m):
        if number <0:
            return number % -m
        return number % m

    MAX_INT = 2 ** 31 - 1 # 2146483647
    MIN_INT = -2 ** 31 # -2146483648

    res = 0
    while x:
        pop = mod(x,10)
        x = divide(x,10)
        if res > divide(MAX_INT, 10) or (res == divide(MAX_INT, 10) and pop > 7):
            return 0
        if res < divide(MIN_INT, 10) or (res == divide(MIN_INT, 10) and pop < -8):
            return 0
        res = res * 10 + pop

    return res

#slow runtime but good memory usage


def reverse(self, x: int) -> int:
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
        if result > (2 ** 31 - 1) or result < -(2**31):
            return 0
        else:
            return result

#faster but has worse memory usage