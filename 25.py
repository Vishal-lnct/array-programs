#25. Find Majority Element: Find the element that appears more than n/2 times.

def majorityele(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

        if freq[num] > len(arr)//2:
            return num

    return -1

s=[3,4,3,6,3,7,3]
print(majorityele(s))
