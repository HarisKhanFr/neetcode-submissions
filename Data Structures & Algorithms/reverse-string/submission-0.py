class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r and l != r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            r -= 1
            l +=1