# numbers = {1, 2, 3, 4, 5}
# print(numbers)

# # second_numbers = [10, 11, 12, 12, 13, 15]
# # print(set(second_numbers))

# numbers.add(6)
# print(numbers)

# # numbers.add(1)
# # print(numbers)

# numbers.remove(3)
# print(numbers)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set2.union(set1)
print(union)

intersect = set2.intersection(set1)
difference = set2.difference(set1)

print(intersect)
print(difference)