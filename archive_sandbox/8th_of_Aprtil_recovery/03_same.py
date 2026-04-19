## SMALL EXERCISES (LIST, TUPLE, SET, DICT) ##

# 1: Words can be writed in list only one time
words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
set_words = set(words) # set can only store one copy of each word
words = list(set_words)

print(words)



print()
print()
print()



# 2: for every point in list print x and y coordinate
points = [(1, 2), (3, 4), (5, 6)]

for x,y in points:
    print(f'X:{x} and Y:{y}.')



print()
print()
print()



# 3: "Unique letters" 
text = 'hello world'
set_from_text = set(text) - {' '}
print(f'All unique letters are: {set_from_text}.')



print()
print()
print()



# 4: Count the copies
words = ["cat", "dog", "cat", "bird", "dog", "cat"]

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)



print()
print()
print()



# 5: Mini profile
user = {
    "name": "Alex",
    "age": 18,
    "location": (52.5, 13.4)
}

x, y = user["location"]

print(f'{user["name"]} is {user["age"]} years old and located at {x} {y}')