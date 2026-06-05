def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
nums=[10,25,45,60,5,100,30]
target=45
result=linear_search(nums,target)
print("Found at index: ",result if result!=-1 else "Not found")