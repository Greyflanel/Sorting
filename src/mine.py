arr = [6, 5, 8, 4, 2, 9, 1, 0, 3, 7]

 
def bubble_sort( arr ):
    sort_complete = len(arr)
    while sort_complete != 0:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        sort_complete -= 1        
    return print(arr)
bubble_sort(arr)