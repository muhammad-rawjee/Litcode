class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        some_set = set()

        for val in nums:
            if val in some_set:
                return True
            
            some_set.add(val)
        return False