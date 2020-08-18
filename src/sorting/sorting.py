# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    a = 0
    b = 0
    c = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        else:
            merged_arr[c] = arrB[b]
            b += 1
        c += 1
    
    while a < len(arrA):
        merged_arr[c] = arrA[a]
        c += 1
        a += 1
    while b <len(arrB): 
        merged_arr[c] = arrB[b]
        c += 1
        b += 1
        
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        a = len(arr)
        b = 0
        c = (b + a) // 2
        left = merge_sort(arr[:c])
        right = merge_sort(arr[c:])
        return merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

