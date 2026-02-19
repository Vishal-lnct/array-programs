#Maximum Sum Subarray (Kadane's Algorithm)
def maxsubarray(arr):
    maxi = arr[0]
    current = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maxi = max(maxi, current)

    return maxi


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarray(arr))
