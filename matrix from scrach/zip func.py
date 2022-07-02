def zip_like(x,y):
    zip_like_list=[]
    for i in range (len(x) if len(x)<len(y) else len(y)):
        zip_like_list.append((x[i],y[i]))
    return zip_like_list


x = [1,2,12,31,2]
y = [1,3,6,12,3,1231,2]
print(zip_like (x,y))