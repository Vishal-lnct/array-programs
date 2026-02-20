#33. Find Maximum Difference (j > i)


def maxDifference(arr):
    if len(arr) < 2:
        return -1

    mini = arr[0]
    maxi= arr[1] - arr[0]

    for i in range(1, len(arr)):
        maxi = max(maxi, arr[i] - mini)
        mini = min(mini, arr[i])

    return maxi


arr = [7,1,5,3,6,4]
print(maxDifference(arr))