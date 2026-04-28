# List Comprehension


# 1 #
nums = range(1, 11)
n = [f"{x} is odd" if x % 2 != 0 else f"{x} is even" for x in nums]

print(n)
print()
print()


# 2 #
nums = [-3, -2, -1, 0, 1, 2, 3]
n = [x if x >= 0 else 0 for x in nums]

print(n)
print()
print()



# Higher Order Functions

# 1 #
nums = [1, 2, 3, 4, 5]
n = list( map(lambda x: x * 2, nums))

print(n)
print()
print()