#Remove given Element from Array

def remove(arr,num):
    n=len(arr)
    s=[]

    for i in range(n):
        if arr[i]!=num:
            s.append(arr[i])


    return s


p=[2,5,7,1,9]
tar=7

print(remove(p,tar))