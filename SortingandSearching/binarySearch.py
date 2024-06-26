def binary(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1

arr=[1,2,3,4,5,6,7,8,0,10]  

print(binary(arr,6))