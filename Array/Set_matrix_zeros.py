# problem: https://leetcode.com/problems/set-matrix-zeroes/description/


# Approach 1: Time: O(m*n), Space:O(numbers of zeros)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row= len(matrix)
        column=len(matrix[0])
        arr=[]
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    arr.append([i,j])
        while len(arr)!=0:
            [i,j]=arr.pop()
            for k in range(max(row,column)):
                if k<column:
                    matrix[i][k]=0
                if k<row:
                    matrix[k][j]=0
        return matrix
    
# Approach 2: Time: O(m*n*max(m, n)), Space:O(m*n)

    
import copy
class Solution: 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row= len(matrix)
        column=len(matrix[0])
        cpy_matrix=copy.deepcopy(matrix)
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    for k in range(max(row,column)):
                        if k<column:
                            cpy_matrix[i][k]=0
                        if k<row:
                            cpy_matrix[k][j]=0
        for i in range(row):
            for j in range(column):
                matrix[i][j]=cpy_matrix[i][j]


# Approach 3: Time: O(m*n), Space:O(m+n)

                
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowlen= len(matrix)
        columnlen=len(matrix[0])
        row=[1]*rowlen
        column=[1]*columnlen
        for i in range(rowlen):
            for j in range(columnlen):
                if matrix[i][j]==0:
                    row[i]=0
                    column[j]=0
        for k in range(rowlen):
            if row[k]!=0:
                continue
            for l in range(columnlen):
                matrix[k][l]=0

        for m in range(columnlen):
            if column[m]!=0:
                continue
            for n in range(rowlen):
                matrix[n][m]=0


        
                    
# Approach 4: Time: O(m*n), Space:O(1)

            
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowlen = len(matrix)
        columnlen = len(matrix[0])
        fstrowzero = False
        fstcolumnzero = False
        for k in range(columnlen):
            if matrix[0][k] == 0:
                fstrowzero = True
                break
        for i in range(rowlen):
            if matrix[i][0] == 0:
                fstcolumnzero = True
                break
        for i in range(1, rowlen):
            for j in range(1, columnlen):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, rowlen):
            for j in range(1, columnlen):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if fstrowzero:
            for k in range(columnlen):
                matrix[0][k] = 0
        if fstcolumnzero:
            for i in range(rowlen):
                matrix[i][0] = 0