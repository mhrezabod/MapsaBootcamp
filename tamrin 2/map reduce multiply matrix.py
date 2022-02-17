from unittest import result


mat_1 = [

    [1,3,5],
    [2,5,2],
    [1,4,2]
]

mat_2 = [

    [1,0,0],
    [0,1,0],
    [0,0,1]
]

def matrix_multiply(mat1,mat2):
    mat1_row= len(mat1)
    mat1_col= (lambda mat1=mat1: len(mat1[0]) if len(mat1)> 0 else 0)()
    mat2_row= len(mat2)
    mat2_col= (lambda mat2=mat2: len(mat2[0]) if len(mat2)> 0 else 0)()
   
    if mat1_col==mat2_row:
        result=[[0 for x in range (mat2_col)] for y in range (mat1_row)]
        


        return result
    else:
        raise Exception ("zarb pazir nist")
                   

print(matrix_multiply(mat_1,mat_2))


a=map(lambda x,y:x*y, mat_1[0:][0:], mat_2[0:][0:])
print(list(a))