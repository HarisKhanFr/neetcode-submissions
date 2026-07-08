class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fMap = {} #number: # of times it was repeated

        if len(nums) == k:
            return nums
        
        for num in nums:
            if num not in fMap.keys():
                fMap[num] = nums.count(num)

        final = []
        for i in range(k):
            for num, frequency in fMap.items():
                if frequency == max(fMap.values()):
                    fMap.pop(num)
                    final.append(num)
                    break
        
        return final
