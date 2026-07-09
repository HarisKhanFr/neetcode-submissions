class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #booly = False
        total = 1
        for num in nums:
                if num != 0:
                    total *= num

        if nums.count(0) == 1:
            final = [0] * len(nums)
            final[nums.index(0)] = total
            return final

        elif nums.count(0) >= 2:
            for i in range(len(nums)):
                nums[i] = 0
            return nums

        for i in range(len(nums)):
            nums[i] = total//nums[i]

        return nums
        