#Find the Second Largest Element

def seclargest(arr):
    maxi=arr[0]
    n=len(arr)
    for i in range(n):
        if arr[i]>maxi:
            maxi=arr[i]
    secmax=arr[0]       
    for i in range(n):
        if arr[i]>secmax and arr[i]!=maxi:
            secmax=arr[i]

    return secmax 


s=[3,4,6,8,4]

print(seclargest(s))
