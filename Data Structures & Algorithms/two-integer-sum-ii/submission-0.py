class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            need = target - numbers[i]

            if need in seen:
                return [seen[need] + 1, i+1]
            
            seen[numbers[i]] = i
        return []