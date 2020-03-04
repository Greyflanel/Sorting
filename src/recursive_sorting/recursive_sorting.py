# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if(arrA[i] <= arrB[j]):
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    return merged_arr + arrA[i:] + arrB[j:]



def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    merged_arr = []
    i = 0
    j = 0
    
    while i < len(arrA) and j < len(arrB):
        if(arrA[i] <= arrB[j]):
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    return merged_arr + arrA[i:] + arrB[j:]


def merge_sort( arr ):
    if(len(arr) <= 1):
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[0:half])
    right = merge_sort(arr[half:])
    
    return merge(left, right)

print(merge_sort([8,5,3,7,9]))


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
