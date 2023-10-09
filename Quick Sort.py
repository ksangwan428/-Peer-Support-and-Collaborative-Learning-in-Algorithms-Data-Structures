def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        # Separately sort elements before and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]
quick_sort(numbers, 0, len(numbers)-1)
print("Sorted list:", numbers)


# Quick Sort:

# How it works: QuickSort is a divide and conquer algorithm that picks an element as a pivot and partitions the list around the pivot. The pivot element is placed in its sorted position, and then the list is divided into two parts and the process is repeated.
# Description:
# Choose a pivot. Common choices are the first element, the last element, or a random element.
# Partition the list such that all elements smaller than the pivot come before the pivot and all elements greater than the pivot come after it.
# Recursively apply the above steps to the sub-lists of elements with smaller values and separately to the sub-list of elements with greater values.