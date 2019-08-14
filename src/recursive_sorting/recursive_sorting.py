# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #iterate through merged_arr and insert smallest item in arrA and arrB until merged is full
    for i in range(0, len(merged_arr)):
        #if arrA is empty, fill from arrB
        if len(arrA) == 0:
            merged_arr[i] = min(arrB)
            arrB.remove(min(arrB))
        #vice-versa
        elif len(arrB) == 0:
            merged_arr[i] = min(arrA)
            arrA.remove(min(arrA))
        #if the smallest item in arrA < smallest item in arrB, insert that item and remove from arrA
        elif min(arrA) < min(arrB):
            merged_arr[i] = min(arrA)
            arrA.remove(min(arrA))
        #vice-versa
        elif min(arrB) < min(arrA):
            merged_arr[i] = min(arrB)
            arrB.remove(min(arrB))
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #base case
    if len(arr) == 0 or len(arr) == 1:
        return arr
    #split array
    pivot = len(arr)//2
    #mergesort both sides
    leftArr = merge_sort(arr[0:pivot])
    rightArr = merge_sort(arr[pivot:])

    return merge(leftArr, rightArr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
