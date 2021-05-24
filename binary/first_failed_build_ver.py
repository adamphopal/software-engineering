"""
S,S,S,F,F,F,F,F,F,F
"""
#Binary Search
#Let's suppose you are running automatic build system.
#[S, S ,S, F, F, F, F] (S: build success, F: build failed)
#this example shows one developer pushed bad code after third build, and
#we can see build failure from fourth build.

#Find first failed build in time complexity O(log N)

def binary_search(input, l, r):
    if len(input) < 1:
        return -1

    while l < r:
        mid = (l + r) // 2
        if input[mid] == "F":
            r = mid
        else:
            l = mid + 1

    return l if input[l] == "F" else -1


input = ["S", "S", "S", "F", "F", "F", "F", "F", "F", "F"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

input = ["F", "F", "F"]
idx = binary_search(input, 0 , len(input)-1)
print(idx)

#input = ["S", "S", "S"]
#idx = binary_search(input, 0 , len(input)-1)
#print(idx)

#input = ["S"]
#idx = binary_search(input, 0 , len(input)-1)
#print(idx)

#input = []
#idx = binary_search(input, 0 , len(input)-1)
#print(idx)
