#29. Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.

def longest(nums):
    if not nums:
        return 0

    x = set(nums)
    longest = 0

    for num in x:

      
        if num - 1 not in x:

            current = num
            length = 1

            while current + 1 in x:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100,4,200,1,3,2,5,8,9]
print(longest(arr))