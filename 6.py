#Check if Array is Sorted

def check(arr):
    n=len(arr)

    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True    
        

s=[3,5,6,7,1]
print(check(s))        