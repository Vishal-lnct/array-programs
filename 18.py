18. #Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.


def move(arr):
    k = 0  

   
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k] = arr[i]
            k += 1

    
    while k < len(arr):
        arr[k] = 0
        k += 1

    return arr


arr = [0,1,0,3,12]
print(move(arr))
