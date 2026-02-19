#Reverse an Array

def revarray(arr):
    left=0
    right=len(arr)-1


    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    return arr

s=[4,9,1,3,2,5,]

revarray(s)
n=len(s)
for i in range(n):
    print(s[i],end=" ")