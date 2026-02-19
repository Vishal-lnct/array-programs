#Find All Subarrays
def subarray(arr):
    n = len(arr)

    for i in range(n):             
        for j in range(i, n):       
            for k in range(i, j+1): 
                print(arr[k], end=" ")
            print()
            

arr = [1,2,3]
subarray(arr)
