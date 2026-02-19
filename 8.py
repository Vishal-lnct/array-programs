#Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

def sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1):
            if arr[i]+arr[j]==target:
                return{arr[i],arr[j]}
            

s=[2,3,5,6,8]
target=9
print(sum(s,target))            
