from random import randint, choice, sample
from collections import deque

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
max_x = int(input('Maximum X symbols: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = randint(min_n, max_n)
        values = [randint(-1000000, 1000000) for i in range(n)]

        k = randint(0, n - 1)
        shifted_values = deque(values)
        shifted_values.rotate(k)
        shifted_values = [str(i) for i in shifted_values]

        hidden_value_indices = sample(range(n), randint(1, max_x if max_x > 0 else n - 1))
        hidden_values = [str(values[i]) if i not in hidden_value_indices else 'X' for i in range(n)]

        input_file.write('{}\n{}\n{}'.format(n, ' '.join(hidden_values), ' '.join(shifted_values)))
        output_file.write(f'{k}')