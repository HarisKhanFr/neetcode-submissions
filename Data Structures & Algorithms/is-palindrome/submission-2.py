class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""

        for letter in s:
            if letter.isalnum():
                news += letter.lower()

        return news == news[::-1]