#Find Duplicates in an Array

def find(arr):

    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return arr[i]
            

s=[2,3,5,6,7,3]

print(find(s))