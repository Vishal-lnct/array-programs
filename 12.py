#Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.arr = [1, 2, 4, 5]
def find(arr,n):
    sum=0
   
    for i in range(len(arr)):
        sum+=arr[i]

    x=  n*(n+1)//2
    return x-sum

x = [1, 2, 4, 5]
n=5
print(find(x,n))  