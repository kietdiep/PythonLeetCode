n = 4

# expected output = 1211

# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n-1))
    
    def say(self, n):
        if len(n) == 1:
            return "1" + str(n)
        
        count = 1
        res = ""
        cur = n[0]
        for char in n[1:]:
            if char != cur:
                res += str(count) + cur
                cur = char
                count = 1
            else:
                count += 1
                
        res += str(count) + cur
                
        return res
        