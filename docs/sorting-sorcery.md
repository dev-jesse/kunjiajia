# Sorting Sorcery
> "Stay the course." - John Gresham Machen

Sorting algorithms are heavily tested and used in question. A sorting algorithm puts elements of a array in a desired order.

## Quicksort
A divide and conquer algorithm where an array is divided into subarrays by placing numbers on either sides of the pivot based on numerical value. For more information read [here](https://www.programiz.com/dsa/quick-sort).

```py
def quicksort(array, start, end):
    if start >= end:
        return

    left, right = start, end
    # key point 1: pivot should be a value, not an index
    pivot = array[(start + end) // 2]

    # key point 2: should always be left <= right not left < right
    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quicksort(array, start, right)
    quicksort(array, left,  end)
```

## Merge Sort
Merge Sort is a divide and conquer algorithm like Quicksort. It divides the input array into two halves recursively, and then at merges them together in our desired order.

```py
def mergesort(array):
    if not array:
        return
    
    # key point 1: need to keep temporary array to track items
    temp_arr = [0 for _ in range(len(array))]

def mergesort_helper(array, start, end, temp):
    if start >= end:
        return 

    mergesort_helper(array, start, (start + end) // 2, temp)
    mergesort_helper(array, (start + end) // 2 + 1, end, temp)
    merge()

def merge(array, start, mid, end, temp):
    left = start
    right = mid + 1
    index = start

    # key point 2: mid and end are inclusive (i.e. <=)
    while left <= mid and right <= end:
        if array[left] < array[right]:
            temp[index] = array[left]
            left += 1
        else:
            temp[index] = array[right]
            right += 1
        index += 1

    while left <= mid:
        temp[index] = array[left]
        left += 1
        index += 1
    
    while right <= end:
        temp[index] = array[right]
        right += 1
        index += 1

    for i in range(start, end + 1):
        array[i] = temp[i]
```