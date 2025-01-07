class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # have a memory {}
        memory = {}

        #iterate through nums
        for num in nums:
            #check if the num is in memory
            if num in memory:
                # return True (there is a duplicate)
                return True
            #add the num memory
            else:
                memory[num] = True
        return False
