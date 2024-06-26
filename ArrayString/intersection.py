def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    intersection=[]
    i,j=0, 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            if len(intersection)==0 or arr1[i] != intersection[-1]:
                intersection.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return intersection
print(intersection([1,2,0,8,4,5],[1,2,3,4,5,6]))