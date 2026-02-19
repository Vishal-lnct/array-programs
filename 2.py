#Find the Maximum & Minimum Element

def maxi(arr):
    maxi=arr[0]
    n=len(arr)

    for i in range(n):
        if arr[i]>maxi:
            maxi=arr[i]

    return maxi



def mini(arr):
    mini=arr[0]
    n=len(arr)

    for i in range(n):
        if arr[i]<mini:
            mini=arr[i]

    return mini


s=[3,5,6,8,1]

maximum=maxi(s)
minimum=mini(s)

print(maximum)
print(minimum)