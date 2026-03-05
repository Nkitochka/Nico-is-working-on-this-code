fruits = ('mango', 'apple', 'banana')
vegetables = ('carrot', 'potato', 'tomato')
animal_products = ('pork', 'meat')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))

print(food_stuff_lt[3:5])

part1_food_stuff_lt = food_stuff_lt[:3] + food_stuff_lt[5:]
print(part1_food_stuff_lt)
del food_stuff_tp

###################################
print()
print()


nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print(f'Estonia is Nordic country? ... {'Estonia' in nordic_countries}')
print(f'Iceland is Nordic country? ... {'Iceland' in nordic_countries}')
