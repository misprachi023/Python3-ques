def rotateArray(arr, k):
    n=len(arr)
    k=k%n
    return arr[-k:]+arr[:-k]
print(rotateArray([2,4,7,8,92,34,5], 3))