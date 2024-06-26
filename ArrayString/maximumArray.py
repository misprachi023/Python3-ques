def findMax(arr):
    max_ele= arr[0]
    for num in arr:
        if num>max_ele:
            max_ele=num
    return max_ele
print(findMax([2,5,6,8,9,0,4,4]))
    