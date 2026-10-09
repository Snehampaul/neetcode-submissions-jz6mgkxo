class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        chars = set()
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[i])
            distance = i - left +1
            max_length = max(distance , max_length)
        return max_length
            
