class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index,curr):
            if len(digits) == len(curr):
                res.append(curr)
                return
            for c in digitToChar[digits[index]]:
                backtrack(index+1,curr + c)

        if digits:
            backtrack(0,"")

        return res



