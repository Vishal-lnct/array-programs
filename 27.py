27. #Find the First Missing Positive: Find the smallest positive integer missing in the array.

def find(nums):
    n = len(nums)

    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            index = nums[i] - 1
            nums[i], nums[index] = nums[index], nums[i]

   
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

  
    return n + 1


arr = [3,4,-1,1]
print(find(arr))