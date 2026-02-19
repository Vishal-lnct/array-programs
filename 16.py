#Check if Two Arrays Are Equal: if two arrays contain the same elements
def equal(a, b):
    return sorted(a) == sorted(b)


a = [1,2,3,4]
b = [4,3,2,1]

print(equal(a, b))
