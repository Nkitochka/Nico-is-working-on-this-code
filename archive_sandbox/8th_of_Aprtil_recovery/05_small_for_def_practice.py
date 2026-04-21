n = int(input('What is the last number? '))

def count_even_numbers(n):
    count = 0
    for i in range(1, n):
        if i % 2 == 0:
            count += 1
        print(f'Number: {i}\n')
    
    return count

print(f'There is {count_even_numbers(n)} even numbers')