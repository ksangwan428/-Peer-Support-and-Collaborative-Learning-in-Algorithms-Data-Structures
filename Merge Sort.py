def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively divide the list until individual elements
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(5)]
merge_sort(numbers)
print("Sorted list:", numbers)




# Merge Sort:

# How it works: MergeSort is a divide and conquer algorithm that divides the list into two halves, sorts them, and then merges the sorted halves.
# Description:
# If the list has only one element, return the list (base condition).
# Split the list into two halves.
# Recursively sort both halves.
# Merge the two halves together to get a sorted list.
