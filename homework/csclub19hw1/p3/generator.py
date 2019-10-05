from random import randint, random
from string import ascii_lowercase

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

        values = [randint(-10**9, 10**9) for _ in range(n)]
        values_str = ' '.join(str(v) for v in values)
        input_file.write(f'{values_str}\n')

        values.sort()
        min_delta = 1000000001
        for i in range(n-1):
            min_delta = min(min_delta, abs(values[i]-values[i+1]))

        max_delta = abs(values[0] - values[n - 1])
        output_file.write(f'{min_delta}\n{max_delta}\n')
        