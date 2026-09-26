class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char.lower() for char in s if char.isalnum())
        end = len(text) - 1
        i = 0
        while i<end:
            if(text[i] != text[end]):
                return False
            end -= 1
            i += 1
        return True



