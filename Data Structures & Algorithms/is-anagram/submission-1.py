class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t = list(t)

        for x in s:
            if x in t:
                t.remove(x)

        if t == []:
            return True
        else:
            return False
