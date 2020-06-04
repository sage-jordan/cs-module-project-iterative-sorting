def linear_search(arr, target): # linear search for a number in list

    for i in range(len(arr)): # loop over list

        if arr[i] == target: # if this loop matches

            return i # return index

    return -1   # not found


def binary_search(arr, target): # binary search for a number in list
    low = 0 # low = index of 0
    high = len(arr) - 1 # high = index of last value
    mid = 0 # mid = index of starting point

    while low <= high: # handle if list is empty or item is not found
        mid = (high + low)
        # Check if target is found
        if arr[mid] < target: 
            low = mid + 1
        # If target is greater, ignore left half
        elif arr[mid] > target:
            high = mid - 1
        # If target is smaller, ignore right half
        else:
            return mid
    return -1  # not found
