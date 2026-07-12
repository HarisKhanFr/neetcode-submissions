class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        highest = 0

        for num in nums:
            if num - 1 not in nums:
                temp = num
                tempHighest = 0

                while temp in nums:
                    tempHighest += 1
                    temp += 1

                if tempHighest > highest:
                    highest = tempHighest

        return highest