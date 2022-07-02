def remove_local_max(lenght,list_):

    count=0
    for i in range(1,lenght-1):
        if list_[i-1]<list_[i]>list_[i+1]:
            try:
                if list_[i+2]>= list_[i]:
                    list_[i+1]=list_[i+2]
                    count+=1
                else:
                    list_[i+1]=list_[i]
                    count+=1
            except:
                list_[i]=max(list_[i+1],list_[i-1])
                count+=1

    return count,list_

print(remove_local_max(3,[2,1,2]))
print(remove_local_max(4,[1,2,3,1]))
print(remove_local_max(5,[1,2,1,2,1]))
print(remove_local_max(9,[1,2,1,3,2,3,1,2,1]))
