# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Check base case
    if start <= end:
        mid = (start + end) // 2
        # if element is present at the middle itself
        if arr[mid] == target:
            return mid
        # if element is smaller than mid, 
        # then it can only be present in the left subarray
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid - 1)
    else:
        # Element is not present in the array
        return -1



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

