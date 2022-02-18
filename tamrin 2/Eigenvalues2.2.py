

def Eigenvalues (mat):
    
    b= -(mat[0][0]+mat[1][1])
    c= mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
    a=1

    delta= (b**2)-(4*a*c)

    if delta>0 :

        k= [(-b+(delta)**(1/2))/2,(-b-(delta)**(1/2))/2]
    
    elif delta==0:

        k=-b/2*a
    
    else :
        print("nadarad")
    

    return k


print(Eigenvalues([[4,1],[-2,1]]))