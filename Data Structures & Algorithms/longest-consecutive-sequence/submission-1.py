class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums = set(nums)
        highest = 1

        for num in nums:
            if num - 1 not in nums:
                temp = num
                tempHighest = 1

                while temp + 1 in nums:
                    tempHighest += 1
                    temp += 1

                if tempHighest > highest:
                    highest = tempHighest

        return highest