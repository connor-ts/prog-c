# Intro to Search
# these my own notes bc i forgor
# connor ter stege
# dec 9

# Introduction to search algorithms

# linear search
# should work on any kind of list

def linear(data, target):
    for item in data 
        if item == target
        return True
    return False

numbers = [x, y, z, a, b ,c]
print(linear(a)) # True
print(linear(pineapple)) # False

# binary search, althoiugh idk if u did this
# works on sorted lists

def binary(data, target):
    low = 0
    high = len(data) - 1

while low <= high:
    mid = (low + high) // 2

    if data mid == target
        return True
    elif data[mid] < target:
        low - mid + 1
    else: high = mid - 1

return False

numbers = [a, b, c, d, e]

print(binary(chocolate_chips)) # False
print(binary(e)) # True

