class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr1 = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not arr1 or not temperatures[i] > arr1[-1][0]:
                arr1.append([temperatures[i], i])
            else:
                while arr1 and temperatures[i] > arr1[-1][0]:
                    results[arr1[-1][1]] = i - arr1[-1][1]
                    arr1.pop()

                arr1.append([temperatures[i], i])

        return results