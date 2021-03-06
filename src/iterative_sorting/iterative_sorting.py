# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        smallest_index = i
        for new_i in range(i+1, len(arr)): # took out -1 here and it worked?
            if arr[new_i] < arr[smallest_index]:
                smallest_index = new_i
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Loop through your array
    for index in range(1, len(arr)):
        temp = arr[index]
        # Compare each element to its neighbor
        while index > 0 and temp < arr[index - 1]:
            # If elements in wrong position (relative to each other, swap them)
            arr[index] = arr[index - 1]
            index -= 1

        arr[index] = temp

    return arr

[1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# # Loop through your array
#     for item in arr:
#         count = 0
#     # Compare each element to its neighbor
#         if item > arr[count + 1]:
#             # If elements in wrong position (relative to each other, swap them)
#             temp = arr[0]
#             arr[0] = arr[1]
#             arr[1] = temp
#         # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
#         else: 
#             return bubble_sort(arr)

#     return arr
'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    counts = [0] * (maximum + 1)

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[num] += 1    

    j = 0
    for i in range(0, len(counts)):
        while counts[i]> 0:
            arr[j] = i
            j += 1
            counts[i] -=1
    return arr
