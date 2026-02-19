#17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def check(arr):
    n = len(arr)
    s = []

    for i in range(n):
        x = arr[i]
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                break
        else:   
            s.append(arr[i])

    return s


arr = [2,4,8,7,5,6]
print(check(arr))
 
