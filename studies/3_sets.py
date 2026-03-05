# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update({'Yandex', 'Mail.ru', 'Valve'})
print(it_companies)

it_companies.pop()

C = A.union(B)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

A.update(B)
B.update(A)

A.symmetric_difference(B)

del B
del A

#################################################################

print(f'List lenght: {len(age)}')

age_st = set(age)
print(f'Set lenght: {len(age_st)}')
