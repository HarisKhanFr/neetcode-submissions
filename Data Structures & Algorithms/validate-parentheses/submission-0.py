class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {"(":")", "{":"}","[":"]"}
        arr1 = []

        for char in s:
            if char in paranthesis.values():
                if len(arr1) == 0:
                    return False
                temp = arr1.pop()
                if not char == paranthesis[temp]:
                    return False
            else:
                arr1.append(char)

        if len(arr1) == 0:
            return True
        return False
