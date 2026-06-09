import time
import sys
def binary_search(sorted_arr,target):
    low,high=0,len(sorted_arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if sorted_arr[mid]==target:
            return mid
        elif sorted_arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print("---O(logn)Time and O(1) Space complexity")
data_size=10_000_000
data=[i*2 for i in range(data_size)]
target=9876542
start=time.perf_counter()
result_index=binary_search(data,target)
end=time.perf_counter()
if result_index!=-1:
    print(f"Found target {target} at index {result_index}.")
else:
    print(f"Target {target} not found.")
print(f"Time taken({len(data)} elements): {(end-start)*1_000_000:.2f} microseconds")

print(f"Memory used by data list:{sys.getsizeof(data)} bytes")