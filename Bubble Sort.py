def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                # than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]
bubble_sort(numbers)
print("Sorted list:", numbers)


# Bubble Sort:

# How it works: Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated for every element until no swaps are needed, which means the list is sorted.
# Description:
# Starting from the first element, compare it with the next element.
# If the current element is greater than the next element, they are swapped.
# Move on to the next element and repeat the above steps until the end of the list.
# After the first pass, the largest element bubbles up to the last position.
# Repeat the process for the rest of the list excluding the last element, then the second last, and so on.
# If during a pass, no swaps are made, it means the list is already sorted, so we can break out of the loop.