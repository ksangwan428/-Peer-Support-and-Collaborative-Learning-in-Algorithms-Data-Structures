def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]
selection_sort(numbers)
print("Sorted list:", numbers)


# Selection Sort:

# How it works: Selection sort divides the list into a sorted and an unsorted region. It repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted region and swaps it with the first unsorted element.
# Description:
# Start from the first element as the minimum.
# Compare this element with the next element till the end of the list to find the smallest element.
# Swap the smallest element with the first element.
# Move to the next element and repeat the above steps until the entire list is sorted.