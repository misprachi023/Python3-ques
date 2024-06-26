def findMin(arr):
    min_ele=arr[0]
    for num in arr:
        if num<min_ele:
            min_ele=num
    return min_ele
print(findMin([2,5,6,8,9,0,-1,4,4]))