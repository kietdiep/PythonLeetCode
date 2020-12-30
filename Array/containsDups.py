def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for num in nums:
            if num in table:
                return True
            else:
                table.add(num)
        return False

#Attempted to do this with a list but lookup times for lists are slower
# sets have the fastest lookup time
# since we dont need a key