# Little exersices to learn the basics
#1
nums = [1, 2, 3, 4, 5]
n = [x + 1 for x in nums]
print(n)
print('\n\n')

#2
nums = [2, 5, 8, 1, 0]
n = [x for x in nums if x > 2]
print(n)
print('\n\n')

#3
words = ["cat", "dog", "elephant"]
w = [len(x) for x in words]
print(w)
print('\n\n')

#4
nums = [2, 5, -8, 1, 0, 7, -12, -6, 6, 12, 0]
n = [x if x > 0 else 0 for x in nums]
print(n)
print('\n\n')

#5
nums = [5, -3, 0, 2, -1]
n = [x if x % 2 == 0 else -1 for x in nums]
print(n)
print('\n\n')

#6
words = ["apple", "banana", "kiwi", "pear", "grape"]
w = [x if len(x) <= 4 else "long" for x in words]
print(w)
print('\n\n')

#7
nums = [3, 10, 15, 8, 21, 4]
n = ['FIZZ' if x % 3 == 0 else 'BUZZ' if x % 5 == 0 else x for x in nums]
print(n)
print('\n\n')


#8
inputs = [" 123", "hello", " 45", "world", "0", "  8 "]
a = [int(x) if (x.strip()).isdigit() == True else "INVALID" for x in inputs]
print(a)
print('\n\n')