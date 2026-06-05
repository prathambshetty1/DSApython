def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
nums=[10,25,45,60,65,100,130]
target=65
result=binary_search(nums,target)
print("Found at index: ",result if result!=-1 else "Not found")