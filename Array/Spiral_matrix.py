# Problem: https://leetcode.com/problems/spiral-matrix/description/

# Approach 1: Time: O(m*n), Space: O(m*n).

def spiral_matrix(matrix):
    result=[]
    row_len=len(matrix)
    column_len=len(matrix[0])
    srt_clm=srt_row=0
    end_row=row_len-1
    end_column=column_len-1
    while(len(result)<row_len*column_len):
        for i in range(srt_clm,end_column+1):
            result.append(matrix[srt_row][i])
        srt_row+=1
        for j in range(srt_row,end_row+1):
            result.append(matrix[j][end_column])
        end_column-=1
        if (srt_row<=end_row):
            for k in range(end_column,srt_clm-1,-1):
                result.append(matrix[end_row][k])
            end_row-=1
        if (srt_clm<=end_column):
            for l in range(end_row,srt_row-1,-1):
                result.append(matrix[l][srt_clm])
            srt_clm+=1
    return result
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))

