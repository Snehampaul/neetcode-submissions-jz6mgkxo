class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
     result = []
     current = []
     def backtrack(start , remaining):
        if remaining == 0:
            result.append(current[:])
            return

        for i in range(start , len(nums)):
            value = nums[i]
            if value > remaining:
                continue

            current.append(value)
            backtrack(i,remaining - value)
            current.pop()

     backtrack(0,target)
     return result  