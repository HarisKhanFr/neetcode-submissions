class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        array1 = []

        for i in range(len(nums)):
            total = 1
            for x in range(len(nums)):
                if x != i:
                    total *= nums[x]
            array1.append(total)

        return array1