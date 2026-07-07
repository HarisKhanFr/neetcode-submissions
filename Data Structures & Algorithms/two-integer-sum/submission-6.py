class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {} #num : index, num is the # required to add up to target

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in map:
                return [map[temp], i]
            else:
                map[nums[i]] = i