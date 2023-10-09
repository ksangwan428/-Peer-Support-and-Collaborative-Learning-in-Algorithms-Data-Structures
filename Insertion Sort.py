def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1] that are
        # greater than key to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]
insertion_sort(numbers)
print("Sorted list:", numbers)


# Insertion Sort:

# How it works: Insertion Sort builds the final sorted list one item at a time. It's analogous to the way you might sort playing cards in your hands.
# Description:
# Start from the second element (index 1).
# Compare this element with the previous elements.
# If this element is smaller than the previous element, compare it with the elements before the previous element, and so on. This process continues until we reach an element smaller than the current element or the beginning of the list.
# Place the current element in the correct position so that the elements before are smaller than the current element.
# Move on to the next element and repeat the above steps.