# TO-DO: Complete the selection_sort() function below

z = [3, 2, 5, 6, 1, 7, 4, 8, 10, 9]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
       # print(f"looping: {smallest_index}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop over the array starting at smallest index
        # compare smallest index to the next index through the loop
        # if element is less than the smallest set element as new min
        for a in range(cur_index, len(arr)):
            # print(arr[a])
            if arr[smallest_index] > arr[a]:
                smallest_index = a

           # print(f"new smallest: {smallest_index}")
           # print(arr[smallest_index])
            # TO-DO: swap
            # multiple assignment format val_1, val_2 = val_2, val_1
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# selection_sort(z)
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop the array
    swap = True
    while swap == True:
        swap = False
        # for i in range(len(arr)):
        # print(f"Loop:{i}")
        # compare each element to neighbor ( + 1)
        # if element > neighbor swap them
        for a in range(len(arr) - 1):
            if arr[a] > arr[a + 1]:
                # use multiple assignment
                arr[a], arr[a + 1] = arr[a + 1], arr[a]
                swap = True
                print(arr)

    return arr


bubble_sort(z)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
