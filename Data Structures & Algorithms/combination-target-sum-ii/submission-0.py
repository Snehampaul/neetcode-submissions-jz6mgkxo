class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        candidates.sort()       
        def backtrack(start , remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start , len(candidates)):
                value = candidates[i]
                if value > remaining:
                    continue
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current.append(value)
                backtrack(i+1,remaining-value)
                current.pop()

        backtrack(0,target)
        return result 