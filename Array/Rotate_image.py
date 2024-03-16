# Problem: https://leetcode.com/problems/rotate-image/description/

# Approach 1: Time:O(m*n), Space:O(m*n) this solution is based on common sequence or index

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        matrix_1=[[0]*n for i in range(n)]
        k=0
        for p in range(len(matrix)):
            i=(len(matrix)-1)
            for j in range(len(matrix)):
                matrix_1[k][j]=matrix[i][k]
                i-=1
            k+=1
        for i in range(n):
            for j in range(n):
                matrix[i][j]=matrix_1[i][j]
        return matrix
    

# Approach 2: Time:O(m*n), Space:O(1)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for k in range(len(matrix)):
            matrix[k].reverse()
    