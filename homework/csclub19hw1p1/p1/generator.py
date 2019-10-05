from random import randint, random, choice
from string import ascii_lowercase

MAX_RADIUS = 10000
MAX_THETA = 360

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
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = n_values[i-1]
        input_file.write(f'{n}\n')

        columns = []
        for j in range(n):
            column = ''.join(choice(ascii_lowercase) for _ in range(n))
            # 50% chance for the column to be sorted
            if random() <= 0.5:
                column = ''.join(sorted(column))

            columns.append(column)

        rows = []
        for j in range(n):
            row = ''.join(columns[k][j] for k in range(n))
            rows.append(list(row))

            input_file.write(f'{row}\n')

        result = 0
        for column in zip(*rows):
            if any (column[i] > column[i+1] for i in range(len(column)-1)):
                result += 1
        
        output_file.write(f'{result}\n')