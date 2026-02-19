#Merge Two Sorted Arrays


def merge(a, b):
    i = j = 0
    x = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
           x.append(a[i])
           i += 1
        else:
            x.append(b[j])
            j += 1

    while i < len(a):
      x.append(a[i])
      i += 1

    while j < len(b):
      x.append(b[j])
      j += 1


    return x


a = [1,3,5]
b = [2,4,6]

print(*merge(a, b))
