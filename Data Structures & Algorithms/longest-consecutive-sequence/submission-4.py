class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                temp = num
                tempLong = 0
                while temp in nums:
                    temp += 1
                    tempLong += 1

                longest = max(longest, tempLong)

        return longest