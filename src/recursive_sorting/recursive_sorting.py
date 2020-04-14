# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #print('element', elements)
    merged_arr = [0] * elements
    # TO-DO
    #print(f"merged arr: {merged_arr}")
    # i increments every time
    i = 0
    # j k increment as the value is smaller and become the new index being added and helps sort
    j = 0
    k = 0
    # loop thru elements
    for i in range(i, elements):
        #print(f"arrA: {arrA}, arrB: {arrB}")
        if j >= len(arrA):  # check to see if A is empty
            merged_arr[i] = arrB[k]
            k += 1
        elif k >= len(arrB):  # check if B is empty
            merged_arr[i] = arrA[j]
            j += 1
        # compare arrA values to arrB values to find smallest
        elif arrA[j] < arrB[k]:
            # replace value on merged arr based on loop of i
            merged_arr[i] = arrA[j]
            j += 1
            #print(f"j: {j}")
        elif arrB[k] < arrA[j]:
            merged_arr[i] = arrB[k]
            # print(f"k:{k}")
            k += 1
    return merged_arr


#merge([1, 2, 7], [4, 5, 6])
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # if len(arr) <= 1
    if len(arr) > 1:
        # mid = length//2 so always a whole num
        mid = len(arr) // 2
        # print(arr[mid:])
        # lhs sort rhs sort
        # everything to the left of index mid [:mid]
        lhs = merge_sort(arr[:mid])
        # everything to the right of index mid [mid:]
        rhs = merge_sort(arr[mid:])
        # call merge() to add them together
        arr = merge(lhs, rhs)

    return arr


print(merge_sort([3, 7, 4, 10, 9, 8, 2, 1, 6, 5]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
