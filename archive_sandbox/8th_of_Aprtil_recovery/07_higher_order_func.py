def space():
    print()
    print('-' * 20)
    print()
### 
#1# BASICS
### 
def say_hi():
    print('Hi!')

f = say_hi
f()

space()


###
#2#
###
def say_bye():
    print('Bye!')
    
def execute_twice(func):
    func()
    func()

execute_twice(say_bye)


space()

###
#3#
###
def add_one(x):
    return x + 1

def apply(func, value):
    return func(value)

print(apply(add_one, 9))


space()

###
#4#    LAMBDA, MAP AND FILTER
###
print(apply(lambda x: x + 10, 5))


space()


###
#5#
###
nums = [3, 6, 9]
after_div = map(lambda x: x / 3, nums)
print(list(after_div))


space()


###
#6#
###
nums = [5, 12, 7, 20, 3]
filtered_nums = list(filter(lambda x: x > 10, nums))
print(filtered_nums)

filtered_and_map = list(map(lambda x: x - 11, filtered_nums))
print(filtered_and_map)


space()

###
#7#
###
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
mult_evens = list(map(lambda x: x * 10, even_nums))
print(mult_evens)


###
#8# CLOSURE
###
def make_adder(n):
    def adder(x):
        return x + n
    return adder

plus_ten = make_adder(10)
print(plus_ten(19))

def make_multiplier(n):
    return lambda x: x * n

mul3 = make_multiplier(3)
print(mul3(4))

