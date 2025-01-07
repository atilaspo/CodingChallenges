class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        length = 0
        longest = 0

        for num in nums:
            #identify the sequence starter
            if num - 1 not in nums:
                length = 1
                # check if the next number is in the set
                while num + length in set_nums:
                    # length ++
                    length += 1
            # max(lenght, longest)
            longest = max(length, longest)
        return longest