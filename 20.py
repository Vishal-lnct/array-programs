#Rotate Array to the Left by k Positions
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_left(arr, k):
    n = len(arr)
    k = k % n   # handle k > n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


arr = [1,2,3,4,5]
k = 2
print(rotate_left(arr, k))
