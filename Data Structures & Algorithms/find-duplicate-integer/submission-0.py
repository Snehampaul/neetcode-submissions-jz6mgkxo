class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        same = set()
        for i in nums:
            if i not in same:
                same.add(i)
            else:
                return i
        

