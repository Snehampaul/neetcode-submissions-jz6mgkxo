class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up = 0
        down = m-1
        while up <= down:
            mid_r = (up + down) // 2
            if target >= matrix[mid_r][0] and target<= matrix[mid_r][n-1]:
                left = 0
                right = n-1
                while left <= right:
                    mid = (left+right) // 2
                    if matrix[mid_r][mid] == target:
                        return True

                    elif target < matrix[mid_r][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            elif target < matrix[mid_r][0]:
                down = mid_r-1
            else:
                up = mid_r + 1

        return False
                






