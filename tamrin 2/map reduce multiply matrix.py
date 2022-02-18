from functools import reduce
from unittest import result


mat_1 = [

    [2,-2,-4],
    [-1,3,4],
    [1,-2,-3]
]


mat_2 = [

    [1,0,0],
    [0,1,0],
    [0,0,1]
]
def transpose (matrix):
    mat_row= len(matrix)
    mat_col= len(matrix[0])
    mat_new= [[0 for x in range (mat_row)] for y in range (mat_col)]
    for i in range (mat_row):
        for j in range (mat_col):
            mat_new[j][i]=matrix[i][j]
    return mat_new


def matrix_multiply(mat1,mat2):
    mat1_row= len(mat1)
    mat1_col= (lambda mat1=mat1: len(mat1[0]) if len(mat1)> 0 else 0)()
    mat2_row= len(mat2)
    mat2_col= (lambda mat2=mat2: len(mat2[0]) if len(mat2)> 0 else 0)()
   
    if mat1_col==mat2_row:
        result=[[0 for x in range (mat2_col)] for y in range (mat1_row)]
        for i in range (mat1_row):
            for j in range (mat2_col):
                    result[i][j]+= reduce(lambda x,y:x+y, map(lambda x,y:x*y,mat1[i],transpose(mat2)[j]))
        return result
    else:
        raise Exception ("zarb pazir nist")
                   

print(matrix_multiply(mat_1,mat_2))