class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()

        for letter in s:
            if letter not in valid:
                s = s.replace(letter, "")
        
        return s == s[::-1]