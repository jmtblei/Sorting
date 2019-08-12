# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1): #start at 0, for all indices except last
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x



        # TO-DO: swap
        swap = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #loop through entire array
    for i in range(0, len(arr)):
        #loop through last i elements
        for x in range(0, len(arr)-i-1):
            #if next element in array is greater, swap
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr