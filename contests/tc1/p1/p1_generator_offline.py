from random import randint, random

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')
n_values = uniform_random_list(min_n,max_n+1,test_cases)

QUARTER = 1/4

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = n_values[i-1]
        input_file.write(f'{n}\n')
        for i in range(n):
            x = randint(-10000, 10000)
            y = randint(-10000, 10000)
            operation = ''
            chance = random()
            
            if chance < QUARTER:
                operation = 'ADD'
                solution = x+y
            elif chance >= QUARTER and chance < 2 * QUARTER:
                operation = 'SUB'
                solution = x-y
            elif chance >= 2 * QUARTER and chance < 3 * QUARTER:
                operation = 'MUL'
                solution = x*y
            elif chance >= 3 * QUARTER and chance <= 1:
                operation = 'DIV'
                if y == 0:
                    y = 1
                
                solution = x//y

            input_file.write(f'{operation} {x} {y}\n')
            output_file.write(f'{solution}\n')

            