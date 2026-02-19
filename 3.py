# Find the Sum of Elements
def sum(arr):
    x=0
    n=len(arr)
    for i in range(n):
        x=x+arr[i]

    return x


s=[4,5,2,1,8]
total=sum(s)
print(total)