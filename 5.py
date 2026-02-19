#Count Frequency of Elements

def freq(arr):
    mp = {}

    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    return mp


arr = [1, 2, 2, 3, 1, 4, 2]
result = freq(arr)

for key in result:
    print(key, result[key])


