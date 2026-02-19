#Find Subarray with Given Sum.
def sum(arr, target):
    left = 0
    current = 0

    for right in range(len(arr)):
        current += arr[right]

        while current > target:
            current -= arr[left]
            left += 1

        if current == target:
            return arr[left:right+1]

    return -1


arr = [1,2,3,7,5]
target = 12

print(sum(arr, target))

