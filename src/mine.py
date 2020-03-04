
arrA = [6, 7, 8, 9]
arrB = [1, 2, 3, 4, 5]


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

merge(arrA, arrB)

def merge_sort( arr ):
    if(len(arr) <= 1):
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[0:half])
    right = merge_sort(arr[half:])
    
    return merge(left, right)

print(merge_sort([8,5,3,7,9]))
    