mat = [

    [1,3,5],
    [2,5,2],
    [1,4,2]
]

def transpose (matrix):
    mat_row= len(mat)
    mat_col= len(mat[0])
    mat_new= [[0 for x in range (mat_row)] for y in range (mat_col)]
    for i in range (mat_row):
        for j in range (mat_col):
            mat_new[j][i]=mat[i][j]
    return mat_new


print(transpose(mat))
