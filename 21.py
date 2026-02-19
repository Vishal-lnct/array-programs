# Find the Kth Smallest Element

def small(arr,k):
    n=len(arr)
    arr.sort()

    return arr[k-1]


arr=[4,6,8,3,2,9]
k=3
print(small(arr,3))
    



