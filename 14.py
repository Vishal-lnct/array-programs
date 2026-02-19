#14. Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6]

print(intersection(arr1,arr2))