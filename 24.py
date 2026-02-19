#24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

def rearrange(arr):
    n = len(arr)
    left = 0
    right = n - 1
    result = []

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])

        left += 1
        right -= 1

    return result


arr = [1, 2, 3, 4, 5, 6]
print(rearrange(arr))
