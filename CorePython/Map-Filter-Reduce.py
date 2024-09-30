
# MAP

# def cube(x):
#     return x * x * x

# print(cube(2))

# l = [1,2,3,4,5,6,7,8]

# newl = list(map(cube, l))
# print(newl)

# FILTER

l = [1, 2, 3, 4, 2, 3, 4, 2, 1, 2, 3, 1, 4, 1, 3, 4, 2, 5, 6, 7]
unique_list = list(set(l))

print(unique_list)

from collections import Counter

l = [1, 2, 3, 4, 2, 3, 4, 2, 1, 2, 3, 1, 4, 1, 3, 4, 2, 5, 6, 7]

counter = Counter(l)
duplicate_elements = [element for element, count in counter.items() if count > 1]

print("duplicate_elements :- ",duplicate_elements)
