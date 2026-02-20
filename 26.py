#Find Peak Element: A peak element is greater than its neighbors. Find one such element
def findPeak(arr):
    n = len(arr)

    for i in range(n):
       if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):

            return arr[i]
s=[4,5,2,1]

print(findPeak(s))